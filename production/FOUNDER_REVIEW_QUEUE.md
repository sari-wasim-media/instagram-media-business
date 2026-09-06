# Founder review queue — proposed lock values from the Creative System sprint

**Every item below is a proposal.** None is a decision until Sari and Wasim record it (each document carries
its own decision block, and `DECISIONS.md` gets the entry). Nothing here reopens a founder-locked decision;
each item fills a value the lock left to be fixed at template lock or before Day 1.

**Recommended review order:** items 1–4 (they gate production), then 5–9, then 10–13.

| # | Proposed lock value | Recommendation | Reasoning and decision block |
|---|---|---|---|
| 1 | **House System v1** — canvases, bands, palette, type, components, motion grammar, audio rule | Approve as the frozen house template set | `house-style/HOUSE_STYLE.md`; specimens in `templates/renders/` |
| 2 | **C2 ranked-item count = 7** in every C2 piece, every format | **7** (runner-up 8; 5 rejected) | `templates/C2_RANKED_ITEM_COUNT_DECISION.md` — the eight-criterion comparison; 147 images total, 42 for the gate |
| 3 | **C1 verdict scale COP · WAIT · PASS** with the four-criterion rubric (0–8), one-step override allowed | Approve | `templates/C1_RELEASE_VERDICT_DESK.md` §1 |
| 4 | **Story rotation** (Mon DROP CALENDAR · Tue PRICE CHECK · Wed THE POLL · Thu DESK NOTES · Fri THE VERDICT · Sat TWO SHOES · Sun THE WEEK) and **sticker weekday = Wednesday**, poll by default, quiz allowed | Approve | `templates/STORY_TEMPLATE_AND_ROTATION.md` §2–§3, §7 |
| 5 | **Fixed AI disclosure line:** "Imagery in this post is AI-generated and illustrative. It does not depict a real product." — in the caption and in an on-artwork block | Approve; keep both placements | `policy/AI_IMAGERY_POLICY_PACK.md` §3 |
| 6 | **AI tool candidate: Adobe Firefly** (alternate: Gemini) — the founders must verify the licence themselves (gate item 9) | Verify Firefly first | `policy/AI_IMAGERY_POLICY_PACK.md` §5; `assets/SOURCING_ROUTES_RESEARCH.md` §6 |
| 7 | **Source-class priority per engine** and the **residual trademark-risk acceptance** for product photography | Approve the order; sign the acceptance | `assets/SOURCE_CLASS_DECISION.md` §2, §4 |
| 8 | **Caption architecture and hashtag operating form** (3–5 tags: 2–3 subject + 1 fixed category + ≤ 1 community; ban list; alt text always; American spelling) | Approve | `policy/CAPTION_AND_HASHTAG_POLICY.md` |
| 9 | **Comment-reply policy** (24 h window, substantive comments, cap 15/post, like all, hide spam, no pins, no DM outreach) | Approve | `policy/COMMENT_REPLY_POLICY.md` |
| 10 | **Scheduling tool and publish settings** (Business Suite desktop; Reels share-to-feed ON; Facebook share OFF; no Trial; no location/tags; AI label ON for six only) | Approve | `policy/SCHEDULING_AND_PUBLISH_SETTINGS.md` |
| 11 | **Reserve composition** (C2 Reel + Caro, C3 Reel + Caro + Stat, C4 Reel + Caro) | Approve | `operations/RESERVE_REGISTER.md` |
| 12 | **Two operational readings of locked rules:** the C1 queue window (news ≤ 7 d before or release ≤ 10 d after publish) and C2's subject handling (theme = subject; #1 pick logged as secondary subject) | Approve | `backlog/README.md` §2; `templates/C2_RANKINGS_AND_TIER_LISTS.md` §7 |
| 13 | **Producer alternation by format batch, never by account** | Approve | `operations/PRODUCTION_RHYTHM.md` §4 |

## Findings surfaced for the founders (no locked decision needs reopening)

1. **Brand press imagery is not usable by default.** Of the newsroom terms read on 2026-09-05, only PUMA's
   media hub states an editorial clearance; Nike, adidas, ASICS, HOKA, Vans and Crocs grant personal,
   non-commercial use only. The gate already conditioned press assets on verified terms; the practical
   consequence is that C1 must work without a product photo (it now does) and C2 must rely on owned, free-
   licence and illustrated imagery.
2. **C3's "manual collection from public marketplace pages" needs the terms check the locked rule already
   demands — and several terms fail it.** StockX and Flight Club snippets reach manual copying; Stadium
   Goods restricts to personal, non-commercial use. C3's default sources are published reports and brand
   release notes until a founder clears a marketplace row in the register.
3. **Instagram Insights now names unique accounts "Viewers"**, not "Accounts reached". The locked Reach-
   denominator rule is unchanged; the tracking sheet says which field to record.
4. **The platform hashtag cap is now 5**, which matches the locked 3–5 policy exactly.
5. **Only Meta's Sound Collection is cleared for business accounts**; CapCut's "commercial" sounds are
   cleared for CapCut/TikTok only. The locked audio rule ("licensed or royalty-free") is satisfied by using
   Sound Collection at upload and nothing else.

## After approval

Record each accepted item in `DECISIONS.md` (ACTIVE · template lock), tick the decision blocks, and move the
scorecards in `gates/` forward. Then the founder work in `PRE_LAUNCH_RUNBOOK.md` begins.

## Git

This sprint's work sits on the task branch `claude/instagram-creative-system-sprint-74ibb0`. Per
`WORKFLOW.md` §4, opening the pull request and merging to `main` wait for the active founder's approval.
