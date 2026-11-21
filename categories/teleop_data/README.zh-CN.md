# 遥操作与数据采集装置

本页是 [Awesome Open Embodied Robotics](../../README.zh-CN.md) 的一部分，提供本类别的逐字段对照表和简短对比分析。整体清单见[首页](../../README.zh-CN.md)。

[English](README.md) · [贡献指南](../../CONTRIBUTING.zh-CN.md) · [许可证](../../LICENSE) · 数据：[`data/projects.yaml`](../../data/projects.yaml)

本类别内项目按**英文名称字母顺序**排列。星标数、价格、更新时间和商业关系都不参与排序。

硬件许可证与软件许可证分开记录，来源是 LICENSE 文件或官方许可证声明。找不到时填写「未知」。

仓库活跃度（星标、最近一次提交）记录于 **2026-11-21**（Asia/Shanghai）。YAML 中的提交时间是 UTC，这里转换为 Asia/Shanghai 显示。这些数字会变化，请当作快照。

## 对照表

| 图片 | 项目 | 维护者 | 简介 | 自由度 / 规格 | 电机与通信 | 约略 BOM 成本 | 软件生态 | 许可证（硬件 / 软件） | 仓库活跃度 | 购买渠道 | 核实状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <img src="https://dex-umi.github.io/static/images/teaser.png" alt="DexUMI" width="120"> | [DexUMI](https://dex-umi.github.io/)<br>([仓库](https://github.com/real-stanford/DexUMI)) | REAL lab collaborators (Stanford, Columbia, JPMorgan AI Research, CMU, and NVIDIA affiliations on the source index) | 将人手作为通用操作接口、用于采集灵巧操作数据的系统，提供开源软件和硬件说明。 | 未知 | 未知<br>通信：未知 | 未知 | 未知 | 硬件: 未知<br>软件: MIT | 星标 280<br>最近提交 2026-04-19 07:04 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |
| <img src="https://do-glove.github.io/static/images/glove_explosion.png" alt="DOGlove" width="120"> | [DOGlove](https://do-glove.github.io/)<br>([仓库](https://github.com/TEA-Lab/DOGlove)) | TEA Lab (Tsinghua University and collaborators listed on the source index) | 面向灵巧遥操作与数据采集的低成本开源力反馈手套（RSS 2025）。 | 5 (source index technical specs; official site/docs should be used to confirm before building) | ROBOTIS Dynamixel (official README installation includes Dynamixel Wizard)<br>通信：Dynamixel bus | 未知 | 未知 | 硬件: 未知<br>软件: MIT | 星标 148<br>最近提交 2026-04-19 06:45 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |
| <img src="https://wuphilipp.github.io/gello_site/static/images/teaser_final.png" alt="GELLO" width="120"> | [GELLO](https://wuphilipp.github.io/gello_site/)<br>([仓库](https://github.com/wuphilipp/gello_software)) | Philipp Wu and collaborators (UC Berkeley) | 面向机械臂的通用、低成本遥操作框架，基于 Dynamixel，软件与机械结构分仓库开源。 | 未知 | ROBOTIS Dynamixel<br>通信：Dynamixel bus | 未知 | 未知 | 硬件: MIT<br>软件: MIT | 星标 566<br>最近提交 2026-11-09 22:16 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |
| <img src="https://behavior-robot-suite.github.io/assets/img/system_overview.png" alt="JoyLo" width="120"> | [JoyLo](https://behavior-robot-suite.github.io/)<br>([仓库](https://github.com/behavior-robot-suite/brs-ctrl)) | BEHAVIOR Robot Suite authors (Stanford University affiliation on the source index) | BEHAVIOR Robot Suite 中用于全身家务操作数据采集的遥操作/主动端装置，官方控制仓库中提供硬件文件。 | 未知 | ROBOTIS Dynamixel (source index)<br>通信：Dynamixel bus | 未知 | 未知 | 硬件: 未知<br>软件: MIT | 星标 148<br>最近提交 2025-11-18 15:34 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |
| <img src="https://raw.githubusercontent.com/InternRobotics/OpenHomie/main/teaser.png" alt="OpenHomie" width="120"> | [OpenHomie](https://homietele.github.io/)<br>([仓库](https://github.com/InternRobotics/OpenHomie)) | OpenHomie / HOMIE authors (Shanghai AI Lab and CUHK affiliations on the source index; repository now under InternRobotics) | HOMIE 的开源软件与硬件：面向人形机器人运动-操作遥操作的同构外骨骼座舱。 | 未知 | ROBOTIS Dynamixel (source index)<br>通信：Dynamixel bus | 未知 | 未知 | 硬件: See notes<br>软件: See notes | 星标 625<br>最近提交 2026-09-09 04:28 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |
| <img src="https://specialist-ai.github.io/specialist-docs/manuals/handheld/cover.png" alt="Specialist" width="120"> | [Specialist](https://specialist-ai.github.io/)<br>([仓库](https://github.com/specialist-ai/specialist)) | Yufeng Chi, Qiayuan Liao, and collaborators (UC Berkeley / Hybrid Robotics) | 面向大规模采集机器人训练数据的手持/主动夹爪接口。手持夹爪用 Insta360 相机和打印标记记录示范，同几何的主动夹爪把策略部署到机械臂上，无需重定向。 | Two coupled finger joints (1:1 gear); the actuated variant is driven by one servo on the right finger (official description repository)<br>Handheld: 177 × 94 × 115 mm, 315 g with camera, official cost USD 320. Actuated: 480 g, official cost USD 380. Camera is Insta360 X3 (2880 × 2880 per lens, 30 fps). Official site reports median tracking error of 3.0 mm and new-location setup in 30 seconds or less. | Handheld is finger-driven with a return spring (no servo). Actuated variant uses a Feetech STS3215 12 V servo.<br>通信：Handheld is standalone (no computer, cable, or tracking system while recording). Actuated variant uses a Feetech STS serial bus (STS3215 plus a serial bus servo driver board, official BOM). | Official site lists USD 320 per handheld gripper and USD 380 per actuated gripper | MuJoCo, ROS 2 | 硬件: 未知<br>软件: MIT | 星标 85<br>最近提交 2026-11-09 07:07 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |
| <img src="https://vision-in-action.github.io/images/teaser_v2.5.png" alt="ViA" width="120"> | [ViA](https://vision-in-action.github.io/)<br>([仓库](https://github.com/haoyu-x/vision-in-action)) | Stanford University (Vision in Action authors) | Vision in Action：开源主动感知系统，公开硬件重点是机器人颈部，并与 ARX 机械臂和 ROS 一起用于基于演示的学习。 | 未知 | Unknown (used with ARX arms; neck actuators not summarized as a single official SKU in the README section we opened)<br>通信：USB-CAN mentioned for ARX arm setup in the official README | 未知 | ROS | 硬件: 未知<br>软件: MIT | 星标 150<br>最近提交 2026-04-22 11:01 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |

## 对比分析

GELLO、JoyLo 和 OpenHomie 是用于采集操作数据的主动端或同构遥操作系统，大多基于 Dynamixel。GELLO 的软件与机械仓库均为 MIT。OpenHomie 的 LICENSE 文件是 CC BY-NC 4.0，但其 README 写的是 CC BY-NC-SA 4.0——两者都照实记录。DOGlove 是力反馈手套（官方材料：5 自由度、Dynamixel，仓库 MIT；源网站列出的 4500 未写明币种，本目录未采用该数字）。DexUMI 把人手当作灵巧操作的数据采集接口（软件 MIT）。Specialist 是面向采集机器人训练数据的 UMI 式手持与主动夹爪。官方网站列出的成本为每个手持夹爪 320 美元、每个主动夹爪 380 美元。软件许可证为 MIT。没有找到单独的官方硬件设计许可证，因此硬件许可证记为「未知」。ViA（Vision in Action）在源网站被标成轮式机器人，但官方材料描述的是主动感知系统，公开硬件重点是机器人颈部，并与 ARX 机械臂和 ROS 配合；因此放到本类，而不是移动操作机器人。

## 免责声明

成本、交期和购买信息都会变化。购买或动手制作前，请向官方项目核实价格与许可证。本目录不构成对任何卖方的背书，也不构成许可证方面的法律意见。

_由 `scripts/generate_readme.py` 根据 `data/projects.yaml` 生成。对源核查快照：2026-11-21（Asia/Shanghai）。_
