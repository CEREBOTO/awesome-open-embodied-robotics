# 单臂 / 双臂机械臂

本页是 [Awesome Open Embodied Robotics](../../README.zh-CN.md) 的一部分，提供本类别的逐字段对照表和简短对比分析。整体清单见[首页](../../README.zh-CN.md)。

[English](README.md) · [贡献指南](../../CONTRIBUTING.zh-CN.md) · [许可证](../../LICENSE) · 数据：[`data/projects.yaml`](../../data/projects.yaml)

本类别内项目按**英文名称字母顺序**排列。星标数、价格、更新时间和商业关系都不参与排序。

硬件许可证与软件许可证分开记录，来源是 LICENSE 文件或官方许可证声明。找不到时填写「未知」。

仓库活跃度（星标、最近一次提交）记录于 **2026-11-21**（Asia/Shanghai）。YAML 中的提交时间是 UTC，这里转换为 Asia/Shanghai 显示。这些数字会变化，请当作快照。

## 对照表

| 图片 | 项目 | 维护者 | 简介 | 自由度 / 规格 | 电机与通信 | 约略 BOM 成本 | 软件生态 | 许可证（硬件 / 软件） | 仓库活跃度 | 购买渠道 | 核实状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <img src="https://martinpeticco.com/dexwrist/static/images/gearboxregular.png" alt="DexWrist" width="120"> | [DexWrist](https://martinpeticco.com/dexwrist/) | Improbable AI Lab, MIT | 紧凑的 2 自由度准直驱机器人腕部（俯仰-偏航），面向狭窄空间和接触丰富的操作，定位为现有机械臂的可替换升级。 | 2 (pitch–yaw); roll is assumed to come from the upstream arm<br>Official paper: 0.97 kg; ±40° ROM in both DoFs; rated torque 3.75±0.05 Nm. Official project page: measured no-load speed 96.6±9.4 rpm. | CubeMars GL40 with 13:1 planetary gearboxes (paper)<br>通信：未知 | 未知 | 未知 | 硬件: 未知<br>软件: 未知 | 星标 未知<br>最近提交 未知<br>统计截至 2026-11-21 | 未知 | 未核实 |
| <img src="https://openarm.dev/images/img_introducing_v2.webp" alt="OpenArm" width="120"> | [OpenArm](https://openarm.dev/)<br>([仓库](https://github.com/enactic/openarm)) | Enactic (OpenArm project) | 完全开源的人体尺度机械臂平台，每臂 7 自由度、准直驱，面向接触丰富的遥操作、模仿学习和具身智能研究，通常以双臂系统部署。 | 7 per arm<br>Official docs: nominal payload 4.1 kg, peak 6.0 kg per arm; aluminum + stainless structure; CAN-FD control | DAMIAO DM-J8009P-2EC, DM4340 series, and DM-J4310-2EC (OpenArm 2.0 motor page, updated 2026-11-16). The DM4340 series is not a quasi-direct-drive motor. Earlier docs placed DM-J8009P-2EC on J1/J2 and the 4340 series and DM-J4310-2EC on later joints; the current page text does not restate that placement.<br>通信：CAN-FD / SocketCAN | About USD 6,500 for a complete bimanual system (official GitHub README). | ROS 2, MoveIt, MuJoCo, Isaac Lab, LeRobot | 硬件: CERN-OHL-S-2.0<br>软件: Apache-2.0 | 星标 3714<br>最近提交 2026-11-16 12:45 (Asia/Shanghai)<br>统计截至 2026-11-21 | [Official purchase page](https://docs.openarm.dev/purchase/) (Official project documentation)<br>[Cereboto](https://cereboto.com/product/openarm-2-robotic-arm-kit/) (Also sells V1.1, Mini, Cell, and KER) | 已对源核查 |
| <img src="https://raw.githubusercontent.com/TheRobotStudio/SO-ARM100/main/media/SO101_Follower.webp" alt="SO-101" width="120"> | [SO-101](https://github.com/TheRobotStudio/SO-ARM100) | The Robot Studio, in collaboration with Hugging Face | 低成本 3D 打印主从机械臂（SO-100 的后继型号），面向与 LeRobot 软件栈配合的模仿学习和遥操作。 | 6 arm DoF plus gripper (leader and follower each use a set of Feetech STS3215 servos; official parts table)<br>Leader and follower pair; follower STS3215 offered in 7.4 V and 12 V variants | Feetech STS3215 bus servos<br>通信：Feetech STS serial bus (TTL-style servo bus) | Unknown as a single official DIY total. Official README publishes a parts table and also mentions commercial kits. | LeRobot | 硬件: Apache-2.0<br>软件: Apache-2.0 | 星标 8178<br>最近提交 2026-11-20 23:10 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |
| <img src="https://raw.githubusercontent.com/roboninecom/SO-ARM102/main/assets/images/photos/so-arm-102-live.jpg" alt="SO-ARM 102" width="120"> | [SO-ARM 102](https://github.com/roboninecom/SO-ARM102) | Robonine | 开源主从机械臂套件，面向遥操作和模仿学习；每臂 5 自由度外加平行夹爪，是 SO-ARM 100/101 的后继型号，可与 LeRobot 配合使用。 | 5 arm DoF plus gripper (official README)<br>Parallel gripper with 85 mm span; rated payload 300 g; horizontal reach 483 mm and 473 mm behind the base; base rotation 352°. Standard kit is one leader and one follower; two kits can be used as a bimanual setup. Official comparison with SO-ARM 101 is in the project README and docs/specifications.md. | Follower uses 2× Feetech STS3235, 2× STS3250, and 2× STS3215; leader uses 6× STS3215 (official README)<br>通信：Feetech STS serial bus via a Waveshare Bus Servo Adapter (official README) | Official DIY budget about USD 342 for components, or about USD 388 including printing material (README cites USD 342.4 / USD 388.4 before shipping and taxes) | LeRobot | 硬件: CERN-OHL-P-2.0<br>软件: Apache-2.0 | 星标 289<br>最近提交 2026-11-19 17:50 (Asia/Shanghai)<br>统计截至 2026-11-21 | [Official kit](https://robonine.com/shop/so-arm102-robotic-arm-kit/) (Official manufacturer store of the project maintainer) | 已对源核查 |

## 对比分析

这一批机械臂其实处在三个不同层。SO-101 是围绕飞特 STS3215 总线舵机和 LeRobot 软件栈的低成本 3D 打印主从臂。SO-ARM 102 由 Robonine 维护，是同一低成本主从层中 SO-ARM 100 与 SO-101 的后继型号，可与 LeRobot 配合使用。每臂 5 自由度外加平行夹爪（跨度 85 毫米），额定负载 300 克，水平伸展 483 毫米（底座后方 473 毫米）。官方 DIY 预算约为零件 342 美元，或含打印材料约 388 美元。硬件设计为 CERN-OHL-P-2.0，软件为 Apache-2.0。GitHub 许可证 API 将仓库显示为 CC-BY-4.0，对应文档许可。OpenArm 是人体尺度、每臂 7 自由度的准直驱平台，控制总线为 CAN-FD，官方README 给出完整双臂系统约 6,500 美元，许可证划分清楚（硬件 CERN-OHL-S-2.0，软件 Apache-2.0）。DexWrist 是 2 自由度研究用腕部，定位为可替换的俯仰-偏航关节；但在本次对源核查之日，我们没有找到公开的 CAD 或固件仓库，开源状态尚未确认。

## 免责声明

成本、交期和购买信息都会变化。购买或动手制作前，请向官方项目核实价格与许可证。本目录不构成对任何卖方的背书，也不构成许可证方面的法律意见。

_由 `scripts/generate_readme.py` 根据 `data/projects.yaml` 生成。对源核查快照：2026-11-21（Asia/Shanghai）。_
