# Awesome Open Embodied Robotics

An independent, community-driven directory of open-source embodied robotics projects, maintained by Cereboto to help developers discover, compare, and build the next generation of intelligent robots.

This directory is independent and community-driven. Cereboto maintains the list and also sells open-source embodied-robot hardware at [cereboto.com](https://cereboto.com/). Commercial partnerships do not affect ranking, and no brand is excluded for competitive reasons.

[简体中文](README.zh-CN.md) · [Contributing](CONTRIBUTING.md) · [License](LICENSE) · Data: [`data/projects.yaml`](data/projects.yaml)

## Contents

- [Single-arm / dual-arm manipulators](#single-arm-dual-arm-manipulators) (3)
- [Humanoids](#humanoids) (4)
- [Mobile manipulators](#mobile-manipulators) (3)
- [Quadruped / legged](#quadruped-legged) (4)
- [Dexterous hands & grippers](#dexterous-hands-grippers) (10)
- [Teleoperation & data-collection devices](#teleoperation-data-collection-devices) (6)
- [Desktop / educational robots](#desktop-educational-robots) (3)

## How this list is organized

Within each category, projects are sorted **alphabetically by English name**. That is an objective rule: star counts, price, recency, and commercial relationships are not used for ranking.

This homepage is the overall inventory. Detailed field-by-field tables and short comparison notes live on each category page, linked from the sections below.

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

## Disclosure policy

Cereboto sells kits and assembled products related to some projects in this list. Those entries carry a disclosure next to the project name and in the category comparison tables. Cereboto is not given special placement; the same alphabetical rule applies. Purchase links in this directory are limited to official or upstream sources (the project's own shop, official documentation or BOM, or an official manufacturer store) and, where Cereboto actually sells the product, a Cereboto product page. This is not a claim that no other sellers exist. Being a Cereboto product, or not being one, does not change rank or eligibility.

## License of this directory

The text of this directory (YAML data, generated READMEs, contributing guides, and issue/PR templates) is licensed under [CC BY 4.0](LICENSE). The generator script `scripts/generate_readme.py` is licensed under the [MIT License](LICENSE-CODE). These licenses do not change the licenses of the listed projects, which remain their own.

## Single-arm / dual-arm manipulators

- [DexWrist](https://dexwrist.csail.mit.edu/) — A compact 2-DoF quasi-direct-drive robotic wrist (pitch–yaw) for constrained and contact-rich manipulation, presented as a drop-in upgrade for existing arms.
- [OpenArm](https://openarm.dev/) — A fully open-source, human-scale 7-DoF-per-arm quasi-direct-drive platform for contact-rich teleoperation, imitation learning, and physical AI research, typically deployed as a bimanual system. Disclosure: sold by Cereboto
- [SO-101](https://github.com/TheRobotStudio/SO-ARM100) — A low-cost 3D-printed leader/follower robot arm (successor to SO-100) designed to work with the LeRobot stack for imitation learning and teleoperation.

[Detailed comparison](categories/manipulators/README.md)

## Humanoids

- [Berkeley Humanoid Lite](https://lite.berkeley-humanoid.org/) — An open, largely 3D-printed research humanoid with modular cycloidal gearboxes, designed so that parts can be sourced from common e-commerce vendors.
- [Fourier N1](https://www.fftai.cn/open-source/18) — Fourier's first open-release humanoid (Nexus-01): a 1.3 m, 38 kg, 23-DoF platform with official BOM, drawings, assembly guides, and SDK documentation.
- [Poppy Humanoid](https://www.poppy-project.org/en/robots/poppy-humanoid/) — A modular, 3D-printed educational and research humanoid with 25 Dynamixel actuators, historically one of the most widely documented open humanoid kits.
- [ToddlerBot](https://toddlerbot.github.io/) — An open, ML-oriented loco-manipulation humanoid platform with a public BOM, assembly manual, and simulation-to-real software stack.

[Detailed comparison](categories/humanoids/README.md)

## Mobile manipulators

- [AhaRobot](https://aha-robot.github.io/) — A low-cost open bimanual mobile manipulator for embodied-AI research, with separate software and hardware repositories.
- [TidyBot++](https://tidybot2.github.io/) — An open holonomic (swerve-drive) mobile manipulator for robot learning, with a published BOM and support for interchangeable commercial arms.
- [XLeRobot](https://github.com/Vector-Wangel/XLeRobot) — A practical dual-arm mobile home robot that combines two SO-101 arms with an omni-wheel base, aimed at household manipulation at a low official BOM cost.

[Detailed comparison](categories/mobile_manipulators/README.md)

## Quadruped / legged

- [AlexbotMini](https://roboparty.feishu.cn/wiki/IRANwwUcWi8EpLkuGC3c3G3Envf) — An open biped aimed at reinforcement-learning locomotion research, with mechanics, hardware, and algorithm repositories.
- [Micro Wheeled-leg Robot](https://github.com/MuShibo/Micro-Wheeled_leg-Robot) — A desktop-scale two-wheeled-leg robot with an ESP32 controller, Feetech bus servos in the legs, and simpleFOC wheel drives.
- [Open Duck Mini](https://github.com/apirrone/Open_Duck_Mini) — A desktop-scale open biped inspired by Disney's BDX droid, with a public BOM, print files, and a separate runtime repository. Disclosure: sold by Cereboto
- [Unitree Qmini](https://github.com/unitreerobotics/Qmini) — A fully 3D-printable open biped that uses 11 Unitree 8010 motors and a Raspberry Pi 4B reference computer, with a companion RL deployment stack.

[Detailed comparison](categories/legged/README.md)

## Dexterous hands & grippers

- [DexHand](https://www.dexhand.org/) — An open, 3D-printable dexterous humanoid hand intended as a low-cost research platform for grasping and manipulation.
- [Dextra](https://hackaday.io/project/9890-dextra) — An older open anthropomorphic robot-hand project documented on Hackaday.io, with published files, logs, and assembly instructions.
- [eFlesh](https://e-flesh.com/) — A highly customizable magnetic tactile sensor that uses cut-cell microstructures, released with an accompanying open repository.
- [FreeTacMan](https://freetacman.github.io/) — A robot-free visuo-tactile data-collection system for contact-rich manipulation (ICRA 2026), with an open software repository.
- [LEAP Hand](https://v1.leaphand.com/) — The first-generation LEAP dexterous hand: a low-cost, anthropomorphic, Dynamixel-based platform for robot learning, with public assembly and parts pages.
- [LEAP Hand V2](https://v2.leaphand.com/) — A low-cost, easy-to-assemble hybrid rigid-soft dexterous hand for robot learning. Official materials describe an 8-motor, highly dexterous design with 3D-printed parts.
- [LEAP Hand V2 Advanced](https://v2-adv.leaphand.com/) — A 17-DoF hybrid rigid-soft successor in the LEAP v2 line, with powered palm articulations and Dynamixel actuation, plus a public API/IK repository.
- [ORCA Hand](https://www.orcahand.com/) — A 17-DoF tendon-driven dexterous hand with open hardware files and a Python controller that supports Dynamixel or Feetech motors.
- [Robot Nano Hand](https://robotnanohand.com/) — An open robot-hand project with a public website, component list, assembly steps, and files hosted on GitLab and Thingiverse.
- [RUKA](https://ruka-hand.github.io/) — An open humanoid hand that rethinks mechanical design together with learning-based control, with public BOM, CAD, and software.

[Detailed comparison](categories/hands_grippers/README.md)

## Teleoperation & data-collection devices

- [DexUMI](https://dex-umi.github.io/) — A system that uses the human hand as a universal manipulation interface for collecting dexterous-manipulation data, with open software and hardware instructions.
- [DOGlove](https://do-glove.github.io/) — A low-cost open haptic force-feedback glove for dexterous teleoperation and data collection (RSS 2025).
- [GELLO](https://wuphilipp.github.io/gello_site/) — A general, low-cost, Dynamixel-based teleoperation framework for robot manipulators, with separate open software and mechanical repositories.
- [JoyLo](https://behavior-robot-suite.github.io/) — A teleoperation / leader device in the BEHAVIOR Robot Suite for whole-body household manipulation data collection, with public hardware files in the official control repository.
- [OpenHomie](https://homietele.github.io/) — Open software and hardware for HOMIE, an isomorphic exoskeleton cockpit for humanoid loco-manipulation teleoperation.
- [ViA](https://vision-in-action.github.io/) — Vision in Action: an open active-perception stack whose public hardware focus is a robotic neck, used with ARX arms and ROS for demonstration-based learning.

[Detailed comparison](categories/teleop_data/README.md)

## Desktop / educational robots

- [EchoEar](https://oshwhub.com/esp-college/echoear) — A desktop AI companion (ESP-VoCat / 喵伴) with a round touch screen, voice interaction, and optional rotating base, published as an open-hardware example in the ESP-Brookesia ecosystem.
- [Morpheus](https://jiawenyang-ch.github.io/Morpheus-Hardware-Design/) — A neural-driven animatronic face with hybrid actuation and 33 actuators, released with open hardware and software repositories (RSS 2025).
- [OttoDIY](https://www.ottodiy.com/) — A widely used 3D-printable open educational walking robot, with official Arduino libraries and a project website for design and academy materials.

[Detailed comparison](categories/desktop_educational/README.md)

## Disclaimer

Costs, lead times, and purchase information change. Confirm prices and licenses with the official project before you buy or build. This directory is not an endorsement of any seller, and it is not legal advice about licenses.

_Generated from `data/projects.yaml` by `scripts/generate_readme.py`. Source-check snapshot: 2026-11-20 (Asia/Shanghai)._
