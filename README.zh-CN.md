# Awesome Open Embodied Robotics

[![Discord](https://img.shields.io/badge/Discord-5865F2?logo=discord&logoColor=white)](https://discord.gg/fqczequGXj)

一份独立、由社区驱动的开源具身机器人项目目录，由 Cereboto 维护，帮助开发者发现、比较并动手制作下一代智能机器人。

本目录独立、由社区驱动。Cereboto 负责维护这份名单，同时也在 [cereboto.com](https://cereboto.com/) 销售开源具身机器人硬件。商业合作不影响排序，也不会因为竞争关系而排除任何品牌。

[English](README.md) · [贡献指南](CONTRIBUTING.zh-CN.md) · [许可证](LICENSE) · 数据：[`data/projects.yaml`](data/projects.yaml)

## 目录

- [单臂 / 双臂机械臂](#单臂-双臂机械臂)（4）
- [人形机器人](#人形机器人)（4）
- [移动操作机器人](#移动操作机器人)（4）
- [四足 / 腿式机器人](#四足-腿式机器人)（4）
- [灵巧手与夹爪](#灵巧手与夹爪)（10）
- [遥操作与数据采集装置](#遥操作与数据采集装置)（7）
- [桌面 / 教育机器人](#桌面-教育机器人)（3）

## 单臂 / 双臂机械臂

| 图片 | 项目 | 简介 |
| --- | --- | --- |
| <img src="https://martinpeticco.com/dexwrist/static/images/gearboxregular.png" alt="DexWrist" width="120"> | [DexWrist](https://dexwrist.csail.mit.edu/) | 紧凑的 2 自由度准直驱机器人腕部（俯仰-偏航），面向狭窄空间和接触丰富的操作，定位为现有机械臂的可替换升级。 |
| <img src="https://openarm.dev/images/img_introducing_v2.webp" alt="OpenArm" width="120"> | [OpenArm](https://openarm.dev/) | 完全开源的人体尺度机械臂平台，每臂 7 自由度、准直驱，面向接触丰富的遥操作、模仿学习和具身智能研究，通常以双臂系统部署。 Disclosure: sold by Cereboto |
| <img src="https://raw.githubusercontent.com/TheRobotStudio/SO-ARM100/main/media/SO101_Follower.webp" alt="SO-101" width="120"> | [SO-101](https://github.com/TheRobotStudio/SO-ARM100) | 低成本 3D 打印主从机械臂（SO-100 的后继型号），面向与 LeRobot 软件栈配合的模仿学习和遥操作。 |
| <img src="https://raw.githubusercontent.com/roboninecom/SO-ARM102/main/assets/images/photos/so-arm-102-live.jpg" alt="SO-ARM 102" width="120"> | [SO-ARM 102](https://github.com/roboninecom/SO-ARM102) | 开源主从机械臂套件，面向遥操作和模仿学习；每臂 5 自由度外加平行夹爪，是 SO-ARM 100/101 的后继型号，可与 LeRobot 配合使用。 |

[详细对比](categories/manipulators/README.zh-CN.md)

## 人形机器人

| 图片 | 项目 | 简介 |
| --- | --- | --- |
| <img src="https://lite.berkeley-humanoid.org/static/berkeley-humaonid-lite-cover.png" alt="Berkeley Humanoid Lite" width="120"> | [Berkeley Humanoid Lite](https://lite.berkeley-humanoid.org/) | 开放的、以 3D 打印为主的研究用人形机器人，采用模块化摆线减速器，零件可从常见电商采购。 |
| <img src="https://raw.githubusercontent.com/FFTAI/Wiki-GRx-Pipeline/FourierN1/pictures/developer_banner.png" alt="傅利叶 N1" width="120"> | [傅利叶 N1](https://www.fftai.cn/open-source/18) | 傅利叶首款开源发布的人形机器人（Nexus-01）：身高 1.3 米、体重 38 公斤、23 自由度，官方提供 BOM、图纸、装配指南和 SDK 文档。 |
| <img src="https://raw.githubusercontent.com/poppy-project/poppy-humanoid/master/doc/img/poppy-humanoid-github.jpg" alt="Poppy Humanoid" width="120"> | [Poppy Humanoid](https://www.poppy-project.org/en/robots/poppy-humanoid/) | 模块化、可 3D 打印的教育与研究用人形机器人，使用 25 个 Dynamixel 执行器，是文档较完整的早期开源人形套件之一。 |
| <img src="https://raw.githubusercontent.com/hshi74/toddlerbot/main/docs/_static/banner.png" alt="ToddlerBot" width="120"> | [ToddlerBot](https://toddlerbot.github.io/) | 面向机器学习的开源运动-操作人形平台，提供公开 BOM、装配手册以及仿真到实物的软件栈。 |

[详细对比](categories/humanoids/README.zh-CN.md)

## 移动操作机器人

| 图片 | 项目 | 简介 |
| --- | --- | --- |
| <img src="https://aha-robot.github.io/static/images/hardware.png" alt="AhaRobot" width="120"> | [AhaRobot](https://aha-robot.github.io/) | 面向具身智能研究的低成本开源双臂移动操作机器人，软件与硬件分仓库发布。 |
| <img src="https://robotmabel.github.io/website/assets/og.jpg" alt="MABEL" width="120"> | [MABEL](https://robotmabel.github.io/website/) | 开源 56 自由度仿人移动双臂机器人，包含三模块全向转向底盘、升降柱、俯仰躯干、3 自由度头部、两套源于 OpenArm 的 7 自由度机械臂，以及两套源于 ORCA 的 17 自由度灵巧手；支持 Vision Pro 全身遥操作，并提供 ROS 2、MuJoCo 和 LeRobot 支持。 |
| <img src="https://tidybot2.github.io/images/og-image.jpg" alt="TidyBot++" width="120"> | [TidyBot++](https://tidybot2.github.io/) | 面向机器人学习的开源全向（转向轮）移动操作平台，提供公开 BOM，并支持更换不同的商用机械臂。 |
| <img src="https://github.com/user-attachments/assets/682ef049-bb42-4b50-bf98-74d6311e774d" alt="XLeRobot" width="120"> | [XLeRobot](https://github.com/Vector-Wangel/XLeRobot) | 面向家庭操作的实用双臂移动机器人，由两台 SO-101 机械臂加全向轮底盘组成，官方给出较低的 BOM 成本。 |

[详细对比](categories/mobile_manipulators/README.zh-CN.md)

## 四足 / 腿式机器人

| 图片 | 项目 | 简介 |
| --- | --- | --- |
| <img src="https://raw.githubusercontent.com/Alexhuge1/Alexbotmini_hardware/main/1_Mechanic/Alexbotmini_V1.0/4_Photos/alexbotmini_stand.jpg" alt="AlexbotMini" width="120"> | [AlexbotMini](https://roboparty.feishu.cn/wiki/IRANwwUcWi8EpLkuGC3c3G3Envf) | 面向强化学习步态研究的开源双足机器人，提供机械、硬件和算法相关仓库。 |
| <img src="https://raw.githubusercontent.com/MuShibo/Micro-Wheeled_leg-Robot/master/4.Docs/Image/RobotReal.jpg" alt="桌面轮足机器人" width="120"> | [桌面轮足机器人](https://github.com/MuShibo/Micro-Wheeled_leg-Robot) | 桌面级双轮腿机器人，主控为 ESP32，腿部使用飞特总线舵机，轮部使用 simpleFOC 无刷驱动。 |
| <img src="https://github.com/user-attachments/assets/e240c06e-769f-4c87-b65f-189a442cf1e9" alt="Open Duck Mini" width="120"> | [Open Duck Mini](https://github.com/apirrone/Open_Duck_Mini) | 受迪士尼 BDX 机器人启发的桌面尺度开源双足，提供公开 BOM、打印文件以及独立的运行时仓库。 Disclosure: sold by Cereboto |
| <img src="https://raw.githubusercontent.com/unitreerobotics/Qmini/main/images/Qmini.jpeg" alt="宇树 Qmini" width="120"> | [宇树 Qmini](https://github.com/unitreerobotics/Qmini) | 可完全 3D 打印的开源双足，使用 11 个宇树 8010 电机，参考主控为树莓派 4B，并有配套的强化学习部署栈。 |

[详细对比](categories/legged/README.zh-CN.md)

## 灵巧手与夹爪

| 图片 | 项目 | 简介 |
| --- | --- | --- |
| <img src="https://github.com/iotdesignshop/dexhand-ble/assets/2821763/de311dc5-b41e-4f2f-b8e6-849a51983018" alt="DexHand" width="120"> | [DexHand](https://www.dexhand.org/) | 开源、可 3D 打印的仿人灵巧手，定位为低成本的抓取与操作研究平台。 |
| <img src="https://cdn.hackaday.io/images/resize/600x600/5835141474981681029.jpg" alt="Dextra" width="120"> | [Dextra](https://hackaday.io/project/9890-dextra) | 较早的开源仿人机械手项目，记录在 Hackaday.io，提供文件、开发日志和装配说明。 |
| <img src="https://e-flesh.com/static/images/graphics-3-1.png" alt="eFlesh" width="120"> | [eFlesh](https://e-flesh.com/) | 采用切胞微结构的可定制磁性触觉传感器，并附有开源仓库。 |
| <img src="https://raw.githubusercontent.com/OpenDriveLab/FreeTacMan/main/figure/FreeTacMan_teaser.gif" alt="FreeTacMan" width="120"> | [FreeTacMan](https://freetacman.github.io/) | 面向接触丰富操作的、无需机器人本体的视触觉数据采集系统（ICRA 2026），软件仓库开源。 |
| <img src="https://v1.leaphand.com/static/videos/teaser.png" alt="LEAP Hand" width="120"> | [LEAP Hand](https://v1.leaphand.com/) | 第一代 LEAP 灵巧手：面向机器人学习的低成本仿人平台，使用 Dynamixel，并提供公开的装配与零件页面。 |
| <img src="https://v2.leaphand.com/static/figures/size_comparison.jpg" alt="LEAP Hand V2" width="120"> | [LEAP Hand V2](https://v2.leaphand.com/) | 面向机器人学习的低成本、易组装刚软混合灵巧手。官方材料描述为 8 电机、高灵巧、零件可 3D 打印的设计。 |
| <img src="https://v2-adv.leaphand.com/static/figures/mounted.jpg" alt="LEAP Hand V2 Advanced" width="120"> | [LEAP Hand V2 Advanced](https://v2-adv.leaphand.com/) | LEAP v2 系列中的 17 自由度刚软混合后继型号，带掌部主动关节，使用 Dynamixel，并提供公开的 API/IK 仓库。 |
| <img src="https://raw.githubusercontent.com/orcahand/orcahand_hardware/main/assets/banner.png" alt="ORCA Hand" width="120"> | [ORCA Hand](https://www.orcahand.com/) | 17 自由度腱传动灵巧手，硬件文件开源，Python 控制器支持 Dynamixel 或飞特电机。 |
| <img src="https://robotnanohand.com/wp-content/uploads/2021/10/front_cover.jpg" alt="Robot Nano Hand" width="120"> | [Robot Nano Hand](https://robotnanohand.com/) | 开源机械手项目，官方网站提供零件清单和装配步骤，文件托管在 GitLab 和 Thingiverse。 |
| <img src="https://raw.githubusercontent.com/ruka-hand/RUKA/main/assets/ruka.gif" alt="RUKA" width="120"> | [RUKA](https://ruka-hand.github.io/) | 将机械设计与基于学习的控制一并开源的仿人灵巧手，提供公开 BOM、CAD 和软件。 |

[详细对比](categories/hands_grippers/README.zh-CN.md)

## 遥操作与数据采集装置

| 图片 | 项目 | 简介 |
| --- | --- | --- |
| <img src="https://dex-umi.github.io/static/images/teaser.png" alt="DexUMI" width="120"> | [DexUMI](https://dex-umi.github.io/) | 将人手作为通用操作接口、用于采集灵巧操作数据的系统，提供开源软件和硬件说明。 |
| <img src="https://do-glove.github.io/static/images/glove_explosion.png" alt="DOGlove" width="120"> | [DOGlove](https://do-glove.github.io/) | 面向灵巧遥操作与数据采集的低成本开源力反馈手套（RSS 2025）。 |
| <img src="https://wuphilipp.github.io/gello_site/static/images/teaser_final.png" alt="GELLO" width="120"> | [GELLO](https://wuphilipp.github.io/gello_site/) | 面向机械臂的通用、低成本遥操作框架，基于 Dynamixel，软件与机械结构分仓库开源。 |
| <img src="https://behavior-robot-suite.github.io/assets/img/system_overview.png" alt="JoyLo" width="120"> | [JoyLo](https://behavior-robot-suite.github.io/) | BEHAVIOR Robot Suite 中用于全身家务操作数据采集的遥操作/主动端装置，官方控制仓库中提供硬件文件。 |
| <img src="https://raw.githubusercontent.com/InternRobotics/OpenHomie/main/teaser.png" alt="OpenHomie" width="120"> | [OpenHomie](https://homietele.github.io/) | HOMIE 的开源软件与硬件：面向人形机器人运动-操作遥操作的同构外骨骼座舱。 |
| <img src="https://specialist-ai.github.io/specialist-docs/manuals/handheld/cover.png" alt="Specialist" width="120"> | [Specialist](https://specialist-ai.github.io/) | 面向大规模采集机器人训练数据的手持/主动夹爪接口。手持夹爪用 Insta360 相机和打印标记记录示范，同几何的主动夹爪把策略部署到机械臂上，无需重定向。 |
| <img src="https://vision-in-action.github.io/images/teaser_v2.5.png" alt="ViA" width="120"> | [ViA](https://vision-in-action.github.io/) | Vision in Action：开源主动感知系统，公开硬件重点是机器人颈部，并与 ARX 机械臂和 ROS 一起用于基于演示的学习。 |

[详细对比](categories/teleop_data/README.zh-CN.md)

## 桌面 / 教育机器人

| 图片 | 项目 | 简介 |
| --- | --- | --- |
| <img src="https://image.lceda.cn/oshwhub/pullImage/fafb5929527c4adfacbdf7070f97a870.jpg" alt="EchoEar（喵伴）" width="120"> | [EchoEar（喵伴）](https://oshwhub.com/esp-college/echoear) | 桌面 AI 陪伴设备（ESP-VoCat / 喵伴），带圆形触摸屏、语音交互和可选旋转底座，作为 ESP-Brookesia 生态中的开源硬件示例发布。 |
| <img src="https://raw.githubusercontent.com/ZZongzheng0918/Morpheus-Hardware/main/media/teaser.png" alt="Morpheus" width="120"> | [Morpheus](https://jiawenyang-ch.github.io/Morpheus-Hardware-Design/) | 采用混合驱动、33 个执行器的神经驱动仿生表情脸，软硬件仓库开源（RSS 2025）。 |
| <img src="https://custom-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_9000,w_1200,f_auto,q_auto/838564/935880_609691.png" alt="OttoDIY" width="120"> | [OttoDIY](https://www.ottodiy.com/) | 广泛使用的 3D 打印开源教育行走机器人，官方提供 Arduino 库，并在项目网站发布设计和教程。 |

[详细对比](categories/desktop_educational/README.zh-CN.md)

## 如何组织

同一类别内，项目按**英文名称字母顺序**排列。这是一条客观规则：星标数、价格、更新时间以及商业关系都不参与排序。

本首页是整体清单。逐字段对照表和简短对比分析放在各类别页面中，从上面各节可以进入。

硬件许可证与软件许可证分开记录，来源是 LICENSE 文件或官方许可证声明，并显示在各类别的对比表中。找不到时填写「未知」。

仓库活跃度（星标、最近一次提交）记录于 **2026-11-20**（Asia/Shanghai），并显示在各类别页面中。YAML 中的提交时间是 UTC，类别页转换为 Asia/Shanghai 显示。这些数字会变化，请当作快照。

## 收录标准

同时满足以下条件的项目可以收录：

1. 属于**开源机器人硬件**项目——在物理世界中感知并执行动作的机器人或紧密耦合设备，包括机械臂、灵巧手、移动底座、腿式机器人、遥操作与数据采集硬件、教学平台，以及密切相关的传感器或表情/面部硬件。
2. **设计文件和/或源代码已公开**，或官方维护者已宣布可获取的开源发布。仅有论文或宣传页，不足以作为已确认条目。
3. 条目能指向**一手来源**（官方仓库、文档或机构页面）。
4. 不能仅仅为了宣传闭源产品而收录。

本目录聚焦开源机器人硬件。某项目官方使用的软件栈可以记录在该项目的 `software_ecosystem` 字段中。

接近符合条件、但未能找到公开设计文件的项目，可以保留并标为**未核实**，同时写明缺口，避免悄悄漏掉，或把尚未开源的项目写成已开源。

本初稿先从一份公开项目索引播种，再对照一手来源核对。欢迎通过 Pull Request 增补、勘误、调整分类或移除条目。详见 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。

## 核实等级

- **官方核实** — 该项目的维护者或官方机构已确认本目录条目（例如在跟踪 issue 中回复，或提交确认用的 Pull Request）。本初稿中的条目都还没有这一状态。
- **社区核实** — 有独立贡献者对照实物复现核查了该条目，或提供了超出阅读公开页面的、带日期的证据。本初稿中的条目都还没有这一状态。
- **已对源核查** — 本目录维护者已在标注的截止日期，对照公开的一手来源（官方仓库、文档或商家页面）核对所列信息。这不等于项目维护者确认，也不等于已经复现硬件。
- **未核实** — 条目为新提交，或关键信息（包括设计文件是否已公开）无法从公开一手来源确认。

本初稿中没有任何条目属于「官方核实」或「社区核实」。大多数条目是「已对源核查」：我们查阅了公开的一手来源，但项目维护者尚未确认条目文本。

## 本目录的许可证

本目录的文本（YAML 数据、生成的 README、贡献指南和 Issue/PR 模板）使用 [CC BY 4.0](LICENSE) 许可。生成脚本 `scripts/generate_readme.py` 使用 [MIT 许可证](LICENSE-CODE)。上述许可不改变被收录项目自身的许可证。

## 免责声明

成本、交期和购买信息都会变化。购买或动手制作前，请向官方项目核实价格与许可证。本目录不构成对任何卖方的背书，也不构成许可证方面的法律意见。

_由 `scripts/generate_readme.py` 根据 `data/projects.yaml` 生成。对源核查快照：2026-11-20（Asia/Shanghai）。_
