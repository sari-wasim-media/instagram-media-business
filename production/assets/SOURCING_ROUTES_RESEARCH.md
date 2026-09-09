# Sourcing routes — research record (accessed 2026-09-05)

**What this is.** The rights and terms research behind `SOURCE_CLASS_DECISION.md`, `C2_SOURCING_ROUTES.md`
and `C3_DATA_SOURCE_TOS_REGISTER.md`, done from the repository on 2026-09-05 by reading the pages named below.
**What it is not:** legal advice, and not a substitute for the founders' own verification — several pages
could not be fetched and are marked so. Terms change; re-read before relying on any of them.

Legend: **V** = read directly on the first-party page · **S** = first-party page blocked; wording is a search
snippet of that page, unverified · **CNF** = could not fetch — founder must read directly.

---

## 1. Brand newsroom / press-asset terms

| Brand | Press site | Terms read | Editorial use granted? | Social use addressed? | Restriction | Status |
|---|---|---|---|---|---|---|
| Nike / Jordan | about.nike.com/en/newsroom · media-assets.nike.com | Nike Terms of Use (Oct 2025) | No — "personal, noncommercial use" | No | Content owned by Nike; marks need written permission; bans "data mining, robots, scraping" | V (asset library gating CNF) |
| adidas | news.adidas.com | adidas-group.com/en/legal-notice | No | No | "may not modify, copy, distribute … publish … the Content" except as permitted | V |
| New Balance | newbalance.newsmarket.com | newbalance.com/terms.html | Unknown | Unknown | Snippet: "rights-free for editorial purposes only" | CNF / S |
| ASICS | corp.asics.com/en/press | corp.asics.com/en/p/status | No — "prior written authorization" | No | Copy/repurpose/display prohibited | V |
| **PUMA** | **mediahub.puma.com** | about.puma.com/en/legal | **Yes** — "cleared for editorial and news use across media channels" | Not explicitly | Marks need written authorization | **V** |
| Salomon (Amer Sports) | amersports.com/newsroom/materials-for-media | amersports.com/site-terms | Yes for press releases and "public" material, "by mentioning the source" | No | Otherwise "private, non-commercial use" | V |
| HOKA (Deckers) | ir.deckers.com | deckers.com/terms-of-use (Jan 2025) | No | No | Prohibits "any collection or commercial use of any photographs" and "any non-personal use of our product names, listings, descriptions, or prices" | V |
| On | press.on-running.com | none found; on.com T&Cs did not load | Unknown | Unknown | press@on.com | CNF |
| Converse | — | converse.com terms | Unknown | Unknown | Snippet: "personal, non-commercial use" | CNF / S |
| Vans (VF) | vfc.com/news/media-assets | vfc.com/terms-of-use (2008) | No | No | "personal, non-commercial use only" | V (vans.com CNF) |
| Reebok | news.reebok.com | reebok.com terms | Unknown | Unknown | — | CNF |
| Crocs | investors.crocs.com | crocs.com terms (2020) | No | No | "individual use only"; no republication without written permission | V |

**Reading:** only PUMA states an editorial clearance in text that was actually read, and even that does not
mention social or commercial use. No brand read grants social-media use. Press imagery is therefore **not a
default route** for C1 or C2; it is a per-brand exception that requires the founders to read the terms,
archive them, and log the licence reference per asset (`PRESS_VERIFIED` class).

## 2. Marketplace and data-source terms (C3)

| Source | Terms | Automated collection | Manual copying / republication | Status |
|---|---|---|---|---|
| StockX | stockx.com/terms | Banned (S) | Snippet bans "automated **or manual** means … copy any information … for any purpose without our express written permission" and public display of content without permission | **CNF / S — founder must read** |
| GOAT | goat.com/terms | Banned (S) | Snippet: view/print "solely for personal and non-commercial purposes" | CNF / S |
| eBay | User Agreement (eff. 28 Jun 2026), §3 | Banned: "robot, spider, scraper, data mining tools … or any automated means" | No personal-use grant; reproducing content "that belongs to eBay or someone else" listed as possible infringement | V |
| Grailed | grailed.com/about/terms | Banned incl. LLM tools (S) | Snippet: no copying/displaying "except as expressly permitted" | CNF / S |
| Flight Club | flightclub.com/terms-conditions | Banned (S) | Snippet reaches "any manual or automated application or means to extract … reproduce" | CNF / S |
| Stadium Goods | terms-of-service (Oct 2024) §11–13 | Banned ("scrape") | "Content of this Site is for personal use only"; "may only use the Site for non-commercial use" | V |
| KLEKT | terms-of-service (Jun 2026) §4.1 | No clause found | "personal, non-business purposes only" | V |
| Laced | terms-and-conditions (Jan 2025) §15 | No clause found | IP-ownership clause only; no republication bar found | V |
| Published reports (e.g. StockX "Big Facts" H1-2026 via PR Newswire, 12 Aug 2026) | press release | n/a | A press release exists to be cited; no citation policy beyond the wire byline | V |

