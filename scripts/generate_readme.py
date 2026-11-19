#!/usr/bin/env python3
# Copyright (c) 2026 Cereboto
# SPDX-License-Identifier: MIT
"""Render README.md and README.zh-CN.md from data/projects.yaml."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Install it with: pip install -r requirements.txt"
    ) from exc

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "projects.yaml"
SHANGHAI = timezone(timedelta(hours=8), name="Asia/Shanghai")

STATUS_EN = {
    "official_verified": "Official verified",
    "community_verified": "Community verified",
    "source_checked": "Source-checked",
    "unverified": "Unverified",
}
STATUS_ZH = {
    "official_verified": "官方核实",
    "community_verified": "社区核实",
    "source_checked": "已对源核查",
    "unverified": "未核实",
}


def load() -> dict:
    with DATA.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def sort_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (name or "").lower())


def md_link(label: str, url: str | None) -> str:
    if not url or url in {"Unknown", "未知"}:
        return label
    return f"[{label}]({url})"


def unknown(value, lang: str) -> str:
    if value in (None, "", "Unknown"):
        return "未知" if lang == "zh" else "Unknown"
    return str(value)


def fmt_commit(iso: str, lang: str) -> str:
    if not iso or iso in {"Unknown", "未知"}:
        return "未知" if lang == "zh" else "Unknown"
    raw = iso.strip()
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        local = dt.astimezone(SHANGHAI)
        stamp = local.strftime("%Y-%m-%d %H:%M")
        return f"{stamp} (Asia/Shanghai)"
    except ValueError:
        return raw


def fmt_ecosystem(items, lang: str) -> str:
    if not items:
        return "未知" if lang == "zh" else "Unknown"
    return ", ".join(items)


def fmt_licenses(p: dict, lang: str) -> str:
    hw = unknown(p.get("hardware_license"), lang)
    sw = unknown(p.get("software_license"), lang)
    label_hw = "硬件" if lang == "zh" else "HW"
    label_sw = "软件" if lang == "zh" else "SW"
    return f"{label_hw}: {hw}<br>{label_sw}: {sw}"


def fmt_channels(channels, lang: str) -> str:
    if not channels:
        return "未知" if lang == "zh" else "Unknown"
    parts = []
    for ch in channels:
        name = ch.get("name") or ""
        url = ch.get("url")
        note = ch.get("note")
        text = md_link(name, url) if url else name
        if note:
            text += f" ({note})"
        parts.append(text)
    return "<br>".join(parts)


def fmt_activity(p: dict, lang: str) -> str:
    stars = unknown(p.get("repo_stars"), lang)
    commit = fmt_commit(p.get("repo_last_commit") or "", lang)
    as_of = p.get("repo_activity_as_of") or ""
    if lang == "zh":
        return f"星标 {stars}<br>最近提交 {commit}<br>统计截至 {as_of}"
    return f"{stars} stars<br>Last commit {commit}<br>As of {as_of}"


def fmt_specs(p: dict, lang: str) -> str:
    dof = unknown(p.get("dof"), lang)
    specs = p.get("key_specs")
    if specs and specs not in {"Unknown", "未知"}:
        return f"{dof}<br>{specs}"
    return dof


def fmt_motors(p: dict, lang: str) -> str:
    motors = unknown(p.get("motors"), lang)
    comm = unknown(p.get("communication"), lang)
    if lang == "zh":
        return f"{motors}<br>通信：{comm}"
    return f"{motors}<br>Comms: {comm}"


def fmt_disclosure(p: dict, lang: str) -> str:
    if p.get("cereboto_related") or p.get("disclosure"):
        text = p.get("disclosure") or "Disclosure: sold by Cereboto"
        if lang == "zh":
            # Keep a faithful disclosure; add a Chinese gloss.
            return f"{text}<br>（Cereboto 有销售该项目相关产品）"
        return text
    return "—" if lang == "en" else "—"


def project_title(p: dict, lang: str) -> str:
    name = p["name_zh"] if lang == "zh" else p["name"]
    url = p.get("website") if p.get("website") not in (None, "Unknown") else p.get("repo")
    linked = md_link(name, url if url not in (None, "Unknown") else None)
    repo = p.get("repo")
    if repo and repo not in {"Unknown", "未知"} and repo != url:
        label = "仓库" if lang == "zh" else "repo"
        linked += f"<br>({md_link(label, repo)})"
    return linked


def render_table(projects: list[dict], lang: str) -> str:
    if lang == "zh":
        headers = [
            "项目",
            "维护者",
            "简介",
            "自由度 / 规格",
            "电机与通信",
            "约略 BOM 成本",
            "软件生态",
            "许可证（硬件 / 软件）",
            "仓库活跃度",
            "购买渠道",
            "核实状态",
            "披露",
        ]
    else:
        headers = [
            "Project",
            "Maintainer",
            "Description",
            "DoF / key specs",
            "Motors & comms",
            "Approx. BOM cost",
            "Software ecosystem",
            "Licenses (hardware / software)",
            "Repo activity",
            "Purchase channels",
            "Verification",
            "Disclosure",
        ]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for p in projects:
        status = (STATUS_ZH if lang == "zh" else STATUS_EN)[p["verification_status"]]
        row = [
            project_title(p, lang),
            unknown(p.get("maintainer"), lang),
            p.get("description_zh") if lang == "zh" else p.get("description"),
            fmt_specs(p, lang),
            fmt_motors(p, lang),
            unknown(p.get("bom_cost"), lang),
            fmt_ecosystem(p.get("software_ecosystem") or [], lang),
            fmt_licenses(p, lang),
            fmt_activity(p, lang),
            fmt_channels(p.get("purchase_channels") or [], lang),
            status,
            fmt_disclosure(p, lang),
        ]
        # Escape pipes inside cells
        row = [c.replace("|", "\\|").replace("\n", "<br>") for c in row]
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def grouped(data: dict) -> list[tuple[dict, list[dict]]]:
    projects = data["projects"]
    by_cat: dict[str, list[dict]] = {}
    for p in projects:
        by_cat.setdefault(p["category"], []).append(p)
    out = []
    for cat in data["categories"]:
        items = sorted(by_cat.get(cat["id"], []), key=lambda p: sort_key(p["name"]))
        out.append((cat, items))
    return out


def toc(groups, lang: str) -> str:
    lines = []
    for cat, items in groups:
        title = cat["title_zh"] if lang == "zh" else cat["title"]
        anchor = slug(title)
        n = len(items)
        suffix = f"（{n}）" if lang == "zh" else f" ({n})"
        lines.append(f"- [{title}](#{anchor}){suffix}")
    return "\n".join(lines)


def slug(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", "-", s.strip())
    return s


def render_en(data: dict) -> str:
    d = data["directory"]
    groups = grouped(data)
    as_of = data["as_of"]
    tz = data["as_of_timezone"]
    parts = [
        f"# {d['title']}",
        "",
        d["tagline_en"],
        "",
        "This directory is independent and community-driven. Cereboto maintains the list and also sells open-source embodied-robot hardware at [cereboto.com](https://cereboto.com/). Commercial partnerships do not affect ranking, and no brand is excluded for competitive reasons.",
        "",
        f"[简体中文](README.zh-CN.md) · [Contributing](CONTRIBUTING.md) · [License](LICENSE) · Data: [`data/projects.yaml`](data/projects.yaml)",
        "",
        "## Contents",
        "",
        toc(groups, "en"),
        "",
        "## How this list is organized",
        "",
        "Within each category, projects are sorted **alphabetically by English name**. That is an objective rule: star counts, price, recency, and commercial relationships are not used for ranking.",
        "",
        "Hardware licenses and software licenses are recorded separately, from LICENSE files or official license statements. If a license could not be found, the field is `Unknown`.",
        "",
        f"Repository activity (stars and last commit) was recorded on **{as_of}** ({tz}). Commit timestamps are stored in UTC in the YAML and displayed here in Asia/Shanghai. Figures change; treat them as a snapshot.",
        "",
        "## Inclusion criteria",
        "",
        "A project can be listed when all of the following hold:",
        "",
        "1. It is relevant to **embodied robotics** (robots or tightly coupled devices that sense and act in the physical world, including arms, hands, mobile bases, legged robots, teleoperation and data-collection hardware, educational platforms, and closely related sensors or face/expression hardware).",
        "2. **Design files and/or source code are publicly available**, or the official maintainer has announced a public open-source release whose files can be retrieved. A paper or marketing page alone is not enough for a confirmed listing.",
        "3. The listing can point to a **primary source** (official repository, documentation, or organization page).",
        "4. The project is not listed solely to advertise a closed product.",
        "",
        "Projects that almost qualify, but whose public design files could not be found, may be kept with verification status **Unverified** and an explicit note, so the gap is visible rather than silent.",
        "",
        "This first draft was seeded from a public project index and then checked against primary sources. Entries may be added, corrected, recategorized, or removed by pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).",
        "",
        "## Verification levels",
        "",
    ]
    for level in data["verification_levels"]:
        parts.append(f"- **{level['title_en']}** — {level['definition_en']}")
    parts += [
        "",
        "No entry in this first draft is Official verified or Community verified. Most entries are Source-checked: we read public primary sources, but project maintainers have not confirmed the text.",
        "",
        "## Disclosure policy",
        "",
        "Cereboto sells kits and assembled products related to some projects in this list. Those entries carry a disclosure in the table. Cereboto is not given special placement; the same alphabetical rule applies. Purchase links in this directory are limited to official or upstream sources (the project's own shop, official documentation or BOM, or an official manufacturer store) and, where Cereboto actually sells the product, a Cereboto product page. This is not a claim that no other sellers exist. Being a Cereboto product, or not being one, does not change rank or eligibility.",
        "",
        "## License of this directory",
        "",
        "The text of this directory (YAML data, generated READMEs, contributing guides, and issue/PR templates) is licensed under [CC BY 4.0](LICENSE). The generator script `scripts/generate_readme.py` is licensed under the [MIT License](LICENSE-CODE). These licenses do not change the licenses of the listed projects, which remain their own.",
        "",
    ]
    for cat, items in groups:
        parts.append(f"## {cat['title']}")
        parts.append("")
        if not items:
            parts.append(cat.get("empty_en") or "_No projects in this category in the current data file._")
            parts.append("")
            continue
        parts.append(render_table(items, "en"))
        parts.append("")
        if cat.get("comparison_en"):
            parts.append("### Comparison")
            parts.append("")
            parts.append(cat["comparison_en"])
            parts.append("")
    parts += [
        "## Disclaimer",
        "",
        "Costs, lead times, and purchase information change. Confirm prices and licenses with the official project before you buy or build. This directory is not an endorsement of any seller, and it is not legal advice about licenses.",
        "",
        f"_Generated from `data/projects.yaml` by `scripts/generate_readme.py`. Source-check snapshot: {as_of} ({tz})._",
        "",
    ]
    return "\n".join(parts)


def render_zh(data: dict) -> str:
    d = data["directory"]
    groups = grouped(data)
    as_of = data["as_of"]
    tz = data["as_of_timezone"]
    parts = [
        f"# {d['title']}",
        "",
        d["tagline_zh"],
        "",
        "本目录独立、由社区驱动。Cereboto 负责维护这份名单，同时也在 [cereboto.com](https://cereboto.com/) 销售开源具身机器人硬件。商业合作不影响排序，也不会因为竞争关系而排除任何品牌。",
        "",
        f"[English](README.md) · [贡献指南](CONTRIBUTING.zh-CN.md) · [许可证](LICENSE) · 数据：[`data/projects.yaml`](data/projects.yaml)",
        "",
        "## 目录",
        "",
        toc(groups, "zh"),
        "",
        "## 如何组织",
        "",
        "同一类别内，项目按**英文名称字母顺序**排列。这是一条客观规则：星标数、价格、更新时间以及商业关系都不参与排序。",
        "",
        "硬件许可证与软件许可证分开记录，来源是 LICENSE 文件或官方许可证声明。找不到时填写「未知」。",
        "",
        f"仓库活跃度（星标、最近一次提交）记录于 **{as_of}**（{tz}）。YAML 中的提交时间是 UTC，这里转换为 Asia/Shanghai 显示。这些数字会变化，请当作快照。",
        "",
        "## 收录标准",
        "",
        "同时满足以下条件的项目可以收录：",
        "",
        "1. 属于**具身机器人**及相关装置（在物理世界中感知并执行动作的机器人或紧密耦合设备，包括机械臂、灵巧手、移动底座、腿式机器人、遥操作与数据采集硬件、教学平台，以及密切相关的传感器或表情/面部硬件）。",
        "2. **设计文件和/或源代码已公开**，或官方维护者已宣布可获取的开源发布。仅有论文或宣传页，不足以作为已确认条目。",
        "3. 条目能指向**一手来源**（官方仓库、文档或机构页面）。",
        "4. 不能仅仅为了宣传闭源产品而收录。",
        "",
        "接近符合条件、但未能找到公开设计文件的项目，可以保留并标为**未核实**，同时写明缺口，避免悄悄漏掉，或把尚未开源的项目写成已开源。",
        "",
        "本初稿先从一份公开项目索引播种，再对照一手来源核对。欢迎通过 Pull Request 增补、勘误、调整分类或移除条目。详见 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。",
        "",
        "## 核实等级",
        "",
    ]
    for level in data["verification_levels"]:
        parts.append(f"- **{level['title_zh']}** — {level['definition_zh']}")
    parts += [
        "",
        "本初稿中没有任何条目属于「官方核实」或「社区核实」。大多数条目是「已对源核查」：我们查阅了公开的一手来源，但项目维护者尚未确认条目文本。",
        "",
        "## 披露政策",
        "",
        "Cereboto 销售本名单中部分项目的套件或整机。这些条目会在表格中披露。Cereboto 没有特殊位次，排序规则同样是字母顺序。本目录中的购买链接仅包括官方或上游来源（项目自己的商店、官方文档或 BOM、或官方制造商商店），以及 Cereboto 确实在售时的 Cereboto 产品页。这并不表示不存在其他商家。是否为 Cereboto 在售产品，不影响排序或收录资格。",
        "",
        "## 本目录的许可证",
        "",
        "本目录的文本（YAML 数据、生成的 README、贡献指南和 Issue/PR 模板）使用 [CC BY 4.0](LICENSE) 许可。生成脚本 `scripts/generate_readme.py` 使用 [MIT 许可证](LICENSE-CODE)。上述许可不改变被收录项目自身的许可证。",
        "",
    ]
    for cat, items in groups:
        parts.append(f"## {cat['title_zh']}")
        parts.append("")
        if not items:
            parts.append(cat.get("empty_zh") or "_当前数据文件中，本类别还没有项目。_")
            parts.append("")
            continue
        parts.append(render_table(items, "zh"))
        parts.append("")
        if cat.get("comparison_zh"):
            parts.append("### 对比分析")
            parts.append("")
            parts.append(cat["comparison_zh"])
            parts.append("")
    parts += [
        "## 免责声明",
        "",
        "成本、交期和购买信息都会变化。购买或动手制作前，请向官方项目核实价格与许可证。本目录不构成对任何卖方的背书，也不构成许可证方面的法律意见。",
        "",
        f"_由 `scripts/generate_readme.py` 根据 `data/projects.yaml` 生成。对源核查快照：{as_of}（{tz}）。_",
        "",
    ]
    return "\n".join(parts)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check that generated READMEs are up to date")
    args = parser.parse_args(argv)

    data = load()
    outputs = {
        ROOT / "README.md": render_en(data),
        ROOT / "README.zh-CN.md": render_zh(data),
    }
    if args.check:
        stale = []
        for path, text in outputs.items():
            existing = path.read_text(encoding="utf-8") if path.exists() else ""
            if existing != text:
                stale.append(str(path))
        if stale:
            print("Out of date:", ", ".join(stale), file=sys.stderr)
            return 1
        print("READMEs are up to date.")
        return 0

    for path, text in outputs.items():
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
