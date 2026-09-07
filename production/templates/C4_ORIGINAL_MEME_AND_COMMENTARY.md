# C4 — Original Meme & Commentary · house template

**Engine definition (locked):** originated formats using owned or licensed imagery and original writing.
**Hard rule: never a reposted meme template, never a screenshot of another account, never someone else's
watermarked image.** Reel primary, static secondary. Distribution thesis: sends ÷ reach — memes travel by DM.
Highest quality variance of the four engines.

**Template status: PROPOSED — founder review required.** Specimens: `renders/c4/`.

C4 carries 21 posts: 12 Reels, 6 Carousels, 3 Statics (A: 6R/3C/1S · B: 6R/3C/2S). **Six of them are the
AI-imagery sub-test** (`../../experiment/active-84-post-plan/AI_IMAGERY_SUBTEST.md`): `B-W2-C4-REE-01`,
`A-W2-C4-CAR-01`, `B-W2-C4-STA-01`, `A-W4-C4-REE-01`, `B-W5-C4-CAR-01`, `A-W6-C4-STA-01`. None in Week 1.

Because C4 may never borrow a template, the house has to **own** its recurring formats. Seven are defined
below. A C4 piece is always one of these seven, executed in the house system, with new writing. Recurring
formats are the engine; consecutive instances use disjoint subjects (anti-duplication rule 12).

---

## 1. The seven named formats

| # | Format | What it is | Imagery | Best formats | Specimen |
|---|---|---|---|---|---|
| 1 | **TWO SHOES, ONE VERDICT** | Two products side by side, one ruling in an ink box | 2 (owned / licensed / self-drawn) | Static · Story · Reel (A, B, ruling as three beats) | `c4_static_two_shoes_one_verdict` |
| 2 | **THE RECEIPT** | A house-drawn receipt itemising a collector truth (the resale L, the cost of the hobby) | 0 | Static · Carousel (receipt, then the "total") | `c4_static_the_receipt` |
| 3 | **HOT TAKE TICKET** | One opinion on a ticket stub, numbered | 0 | Static · Reel (ticket tears to reveal the line) | `c4_static_hot_take_ticket` |
| 4 | **SNEAKERHEAD MATH** | An equation of collector logic with plates as operands | 0–3 | Static · Reel | `c4_static_sneakerhead_math` |
| 5 | **GROUP CHAT** | A house-drawn chat card dramatising a conversation; punchline slide | 0 | Carousel · Reel (bubbles appear per beat) | `c4_car_group_chat_01/02` |
| 6 | **EXPECTATION / REALITY** | Split card, two illustrated or photographed scenes, the caption is the joke | 2 | Static · Carousel · Reel | `c4_ai_slot_static_expectation_reality` (AI-slot specimen) |
| 7 | **INNER MONOLOGUE** | Kinetic say/think pairs over one hero image | 1 | Reel (primary Reel format) | `c4_reel_01/02_inner_monologue` |

Chat bubbles, receipts and tickets are **original house UI** drawn in the system (rounded bubbles in ink-3
and accent, mono receipt on white, paper ticket with a tear line). They imitate no real app, retailer or
venue, carry no logos, and are never screenshots.

## 2. Writing rules — where the quality variance is controlled

- Every piece has one observation about collector behaviour, resale reality or the culture — never about a
  named person, never about a specific real transaction by an identifiable account.
- The joke is in the writing; the imagery is a straight man. If the image has to carry the joke, it is the
  wrong format.
