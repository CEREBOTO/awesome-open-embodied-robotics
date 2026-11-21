# 移动操作机器人

本页是 [Awesome Open Embodied Robotics](../../README.zh-CN.md) 的一部分，提供本类别的逐字段对照表和简短对比分析。整体清单见[首页](../../README.zh-CN.md)。

[English](README.md) · [贡献指南](../../CONTRIBUTING.zh-CN.md) · [许可证](../../LICENSE) · 数据：[`data/projects.yaml`](../../data/projects.yaml)

本类别内项目按**英文名称字母顺序**排列。星标数、价格、更新时间和商业关系都不参与排序。

硬件许可证与软件许可证分开记录，来源是 LICENSE 文件或官方许可证声明。找不到时填写「未知」。

仓库活跃度（星标、最近一次提交）记录于 **2026-11-21**（Asia/Shanghai）。YAML 中的提交时间是 UTC，这里转换为 Asia/Shanghai 显示。这些数字会变化，请当作快照。

## 对照表

| 图片 | 项目 | 维护者 | 简介 | 自由度 / 规格 | 电机与通信 | 约略 BOM 成本 | 软件生态 | 许可证（硬件 / 软件） | 仓库活跃度 | 购买渠道 | 核实状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <img src="https://aha-robot.github.io/static/images/hardware.png" alt="AhaRobot" width="120"> | [AhaRobot](https://aha-robot.github.io/)<br>([仓库](https://github.com/hilookas/astra_ws)) | Tianjin University (AhaRobot authors) | 面向具身智能研究的低成本开源双臂移动操作机器人，软件与硬件分仓库发布。 | 未知 | Feetech servos (source and official materials)<br>通信：未知 | 未知 | ROS | 硬件: GPL-3.0<br>软件: GPL-3.0 | 星标 25<br>最近提交 2026-10-12 20:22 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |
| <img src="https://robotmabel.github.io/website/assets/og.jpg" alt="MABEL" width="120"> | [MABEL](https://robotmabel.github.io/website/)<br>([仓库](https://github.com/robotmabel/open_mabel)) | The MABEL Authors (NYU Center for Robotics and Embodied Intelligence (CREO) and University of Toronto) | 开源 56 自由度仿人移动双臂机器人，包含三模块全向转向底盘、升降柱、俯仰躯干、3 自由度头部、两套源于 OpenArm 的 7 自由度机械臂，以及两套源于 ORCA 的 17 自由度灵巧手；支持 Vision Pro 全身遥操作，并提供 ROS 2、MuJoCo 和 LeRobot 支持。 | 56 functional DOF (59 motors), as stated by the official README, website, and build overview<br>Fingertip reach 0-2.23 m (floor to overhead); lift travel 0.635 m; base footprint 0.49 m; mass about 62 kg; 24 V untethered. From the official build overview: https://robotmabel.github.io/website/docs/overview.html | Three-module swerve base uses REV NEO + NEO 550 per module with 6× SPARK on CAN; lift is a FlexiSpot E7 Pro column (brushed DC + leadscrew, RP2040 Pico); torso is a DaMiao DM-J10422P; arms are OpenArm-derived DaMiao quasi-direct-drive; hands use 17 Feetech TTL servos each (ORCA-derived); neck yaw is DaMiao on CAN, neck roll and pitch are 2× Dynamixel XC330-T181. Source: official README and https://robotmabel.github.io/website/docs/overview.html<br>通信：CAN for the swerve base (SPARK), body/torso, each arm, and neck yaw; 1 MHz TTL chain per hand; Dynamixel bus for neck roll and pitch. Source: official README and overview. | Official listed parts subtotals (price basis 31 July 2026; configuration updated 22 September 2026): Essential US$8,056.03, Recommended US$9,283.03, Maximum US$14,721.06. Core BOM about US$7,650.29, shared by every tier. Totals exclude unpriced items, optional storage, operator equipment, shipping, taxes, and labor. | ROS 2, MuJoCo, LeRobot, Isaac Sim, Isaac Lab | 硬件: CERN-OHL-S-2.0<br>软件: Apache-2.0 | 星标 64<br>最近提交 2026-11-19 23:41 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |
| <img src="https://tidybot2.github.io/images/og-image.jpg" alt="TidyBot++" width="120"> | [TidyBot++](https://tidybot2.github.io/)<br>([仓库](https://github.com/jimmyyhwu/tidybot2)) | Jimmy Wu and collaborators (Princeton, Stanford, Dexterity affiliations on the source index) | 面向机器人学习的开源全向（转向轮）移动操作平台，提供公开 BOM，并支持更换不同的商用机械臂。 | Mobile base plus a swappable arm (official reference designs: Kinova Gen3 7-DoF, Franka, or ARX5)<br>Holonomic MK4 swerve modules; official Kinova-tab mobile-base BOM total USD 5,379.63, excluding the arm and some compute items listed without a price | 8× Kraken X60 (drive system) plus the chosen arm's own actuators<br>通信：CAN (CTRE / Phoenix-style drive stack; official BOM has a CAN system section) | Mobile base USD 5,379.63 on the official Kinova BOM tab (as published on the docs page). Complete system cost depends on the arm (Kinova/Franka/ARX5) and is not a single official total. | ROS 2 | 硬件: 未知<br>软件: MIT | 星标 624<br>最近提交 2025-03-27 11:31 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |
| <img src="https://github.com/user-attachments/assets/682ef049-bb42-4b50-bf98-74d6311e774d" alt="XLeRobot" width="120"> | [XLeRobot](https://github.com/Vector-Wangel/XLeRobot) | Vector-Wangel | 面向家庭操作的实用双臂移动机器人，由两台 SO-101 机械臂加全向轮底盘组成，官方给出较低的 BOM 成本。 | Two SO-101 arms plus an omni-wheel base and a 2-DoF neck (official README)<br>Official basic configuration uses a laptop and a single RGB head camera; optional Pi / RealSense upgrades are priced separately | Feetech STS3215 (17 servos in official BOM materials: 12 for two SO-101 arms, 3 for the omni-wheel base, 2 for the head)<br>通信：Feetech STS serial bus | About USD 660 / EUR 680 / CNY 3,999 for the basic configuration; excludes 3D printing, tools, shipping, and taxes (official README) | LeRobot | 硬件: Apache-2.0<br>软件: Apache-2.0 | 星标 5841<br>最近提交 2026-11-17 01:55 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |

## 对比分析

这四款的主要差别在成本和所搭配的手臂。XLeRobot 明确是双 SO-101 加全向轮的家用操作机器人，官方 README 给出基础 BOM 约 660 美元（不含打印、工具、运费和税），并处于 LeRobot 生态中。AhaRobot 是天津大学的低成本双臂移动操作平台，使用飞特舵机，软硬件仓库均为 GPL-3.0；我们打开的官方页面里没有确认到一个单独的 BOM 总价。MABEL 是 56 自由度全身平台（机械臂源于 OpenArm，灵巧手源于 ORCA）；官方列出的 Essential、Recommended 与 Maximum 零件小计分别约为 8,056、9,283 与 14,721 美元（2026 年 7 月价格基准）。TidyBot++ 是全向转向（swerve）研究用移动底座（Kraken X60 / CAN），官方 BOM 支持更换 Kinova、Franka 或 ARX5 手臂。Kinova 分页上移动底座合计为 5,379.63 美元，不包括手臂本身，整机价格取决于所选手臂。

## 免责声明

成本、交期和购买信息都会变化。购买或动手制作前，请向官方项目核实价格与许可证。本目录不构成对任何卖方的背书，也不构成许可证方面的法律意见。

_由 `scripts/generate_readme.py` 根据 `data/projects.yaml` 生成。对源核查快照：2026-11-21（Asia/Shanghai）。_
