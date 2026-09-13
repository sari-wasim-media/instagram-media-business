# Production tooling — decided defaults

**Status: ACTIVE — delegated production decision (2026-09-08)**, under the founders' tool-selection autonomy
decision of the same date. **Selection is not purchase.** Every tool below is chosen on its free tier; any
paid plan, paid licence, paid stock credit or other financial commitment needs explicit founder approval
before it happens, and creating an account with any tool is the founders accepting that tool's terms.
Research behind the choices: `../assets/SOURCING_ROUTES_RESEARCH.md` §5–§6.

| Job | Tool | Tier | Why | Rules |
|---|---|---|---|---|
| Statics and carousel slides | **Figma** (browser or desktop) | Free | Pixel-exact 1080 × 1350 frames, Google Fonts built in (Bebas Neue, Inter, IBM Plex Mono), no stock-content licence ambiguity, one shared file for both founders, terms leave all rights with the customer | Build one master per frame type from `../house-style/HOUSE_STYLE.md`; export PNG at 1×; never use Figma Community assets in production frames |
| Reel assembly (48 Reels) | **CapCut desktop** | Free | Fastest cut-based assembly of still frames with timed text; both founders can learn it in an hour | **No CapCut music, templates, effects, stickers, fonts or "commercial" sounds** — its commercial sounds are cleared for CapCut/TikTok only. Import the house frames, cut to the beat table, export 1080 × 1920, 30 fps, H.264, no watermark. Add audio **at upload** from Sound Collection. Note: CapCut's terms grant CapCut a broad licence over uploaded user content; the founders accept that when they create the account. Alternative with no such clause: DaVinci Resolve (free) or the house renderer + ffmpeg |
| Frame source for Reels and Stories | **The house renderer** (`../templates/src/render_frames.py`) or Figma | — | Frames come out at exact canvas sizes with the fonts embedded | Production frames drop the specimen tag; the renderer is a local aid, not automation |
| Scheduling | **Meta Business Suite, desktop** | Free | Both accounts in one place, screenshot-able scheduled list, Stories schedulable (sticker preservation unverified) | Time-zone check before Week 1; Wednesday sticker Story posted manually; `../policy/SCHEDULING_AND_PUBLISH_SETTINGS.md` |
| Audio | **Instagram Sound Collection** (in the Reels composer at upload) | Free | The one library Meta states is royalty-free and cleared for business and commercial use | Logged in `../assets/audio_ledger.csv`; the 14-day rules |
| AI illustration (six C4 slots + the test piece) | **Adobe Firefly** (web) | Free tier first | Adobe states its models are commercially safe and attaches Content Credentials, which lets Instagram's AI label appear on its own | The founders verify the current terms and record tool, version, plan and date (Sourcing Gate item 9); if the free allowance is too small for the test piece plus the six slots, a paid plan is a founder decision. Alternate: Google Gemini (SynthID) |
| Free stock | **Unsplash**, then **Pexels** | Free | Commercial use permitted; licence text archived per asset | Under the accepted trademark posture and its §5 rule (`../TRADEMARK_RISK_REVIEW.md`); never Pixabay for branded products; no "editorial use only" assets anywhere |
| Paid stock (gap-filler only) | Adobe Stock single credits | **Paid — founder approval per purchase** | Standard licence covers social posting | Route P in `../assets/C2_SOURCING_ROUTES.md`; expected use ≤ 10 images |
| Owned photography (opportunistic) | Phone camera + a plain backdrop | ~$0 | Route O — **not a scalable route** (2026-09-13: the founders have no owned inventory); the plate discipline is in the appendix of `../assets/C2_SOURCING_ROUTES.md` | Faceless product shots only, when a pair is actually at hand; no rig budget |
| Free-licence discovery (route F) | Openverse (Wikimedia Commons, Flickr — CC0 / public domain only) · Pexels · Unsplash · a reverse-image check (Google Lens / TinEye) | Free | Discovery across the sources inside the `LICENSED_FREE` class; the reverse-image check is the ownership-plausibility step | Licence read on the photo's own page; Unsplash+, BY-SA, NC, ND never; **CC BY not used in the initial test**; per-asset archive |
| Tracking | The XLSX in `experiment/tracking/` (Excel or Google Sheets) | Free | Reach-denominated formulas already in place | Manual entry only; no connectors, no scripts against Instagram |
| Data sheet for C3 | A tab in the same spreadsheet | Free | Source · figure · date · collector per data point | Sources per `../assets/C3_DATA_SOURCE_TOS_REGISTER.md` |
| Validators | `tools/validate_*.py`, `tools/build_tracking_sheet.py`, `tools/instantiate_calendar.py` | — | Python 3 only, no dependencies beyond the standard library (openpyxl and Pillow optional) | Run before scheduling and at the weekly review |

## What is deliberately not used

Canva for production frames (its stock and "editorial use only" content invites licence ambiguity inside a
design; fine for nothing here) · any AI video, interpolation or voice tool (locked) · any scraper, browser
extension or export against marketplaces or Instagram (locked) · any scheduling or analytics tool other than
Meta's own (no third-party API access to the accounts during the experiment) · any paid tier, until the
founders approve one.

## Spending register

| Item | Cost | Approved by founders | Date |
|---|---|---|---|
| (none yet) | | | |
