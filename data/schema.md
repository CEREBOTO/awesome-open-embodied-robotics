# Project data schema

`projects.yaml` is the single source of truth for this directory. Do not edit `README.md` or `README.zh-CN.md` by hand; change the YAML (or the generator) and run:

```bash
pip install -r requirements.txt
python scripts/generate_readme.py
```

## Top-level keys

| Key | Type | Meaning |
| --- | --- | --- |
| `schema_version` | string | Schema version of this file. |
| `as_of` | string | Calendar date (`YYYY-MM-DD`) when activity numbers and source checks were recorded. |
| `as_of_timezone` | string | IANA timezone used when reporting times in the READMEs (this project uses `Asia/Shanghai`). |
| `directory` | object | Name, maintainer, and policy flags for the directory itself. |
| `categories` | list | Category definitions, display order, and short comparison notes. |
| `verification_levels` | list | Public definitions of verification statuses. |
| `projects` | list | One record per listed project. |

## `projects[]` fields

| Field | Type | Meaning |
| --- | --- | --- |
| `id` | string | Stable slug (`kebab-case`). |
| `name` | string | Canonical English name. Used as the alphabetical sort key (case-insensitive, punctuation ignored). |
| `name_zh` | string | Chinese display name (may match `name` when there is no established Chinese form). |
| `category` | string | One of the `categories[].id` values. |
| `type` | string | Optional finer type (for example `tactile_sensor`, `animatronic_face`, `biped`, `wheeled_leg`). |
| `website` | string or `Unknown` | Official project page. |
| `repo` | string or `Unknown` | Primary public repository URL. |
| `docs` | string or `Unknown` | Official documentation. |
| `paper` | string or `Unknown` | Paper or preprint, if any. |
| `maintainer` | string or `Unknown` | Person, lab, or organization that maintains the project. |
| `description` | string | Short English description. |
| `description_zh` | string | Short Chinese description, in sync with `description`. |
| `dof` | string or `Unknown` | Degrees of freedom / actuated joints, as stated by the official source. |
| `key_specs` | string or `Unknown` | Other notable physical specs (size, payload, and similar). |
| `motors` | string or `Unknown` | Actuator brand and model when known. |
| `communication` | string or `Unknown` | Bus or protocol (CAN, RS-485, Dynamixel TTL, and similar). |
| `bom_cost` | string or `Unknown` | Approximate build or kit cost, with currency. Never invent a number. |
| `bom_cost_source` | string or `Unknown` | Where the cost figure came from. |
| `software_ecosystem` | list of strings | Named stacks actually mentioned by official sources (LeRobot, ROS 2, MuJoCo, Isaac Lab, …). Empty if none confirmed. |
| `hardware_license` | string or `Unknown` | License covering CAD / mechanical / PCB design, taken from a LICENSE file or an official license statement. |
| `software_license` | string or `Unknown` | License covering source code, taken from a LICENSE file or an official license statement. |
| `license_notes` | string | Discrepancies, multiple repos, or “file not found” notes. |
| `repo_stars` | string or `Unknown` | Star count of the primary repo, as reported by the recorded source. |
| `repo_last_commit` | string or `Unknown` | Last commit timestamp on the default branch, in UTC (`YYYY-MM-DDTHH:MM:SSZ`). |
| `repo_activity_as_of` | string | Date the activity figures were recorded. |
| `repo_activity_source` | string | How stars and the last commit were obtained. |
| `purchase_channels` | list | Official or upstream ways to obtain a unit or parts (the project's own shop, official documentation or BOM, or an official manufacturer store). A Cereboto product page may be included only when Cereboto actually sells the product, with a disclosure. Do not list third-party, peer, or competitor vendors. Each item has `name`, `url`, and optional `note`. |
| `cereboto_related` | boolean | True if Cereboto sells or officially partners on this project. |
| `disclosure` | string or empty | Public disclosure text when `cereboto_related` is true. |
| `verification_status` | string | One of `official_verified`, `community_verified`, `source_checked`, `unverified`. |
| `verification_notes` | string | Extra context, including unconfirmed open-source status. |
| `sources` | object | Map of claim area (`repo`, `licenses`, `bom_cost`, `specs`, …) to the URLs used. |
| `notes` | string | Any other factual caveat. |

Use the literal strings `Unknown` (English fields) and `未知` (Chinese fields) when a fact was not found. Do not guess.