- No engagement bait on the artwork or in the caption (no "tag someone who…", "like if…", "comment your
  size"). A question is fine when it is the joke, not when it is the ask.
- No brand-bashing by name; roast the behaviour, not the company. No counterfeit or replica jokes that could
  read as promotion (locked business constraint). No sexual, political or drug references (business
  content boundaries) — including any play on the account name `sneakerbong`.
- Format lines are fixed voice: receipts end "THANK YOU FOR PLAYING"; tickets carry "ADMIT ONE OPINION";
  Two Shoes rulings begin with the letter of the winner.

## 3. Imagery rules

- Source classes, in order: **self-drawn** (house illustration, silhouettes, typographic art) → **owned
  photographs** (the founders' own pairs; faceless product shots) → **licensed stock** (licence archived;
  see `../assets/SOURCE_CLASS_DECISION.md`). Never a reposted template, never another account's screenshot,
  never a watermarked image, never a frame from a film or show, never a celebrity photograph.
- Plates as everywhere: white plate, no filters, no generative fill.
- Formats 2, 3 and 5 need no imagery at all, which is the deliberate pressure valve: a C4 slot can always be
  filled rights-free.

## 4. The six AI slots — the same template, different plate contents

Inside the six locked slots **only**, the imagery in the plate is an AI-generated **illustration**. Everything
else is identical: same format from the seven above, same layout, same beats, same caption architecture.
Best-fitting formats: EXPECTATION / REALITY (two illustrated scenes), INNER MONOLOGUE (one illustrated hero),
SNEAKERHEAD MATH (illustrated operands), TWO SHOES with two *abstract* illustrated "shoes" that are not real
products. The prohibited-use list in `AI_IMAGERY_SUBTEST.md` §5 applies in full — no real specific product,
no brand mark, no real person, no generative video, no reconstruction of a third-party image.

**Nothing on the artwork marks the post as AI-treated.** Disclosure is the identical fixed caption line
(locked requirement) plus the platform AI label, switched on when posting and never removed. Adding a visible
disclosure element to the frame would introduce a second visual difference between AI and non-AI C4 posts on
top of the imagery itself, which is the one difference the sub-test is meant to measure. The plate labels
in the specimens are annotations, not production elements. Full policy, wording and provenance fields:
`../policy/AI_IMAGERY_POLICY_PACK.md`.

Slot-by-format assignment is already fixed by the matrix: two Reels, two Carousels, two Statics. Recommended
format per slot (proposal, free to change at production as long as it is one of the seven):

| Slot | Format | Suggested house format |
|---|---|---|
| `B-W2-C4-REE-01` | Reel | INNER MONOLOGUE, illustrated hero |
| `A-W2-C4-CAR-01` | Carousel | EXPECTATION / REALITY, two illustrated scenes + punchline slide |
| `B-W2-C4-STA-01` | Static | SNEAKERHEAD MATH, illustrated operands |
| `A-W4-C4-REE-01` | Reel | EXPECTATION / REALITY as a three-beat Reel |
| `B-W5-C4-CAR-01` | Carousel | INNER MONOLOGUE as a carousel (say / think pairs per slide) |
| `A-W6-C4-STA-01` | Static | EXPECTATION / REALITY |

## 5. Reel grammar — INNER MONOLOGUE (primary), ~30 s

| Beat | Frame | Duration |
|---|---|---|
| 1 | Hook: "What I say vs what I think at a drop" over the hero plate | 3.0 s |
| 2–7 | Six say/think pairs: SAY line (Bebas 92) · rule · THINK line (Bebas 92, accent); the same hero image holds | 6 × 3.5 s = 21.0 s |
| 8 | Punchline pair, held longer | 4.0 s |
| 9 | End card | 1.5 s |

Total **29.5 s**. Other formats as Reels: TWO SHOES (A 4 s · B 4 s · ruling 5 s · plus a 3 s hook and end
card ≈ 20–24 s — extend each beat to reach 30 s); HOT TAKE TICKET (ticket tears over 3 s, line holds 6 s,
three supporting lines 3 × 3 s, end card ≈ 22 s — add a second take to reach 30 s); GROUP CHAT (bubbles
appear one per 2.5 s beat). Always 20–59 s, target 30–45 s.

## 6. Carousel grammar — 5–6 slides

GROUP CHAT: hook (the premise) · 2–3 chat slides · punchline slide (Bebas 104) · optional receipt-style
"total" slide. EXPECTATION / REALITY: hook · expectation · reality · the line · end. Always ≥ 5 slides (locked
band), ideally 5–6: memes do not want ten swipes.

## 7. Asset count and declared time budgets (Sourcing Gate item 1)

| Format | Rights-clean images | Notes | Declared budget |
|---|---|---|---|
| Static | 0–2 | 0 for formats 2, 3, 5 | 45 min: writing 20 · imagery 10 · layout 10 · caption and QA 5 |
| Carousel | 0–2 | | 60 min |
| Reel | 0–2 | usually 1 hero | 70 min |
| **AI slot (any format)** | 0 photographs; 1–2 AI illustrations | + prompt log, attestation, reviewer, disclosure | budget above **+ 30 min** generation and compliance review, measured at the Sourcing Gate AI test |

Whole experiment: roughly **20–30 images**, of which about 8–12 are AI illustrations in the six slots; no
image is ever reused across pieces.

## 8. Caption template

```
<the line, if it is not already on the artwork — ≤ 100 characters>
<one extra beat, optional>
[AI slots only, fixed:] <disclosure line from ../policy/AI_IMAGERY_POLICY_PACK.md>
#<subject tag> #sneakerhead #sneakermemes   (3–5 tags)
```
