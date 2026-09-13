# Adobe Firefly — terms verification, prepared for the founders (Sourcing Gate item 9)

**Status: MEMO READY — founder confirmation OPEN. Sourcing Gate item 9 is NOT passed.**
Prepared by Claude on 2026-09-11 under delegated production authority as *reading*, not *acceptance*: no account
was created, no terms were accepted, nothing was generated. `GATES.md` §1.4 item 9 and `WORKFLOW.md` §2a keep
the confirmation, the account and any plan decision with Sari and Wasim. This memo exists so that the founders'
half-hour (`PRE_LAUNCH_RUNBOOK.md` step 1) is spent confirming, not searching.

Access date for every source below: **2026-09-11**. Adobe changes these pages; re-open each one on the day
you confirm and check the "last updated" / "effective" line against the one recorded here.

*Re-check 2026-09-13 (Claude, reading only):* the three governing documents still show the same dates —
Product Specific Terms *Effective as of April 23, 2026*; User Guidelines *Last Updated: May 15, 2026*;
General Terms *Published October 3, 2025. Effective as of October 3, 2025*. The memo is current. Nothing
was accepted, no account was created.

---

## 1. Which documents govern Firefly output — the chain

Three documents, and they say so themselves:

| Document | URL | Version on file | Role |
|---|---|---|---|
| **Adobe Generative AI Product Specific Terms** (PDF) | `https://www.adobe.com/go/adobe-gen-ai-addl-terms` | *Effective as of April 23, 2026* (file `…-en_US-20260423`) | The operative terms for Input and Output |
| **Adobe Generative AI User Guidelines** | `https://www.adobe.com/legal/licenses-terms/adobe-gen-ai-user-guidelines.html` | *Last updated May 15, 2026* | Conduct and prohibited-content rules |
| **Adobe General Terms of Use** | `https://www.adobe.com/legal/terms.html` | *Published October 3, 2025. Effective as of October 3, 2025.* | Ownership of Content, licence to Adobe, indemnity, age |

The Product Specific Terms open: *"These Product Specific Terms and the Adobe Generative AI User Guidelines …
govern your use of generative AI features … and are incorporated by reference into the Adobe General Terms of
Use"* (preamble). Reading one of the three is not reading the terms.

Supporting pages (informational, not contractual): Firefly FAQ (`helpx.adobe.com/firefly/web/get-started/
learn-the-basics/adobe-firefly-faq.html`, *last updated May 13, 2026*); Generative credits FAQ
(`helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html`, *last updated Sep 10, 2026*);
Firefly plans (`adobe.com/products/firefly/plans.html`).

---

## 2. The clauses, quoted, mapped to our use

Our use, precisely: a faceless editorial Instagram desk on two accounts; AI imagery in **exactly six C4 slots
plus the one test piece** (`AI_IMAGERY_SUBTEST.md`); the fixed disclosure line on every AI piece; **no real
product, brand mark, logo, wordmark, recognisable model silhouette or person** in any AI asset (policy pack §4);
advertiser revenue possible later; Content Credentials must survive to publication so Instagram's own label
can appear.

### 2.1 Ownership and the right to use Output commercially

| What the terms say (quoted) | Where | What it means for us |
|---|---|---|
| *"The Input and Output are your Content … and all provisions governing Content in the Terms apply to the Input and Output."* | Product Specific Terms §1 | Output is governed by the General Terms' Content provisions — there is **no separate Output licence** to read |
| *"As between you and Adobe, you … retain all rights and ownership of your Content."* | General Terms §4.2 | We own what we generate, as between us and Adobe |
| *"For features without the beta label, you can use Firefly-generated outputs in your commercial projects. For features that are in beta, you can use the Firefly-generated outputs for your commercial projects unless explicitly stated otherwise in the product."* | Firefly FAQ, "Can I use Firefly-generated outputs commercially?" | Commercial use is stated in the FAQ, **not in the contract**. The contract permits it by not restricting it (Output = your Content, all rights retained). Record both |
| *"The Output may not be unique and other users … may generate the same or similar Output. The Output may not be protectable by Intellectual Property Rights."* | Product Specific Terms §3.2 | We cannot claim exclusivity over an AI asset. Irrelevant to the sub-test; relevant if anyone ever proposes an AI asset as a house mark — do not |
| *"Adobe disclaims all warranties, express or implied, regarding the Output, including any implied warranties that the Output will not violate the rights of a third party"* | Product Specific Terms §3.1 | **"Commercially safe" is a training-data claim, not a warranty.** Our own prohibited-use review (policy pack §4–§5) is the safeguard, exactly as designed |

