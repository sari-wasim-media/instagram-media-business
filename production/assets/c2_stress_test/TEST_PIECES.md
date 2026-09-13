# The two stress-test pieces — briefs (fixed before sourcing starts)

**Status: PREPARED, NOT PRODUCED.** Two non-publishing C2 prototypes. They are **not** Week-1 content, are
**not** entered in `../../backlog/backlog.csv`, consume **no** matrix slot, and are **never scheduled or
published** as prototypes. Whether they are later promoted to the two C2 reserve pieces is decided after the
run (`../C2_SUSTAINABILITY_TEST.md` §6), never assumed.

**How the themes were chosen** (delegated production authority, 2026-09-13). Both are lifted from the shape
of the idea bank so they are representative of what the desk will actually publish; both name a specific
colorway per item because the template requires it and that is where sourcing gets hard; each mixes
icons with long-tail items; one includes a PUMA item and one an Amer Sports (Salomon) item so route B is
exercised on the only two brands with an archived editorial reading; the two item sets are disjoint
(anti-duplication rule 12). They were **not** picked for image availability — the point is to find out.

**Fixed-list rule.** The seven items and the two alternates are the whole universe for each piece. An item
may be swapped **only** for one of its alternates, **only** for a sourcing reason, and **every swap is
logged** in `candidates_log.csv` (`clearance_status = SWAPPED_OUT`, reason). **A colorway change inside the
same model is also a logged swap** (same row type, reason `WRONG_ITEM` or `NOT_FOUND`, the new colorway in
the notes) — the pre-scan showed that "the model exists on free stock" and "the named colorway exists on
free stock" are different claims, and the test must count the difference. The swap count is a metric.
Ranking order and tier placement are the producer's editorial call, made during the `RESEARCH` stage and
timed there.

**Colorway names** are written as the desk expects the brand writes them; the producing founder verifies the
exact name on the brand's product page during `RESEARCH` (product pages confirm only —
`../C3_DATA_SOURCE_TOS_REGISTER.md`) and corrects the frame, not the brief.

---

## Piece 1 — `TEST-C2-CAR-01` · Carousel · RANKED

| Field | Value |
|---|---|
| `piece_ref` | `TEST-C2-CAR-01` |
| Format | Carousel, 9 slides (hook · 7 items counting down · THE LIST); optional method slide if wanted |
| Variant | `RANKED` 1–7 |
| Theme (`subject_key`, for the record only) | `theme:retro-runners-everyday-wearability` |
| `title` (hook, ≤ 9 words) | **7 retro runners ranked for everyday wear** |
| `running_head` (≤ 28 chars) | `RETRO RUNNERS, EVERY DAY` |
| `ranked_by` | comfort, versatility, availability at retail — opinion-led, no numeric chip required |
| `method` slide | optional; only if the producer wants to state the three tests |
| Declared budget | 90 min · pass ≤ 135 active minutes |
| Producer | one founder (log initials) — the other founder QA's |

| Item | Model | Colorway (≤ 3 words) | Brand | Expected difficulty (planning note only) |
|---|---|---|---|---|
| 1 | New Balance 990v6 | 'Grey' | New Balance | icon; free stock plausible, colorway common |
| 2 | ASICS Gel-Kayano 14 | 'Cream Black' | ASICS | long tail; specific colorway |
| 3 | Nike Zoom Vomero 5 | 'Photon Dust' | Nike | long tail; specific colorway |
| 4 | New Balance 2002R | 'Rain Cloud' (Protection Pack) | New Balance | long tail; distinctive, so illustration-friendly |
| 5 | Nike P-6000 | 'Metallic Silver' | Nike | mid |
| 6 | Saucony Shadow 6000 | 'Grey' | Saucony | long tail |
| 7 | Salomon XT-6 | 'Black Phantom' | Salomon (Amer Sports) | mid; route B candidate (Amer Sports press material with source credit — founders confirm the reading on the day) |
| alt A | New Balance 1906R | 'Silver Metallic' | New Balance | — |
| alt B | Nike Air Max 1 | 'White Neutral Grey' | Nike | — |