**Reading:** every source with readable terms bans automated collection; StockX's and Flight Club's snippets
extend to manual copying; Stadium Goods and Deckers restrict prices and content to personal use. **"Manual
collection from public marketplace pages" is not automatically clean.** C3's default sources are published
reports and brand release notes; any marketplace is a source only after a founder has read its current
terms and recorded the conclusion in `C3_DATA_SOURCE_TOS_REGISTER.md`.

## 3. Stock photo licences (for photographs showing branded sneakers)

| Licence | Commercial use | The catch | Status |
|---|---|---|---|
| **Unsplash License** | Yes, "including for commercial purposes" | "does not include the right to use: Trademarks, logos, or brands visible in an image"; Unsplash's own help: non-commercial, positive, non-endorsing use is "likely" fine. Unsplash+ adds an IP warranty (up to US$10,000 per photo) | V |
| **Pexels License** | Yes, free to use | "Don't imply endorsement of your product by people or brands on the imagery"; no trademark use | V |
| Pixabay | Yes, except: "If Content contains any recognisable trademarks, logos or brands, you cannot use that Content for commercial purposes" | Effectively excludes sneaker photos | V |
| Wikimedia Commons (CC BY / CC BY-SA) | Yes with attribution (author · title · source · licence · "modified") | BY-SA requires the derivative to carry the same licence; trademark rights are separate | V |
| Adobe Stock Standard | Yes — "Post the asset to a website or social media site" | "Editorial use only" assets may not be used for promotion; 10 credits ≈ US$29.99/month | V |
| Shutterstock Standard / Editorial | Standard yes; Editorial "expressly excludes commercial uses" | Editorial content "cannot be used to sell, promote, or monetize a business" | CNF / S |
| Getty Editorial | No commercial/promotional use (§3.7) | US$167/month for 10 downloads — out of budget | V |

**Reading:** free licences clear the *photographer's copyright*; none clears the *trademark* in frame. That
residual is the same for the founders' own photographs and for every sneaker media page on the platform: it
is handled by nominative, editorial, non-endorsing use — depicting a product to discuss it, never implying the
brand sponsors the post. It is a residual the founders accept knowingly or not at all (see
`SOURCE_CLASS_DECISION.md` §4).

## 4. Fair use and trade dress (secondary sources, not advice)

- U.S. Copyright Office fair-use FAQ: limited portions for "commentary, criticism, news reporting"; "in cases
  of doubt … permission be obtained".
- *Warhol v. Goldsmith* (2023) and *Philpot v. IJR* (4th Cir.): reusing a photograph for the same purpose as
  the original — illustrating the subject — weighs against fair use even with cropping or aesthetic changes.
  **Directly on point for unlicensed brand press photos inside ranking posts.**
- INTA, "Fair Use of Trademarks": nominative fair use covers media reports and commentary that name or depict
  a brand without implying sponsorship.
- *Vans v. MSCHF* (2d Cir. 2023): the Rogers test is unavailable where a sneaker's trade dress is used as a
  source identifier on competing goods. Editorial illustration is a different posture, but it is the line
  that governs silhouette artwork — draw the shoe to discuss it, never to sell a shoe-shaped thing.

## 5. Design, video and audio tools

| Tool | Finding | Status |
|---|---|---|
| Canva Content License | Design use in social posts allowed; "Editorial Use Only" stock barred from commercial/promotional use; no trademark use; no standalone use | CNF / S |
| CapCut Terms (15 Apr 2026) + Materials Licence (22 Jan 2026) | Broad licence to CapCut over user content; only items marked "commercial" are commercial-use; **"Commercial Sounds" may be shared only within CapCut/TikTok** — not Instagram | V |
| Figma Terms (11 Mar 2026) | Customer retains all rights in customer content; no output restriction | V |
| **Instagram audio** | Licensed library "intended for personal, non-commercial use"; "certain business accounts … do not have access"; **Sound Collection: "entirely royalty free and safe to use in Reels and Instagram Stories" and "can be used for commercial purposes"** | V |

**Reading:** edit anywhere, but add music only at upload from Instagram's Sound Collection, and never bake
CapCut or Canva music into an export.

## 6. AI image generators (for the six C4 slots)

| Tool | Commercial / ownership | Provenance metadata | Plan needed | Status |
|---|---|---|---|---|
| **Adobe Firefly** | "commercially safe"; outputs "include Content Credentials that indicate AI was used"; generative-AI guidelines prohibit content violating third-party IP | Content Credentials (C2PA) attached | Free daily generations; Standard US$9.99/mo (free-tier watermark status unverified) | V (FAQ CNF) |
| OpenAI images | "you … own the Output" (S); "All generated images come with C2PA metadata" (S) | C2PA | Same terms | CNF / S |
| Midjourney | "You own all Assets you create" (S); no free trial | No C2PA (secondary) | Paid | CNF / S |
| Ideogram | "we do not restrict your ability to use User Output … including for commercial purposes"; free images are public | None stated | Free tier public | V |
| Google Gemini / Imagen | "Google won't claim ownership over that content"; SynthID; C2PA on Nano Banana Pro | SynthID + C2PA | — | V |
| Stability AI | Own outputs; community licence free under US$1M revenue | API only | — | V |
| Canva Magic Media | User responsible for IP suitability; provenance tags (S) | Tags | — | CNF / S |
| Leonardo.ai | Free tier: Leonardo retains broad rights; paid private: user owns | None stated | Paid for ownership | V |