**No plan-based distinction on commercial use was found anywhere** — not in the three contractual documents,
not in the FAQ, not on the plans page. The free plan's outputs are not described as non-commercial.

### 2.2 What we may not put in, and what we may not generate

| What the terms say (quoted) | Where | Our rule already covers it |
|---|---|---|
| *"You must not submit any Input that: (a) includes trademarks or other materials protected by third-party Intellectual Property Rights, unless you have sufficient rights … (b) is intended to generate Output that is substantially similar to a third party's copyrighted work"* | Product Specific Terms §2 | Policy pack §4 (no product, brand, logo, silhouette, person) and §5 ("never feed a third-party photograph, a brand image or another account's post into a generator"). **Prompts must not name a brand or a model either** — that is an Input "intended to generate" protected matter |
| *"Using Adobe's generative AI features to create, upload, or share content that violates third-party copyright, trademark, privacy, publicity, or other rights is prohibited."* · *"Entering text prompts designed to generate copyrighted, trademarked, or otherwise infringing content"* is listed as prohibited | User Guidelines §2 | Same |
| *"Impersonating other people or entities"* · *"Disseminate misleading, fraudulent, or deceptive content that could lead to real-world harm"* | User Guidelines §1 | The disclosure line and the no-person rule; the desk's factual claims are never carried by an AI asset (C1–C3 are AI-free by lock) |
| *"We may automatically block your Input … if we believe it violates the rights of a third party"* | Product Specific Terms §2 | A blocked prompt is a signal, not an obstacle to route around. Log it in the asset row's notes |

### 2.3 Content Credentials — the thing the sub-test depends on

| What the terms say (quoted) | Where | What it means for us |
|---|---|---|
| *"you must not remove or alter any watermarks or Content Authenticity Initiative metadata (e.g., Content Credentials) that may be generated with the Output, or otherwise attempt to mislead others about the origin of the Output."* | Product Specific Terms §3.1 | Binding on us and **aligned with the sub-test**: the disclosed treatment is what is measured. Export path and any re-encode must preserve the credential; `ai_platform_label_observed` at T+7 is the check |
| *"You must not remove, alter, or disable any Content Credentials"* | User Guidelines §6 | Same |
| *"Adobe may attach or publish Content Credentials for content created or modified with generative AI features"* | User Guidelines §6 | "May", not "will". **Confirm at the test piece** that the exported file actually carries a credential (contentcredentials.org/verify) before relying on Instagram's automatic label; if it does not, apply Instagram's manual AI label as the policy pack already requires |

### 2.4 Training, data and privacy

| What the terms say (quoted) | Where | What it means for us |
|---|---|---|
| *"We will not use your Content to train generative AI models except for Content you chose to submit to the Adobe Stock marketplace."* | General Terms §4.3(C) | Our prompts and outputs are not training data. Do not submit anything to Adobe Stock or the Firefly gallery |
| *"If you submit Output to an Adobe-hosted gallery (such as the Firefly gallery), you grant us a nonexclusive, perpetual, irrevocable, worldwide, royalty-free license … for marketing purposes and to allow other Adobe users to use said Input and Output"* | Product Specific Terms §4 | **Never post to the Firefly gallery / community.** That grant is irrevocable |
| *"You must not … use any content, data, output or other information received or derived from any generative AI features, including any Outputs, to directly or indirectly create, train, test, or otherwise improve any machine learning algorithms"* | Product Specific Terms §3.3 | Not our use |
| *"The current Firefly generative AI models were trained on a dataset of licensed content, such as Adobe Stock, along with public domain content."* | Firefly FAQ, "Where does Firefly get its data from?" | This is the substance of "commercially safe" — recorded so nobody later reads it as a warranty (§2.1) |