Caption skeleton, alt text and slide anatomy: `../../templates/C2_RANKINGS_AND_TIER_LISTS.md` §2, §9.
Images: side profile, toe left, product at 80–90 % of the 936 × 560 plate, one provenance ID per item in the
filename (`TEST-C2-CAR-01__AST-nnnn.<ext>`).

## Piece 2 — `TEST-C2-REE-01` · Reel · TIER

| Field | Value |
|---|---|
| `piece_ref` | `TEST-C2-REE-01` |
| Format | Reel, 36.5 s at house pacing (hook 3.0 s · 7 × [0.4 s number + 3.6 s card] · summary 4.0 s · end card 1.5 s); cover = hook |
| Variant | `TIER` — 7 items in ≤ 4 tiers S / A / B / C; item cards carry the tier badge; the summary is the tier board |
| Theme (`subject_key`, for the record only) | `theme:dad-shoe-tier-list` |
| `title` (hook, ≤ 9 words) | **7 dad shoes, tiered S to C** |
| `running_head` (≤ 28 chars) | `DAD SHOES, S TO C` |
| `ranked_by` | comfort, design, price, ubiquity — opinion-led, no numeric chip required |
| Declared budget | 115 min · pass ≤ 172 active minutes |
| Producer | the other founder (log initials) — the first founder QA's |
| Audio | none baked in; a Sound Collection track would be chosen only at upload, and there is no upload — log nothing in the audio ledger |

| Item | Model | Colorway (≤ 3 words) | Brand | Expected difficulty (planning note only) |
|---|---|---|---|---|
| 1 | New Balance 993 | 'Grey' | New Balance | icon; a different model from 990v6 (rule 12 satisfied at model level) |
| 2 | Nike Air Monarch IV | 'White Navy' | Nike | icon of the category; stock plausible |
| 3 | Fila Disruptor 2 | 'White' | Fila | icon of the category; stock uncertain |
| 4 | adidas Ozweego | 'Core Black' | adidas | mid |
| 5 | Hoka Bondi 8 | 'White' | Hoka (Deckers) | mid; **no press route** (Deckers terms prohibit) |
| 6 | PUMA RS-X | 'White Black' | PUMA | **route B exercise** — PUMA Media Hub, founders confirm the wording and "media channels" on the day, archive the page |
| 7 | Balenciaga Triple S | 'Grey' | Balenciaga | hard; free stock unlikely; the realistic route X / S case |
| alt A | Skechers D'Lites | 'White Silver' | Skechers | — |
| alt B | ASICS Gel-Nimbus 9 | 'White Silver' | ASICS | — |

Reel anatomy and beats: `../../templates/C2_RANKINGS_AND_TIER_LISTS.md` §3; assembly in CapCut desktop or
the house renderer + ffmpeg (`../../operations/TOOLING.md` — no CapCut library content of any kind). Plate
936 × 500 on the item card. Filenames `TEST-C2-REE-01__AST-nnnn.<ext>`.

---

## What "complete" means for both pieces

- Every one of the 7 items has a **CLEARED** candidate with its evidence archived and a `provenance_register.csv`
  row (`piece_ref` = the piece, `slot_id` blank, `engine = C2`); `python3 tools/validate_provenance.py` clean.
- Laid out in the house template; caption written to the C2 skeleton; alt text on every slide / the cover;
  hashtags per policy (never posted, but written — the caption time is part of the burden).
- QA'd by the other founder against `../../operations/PRE_PUBLISH_QA.md` §A–§C/§E — including the
  nominative-use rule — with the sign-off row filled in `RESULTS.md`.
- **Not scheduled. Not published. Not entered in the queue. Not given a date.**
