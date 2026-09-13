# Claude discovery pre-scan — 2026-09-13 (reading only; nothing cleared, nothing downloaded)

**What this is.** Before the founders run the test, Claude scanned the free-licence pool for the 14 items to
give them leads and an early, honest read of route F coverage. **It is not founder time and it clears
nothing**: the four leads it produced are `CANDIDATE` rows in `candidates_log.csv` (`found_by =
CLAUDE_PRESCAN`) that a founder must re-verify — reverse-image check, licence line on the day, archive —
before any of them can become an asset. Its minutes are reported here, apart from the founders' logs.

**Method.** Openverse API (`api.openverse.org/v1/images`, licences CC0 / CC BY / PDM — the scan ran before the
founders' correction excluding CC BY from the initial test; all four leads are CC0, so nothing changes — i.e. the Wikimedia
Commons + Flickr CC pool) queried once per item by model name; Unsplash searched by model name for six items
with the result grid's alt text read and one or two pages opened; four Commons file pages opened and read
(author, source, licence, dimensions, the image itself). Pexels not scanned. **Elapsed: ≈ 6 minutes wall
clock for all 14 items** (14:51–14:57 UTC) — the API answers in seconds; the founders' visual scanning of
Unsplash / Pexels grids, which this pre-scan mostly skipped, is where their minutes will go.

## Per item

| Piece · item | Openverse (CC0 / BY / PDM) | Unsplash (by model name) | Lead? |
|---|---|---|---|
| CAR · 1 New Balance 990v6 'Grey' | 3 hits, all one 2013 Flickr set "New Balance Women's 990 Running Shoes" (slgckgc, CC BY 2.0 — a licence not used in the initial test) — not opened; the date implies a 990v3, not v6 | 65 photos; alt text is model-agnostic ("a pair of new balance shoes on a wooden floor" ×6); the first opened (Archer Allstars, Unsplash License) is a Fresh Foam model, not a 990 | **No** — version mismatch; the grid needs a visual pass |
| CAR · 2 ASICS Gel-Kayano 14 'Cream Black' | 1 hit: Commons, LeDroider, CC0, own work — the **Aritzia** colorway on an ARITZIA box | not scanned | **Lead, colorway mismatch** (`CND-0001`) |
| CAR · 3 Nike Zoom Vomero 5 'Photon Dust' | 1 hit: Commons, LeDroider, CC0, own work — side profile, light grey/cream, on a Nike box | not scanned | **Lead, colorway plausible** (`CND-0002`) |
| CAR · 4 New Balance 2002R 'Rain Cloud' | 3 hits: Commons LeDroider CC0 (brown/plum, three-quarter); a wordpress.org CC0 "Sweet Caramel" (not opened); a Commons "2002 vs 2002R" CC BY 4.0 **unknown author** (a laundering flag — do not use) | not scanned | **Lead, colorway mismatch** (`CND-0003`) |
| CAR · 5 Nike P-6000 'Metallic Silver' | 0 | not scanned | No |
| CAR · 6 Saucony Shadow 6000 'Grey' | 0 | not scanned | No |
| CAR · 7 Salomon XT-6 'Black Phantom' | 0 | not scanned | No — route B (Amer Sports) or X |
| REE · 1 New Balance 993 'Grey' | 0 | not scanned | No |
| REE · 2 Nike Air Monarch IV 'White Navy' | 1 hit: Commons, LeDroider, CC0, own work — **exact colorway**, pair on a Nike box | not scanned | **Lead, colorway match** (`CND-0004`) |
| REE · 3 Fila Disruptor 2 'White' | 0 | results are on-feet / people ("person wearing white Fila running shoes") | No |
| REE · 4 adidas Ozweego 'Core Black' | 0 | generic, people | No |
| REE · 5 Hoka Bondi 8 'White' | 0 | **0 photos** | No |
| REE · 6 PUMA RS-X 'White Black' | 0 | several "a pair of puma sneakers on a shelf" (Zakaria Issaad, Unsplash License, EXIF present) — the one opened is a PUMA **X-Ray** in a store display, so wrong item and store context | No — route B (PUMA Media Hub) |
| REE · 7 Balenciaga Triple S 'Grey' | 0 | generic, people | No — route S |

## What the pre-scan says, honestly

- **4 of 14 items have a plausible free-licence lead, and all four come from one Wikimedia Commons
  contributor** ("LeDroider": phone photographs of pairs on their boxes, self-published as CC0, a consistent
  series — ownership looks plausible but the founders still run the reverse-image check). Two match the
  brief's colorway; two would need a logged colorway swap.
- **10 of 14 have nothing at model level in the CC pool.** Unsplash's index is not model-aware: searching a
  model name returns generic sneaker photos, most with people, so the founders' 10-minute visual box per item
  is real work, not a formality.
- The long tail (P-6000, Shadow 6000, XT-6, 993, Disruptor, Ozweego, Bondi 8, RS-X, Triple S) will therefore
  fall to **route B (PUMA, Amer Sports) or route S (illustration)** — route X is not on the path (founder
  decision, 2026-09-13) — unless the visual
  pass finds what the index cannot. That is exactly what the test is designed to measure — this note does
  not pre-empt its verdict, and it is not a finding until founder time has been spent.
- A colorway change inside the same model is now an explicitly **logged swap** (`TEST_PIECES.md`, fixed-list
  rule), because the pre-scan showed that "the model exists on free stock" and "the named colorway exists on
  free stock" are different claims.

## Not done, deliberately

No image was downloaded. No file page was archived (the founders archive on the day they verify, so the
archive carries their date). No reverse-image check was run. No Pexels or Flickr-direct search. No Unsplash
grid was scanned visually beyond one or two opened pages per item. Nothing here is a clearance.
