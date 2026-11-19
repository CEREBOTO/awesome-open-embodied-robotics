# Desktop / educational robots

This page is part of [Awesome Open Embodied Robotics](../../README.md). It contains the field-by-field comparison table and short comparison notes for this category. For the overall inventory, see the [homepage](../../README.md).

[简体中文](README.zh-CN.md) · [Contributing](../../CONTRIBUTING.md) · [License](../../LICENSE) · Data: [`data/projects.yaml`](../../data/projects.yaml)

Projects in this category are sorted **alphabetically by English name**. Star counts, price, recency, and commercial relationships are not used for ranking.

Hardware licenses and software licenses are recorded separately, from LICENSE files or official license statements. If a license could not be found, the field is `Unknown`.

Repository activity (stars and last commit) was recorded on **2026-11-20** (Asia/Shanghai). Commit timestamps are stored in UTC in the YAML and displayed here in Asia/Shanghai. Figures change; treat them as a snapshot.

## Comparison table

| Project | Maintainer | Description | DoF / key specs | Motors & comms | Approx. BOM cost | Software ecosystem | Licenses (hardware / software) | Repo activity | Purchase channels | Verification | Disclosure |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EchoEar](https://oshwhub.com/esp-college/echoear)<br>([repo](https://github.com/espressif/esp-brookesia/tree/master/examples/echoear)) | Espressif and Coze (乐鑫、扣子), as listed on the source index and the open-hardware page | A desktop AI companion (ESP-VoCat / 喵伴) with a round touch screen, voice interaction, and optional rotating base, published as an open-hardware example in the ESP-Brookesia ecosystem. | Unknown<br>ESP32-S3 class device with 1.85-inch 360×360 round touch screen, 16 MB PSRAM / 16 MB Flash, microSD, Bluetooth LE (official oshwhub page) | Optional rotating base (firmware offered as a separate download on the official page)<br>Comms: Wi-Fi / Bluetooth LE | Unknown | Unknown | HW: GPL-3.0 (as listed on the oshwhub project page)<br>SW: See notes | 853 stars<br>Last commit 2026-11-19 19:18 (Asia/Shanghai)<br>As of 2026-11-20 | [Official oshwhub project (design, BOM, 3D)](https://oshwhub.com/esp-college/echoear) (Open-hardware platform listing) | Source-checked | — |
| [Morpheus](https://jiawenyang-ch.github.io/Morpheus-Hardware-Design/)<br>([repo](https://github.com/ZZongzheng0918/Morpheus-Hardware)) | Morpheus authors (Tsinghua AIR / IIIS, BAAI, MGI Tech, Beihang affiliations on the source index) | A neural-driven animatronic face with hybrid actuation and 33 actuators, released with open hardware and software repositories (RSS 2025). | 33 actuators (official materials and source-index specs)<br>Raspberry Pi 5 as the listed main controller; hybrid rigid and tendon actuation | GuoHua actuators (source index)<br>Comms: Unknown | Unknown | Unknown | HW: MIT<br>SW: MIT | 91 stars<br>Last commit 2025-11-17 17:04 (Asia/Shanghai)<br>As of 2026-11-20 | [Official hardware repo BOM section](https://github.com/ZZongzheng0918/Morpheus-Hardware) (Self-sourced parts) | Source-checked | — |
| [OttoDIY](https://www.ottodiy.com/)<br>([repo](https://github.com/OttoDIY/OttoDIYLib)) | OttoDIY project | A widely used 3D-printable open educational walking robot, with official Arduino libraries and a project website for design and academy materials. | Unknown | Standard hobby servos (exact official SKU not copied from the homepage text we extracted)<br>Comms: Arduino PWM / standard servo interface | Unknown | Unknown | HW: Unknown<br>SW: GPL-3.0 | 218 stars<br>Last commit 2024-05-29 03:32 (Asia/Shanghai)<br>As of 2026-11-20 | [Official website (design / academy / kit paths)](https://www.ottodiy.com/) (The site offers multiple paths for makers and educators) | Source-checked | — |

## Comparison

OttoDIY is a long-running 3D-printed educational walker; the official Arduino library is GPL-3.0, and a separate hardware license file was not confirmed. EchoEar (喵伴 / ESP-VoCat) is a desktop AI companion with a touch screen, not a manipulator, released on an open-hardware platform that lists GPL-3.0; the broader ESP-Brookesia framework is Apache-2.0 according to GitHub's license badge, but a LICENSE file was not found at the repository root paths we tried. Morpheus is a 33-actuator animatronic face (Raspberry Pi 5 in official materials) with MIT-licensed hardware and software repositories; it is not a mobile or manipulation robot, but it is open embodied hardware, so it is kept in this educational / desktop bucket rather than forced into humanoids.

## Disclaimer

Costs, lead times, and purchase information change. Confirm prices and licenses with the official project before you buy or build. This directory is not an endorsement of any seller, and it is not legal advice about licenses.

_Generated from `data/projects.yaml` by `scripts/generate_readme.py`. Source-check snapshot: 2026-11-20 (Asia/Shanghai)._
