# Awesome Open Embodied Robotics

[![Discord](https://img.shields.io/badge/Discord-5865F2?logo=discord&logoColor=white)](https://discord.gg/fqczequGXj)

An independent, community-driven directory of open-source embodied robotics projects, maintained by Cereboto to help developers discover, compare, and build the next generation of intelligent robots.

This directory is independent and community-driven. Cereboto maintains the list and also sells open-source embodied-robot hardware at [cereboto.com](https://cereboto.com/). Commercial partnerships do not affect ranking, and no brand is excluded for competitive reasons.

[简体中文](README.zh-CN.md) · [Contributing](CONTRIBUTING.md) · [License](LICENSE) · Data: [`data/projects.yaml`](data/projects.yaml)

## Contents

- [Single-arm / dual-arm manipulators](#single-arm-dual-arm-manipulators) (4)
- [Humanoids](#humanoids) (4)
- [Mobile manipulators](#mobile-manipulators) (4)
- [Quadruped / legged](#quadruped-legged) (4)
- [Dexterous hands & grippers](#dexterous-hands-grippers) (10)
- [Teleoperation & data-collection devices](#teleoperation-data-collection-devices) (7)
- [Desktop / educational robots](#desktop-educational-robots) (3)

## Single-arm / dual-arm manipulators

| Image | Project | Summary |
| --- | --- | --- |
| <img src="https://martinpeticco.com/dexwrist/static/images/gearboxregular.png" alt="DexWrist" width="120"> | [DexWrist](https://dexwrist.csail.mit.edu/) | A compact 2-DoF quasi-direct-drive robotic wrist (pitch–yaw) for constrained and contact-rich manipulation, presented as a drop-in upgrade for existing arms. |
| <img src="https://openarm.dev/images/img_introducing_v2.webp" alt="OpenArm" width="120"> | [OpenArm](https://openarm.dev/) | A fully open-source, human-scale 7-DoF-per-arm quasi-direct-drive platform for contact-rich teleoperation, imitation learning, and physical AI research, typically deployed as a bimanual system. Disclosure: sold by Cereboto |
| <img src="https://raw.githubusercontent.com/TheRobotStudio/SO-ARM100/main/media/SO101_Follower.webp" alt="SO-101" width="120"> | [SO-101](https://github.com/TheRobotStudio/SO-ARM100) | A low-cost 3D-printed leader/follower robot arm (successor to SO-100) designed to work with the LeRobot stack for imitation learning and teleoperation. |
| <img src="https://raw.githubusercontent.com/roboninecom/SO-ARM102/main/assets/images/photos/so-arm-102-live.jpg" alt="SO-ARM 102" width="120"> | [SO-ARM 102](https://github.com/roboninecom/SO-ARM102) | An open-source leader–follower robot arm kit for teleoperation and imitation learning, each arm with five degrees of freedom plus a parallel gripper. It is a successor to SO-ARM 100 and SO-ARM 101 and is designed to work with LeRobot. |

[Detailed comparison](categories/manipulators/README.md)

## Humanoids

| Image | Project | Summary |
| --- | --- | --- |
| <img src="https://lite.berkeley-humanoid.org/static/berkeley-humaonid-lite-cover.png" alt="Berkeley Humanoid Lite" width="120"> | [Berkeley Humanoid Lite](https://lite.berkeley-humanoid.org/) | An open, largely 3D-printed research humanoid with modular cycloidal gearboxes, designed so that parts can be sourced from common e-commerce vendors. |
| <img src="https://raw.githubusercontent.com/FFTAI/Wiki-GRx-Pipeline/FourierN1/pictures/developer_banner.png" alt="Fourier N1" width="120"> | [Fourier N1](https://www.fftai.cn/open-source/18) | Fourier's first open-release humanoid (Nexus-01): a 1.3 m, 38 kg, 23-DoF platform with official BOM, drawings, assembly guides, and SDK documentation. |
| <img src="https://raw.githubusercontent.com/poppy-project/poppy-humanoid/master/doc/img/poppy-humanoid-github.jpg" alt="Poppy Humanoid" width="120"> | [Poppy Humanoid](https://www.poppy-project.org/en/robots/poppy-humanoid/) | A modular, 3D-printed educational and research humanoid with 25 Dynamixel actuators, historically one of the most widely documented open humanoid kits. |
| <img src="https://raw.githubusercontent.com/hshi74/toddlerbot/main/docs/_static/banner.png" alt="ToddlerBot" width="120"> | [ToddlerBot](https://toddlerbot.github.io/) | An open, ML-oriented loco-manipulation humanoid platform with a public BOM, assembly manual, and simulation-to-real software stack. |

[Detailed comparison](categories/humanoids/README.md)

## Mobile manipulators

| Image | Project | Summary |
| --- | --- | --- |
| <img src="https://aha-robot.github.io/static/images/hardware.png" alt="AhaRobot" width="120"> | [AhaRobot](https://aha-robot.github.io/) | A low-cost open bimanual mobile manipulator for embodied-AI research, with separate software and hardware repositories. |
| <img src="https://robotmabel.github.io/website/assets/og.jpg" alt="MABEL" width="120"> | [MABEL](https://robotmabel.github.io/website/) | An open-source 56-DOF anthropomorphic mobile bimanual robot with a three-module holonomic swerve base, vertical lift, pitching torso, 3-DOF head, two OpenArm-derived 7-DOF arms, and two ORCA-derived 17-DOF hands, with Vision Pro whole-body teleoperation plus ROS 2, MuJoCo, and LeRobot support. |
| <img src="https://tidybot2.github.io/images/og-image.jpg" alt="TidyBot++" width="120"> | [TidyBot++](https://tidybot2.github.io/) | An open holonomic (swerve-drive) mobile manipulator for robot learning, with a published BOM and support for interchangeable commercial arms. |
| <img src="https://github.com/user-attachments/assets/682ef049-bb42-4b50-bf98-74d6311e774d" alt="XLeRobot" width="120"> | [XLeRobot](https://github.com/Vector-Wangel/XLeRobot) | A practical dual-arm mobile home robot that combines two SO-101 arms with an omni-wheel base, aimed at household manipulation at a low official BOM cost. |

[Detailed comparison](categories/mobile_manipulators/README.md)

## Quadruped / legged

| Image | Project | Summary |
| --- | --- | --- |
| <img src="https://raw.githubusercontent.com/Alexhuge1/Alexbotmini_hardware/main/1_Mechanic/Alexbotmini_V1.0/4_Photos/alexbotmini_stand.jpg" alt="AlexbotMini" width="120"> | [AlexbotMini](https://roboparty.feishu.cn/wiki/IRANwwUcWi8EpLkuGC3c3G3Envf) | An open biped aimed at reinforcement-learning locomotion research, with mechanics, hardware, and algorithm repositories. |
| <img src="https://raw.githubusercontent.com/MuShibo/Micro-Wheeled_leg-Robot/master/4.Docs/Image/RobotReal.jpg" alt="Micro Wheeled-leg Robot" width="120"> | [Micro Wheeled-leg Robot](https://github.com/MuShibo/Micro-Wheeled_leg-Robot) | A desktop-scale two-wheeled-leg robot with an ESP32 controller, Feetech bus servos in the legs, and simpleFOC wheel drives. |
| <img src="https://github.com/user-attachments/assets/e240c06e-769f-4c87-b65f-189a442cf1e9" alt="Open Duck Mini" width="120"> | [Open Duck Mini](https://github.com/apirrone/Open_Duck_Mini) | A desktop-scale open biped inspired by Disney's BDX droid, with a public BOM, print files, and a separate runtime repository. Disclosure: sold by Cereboto |
| <img src="https://raw.githubusercontent.com/unitreerobotics/Qmini/main/images/Qmini.jpeg" alt="Unitree Qmini" width="120"> | [Unitree Qmini](https://github.com/unitreerobotics/Qmini) | A fully 3D-printable open biped that uses 11 Unitree 8010 motors and a Raspberry Pi 4B reference computer, with a companion RL deployment stack. |

[Detailed comparison](categories/legged/README.md)

## Dexterous hands & grippers

| Image | Project | Summary |
| --- | --- | --- |
| <img src="https://github.com/iotdesignshop/dexhand-ble/assets/2821763/de311dc5-b41e-4f2f-b8e6-849a51983018" alt="DexHand" width="120"> | [DexHand](https://www.dexhand.org/) | An open, 3D-printable dexterous humanoid hand intended as a low-cost research platform for grasping and manipulation. |
| <img src="https://cdn.hackaday.io/images/resize/600x600/5835141474981681029.jpg" alt="Dextra" width="120"> | [Dextra](https://hackaday.io/project/9890-dextra) | An older open anthropomorphic robot-hand project documented on Hackaday.io, with published files, logs, and assembly instructions. |
| <img src="https://e-flesh.com/static/images/graphics-3-1.png" alt="eFlesh" width="120"> | [eFlesh](https://e-flesh.com/) | A highly customizable magnetic tactile sensor that uses cut-cell microstructures, released with an accompanying open repository. |
| <img src="https://raw.githubusercontent.com/OpenDriveLab/FreeTacMan/main/figure/FreeTacMan_teaser.gif" alt="FreeTacMan" width="120"> | [FreeTacMan](https://freetacman.github.io/) | A robot-free visuo-tactile data-collection system for contact-rich manipulation (ICRA 2026), with an open software repository. |
| <img src="https://v1.leaphand.com/static/videos/teaser.png" alt="LEAP Hand" width="120"> | [LEAP Hand](https://v1.leaphand.com/) | The first-generation LEAP dexterous hand: a low-cost, anthropomorphic, Dynamixel-based platform for robot learning, with public assembly and parts pages. |
| <img src="https://v2.leaphand.com/static/figures/size_comparison.jpg" alt="LEAP Hand V2" width="120"> | [LEAP Hand V2](https://v2.leaphand.com/) | A low-cost, easy-to-assemble hybrid rigid-soft dexterous hand for robot learning. Official materials describe an 8-motor, highly dexterous design with 3D-printed parts. |
| <img src="https://v2-adv.leaphand.com/static/figures/mounted.jpg" alt="LEAP Hand V2 Advanced" width="120"> | [LEAP Hand V2 Advanced](https://v2-adv.leaphand.com/) | A 17-DoF hybrid rigid-soft successor in the LEAP v2 line, with powered palm articulations and Dynamixel actuation, plus a public API/IK repository. |
| <img src="https://raw.githubusercontent.com/orcahand/orcahand_hardware/main/assets/banner.png" alt="ORCA Hand" width="120"> | [ORCA Hand](https://www.orcahand.com/) | A 17-DoF tendon-driven dexterous hand with open hardware files and a Python controller that supports Dynamixel or Feetech motors. |
| <img src="https://robotnanohand.com/wp-content/uploads/2021/10/front_cover.jpg" alt="Robot Nano Hand" width="120"> | [Robot Nano Hand](https://robotnanohand.com/) | An open robot-hand project with a public website, component list, assembly steps, and files hosted on GitLab and Thingiverse. |
| <img src="https://raw.githubusercontent.com/ruka-hand/RUKA/main/assets/ruka.gif" alt="RUKA" width="120"> | [RUKA](https://ruka-hand.github.io/) | An open humanoid hand that rethinks mechanical design together with learning-based control, with public BOM, CAD, and software. |

[Detailed comparison](categories/hands_grippers/README.md)

## Teleoperation & data-collection devices

| Image | Project | Summary |
| --- | --- | --- |
| <img src="https://dex-umi.github.io/static/images/teaser.png" alt="DexUMI" width="120"> | [DexUMI](https://dex-umi.github.io/) | A system that uses the human hand as a universal manipulation interface for collecting dexterous-manipulation data, with open software and hardware instructions. |
| <img src="https://do-glove.github.io/static/images/glove_explosion.png" alt="DOGlove" width="120"> | [DOGlove](https://do-glove.github.io/) | A low-cost open haptic force-feedback glove for dexterous teleoperation and data collection (RSS 2025). |
| <img src="https://wuphilipp.github.io/gello_site/static/images/teaser_final.png" alt="GELLO" width="120"> | [GELLO](https://wuphilipp.github.io/gello_site/) | A general, low-cost, Dynamixel-based teleoperation framework for robot manipulators, with separate open software and mechanical repositories. |
| <img src="https://behavior-robot-suite.github.io/assets/img/system_overview.png" alt="JoyLo" width="120"> | [JoyLo](https://behavior-robot-suite.github.io/) | A teleoperation / leader device in the BEHAVIOR Robot Suite for whole-body household manipulation data collection, with public hardware files in the official control repository. |
| <img src="https://raw.githubusercontent.com/InternRobotics/OpenHomie/main/teaser.png" alt="OpenHomie" width="120"> | [OpenHomie](https://homietele.github.io/) | Open software and hardware for HOMIE, an isomorphic exoskeleton cockpit for humanoid loco-manipulation teleoperation. |
| <img src="https://specialist-ai.github.io/specialist-docs/manuals/handheld/cover.png" alt="Specialist" width="120"> | [Specialist](https://specialist-ai.github.io/) | A handheld-and-actuated gripper interface for collecting robot training data at scale. The handheld gripper records demonstrations with an Insta360 camera and printed tags; a matching actuated gripper deploys the policy on a robot arm without retargeting. |
| <img src="https://vision-in-action.github.io/images/teaser_v2.5.png" alt="ViA" width="120"> | [ViA](https://vision-in-action.github.io/) | Vision in Action: an open active-perception stack whose public hardware focus is a robotic neck, used with ARX arms and ROS for demonstration-based learning. |

[Detailed comparison](categories/teleop_data/README.md)

## Desktop / educational robots

| Image | Project | Summary |
| --- | --- | --- |
| <img src="https://image.lceda.cn/oshwhub/pullImage/fafb5929527c4adfacbdf7070f97a870.jpg" alt="EchoEar" width="120"> | [EchoEar](https://oshwhub.com/esp-college/echoear) | A desktop AI companion (ESP-VoCat / 喵伴) with a round touch screen, voice interaction, and optional rotating base, published as an open-hardware example in the ESP-Brookesia ecosystem. |
| <img src="https://raw.githubusercontent.com/ZZongzheng0918/Morpheus-Hardware/main/media/teaser.png" alt="Morpheus" width="120"> | [Morpheus](https://jiawenyang-ch.github.io/Morpheus-Hardware-Design/) | A neural-driven animatronic face with hybrid actuation and 33 actuators, released with open hardware and software repositories (RSS 2025). |
| <img src="https://custom-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_9000,w_1200,f_auto,q_auto/838564/935880_609691.png" alt="OttoDIY" width="120"> | [OttoDIY](https://www.ottodiy.com/) | A widely used 3D-printable open educational walking robot, with official Arduino libraries and a project website for design and academy materials. |

[Detailed comparison](categories/desktop_educational/README.md)

## How this list is organized

Within each category, projects are sorted **alphabetically by English name**. That is an objective rule: star counts, price, recency, and commercial relationships are not used for ranking.

This homepage is the overall inventory. Detailed field-by-field tables and short comparison notes live on each category page, linked from the sections above.

Hardware licenses and software licenses are recorded separately, from LICENSE files or official license statements, and appear in the category comparison tables. If a license could not be found, the field is `Unknown`.

Repository activity (stars and last commit) was recorded on **2026-11-20** (Asia/Shanghai) and is shown on the category pages. Commit timestamps are stored in UTC in the YAML and displayed there in Asia/Shanghai. Figures change; treat them as a snapshot.

## Inclusion criteria

A project can be listed when all of the following hold:

1. It is an **open-source robot hardware** project — a robot or tightly coupled device that senses and acts in the physical world, including arms, hands, mobile bases, legged robots, teleoperation and data-collection hardware, educational platforms, and closely related sensors or face/expression hardware.
2. **Design files and/or source code are publicly available**, or the official maintainer has announced a public open-source release whose files can be retrieved. A paper or marketing page alone is not enough for a confirmed listing.
3. The listing can point to a **primary source** (official repository, documentation, or organization page).
4. The project is not listed solely to advertise a closed product.

This directory focuses on open-source robot hardware. Software stacks that a listed project officially uses may be recorded in that project's `software_ecosystem` field.

Projects that almost qualify, but whose public design files could not be found, may be kept with verification status **Unverified** and an explicit note, so the gap is visible rather than silent.

This first draft was seeded from a public project index and then checked against primary sources. Entries may be added, corrected, recategorized, or removed by pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Verification levels

- **Official verified** — A maintainer or official organization of the project has confirmed this directory entry (for example by commenting on a tracking issue or submitting a confirmation pull request). None of the first-draft entries have this status.
- **Community verified** — An independent contributor has checked the entry against a physical build, or has provided dated evidence that goes beyond reading public pages. None of the first-draft entries have this status.
- **Source-checked** — Maintainers of this directory have checked the listed claims against public primary sources (official repository, documentation, or vendor pages) on the stated as-of date. This is not confirmation by the project maintainer, and it is not a reproduction of the hardware.
- **Unverified** — The entry is newly submitted, or key claims (including whether design files are publicly released) could not be confirmed from public primary sources.

No entry in this first draft is Official verified or Community verified. Most entries are Source-checked: we read public primary sources, but project maintainers have not confirmed the text.

## License of this directory

The text of this directory (YAML data, generated READMEs, contributing guides, and issue/PR templates) is licensed under [CC BY 4.0](LICENSE). The generator script `scripts/generate_readme.py` is licensed under the [MIT License](LICENSE-CODE). These licenses do not change the licenses of the listed projects, which remain their own.

## Disclaimer

Costs, lead times, and purchase information change. Confirm prices and licenses with the official project before you buy or build. This directory is not an endorsement of any seller, and it is not legal advice about licenses.

_Generated from `data/projects.yaml` by `scripts/generate_readme.py`. Source-check snapshot: 2026-11-20 (Asia/Shanghai)._