### 2.5 Indemnification — read this before anyone says "Adobe covers us"

| What the terms say (quoted) | Where | What it means for us |
|---|---|---|
| *"This section 8 only applies if you: (1) are a Creative Cloud for teams or Creative Cloud for enterprise customer and (2) have purchased a Creative Cloud Pro Plus plan or Creative Cloud, Edition 4 plan that comes with Firefly Output indemnification"* | Product Specific Terms §8 | **Adobe's IP indemnity does NOT apply to the free plan, to Firefly Standard/Pro/Premium individual plans, or to any plan we would realistically hold.** Do not cite it |
| Even where it applies, Adobe has no liability for a claim arising from *"any modification of an Output"*, *"any combination of an Output with any other materials"*, or *"the context in which the Output is used"* | Product Specific Terms §8.3.1 | A meme frame with our typography over an AI plate is a modification and a combination in a context — it would fall outside the indemnity even on an eligible plan |
| *"You will indemnify us and our subsidiaries, affiliates … from any claim(s), demand(s), loss(es), or damage(s) …"* arising from *"your Content"* | General Terms §8.2 | The indemnity runs **from us to Adobe**, not the other way. Our exposure on AI assets is ours; it is managed by the prohibited-use rule, the other-founder review and the six-slot cap |

### 2.6 Availability, plan and credits — operational facts for the six slots

| What the pages say (quoted) | Where | What it means for us |
|---|---|---|
| *"Adobe reserves the right to throttle, limit, disable, suspend, or terminate your right to use or access the generative AI features at any time in our sole discretion without prior notice to you."* | Product Specific Terms §1 | Generate the six slot assets (and spares) **early, in one sitting after the test piece**, not slot by slot during the six weeks. Gemini is the recorded alternate (policy pack §5) — its terms are unread and would need their own memo before use |
| *"Free users of Adobe Firefly … get a limited number of free daily generations across all generative AI features, available on a curated set of models. These limits refresh each day … The number of generations, features, and models are subject to change."* | Generative credits FAQ | The free allowance is **daily and unspecified**. Seven finished assets at roughly 20 credits per image generation (Image 4 Ultra) or 10 (Image 5), with regenerations for the review rule, is a small number of sittings — but do not assume a figure; observe it at the test piece |
| *"For free plans, generative credits are allocated upon first use of a Firefly feature … These credits expire one month from allocation."* · *"generative credits do not roll over"* | Generative credits FAQ | Plan the test piece and the six-slot sitting inside one allocation window |
| Plans page: **Firefly Standard US$9.99/mo, 2,000 credits** · Pro US$19.99/mo, 4,000 · Pro Plus US$49.99/mo, 10,000 · Premium US$199.99/mo, 50,000; *"Your credits reset monthly on your billing date and do not roll over."* | `adobe.com/products/firefly/plans.html` | If the free allowance proves too small at the test piece, **Standard is the smallest paid step — a founder spending decision**, not Claude's |
| Free-tier watermark: **not stated** on the plans page, the FAQ or the credits FAQ. The earlier research note "free-tier watermark status unverified" stays unverified by reading | — | **Verify by observation at the test piece**: inspect the exported file for a visible mark. A visible mark would fail the house template's QA, not the terms |
| *"You must be 13 or older to register for an Adobe ID."* · Firefly is *"not available in Russia, Belarus, and China"* and sanctioned territories | General Terms §1; Firefly FAQ | No issue |

---

## 3. Reading — what the founders are being asked to confirm