**Reading:** Adobe Firefly is the recommended candidate — it states commercial safety in text and attaches
Content Credentials, which is what makes Instagram's "AI info" label appear automatically, which is the
treatment the sub-test wants measured. Gemini is the alternate. Both are **candidates**: `GATES.md` §1.4 item
9 requires the founders to verify the output licence themselves.

## 7. Fonts

Bebas Neue, Inter, IBM Plex Mono (and Anton, not used) are SIL Open Font License 1.1: "Permission is hereby
granted, free of charge … to use, study, copy, merge, embed, modify, redistribute, and sell modified and
unmodified copies of the Font Software." Verified from the `OFL.txt` files Google Fonts serves; copies are
vendored in `../house-style/fonts/`.

## 8. Instagram platform facts that shape the templates and policies (all first-party unless marked)

| Fact | Source |
|---|---|
| The AI label is "AI info"; Meta auto-labels from C2PA/IPTC indicators or self-disclosure; images are not required to be self-labelled, photorealistic video/audio is; penalties possible for failing to label required content; composer toggle "Add AI label" verified on Facebook/Threads, secondary for Instagram | about.fb.com 2024-04 (updated 2024-07/09), transparency.meta.com, facebook.com/help/7434563519957988 |
| In-app scheduling: reels, photos, carousels; up to 25 posts a day, 30 days ahead. Meta's help pages describe Story scheduling in Business Suite (desktop and mobile). **UNVERIFIED:** whether a scheduled Story preserves an interactive poll/quiz sticker — not stated on the pages read and not tested; treated as unsupported until tested on the real account | help.instagram.com/439971288310029, facebook.com/business/help/972600925713914 |
| Carousels up to 20 items; one orientation per carousel | help.instagram.com/269314186824048 |
| Reels over 3 minutes are not recommended; minimum 30 fps and 720 px; feed photos keep resolution at 1080 wide between 566 and 1440 tall (4:5 and 3:4 both supported) | help.instagram.com/2720958398006062, /1038071743007909, /1631821640426723 |
| Hashtags: "up to 5 tags on a post" — more than 5 and the comment does not post; use relevant tags, do not game | help.instagram.com/351460621611097, creators.instagram.com/faq |
| Cross-posting toggles: per post "Also share on…"; account-wide Accounts Center → Sharing across profiles (posts, story, reels); Trial reels are opt-in per reel ("tap Trial") | facebook.com/help/2808345489420767, help.instagram.com/459497729122868, /835643311711702 |
| Insights: the help pages read describe "Views" (plays/displays incl. repeats) and "Viewers" (unique accounts), and "Accounts reached" did not appear on those pages. **UNVERIFIED on the real accounts:** what the Insights screens actually show per format on these two accounts is to be observed at the Week-0 baseline capture. Reach (unique accounts) remains the canonical denominator whatever the UI label | help.instagram.com/788388387972460, /202865988324236 |
| Originality: help page keeps "fewer than 10 unoriginal reels or Feed posts over the last 30 days"; the April 2026 extension to photos and carousels speaks of accounts that "primarily" post unoriginal content and re-eligibility when "most" recent posts are original; borders, watermarks, subtitles, caption credits do not count as material edits | creators.instagram.com/blog/recommendations-and-originality, help.instagram.com/1800814370401535, creators.instagram.com/blog/rewarding-original-creators-on-instagram |
| Engagement bait: the creators FAQ tells creators to avoid "clickbait, engagement bait, or which promotes a contest or giveaway"; Meta's definition: posts that explicitly request votes, shares, comments, tags, likes | creators.instagram.com/faq, transparency.meta.com |
| Sound Collection: royalty-free, commercial use allowed | help.instagram.com/402084904469945 |

## 9. Pages that could not be fetched here

StockX terms · GOAT terms · Grailed terms · Flight Club terms · New Balance terms · Converse terms · Reebok
newsroom and terms · On terms · Shutterstock licence · Canva Content License and AI terms · OpenAI terms ·
Midjourney terms · Leonardo terms · Adobe Firefly FAQ (free-tier watermark) · Meta Sound Collection terms
(login wall) · Instagram's own "Add AI label" composer help article · Instagram Help "Trademark" page.

*Since the founders' conservative data-source posture (2026-09-08), the marketplace and unfetched-brand rows
no longer need reading: a source whose terms do not clearly permit the use is simply not used. The one page
the founders still read themselves is **Adobe Firefly's current terms** (Sourcing Gate item 9).*
