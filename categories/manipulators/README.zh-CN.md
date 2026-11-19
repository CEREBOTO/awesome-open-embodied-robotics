# 单臂 / 双臂机械臂

本页是 [Awesome Open Embodied Robotics](../../README.zh-CN.md) 的一部分，提供本类别的逐字段对照表和简短对比分析。整体清单见[首页](../../README.zh-CN.md)。

[English](README.md) · [贡献指南](../../CONTRIBUTING.zh-CN.md) · [许可证](../../LICENSE) · 数据：[`data/projects.yaml`](../../data/projects.yaml)

本类别内项目按**英文名称字母顺序**排列。星标数、价格、更新时间和商业关系都不参与排序。

硬件许可证与软件许可证分开记录，来源是 LICENSE 文件或官方许可证声明。找不到时填写「未知」。

仓库活跃度（星标、最近一次提交）记录于 **2026-11-20**（Asia/Shanghai）。YAML 中的提交时间是 UTC，这里转换为 Asia/Shanghai 显示。这些数字会变化，请当作快照。

## 对照表

| 项目 | 维护者 | 简介 | 自由度 / 规格 | 电机与通信 | 约略 BOM 成本 | 软件生态 | 许可证（硬件 / 软件） | 仓库活跃度 | 购买渠道 | 核实状态 | 披露 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [DexWrist](https://dexwrist.csail.mit.edu/) | Improbable AI Lab, MIT | 紧凑的 2 自由度准直驱机器人腕部（俯仰-偏航），面向狭窄空间和接触丰富的操作，定位为现有机械臂的可替换升级。 | 2 (pitch–yaw); roll is assumed to come from the upstream arm<br>Official paper: 0.97 kg; ±40° ROM in both DoFs; rated torque 3.75±0.05 Nm | CubeMars GL40 with 13:1 planetary gearboxes (paper)<br>通信：未知 | 未知 | 未知 | 硬件: 未知<br>软件: 未知 | 星标 未知<br>最近提交 未知<br>统计截至 2026-11-20 | 未知 | 未核实 | — |
| [OpenArm](https://openarm.dev/)<br>([仓库](https://github.com/enactic/openarm)) | Enactic (OpenArm project) | 完全开源的人体尺度机械臂平台，每臂 7 自由度、准直驱，面向接触丰富的遥操作、模仿学习和具身智能研究，通常以双臂系统部署。 | 7 per arm<br>Official docs: nominal payload 4.1 kg, peak 6.0 kg per arm; aluminum + stainless structure; CAN-FD control | DAMIAO QDD motors (official hardware docs: DM-J8009P-2EC on J1/J2, DM-J4340 series and DM-J4310-2EC on later joints)<br>通信：CAN-FD / SocketCAN | About USD 6,500 for a complete bimanual system (official GitHub README). | ROS 2, MoveIt, MuJoCo, Isaac Lab, LeRobot | 硬件: CERN-OHL-S-2.0<br>软件: Apache-2.0 | 星标 ≈3.7k<br>最近提交 2026-11-16 12:45 (Asia/Shanghai)<br>统计截至 2026-11-20 | [Official purchase page](https://docs.openarm.dev/purchase/) (Official project documentation)<br>[Cereboto](https://cereboto.com/product/openarm-2-robotic-arm-kit/) (Also sells V1.1, Mini, Cell, and KER)<br>[DIY from official CAD/BOM](https://github.com/enactic/openarm_hardware) (Self-sourced build) | 已对源核查 | Disclosure: sold by Cereboto<br>（Cereboto 有销售该项目相关产品） |
| [SO-101](https://github.com/TheRobotStudio/SO-ARM100) | The Robot Studio, in collaboration with Hugging Face | 低成本 3D 打印主从机械臂（SO-100 的后继型号），面向与 LeRobot 软件栈配合的模仿学习和遥操作。 | 6 arm DoF plus gripper (leader and follower each use a set of Feetech STS3215 servos; official parts table)<br>Leader and follower pair; follower STS3215 offered in 7.4 V and 12 V variants | Feetech STS3215 bus servos<br>通信：Feetech STS serial bus (TTL-style servo bus) | Unknown as a single official DIY total. Official README publishes a parts table and also mentions commercial kits. | LeRobot | 硬件: Apache-2.0<br>软件: Apache-2.0 | 星标 ≈8.2k<br>最近提交 2026-10-06 15:26 (Asia/Shanghai)<br>统计截至 2026-11-20 | [Official parts table (DIY)](https://github.com/TheRobotStudio/SO-ARM100) (Self-sourced BOM in the README) | 已对源核查 | — |

## 对比分析

这一批机械臂其实处在三个不同层。SO-101 是围绕飞特 STS3215 总线舵机和 LeRobot 软件栈的低成本 3D 打印主从臂。OpenArm 是人体尺度、每臂 7 自由度的准直驱平台，控制总线为 CAN-FD，官方README 给出完整双臂系统约 6,500 美元，许可证划分清楚（硬件 CERN-OHL-S-2.0，软件 Apache-2.0）。DexWrist 是 2 自由度研究用腕部，定位为可替换的俯仰-偏航关节；但在本次对源核查之日，我们没有找到公开的 CAD 或固件仓库，开源状态尚未确认。

## 免责声明

成本、交期和购买信息都会变化。购买或动手制作前，请向官方项目核实价格与许可证。本目录不构成对任何卖方的背书，也不构成许可证方面的法律意见。

_由 `scripts/generate_readme.py` 根据 `data/projects.yaml` 生成。对源核查快照：2026-11-20（Asia/Shanghai）。_
