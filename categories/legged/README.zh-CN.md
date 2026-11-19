# 四足 / 腿式机器人

本页是 [Awesome Open Embodied Robotics](../../README.zh-CN.md) 的一部分，提供本类别的逐字段对照表和简短对比分析。整体清单见[首页](../../README.zh-CN.md)。

[English](README.md) · [贡献指南](../../CONTRIBUTING.zh-CN.md) · [许可证](../../LICENSE) · 数据：[`data/projects.yaml`](../../data/projects.yaml)

本类别内项目按**英文名称字母顺序**排列。星标数、价格、更新时间和商业关系都不参与排序。

硬件许可证与软件许可证分开记录，来源是 LICENSE 文件或官方许可证声明。找不到时填写「未知」。

仓库活跃度（星标、最近一次提交）记录于 **2026-11-20**（Asia/Shanghai）。YAML 中的提交时间是 UTC，这里转换为 Asia/Shanghai 显示。这些数字会变化，请当作快照。

## 对照表

| 项目 | 维护者 | 简介 | 自由度 / 规格 | 电机与通信 | 约略 BOM 成本 | 软件生态 | 许可证（硬件 / 软件） | 仓库活跃度 | 购买渠道 | 核实状态 | 披露 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [AlexbotMini](https://roboparty.feishu.cn/wiki/IRANwwUcWi8EpLkuGC3c3G3Envf)<br>([仓库](https://github.com/Alexhuge1/Alexbotmini_hardware)) | 萝博派对 / Alexhuge (Fourier-sponsored per official README) | 面向强化学习步态研究的开源双足机器人，提供机械、硬件和算法相关仓库。 | 12 (listed on the source index technical specs; treat as unverified if not restated in the short README)<br>Official README: lower body 700 mm, upper body 500 mm (about 1.2 m overall), human-proportioned | Fourier actuators (source index; official README names Fourier as sponsor but does not list a motor SKU in the short README)<br>通信：未知 | 未知 | 未知 | 硬件: BSD-3-Clause<br>软件: BSD-3-Clause | 星标 79<br>最近提交 2025-04-15 14:10 (Asia/Shanghai)<br>统计截至 2026-11-20 | [Official BOM spreadsheet in the hardware repo](https://github.com/Alexhuge1/Alexbotmini_hardware) (Path referenced by the source index: 1_Mechanic/.../BOM.xlsx) | 已对源核查 | — |
| [桌面轮足机器人](https://github.com/MuShibo/Micro-Wheeled_leg-Robot) | 世博同学 (MuShibo) | 桌面级双轮腿机器人，主控为 ESP32，腿部使用飞特总线舵机，轮部使用 simpleFOC 无刷驱动。 | 未知<br>ESP32 main board; four self-made PCBs; designed as a beginner-friendly open hardware project | Feetech bus servos (legs) and brushless wheel motors driven with L6234PD013TR / simpleFOC (README)<br>通信：Feetech servo bus; I2C for AS5600 encoders and MPU6050 IMU; Wi-Fi / WebSocket for the web UI | 未知 | 未知 | 硬件: 未知<br>软件: 未知 | 星标 ≈3.9k<br>最近提交 2024-12-12 20:01 (Asia/Shanghai)<br>统计截至 2026-11-20 | [Official BOM spreadsheet](https://github.com/MuShibo/Micro-Wheeled_leg-Robot/blob/master/1.RobotModel/Parts-Purchased/BOM.xlsx) (Self-sourced parts) | 已对源核查 | — |
| [Open Duck Mini](https://github.com/apirrone/Open_Duck_Mini) | Antoine Pirrone and contributors | 受迪士尼 BDX 机器人启发的桌面尺度开源双足，提供公开 BOM、打印文件以及独立的运行时仓库。 | Unknown from a single official one-line spec in the hub README; community/docs materials describe a 14-DoF STS3215 layout — not copied here because it was not in the official hub README we opened<br>Official hub README: about 42 cm tall with legs extended; Raspberry Pi Zero 2W is used in the runtime repo | Feetech STS3215 (widely documented around the project; official runtime/docs materials)<br>通信：Feetech STS serial bus | Full BOM should be under USD 400 (official hub README) | MuJoCo | 硬件: Apache-2.0<br>软件: Apache-2.0 (hub repo); Unknown (runtime repo) | 星标 ≈4.8k<br>最近提交 2026-01-31 18:28 (Asia/Shanghai)<br>统计截至 2026-11-20 | [Official BOM (DIY)](https://github.com/apirrone/Open_Duck_Mini) (Hub README links a spreadsheet / docs)<br>[Cereboto Open Duck Mini V2](https://cereboto.com/product/open-duck-mini-v2/) (Commercial kit) | 已对源核查 | Disclosure: sold by Cereboto<br>（Cereboto 有销售该项目相关产品） |
| [宇树 Qmini](https://github.com/unitreerobotics/Qmini) | Unitree Robotics; training/deployment stack also from VSISLab, Shandong University | 可完全 3D 打印的开源双足，使用 11 个宇树 8010 电机，参考主控为树莓派 4B，并有配套的强化学习部署栈。 | 11 motors (10 for locomotion, 1 neck reserved for expansion; official README)<br>Official README: assemble in about 3–5 hours after printing; Raspberry Pi 4 Model B as the default reference controller | 11× Unitree 8010 (GO-M8010-6 in related docs)<br>通信：Unknown (related write-ups mention RS-485 for Unitree 8010-style actuators, but this was not copied from the official README we opened) | 未知 | Isaac Gym | 硬件: CC BY-NC-SA 4.0<br>软件: MIT (RoboTamer4Qmini); CC BY-NC-SA 4.0 (Qmini repo, which also contains models and DIY files) | 星标 902<br>最近提交 2025-09-17 16:11 (Asia/Shanghai)<br>统计截至 2026-11-20 | [Official DIY files and BOM in the Qmini repo](https://github.com/unitreerobotics/Qmini) (Self-sourced 8010 motors and electronics; no official total price found) | 已对源核查 | — |

## 对比分析

这一批里其实没有经典四足，全部是双足或轮腿，是从源网站的「双足机器人」分类改归到本类的。Open Duck Mini 是桌面尺度（约 42 厘米）双足，官方枢纽仓库写明完整 BOM 低于 400 美元，使用飞特 STS3215，许可证为 Apache-2.0。宇树 Qmini 是可 3D 打印双足，使用 11 个宇树 8010 电机，参考主控为树莓派 4B；官方仓库为 CC BY-NC-SA 4.0，没有找到 BOM 总价。AlexbotMini 是傅利叶赞助的约 1.2 米级双足（README：下半身 700 毫米、上半身 500 毫米），硬件仓库为 BSD-3-Clause；未确认到公开的 BOM 总价。桌面轮足机器人是桌面级双轮腿设计，主控 ESP32，腿部为飞特总线舵机，轮部为 FOC 无刷电机；仓库中没有找到 LICENSE 文件。

## 免责声明

成本、交期和购买信息都会变化。购买或动手制作前，请向官方项目核实价格与许可证。本目录不构成对任何卖方的背书，也不构成许可证方面的法律意见。

_由 `scripts/generate_readme.py` 根据 `data/projects.yaml` 生成。对源核查快照：2026-11-20（Asia/Shanghai）。_
