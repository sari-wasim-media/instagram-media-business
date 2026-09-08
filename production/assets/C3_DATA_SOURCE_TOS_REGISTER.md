# Data-source register — the compliant sources for C3 and for every factual claim

**Sourcing Gate item 6:** *per source, confirm manual collection and republication of derived figures is
permitted; sources recorded; no scraper during the experiment.*

**Status: OPERATIONALISED — ACTIVE, delegated production decision (2026-09-08)**, under the founders'
**conservative data-source posture** of the same date (`DECISIONS.md`): *if the applicable terms do not
clearly permit the intended use, the source is not used; a narrower data set is preferred over ambiguous or
restrictive terms.* That rule removes the facts-versus-terms judgement call an earlier version of this
register asked the founders to make. A source is usable only when it is **published for republication** or
its terms **clearly permit** the use; "no clause found" is not permission.

Research basis: `SOURCING_ROUTES_RESEARCH.md` §2 (accessed 2026-09-05). Re-read a row only if a source
publishes explicit permission or a data-use policy.

## The register

| # | Source | Data | Terms read (2026-09-05) | Conclusion under the conservative posture | Status |
|---|---|---|---|---|---|
| 1 | **Brand press releases and newsroom release notes** (Nike, adidas, New Balance, ASICS, PUMA, Amer Sports, On, Deckers…) | Retail list prices at announcement, release dates, sizing tiers, materials, where sold | Press releases exist to be reported; Amer Sports states public use of press material "by mentioning the source" | The facts in a release are published for reporting. Cite by brand, release title and date. **Never reuse the release's images or text beyond the facts** | **USABLE** |
| 2 | **Published market reports and data press releases** — StockX "Big Facts" (via wire), GOAT / Stadium Goods reports, brand earnings releases, industry and analyst reports | Aggregate price movement, brand share, top sellers, resale medians as reported | A report or wire release is published to be cited | Cite by publisher, title and date. **Reproduce figures, never the report's charts or graphics**; state "as reported by" | **USABLE** |
| 3 | Brand and retailer product pages | Current list price, sizes, availability | Nike / adidas / ASICS / Crocs / VF: personal, non-commercial use; **Deckers bans "any non-personal use of … prices"** | Not a citable source. **Confirmation only**: check that the release note's price still stands; the release note is what is cited. If a price exists only on a product page, the piece states it as "list price shown by the seller on <date>" only when the seller's terms do not restrict it; where they do (Deckers), the figure is not used | **CONFIRM ONLY** |
| 4 | Laced | Resale asks / sales | No scraping or republication clause found | No clause is not permission | **NOT USED** |
| 5 | KLEKT | Resale asks / sales | "personal, non-business purposes only" | Restrictive | **NOT USED** |
| 6 | eBay sold listings | Last-sale prices | Automated means banned; reproducing content "that belongs to eBay or someone else" listed as possible infringement; no personal-use grant | Not clearly permitted | **NOT USED** |
| 7 | StockX live pages | Last-sale medians, volumes | Could not fetch; snippet bans "automated or manual means … copy any information" | Restrictive on its face; its **published reports are row 2** | **NOT USED** |
| 8 | GOAT live pages | Last-sale prices | Could not fetch; snippet: personal, non-commercial only | Restrictive | **NOT USED** |
| 9 | Flight Club | Asks / sales | Could not fetch; snippet reaches manual extraction | Restrictive | **NOT USED** |
| 10 | Stadium Goods live pages | Asks | "Content of this Site is for personal use only"; "non-commercial use" | Restrictive; its published reports are row 2 | **NOT USED** |
| 11 | Grailed | Streetwear resale | Could not fetch; snippet: no copying except as expressly permitted | Restrictive | **NOT USED** |
| 12 | Secondary reporting (sneaker news sites, other accounts) | Anything | Their content is theirs | Never a source. A lead to find the official release or report, which is then cited | **LEAD ONLY** |

## What this means for the engines

- **C1** takes every fact — name, date, price, sizes, where — from the brand's release note or press release
  (row 1), or from the seller's own public announcement of the drop. A release with no confirmed date is not
  eligible for the queue. Retailer pages confirm; they are not cited.
- **C3** builds from rows 1 and 2: **MOVE** charts from report series or a brand's own price history in
  release notes; **SPREAD** from release-note retail against report-stated resale; **SHARE** from report data;
  **BELOW RETAIL** only where a published report states the figures. Live marketplace prices are not
  collected, manually or otherwise. The data set is narrower than the engine definition imagined; that is
  the founders' choice and it is recorded.
- **C2** chips (retail / resale) follow the same rows; a chip that cannot be sourced from rows 1–2 is dropped.
- **Stories** (Tuesday PRICE CHECK) use a figure already sourced for a C3 piece.

## Operating rules

- **No scraper, no extension, no export, no bulk download, ever** (locked).
- Every figure carries its source class, publisher and date on the frame (C3) or in the caption, and in the
  tracking row.
- Sample honesty: state what the report measured, its window and, where given, its sample; never present a
  report's figure as the desk's own measurement.
- If a needed figure exists only in a NOT USED source, the piece is written without it or the subject
  changes. The rule is not re-argued per piece.
- A row moves to USABLE only when the source publishes explicit permission (a press / data-citation policy
  or terms that clearly permit republication of derived figures); record the URL, the clause and the date.

## Gate item 6 — record

Sources permitted: rows 1–2. Sources excluded: rows 4–11 (and row 3 as a citable source). No scraper. The
check is complete under the conservative posture; **Sourcing Gate item 6 passes on this register.**
