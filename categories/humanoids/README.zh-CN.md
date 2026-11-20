# 人形机器人

本页是 [Awesome Open Embodied Robotics](../../README.zh-CN.md) 的一部分，提供本类别的逐字段对照表和简短对比分析。整体清单见[首页](../../README.zh-CN.md)。

[English](README.md) · [贡献指南](../../CONTRIBUTING.zh-CN.md) · [许可证](../../LICENSE) · 数据：[`data/projects.yaml`](../../data/projects.yaml)

本类别内项目按**英文名称字母顺序**排列。星标数、价格、更新时间和商业关系都不参与排序。

硬件许可证与软件许可证分开记录，来源是 LICENSE 文件或官方许可证声明。找不到时填写「未知」。

仓库活跃度（星标、最近一次提交）记录于 **2026-11-20**（Asia/Shanghai）。YAML 中的提交时间是 UTC，这里转换为 Asia/Shanghai 显示。这些数字会变化，请当作快照。

## 对照表

| 图片 | 项目 | 维护者 | 简介 | 自由度 / 规格 | 电机与通信 | 约略 BOM 成本 | 软件生态 | 许可证（硬件 / 软件） | 仓库活跃度 | 购买渠道 | 核实状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <img src="https://lite.berkeley-humanoid.org/static/berkeley-humaonid-lite-cover.png" alt="Berkeley Humanoid Lite" width="120"> | [Berkeley Humanoid Lite](https://lite.berkeley-humanoid.org/)<br>([仓库](https://github.com/HybridRobotics/berkeley-humanoid-lite)) | Hybrid Robotics Lab, UC Berkeley | 开放的、以 3D 打印为主的研究用人形机器人，采用模块化摆线减速器，零件可从常见电商采购。 | 22 actuated joints (6 per leg, 5 per arm; described in official video/materials)<br>Official site: about 0.8 m tall and 16 kg; total hardware cost under USD 5,000 (U.S. market prices) | 3D-printed cycloidal actuators; official BOM discussion cites M6C12 and 5010 motors (quantities on the Humanoid tab of the BOM)<br>通信：未知 | Under USD 5,000 (official website and README, U.S. market prices) | Isaac Lab, MuJoCo | 硬件: CC BY-SA 4.0<br>软件: MIT | 星标 ≈2k<br>最近提交 2026-03-11 04:14 (Asia/Shanghai)<br>统计截至 2026-11-20 | 未知 | 已对源核查 |
| <img src="https://raw.githubusercontent.com/FFTAI/Wiki-GRx-Pipeline/FourierN1/pictures/developer_banner.png" alt="傅利叶 N1" width="120"> | [傅利叶 N1](https://www.fftai.cn/open-source/18)<br>([仓库](https://github.com/FFTAI/fourier-grx-N1)) | Fourier (傅利叶) | 傅利叶首款开源发布的人形机器人（Nexus-01）：身高 1.3 米、体重 38 公斤、23 自由度，官方提供 BOM、图纸、装配指南和 SDK 文档。 | 23<br>Height 1.3 m; mass 38 kg; official materials state a stable running speed up to 3.5 m/s and 2+ hours of motion endurance; FSA 2.0 actuators | Fourier FSA 2.0 integrated actuators (official announcement)<br>通信：未知 | 未知 | MuJoCo | 硬件: 未知<br>软件: Multiple (see notes) | 星标 21<br>最近提交 2026-10-25 12:04 (Asia/Shanghai)<br>统计截至 2026-11-20 | 未知 | 已对源核查 |
| <img src="https://raw.githubusercontent.com/poppy-project/poppy-humanoid/master/doc/img/poppy-humanoid-github.jpg" alt="Poppy Humanoid" width="120"> | [Poppy Humanoid](https://www.poppy-project.org/en/robots/poppy-humanoid/)<br>([仓库](https://github.com/poppy-project/poppy-humanoid)) | Poppy Project (originated at Inria) | 模块化、可 3D 打印的教育与研究用人形机器人，使用 25 个 Dynamixel 执行器，是文档较完整的早期开源人形套件之一。 | 25 Dynamixel actuators (official README)<br>Official README: about 83 cm tall, 3.5 kg; Raspberry Pi 3 or 4 as the embedded computer | ROBOTIS Dynamixel (25 actuators)<br>通信：Dynamixel bus (USB2Dynamixel / USB2AX also supported) | USD 8,000–9,000 for a complete robot, with about 60% in the 25 Dynamixel actuators (official README) | ROS, pypot | 硬件: CC BY-SA 4.0<br>软件: GPL-3.0 | 星标 ≈1.1k<br>最近提交 2021-12-07 02:19 (Asia/Shanghai)<br>统计截至 2026-11-20 | 未知 | 已对源核查 |
| <img src="https://raw.githubusercontent.com/hshi74/toddlerbot/main/docs/_static/banner.png" alt="ToddlerBot" width="120"> | [ToddlerBot](https://toddlerbot.github.io/)<br>([仓库](https://github.com/hshi74/toddlerbot)) | Stanford University (ToddlerBot authors) | 面向机器学习的开源运动-操作人形平台，提供公开 BOM、装配手册以及仿真到实物的软件栈。 | 30 active DoF (7 per arm, 6 per leg, 2 neck, 2 waist; official project materials)<br>Official paper/site materials describe a compact research platform; build cost under USD 6,000 in the project paper | ROBOTIS Dynamixel (official source-site and repo materials)<br>通信：Dynamixel bus | Under USD 6,000 (project paper) | MuJoCo | 硬件: CC BY-NC-SA 4.0<br>软件: MIT | 星标 807<br>最近提交 2026-11-17 06:30 (Asia/Shanghai)<br>统计截至 2026-11-20 | 未知 | 已对源核查 |

## 对比分析

四款都被定位为开放人形平台，但价位、许可证和完整程度差别很大。Berkeley Humanoid Lite 强调低于 5,000 美元、以 3D 打印为主的可复现方案，代码 MIT、资源 CC BY-SA 4.0，并支持 Isaac Lab。ToddlerBot 是更小型的运动-操作研究平台（官方材料为 30 个主动自由度），代码 MIT，设计文件为非商业性的 CC BY-NC-SA；项目论文写明建造成本低于 6,000 美元。Poppy Humanoid 是这里历史最长的教育/研究平台（25 个 Dynamixel 执行器，官方 BOM 约 8,000–9,000 美元），硬件 CC BY-SA 4.0、软件 GPL-3.0；主 CAD 仓库自 2021 年以来没有新的提交。Fourier N1 是 23 自由度、身高 1.3 米、体重 38 公斤的工业背景开源发布，官方提供硬件下载，但我们没有找到硬件许可证；公开 GitHub 一侧主要是文档和 SDK 相关仓库，而不是单一的单体仓库。

## 免责声明

成本、交期和购买信息都会变化。购买或动手制作前，请向官方项目核实价格与许可证。本目录不构成对任何卖方的背书，也不构成许可证方面的法律意见。

_由 `scripts/generate_readme.py` 根据 `data/projects.yaml` 生成。对源核查快照：2026-11-20（Asia/Shanghai）。_
