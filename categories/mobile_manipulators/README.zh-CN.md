# 移动操作机器人

本页是 [Awesome Open Embodied Robotics](../../README.zh-CN.md) 的一部分，提供本类别的逐字段对照表和简短对比分析。整体清单见[首页](../../README.zh-CN.md)。

[English](README.md) · [贡献指南](../../CONTRIBUTING.zh-CN.md) · [许可证](../../LICENSE) · 数据：[`data/projects.yaml`](../../data/projects.yaml)

本类别内项目按**英文名称字母顺序**排列。星标数、价格、更新时间和商业关系都不参与排序。

硬件许可证与软件许可证分开记录，来源是 LICENSE 文件或官方许可证声明。找不到时填写「未知」。

仓库活跃度（星标、最近一次提交）记录于 **2026-11-20**（Asia/Shanghai）。YAML 中的提交时间是 UTC，这里转换为 Asia/Shanghai 显示。这些数字会变化，请当作快照。

## 对照表

| 项目 | 维护者 | 简介 | 自由度 / 规格 | 电机与通信 | 约略 BOM 成本 | 软件生态 | 许可证（硬件 / 软件） | 仓库活跃度 | 购买渠道 | 核实状态 | 披露 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [AhaRobot](https://aha-robot.github.io/)<br>([仓库](https://github.com/hilookas/astra_ws)) | Tianjin University (AhaRobot authors) | 面向具身智能研究的低成本开源双臂移动操作机器人，软件与硬件分仓库发布。 | 未知 | Feetech servos (source and official materials)<br>通信：未知 | 未知 | ROS | 硬件: GPL-3.0<br>软件: GPL-3.0 | 星标 25<br>最近提交 2026-10-12 20:22 (Asia/Shanghai)<br>统计截至 2026-11-20 | [Official project page / BOM pointers](https://aha-robot.github.io/) (Hardware CAD at https://github.com/hilookas/Astra_Hardwares) | 已对源核查 | — |
| [TidyBot++](https://tidybot2.github.io/)<br>([仓库](https://github.com/jimmyyhwu/tidybot2)) | Jimmy Wu and collaborators (Princeton, Stanford, Dexterity affiliations on the source index) | 面向机器人学习的开源全向（转向轮）移动操作平台，提供公开 BOM，并支持更换不同的商用机械臂。 | Mobile base plus a swappable arm (official reference designs: Kinova Gen3 7-DoF, Franka, or ARX5)<br>Holonomic MK4 swerve modules; official Kinova-tab mobile-base BOM total USD 5,379.63, excluding the arm and some compute items listed without a price | 8× Kraken X60 (drive system) plus the chosen arm's own actuators<br>通信：CAN (CTRE / Phoenix-style drive stack; official BOM has a CAN system section) | Mobile base USD 5,379.63 on the official Kinova BOM tab (as published on the docs page). Complete system cost depends on the arm (Kinova/Franka/ARX5) and is not a single official total. | ROS 2 | 硬件: 未知<br>软件: MIT | 星标 626<br>最近提交 2025-03-27 11:31 (Asia/Shanghai)<br>统计截至 2026-11-20 | [Official BOM (DIY)](https://tidybot2.github.io/docs/bom/) (Parts from CTRE, WCP, SDS, AndyMark, Amazon, TAP Plastics, Xometry, plus a separately purchased arm) | 已对源核查 | — |
| [XLeRobot](https://github.com/Vector-Wangel/XLeRobot) | Vector-Wangel | 面向家庭操作的实用双臂移动机器人，由两台 SO-101 机械臂加全向轮底盘组成，官方给出较低的 BOM 成本。 | Two SO-101 arms plus an omni-wheel base and a 2-DoF neck (official README)<br>Official basic configuration uses a laptop and a single RGB head camera; optional Pi / RealSense upgrades are priced separately | Feetech STS3215 (17 servos in official BOM materials: 12 for two SO-101 arms, 3 for the omni-wheel base, 2 for the head)<br>通信：Feetech STS serial bus | About USD 660 / EUR 680 / CNY 3,999 for the basic configuration; excludes 3D printing, tools, shipping, and taxes (official README) | LeRobot | 硬件: Apache-2.0<br>软件: Apache-2.0 | 星标 ≈5.8k<br>最近提交 2026-11-17 01:55 (Asia/Shanghai)<br>统计截至 2026-11-20 | [Official BOM (DIY)](https://xlerobot.readthedocs.io/en/latest/hardware/getting_started/material.html) (Self-sourced parts, including SO-101-compatible servos) | 已对源核查 | — |

## 对比分析

这三款的主要差别在成本和所搭配的手臂。XLeRobot 明确是双 SO-101 加全向轮的家用操作机器人，官方 README 给出基础 BOM 约 660 美元（不含打印、工具、运费和税），并处于 LeRobot 生态中。AhaRobot 是天津大学的低成本双臂移动操作平台，使用飞特舵机，软硬件仓库均为 GPL-3.0；我们打开的官方页面里没有确认到一个单独的 BOM 总价。TidyBot++ 是全向转向（swerve）研究用移动底座（Kraken X60 / CAN），官方 BOM 支持更换 Kinova、Franka 或 ARX5 手臂。Kinova 分页上移动底座合计为 5,379.63 美元，不包括手臂本身，整机价格取决于所选手臂。

## 免责声明

成本、交期和购买信息都会变化。购买或动手制作前，请向官方项目核实价格与许可证。本目录不构成对任何卖方的背书，也不构成许可证方面的法律意见。

_由 `scripts/generate_readme.py` 根据 `data/projects.yaml` 生成。对源核查快照：2026-11-20（Asia/Shanghai）。_
