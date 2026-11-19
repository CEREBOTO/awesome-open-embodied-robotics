# Single-arm / dual-arm manipulators

This page is part of [Awesome Open Embodied Robotics](../../README.md). It contains the field-by-field comparison table and short comparison notes for this category. For the overall inventory, see the [homepage](../../README.md).

[简体中文](README.zh-CN.md) · [Contributing](../../CONTRIBUTING.md) · [License](../../LICENSE) · Data: [`data/projects.yaml`](../../data/projects.yaml)

Projects in this category are sorted **alphabetically by English name**. Star counts, price, recency, and commercial relationships are not used for ranking.

Hardware licenses and software licenses are recorded separately, from LICENSE files or official license statements. If a license could not be found, the field is `Unknown`.

Repository activity (stars and last commit) was recorded on **2026-11-20** (Asia/Shanghai). Commit timestamps are stored in UTC in the YAML and displayed here in Asia/Shanghai. Figures change; treat them as a snapshot.

## Comparison table

| Project | Maintainer | Description | DoF / key specs | Motors & comms | Approx. BOM cost | Software ecosystem | Licenses (hardware / software) | Repo activity | Purchase channels | Verification | Disclosure |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [DexWrist](https://dexwrist.csail.mit.edu/) | Improbable AI Lab, MIT | A compact 2-DoF quasi-direct-drive robotic wrist (pitch–yaw) for constrained and contact-rich manipulation, presented as a drop-in upgrade for existing arms. | 2 (pitch–yaw); roll is assumed to come from the upstream arm<br>Official paper: 0.97 kg; ±40° ROM in both DoFs; rated torque 3.75±0.05 Nm | CubeMars GL40 with 13:1 planetary gearboxes (paper)<br>Comms: Unknown | Unknown | Unknown | HW: Unknown<br>SW: Unknown | Unknown stars<br>Last commit Unknown<br>As of 2026-11-20 | Unknown | Unverified | — |
| [OpenArm](https://openarm.dev/)<br>([repo](https://github.com/enactic/openarm)) | Enactic (OpenArm project) | A fully open-source, human-scale 7-DoF-per-arm quasi-direct-drive platform for contact-rich teleoperation, imitation learning, and physical AI research, typically deployed as a bimanual system. | 7 per arm<br>Official docs: nominal payload 4.1 kg, peak 6.0 kg per arm; aluminum + stainless structure; CAN-FD control | DAMIAO QDD motors (official hardware docs: DM-J8009P-2EC on J1/J2, DM-J4340 series and DM-J4310-2EC on later joints)<br>Comms: CAN-FD / SocketCAN | About USD 6,500 for a complete bimanual system (official GitHub README). | ROS 2, MoveIt, MuJoCo, Isaac Lab, LeRobot | HW: CERN-OHL-S-2.0<br>SW: Apache-2.0 | ≈3.7k stars<br>Last commit 2026-11-16 12:45 (Asia/Shanghai)<br>As of 2026-11-20 | [Official purchase page](https://docs.openarm.dev/purchase/) (Official project documentation)<br>[Cereboto](https://cereboto.com/product/openarm-2-robotic-arm-kit/) (Also sells V1.1, Mini, Cell, and KER)<br>[DIY from official CAD/BOM](https://github.com/enactic/openarm_hardware) (Self-sourced build) | Source-checked | Disclosure: sold by Cereboto |
| [SO-101](https://github.com/TheRobotStudio/SO-ARM100) | The Robot Studio, in collaboration with Hugging Face | A low-cost 3D-printed leader/follower robot arm (successor to SO-100) designed to work with the LeRobot stack for imitation learning and teleoperation. | 6 arm DoF plus gripper (leader and follower each use a set of Feetech STS3215 servos; official parts table)<br>Leader and follower pair; follower STS3215 offered in 7.4 V and 12 V variants | Feetech STS3215 bus servos<br>Comms: Feetech STS serial bus (TTL-style servo bus) | Unknown as a single official DIY total. Official README publishes a parts table and also mentions commercial kits. | LeRobot | HW: Apache-2.0<br>SW: Apache-2.0 | ≈8.2k stars<br>Last commit 2026-10-06 15:26 (Asia/Shanghai)<br>As of 2026-11-20 | [Official parts table (DIY)](https://github.com/TheRobotStudio/SO-ARM100) (Self-sourced BOM in the README) | Source-checked | — |

## Comparison

This first batch covers three very different layers of the arm stack. SO-101 is a low-cost, 3D-printed follower/leader arm built around Feetech STS3215 bus servos and the LeRobot software stack. OpenArm is a human-scale 7-DoF-per-arm quasi-direct-drive platform with a CAN-FD control bus, a stated complete bimanual system price on the order of USD 6,500, and a clearly split license (CERN-OHL-S-2.0 hardware, Apache-2.0 software). DexWrist is a 2-DoF research wrist intended as a drop-in pitch–yaw upgrade, but as of the source-check date we could not find a public CAD or firmware repository, so its open-source status is unconfirmed.

## Disclaimer

Costs, lead times, and purchase information change. Confirm prices and licenses with the official project before you buy or build. This directory is not an endorsement of any seller, and it is not legal advice about licenses.

_Generated from `data/projects.yaml` by `scripts/generate_readme.py`. Source-check snapshot: 2026-11-20 (Asia/Shanghai)._
