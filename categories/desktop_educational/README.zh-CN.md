# 桌面 / 教育机器人

本页是 [Awesome Open Embodied Robotics](../../README.zh-CN.md) 的一部分，提供本类别的逐字段对照表和简短对比分析。整体清单见[首页](../../README.zh-CN.md)。

[English](README.md) · [贡献指南](../../CONTRIBUTING.zh-CN.md) · [许可证](../../LICENSE) · 数据：[`data/projects.yaml`](../../data/projects.yaml)

本类别内项目按**英文名称字母顺序**排列。星标数、价格、更新时间和商业关系都不参与排序。

硬件许可证与软件许可证分开记录，来源是 LICENSE 文件或官方许可证声明。找不到时填写「未知」。

仓库活跃度（星标、最近一次提交）记录于 **2026-11-21**（Asia/Shanghai）。YAML 中的提交时间是 UTC，这里转换为 Asia/Shanghai 显示。这些数字会变化，请当作快照。

## 对照表

| 图片 | 项目 | 维护者 | 简介 | 自由度 / 规格 | 电机与通信 | 约略 BOM 成本 | 软件生态 | 许可证（硬件 / 软件） | 仓库活跃度 | 购买渠道 | 核实状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <img src="https://image.lceda.cn/oshwhub/pullImage/fafb5929527c4adfacbdf7070f97a870.jpg" alt="EchoEar（喵伴）" width="120"> | [EchoEar（喵伴）](https://oshwhub.com/esp-college/echoear)<br>([仓库](https://github.com/espressif/esp-brookesia/tree/master/examples/echoear)) | Espressif and Coze (乐鑫、扣子), as listed on the source index and the open-hardware page | 桌面 AI 陪伴设备（ESP-VoCat / 喵伴），带圆形触摸屏、语音交互和可选旋转底座，作为 ESP-Brookesia 生态中的开源硬件示例发布。 | 未知<br>ESP32-S3 class device with 1.85-inch 360×360 round touch screen, 16 MB PSRAM / 16 MB Flash, microSD, Bluetooth LE (official oshwhub page) | Optional rotating base (firmware offered as a separate download on the official page)<br>通信：Wi-Fi / Bluetooth LE | 未知 | 未知 | 硬件: GPL-3.0 (as listed on the oshwhub project page)<br>软件: See notes | 星标 854<br>最近提交 2026-11-19 19:18 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |
| <img src="https://raw.githubusercontent.com/ZZongzheng0918/Morpheus-Hardware/main/media/teaser.png" alt="Morpheus" width="120"> | [Morpheus](https://jiawenyang-ch.github.io/Morpheus-Hardware-Design/)<br>([仓库](https://github.com/ZZongzheng0918/Morpheus-Hardware)) | Morpheus authors (Tsinghua AIR / IIIS, BAAI, MGI Tech, Beihang affiliations on the source index) | 采用混合驱动、33 个执行器的神经驱动仿生表情脸，软硬件仓库开源（RSS 2025）。 | 33 actuators (official materials and source-index specs)<br>Raspberry Pi 5 as the listed main controller; hybrid rigid and tendon actuation | GuoHua actuators (source index)<br>通信：未知 | 未知 | 未知 | 硬件: MIT<br>软件: MIT | 星标 91<br>最近提交 2025-11-17 17:04 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |
| <img src="https://custom-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_9000,w_1200,f_auto,q_auto/838564/935880_609691.png" alt="OttoDIY" width="120"> | [OttoDIY](https://www.ottodiy.com/)<br>([仓库](https://github.com/OttoDIY/OttoDIYLib)) | OttoDIY project | 广泛使用的 3D 打印开源教育行走机器人，官方提供 Arduino 库，并在项目网站发布设计和教程。 | 未知 | Standard hobby servos (exact official SKU not copied from the homepage text we extracted)<br>通信：Arduino PWM / standard servo interface | 未知 | 未知 | 硬件: 未知<br>软件: GPL-3.0 | 星标 219<br>最近提交 2024-05-29 03:32 (Asia/Shanghai)<br>统计截至 2026-11-21 | 未知 | 已对源核查 |

## 对比分析

OttoDIY 是历史较长的 3D 打印教育行走机器人；官方 Arduino 库为 GPL-3.0，我们没有另外确认到独立的硬件许可证文件。EchoEar（喵伴 / ESP-VoCat）是带触摸屏的桌面 AI 陪伴设备，不是机械臂；开源硬件平台标注 GPL-3.0。更大的 ESP-Brookesia 框架在 GitHub 许可证徽章上显示为 Apache-2.0，但我们尝试的仓库根路径下没有找到 LICENSE 文件。Morpheus 是 33 个执行器的仿生表情脸（官方材料为树莓派 5），软硬件仓库均为 MIT；它不是移动或操作机器人，但是开源具身硬件，因此放在桌面/教育类，而不是强行归入人形机器人。

## 免责声明

成本、交期和购买信息都会变化。购买或动手制作前，请向官方项目核实价格与许可证。本目录不构成对任何卖方的背书，也不构成许可证方面的法律意见。

_由 `scripts/generate_readme.py` 根据 `data/projects.yaml` 生成。对源核查快照：2026-11-21（Asia/Shanghai）。_
