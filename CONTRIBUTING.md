# Contributing

Thank you for helping keep this directory accurate. The list is independent and community-driven. Cereboto maintains the repository and also sells open-source embodied-robot hardware; that does not change how contributions are reviewed.

Please read this guide before opening an issue or pull request. A Chinese version is in [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md).

## What to change

`data/projects.yaml` is the single source of truth. Do not edit `README.md`, `README.zh-CN.md`, or the files under `categories/` by hand. After you change the YAML (or the generator), run:

```bash
pip install -r requirements.txt
python scripts/generate_readme.py
```

Include the regenerated root and category READMEs in the same pull request. English and Chinese pages must stay in sync.

The data schema is documented in [`data/schema.md`](data/schema.md).

## Inclusion criteria

A project can be listed when all of the following hold:

1. It is an **open-source robot hardware** project — a robot or tightly coupled device that senses and acts in the physical world, including arms, hands, mobile bases, legged robots, teleoperation and data-collection hardware, educational platforms, and closely related sensors or face/expression hardware.
2. **Design files and/or source code are publicly available**, or the official maintainer has announced a public open-source release whose files can be retrieved. A paper or marketing page alone is not enough for a confirmed listing.
3. The listing can point to a **primary source** (official repository, documentation, or organization page).
4. The project is not listed solely to advertise a closed product.

This directory focuses on open-source robot hardware. Software stacks that a listed project officially uses may be recorded in that project's `software_ecosystem` field.

If a project almost qualifies but public design files cannot be found, it may be submitted as **Unverified** with an explicit note. Do not invent a repository or a license to make it look complete.

## Verification levels

- **Official verified** — A maintainer or official organization of the project has confirmed this directory entry (for example by commenting on a tracking issue or submitting a confirmation pull request).
- **Community verified** — An independent contributor has checked the entry against a physical build, or has provided dated evidence that goes beyond reading public pages.
- **Source-checked** — Maintainers of this directory have checked the listed claims against public primary sources (official repository, documentation, or vendor pages) on a stated as-of date. This is not confirmation by the project maintainer, and it is not a reproduction of the hardware.
- **Unverified** — The entry is newly submitted, or key claims (including whether design files are publicly released) could not be confirmed from public primary sources.

New community submissions start as **Unverified** unless the pull request already includes a source-check (URLs for each claim) and the reviewer agrees to raise it to **Source-checked**. Do not mark your own project **Official verified** without a public confirmation from the official maintainer. Do not mark an entry **Community verified** only because you read the website.

## Ranking rule

Within each category, projects are sorted **alphabetically by English name**. Star counts, price, recency, and commercial relationships are not used for ranking. If you want a project to appear in a different place, rename it only if that is the project's real name, or propose a documented change to the rule — do not insert dummy prefixes.

## Disclosure policy

If you, your employer, or a vendor you represent sells, sponsors, or officially partners on a listed project, say so in the `disclosure` field and in the pull request. Cereboto-sold or Cereboto-partner projects must use a clear disclosure such as `Disclosure: sold by Cereboto`. Commercial partnerships do not affect ranking, and no brand is excluded for competitive reasons. Purchase channels, when listed, should be official or upstream sources only: the project's own shop, official documentation or BOM, or an official manufacturer store. A Cereboto product page may be listed only for products Cereboto actually sells, with that disclosure. Do not list third-party, peer, or competitor vendors. This is a listing choice, not a claim that no other sellers exist.

## How to add a project

1. Open a [New project](.github/ISSUE_TEMPLATE/new-project.yml) issue, or go straight to a pull request if you already have the YAML fields.
2. Fill the schema fields. Use the literal `Unknown` when you cannot find a fact. Never guess a license, a cost, or a degree-of-freedom count.
3. Record **hardware** and **software** licenses separately, from LICENSE files or official license statements, and link those sources.
4. List official or upstream purchase links when they exist (the project's own shop, official documentation or BOM, or an official manufacturer store). Include a Cereboto product page only when Cereboto actually sells the product, with a disclosure. Do not list third-party or peer vendors.
5. Set `verification_status` honestly.
6. Regenerate the root and category READMEs and open the pull request with the [PR template](.github/PULL_REQUEST_TEMPLATE.md).

## How to correct an entry

Open a [Correction](.github/ISSUE_TEMPLATE/correction.yml) issue or a pull request. Quote the current text, the proposed text, and the primary source URL. If a cost or star count has changed, update the `as_of` date (or the per-project `repo_activity_as_of`) as well.

## Style

- Keep descriptions short and factual.
- Keep English and Chinese fields in sync.
- Do not copy unverified numbers from third-party indexes. If a currency is not stated, do not invent one.

## License of contributions

By contributing, you agree that your changes to the list (including YAML data, generated README text, contributing guides, and issue/PR templates) may be released under [CC BY 4.0](LICENSE). Changes to the generator script may be released under the MIT License (see [LICENSE-CODE](LICENSE-CODE)). You also certify that you have the right to submit the material and that you are not pasting another person's copyrighted text verbatim. These licenses do not change the licenses of the listed projects.
