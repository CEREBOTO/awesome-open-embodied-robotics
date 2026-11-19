# Source-site access notes

The first batch of candidate projects was taken from the user's site
**EAI OSH - 开源硬件创新平台** at `http://47.120.28.66/`.

What we observed on 2026-11-20 (Asia/Shanghai):

- `https://47.120.28.66/` did not complete a TLS handshake from this environment (timeout).
- Plain `http://47.120.28.66/` returned HTTP 200. The site is a Next.js App Router app (`buildId` `X8VwkXg69nM6PsGyr8_mp`). Project cards are loaded client-side, not embedded in the HTML `__NEXT_DATA__` blob.
- The project list is served by `GET http://47.120.28.66/api/projects?page=1&limit=100` (also available as `/api/v1/projects`). Pagination reported `total: 33`.
- Per-project records are also at `GET http://47.120.28.66/api/projects/slug/{slug}` and HTML pages at `http://47.120.28.66/projects/{slug}`. The slug API did not add fields beyond the list payload.
- Other useful endpoints: `/api/categories`, `/api/tags`, `/api/products`.
- Fields on the site were often incomplete (empty GitHub URLs, unspecified currency on `estimatedCost`, placeholder values such as `http:///`). They were treated as leads only. Claims in `data/projects.yaml` were checked against official repositories, documentation, and vendor pages, not copied from the site unless independently confirmed.

The cleaned extract is in `eai-osh-projects.json`. Site-admin email addresses present in the upstream API were removed.
