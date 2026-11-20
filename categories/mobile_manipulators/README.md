# Mobile manipulators

This page is part of [Awesome Open Embodied Robotics](../../README.md). It contains the field-by-field comparison table and short comparison notes for this category. For the overall inventory, see the [homepage](../../README.md).

[简体中文](README.zh-CN.md) · [Contributing](../../CONTRIBUTING.md) · [License](../../LICENSE) · Data: [`data/projects.yaml`](../../data/projects.yaml)

Projects in this category are sorted **alphabetically by English name**. Star counts, price, recency, and commercial relationships are not used for ranking.

Hardware licenses and software licenses are recorded separately, from LICENSE files or official license statements. If a license could not be found, the field is `Unknown`.

Repository activity (stars and last commit) was recorded on **2026-11-20** (Asia/Shanghai). Commit timestamps are stored in UTC in the YAML and displayed here in Asia/Shanghai. Figures change; treat them as a snapshot.

## Comparison table

| Image | Project | Maintainer | Description | DoF / key specs | Motors & comms | Approx. BOM cost | Software ecosystem | Licenses (hardware / software) | Repo activity | Purchase channels | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <img src="https://aha-robot.github.io/static/images/hardware.png" alt="AhaRobot" width="120"> | [AhaRobot](https://aha-robot.github.io/)<br>([repo](https://github.com/hilookas/astra_ws)) | Tianjin University (AhaRobot authors) | A low-cost open bimanual mobile manipulator for embodied-AI research, with separate software and hardware repositories. | Unknown | Feetech servos (source and official materials)<br>Comms: Unknown | Unknown | ROS | HW: GPL-3.0<br>SW: GPL-3.0 | 25 stars<br>Last commit 2026-10-12 20:22 (Asia/Shanghai)<br>As of 2026-11-20 | Unknown | Source-checked |
| <img src="https://tidybot2.github.io/images/og-image.jpg" alt="TidyBot++" width="120"> | [TidyBot++](https://tidybot2.github.io/)<br>([repo](https://github.com/jimmyyhwu/tidybot2)) | Jimmy Wu and collaborators (Princeton, Stanford, Dexterity affiliations on the source index) | An open holonomic (swerve-drive) mobile manipulator for robot learning, with a published BOM and support for interchangeable commercial arms. | Mobile base plus a swappable arm (official reference designs: Kinova Gen3 7-DoF, Franka, or ARX5)<br>Holonomic MK4 swerve modules; official Kinova-tab mobile-base BOM total USD 5,379.63, excluding the arm and some compute items listed without a price | 8× Kraken X60 (drive system) plus the chosen arm's own actuators<br>Comms: CAN (CTRE / Phoenix-style drive stack; official BOM has a CAN system section) | Mobile base USD 5,379.63 on the official Kinova BOM tab (as published on the docs page). Complete system cost depends on the arm (Kinova/Franka/ARX5) and is not a single official total. | ROS 2 | HW: Unknown<br>SW: MIT | 626 stars<br>Last commit 2025-03-27 11:31 (Asia/Shanghai)<br>As of 2026-11-20 | Unknown | Source-checked |
| <img src="https://github.com/user-attachments/assets/682ef049-bb42-4b50-bf98-74d6311e774d" alt="XLeRobot" width="120"> | [XLeRobot](https://github.com/Vector-Wangel/XLeRobot) | Vector-Wangel | A practical dual-arm mobile home robot that combines two SO-101 arms with an omni-wheel base, aimed at household manipulation at a low official BOM cost. | Two SO-101 arms plus an omni-wheel base and a 2-DoF neck (official README)<br>Official basic configuration uses a laptop and a single RGB head camera; optional Pi / RealSense upgrades are priced separately | Feetech STS3215 (17 servos in official BOM materials: 12 for two SO-101 arms, 3 for the omni-wheel base, 2 for the head)<br>Comms: Feetech STS serial bus | About USD 660 / EUR 680 / CNY 3,999 for the basic configuration; excludes 3D printing, tools, shipping, and taxes (official README) | LeRobot | HW: Apache-2.0<br>SW: Apache-2.0 | ≈5.8k stars<br>Last commit 2026-11-17 01:55 (Asia/Shanghai)<br>As of 2026-11-20 | Unknown | Source-checked |

## Comparison

Cost and arm choice dominate the differences. XLeRobot is explicitly a dual SO-101 plus omni-wheel home robot; the official README gives a basic BOM around USD 660 (excluding printing, tools, shipping, and tax) and sits in the LeRobot ecosystem. AhaRobot is a low-cost bimanual mobile manipulator from Tianjin University, with Feetech actuation and GPL-3.0 hardware and software repositories; an official single-number BOM was not confirmed in the pages we opened. TidyBot++ is a holonomic swerve-drive research mobile base (Kraken X60 / CAN) designed to carry interchangeable arms (Kinova, Franka, or ARX5 in the official BOM). The official Kinova-tab mobile-base total is USD 5,379.63, not including the arm itself, so a complete system price depends on which arm you mount.

## Disclaimer

Costs, lead times, and purchase information change. Confirm prices and licenses with the official project before you buy or build. This directory is not an endorsement of any seller, and it is not legal advice about licenses.

_Generated from `data/projects.yaml` by `scripts/generate_readme.py`. Source-check snapshot: 2026-11-20 (Asia/Shanghai)._