Everything the sub-test needs is present in the terms as read on 2026-09-11, with three caveats that are
**facts to observe, not clauses to interpret**:

1. **Commercial use is permitted** — by the FAQ in words, by the contract by construction (Output is your
   Content; all rights retained; no restriction). No plan-based distinction found.
2. **The prohibited-content rules match ours** and are slightly stricter on Input: prompts must not name or
   describe a brand, a model or a person — write prompts as the policy pack's abstract scenes.
3. **Content Credentials must be preserved** — good for us, and binding.
4. ⚠ **Adobe's indemnity does not cover any plan we would hold** and would not cover our composited frames
   even if it did. The AI slots carry our own exposure, managed by our own rules. This is unchanged from
   the sub-test's design; it simply must not be described otherwise.
5. ⚠ **Three things are only observable, not readable:** whether the free tier applies a visible watermark
   today; whether the exported file actually carries a Content Credential; and how many free daily
   generations the account gets. All three are checked **at TEST-AI-01** (Sourcing Gate items 10–12), which
   is why item 9 should be confirmed *before* the test piece and the observations recorded *at* it.

---

## 4. Founder checklist — closes Sourcing Gate item 9

Founder action; ~30 minutes; nothing here is Claude's to do.

- [ ] Open the three governing documents (§1) on the day of confirmation. Check each "last updated" /
      "effective" line against §1. If any has changed, note the new date here and re-read the changed
      sections before ticking the rest.
- [ ] Confirm each line of §2.1 (ownership and commercial use) reads as quoted.
- [ ] Confirm §2.2 (Input and prohibited content) reads as quoted, and that the policy pack's prompt rule is
      understood: **no brand, model, logo, wordmark or person in any prompt**.
- [ ] Confirm §2.3 (Content Credentials must not be removed) reads as quoted.
- [ ] Confirm §2.5: you have read that the indemnity does not apply to our plan, and that the General Terms
      indemnity runs from us to Adobe.
- [ ] Create the Adobe ID / Firefly account as a founder (**an external terms acceptance — founder only**).
      Do not join the Firefly gallery or community; do not submit anything to Adobe Stock.
- [ ] Record in `SOURCING_ROUTES_RESEARCH.md` §6 (Firefly row) and in this file's §5:
      **tool · model version shown in the app · plan (free / Standard / …) · date of account creation ·
      date of confirmation · the "effective" dates of the three documents as seen that day.**
- [ ] Decide the plan: start on the free tier (delegated decision already recorded). **Any paid plan is a
      founder spending approval** — take it only if the free allowance fails at the test piece.
- [ ] Update `production/gates/SOURCING_GATE_SCORECARD.md` item 9 to **PASSED <date>** and sign the AI-arm
      row. Then proceed to TEST-AI-01 (`AI_IMAGERY_POLICY_PACK.md` §7), recording at that step: watermark
      observed Y/N · Content Credential present on the exported file Y/N (contentcredentials.org/verify) ·
      free generations available per day as shown.

## 5. Confirmation record (founders fill in)

| Field | Value |
|---|---|
| Confirmed by | |
| Confirmation date | |
| Adobe ID created (date) | |
| Plan | |
| Firefly model version shown in app | |
| Product Specific Terms effective date seen | |
| User Guidelines last-updated date seen | |
| General Terms effective date seen | |
| Deviations from this memo | |

---

## 6. What this memo did not do

It did not create an account, accept any terms, generate an image, or read Google Gemini's terms (the recorded
alternate — a separate memo if Firefly fails at the test piece). It did not re-run the sourcing research in
`SOURCING_ROUTES_RESEARCH.md`; it read the one page-set that research left to the founders. Quotations are kept
short and are checked against the source PDF and the live pages on the access date; the page-level summaries
were verified against the documents themselves, and two paraphrases that a first pass produced ("you may use
Outputs for any commercial purpose" as contract language; "Adobe indemnifies users") were found **not** to be
in the contract and are recorded here as such so they are not repeated.
