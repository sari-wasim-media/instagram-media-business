# Anti-Duplication, Contamination and Topic Selection — FOUNDER-LOCKED

**Status: ACTIVE.** Binding for the duration of the controlled experiment.

These rules exist to stop two accounts publishing the same post and to stop subject choice tracking
performance. They are deliberately **not** so strict that ordinary sneaker/streetwear coverage becomes
impossible.

---

## 1. Definitions — so the rules are testable

**"Same specific subject"** = any one of: the same product at **colorway/model level** · the same named
release event or drop date · the same named person · the same named retailer or marketplace action · the same
specific numerical claim (a price, a spread, a percentage).

**NOT the same subject:** the same brand · the same silhouette family · the same category · the same news
week · the same data source · the same house template.

**"Same thesis"** = the same argument reduced to one sentence, regardless of subject.

---

## 2. Cross-account rules

1. **Never the same file on both accounts.** No exceptions, ever.
2. **Never the same specific subject on both accounts within 14 days.**
3. **Topic check-out lock:** every subject is checked out to exactly one account and locked to it for
   **14 days**.
4. **Different source imagery on every piece**, even on related subjects. Two pieces may not share a source
   photograph, chart export or licensed asset.
5. **Never the same thesis on both accounts within 14 days**, even with different subjects.
6. **Structural, already in the matrix:** A and B never publish the same engine on the same date. Zero
   collisions across all 42 dates.
7. **Never the same audio track on both accounts within 14 days.**
8. **No adaptation across accounts.** A piece may never be produced for one account because the other
   account's version performed well. Assignment happens **at check-out, before any performance is known**, and
   once logged it cannot be moved. *Breach of this rule is the single most damaging thing that can happen to
   the experiment, because it silently converts a frozen design into an adaptive one.*

---

## 3. Within-account rules

9. **The same specific subject may anchor at most 2 of an account's 42 posts, and never within 10 days.**
10. **The same thesis at most once per account** across the whole experiment.
11. **The same audio track not reused within 14 days** on one account.
12. **No hook-sentence reuse within 7 days** on one account. Recurring *formats* are the engine and are
    expected — but consecutive instances must use **disjoint subject sets**.
13. **Named pressure points.** Two slot pairs are consecutive-day, same-engine **and** same-format on Account
    A. Each pair requires explicitly different subjects, different source imagery and different hooks, checked
    at production and recorded in the tracking row:
    - `A-W3-C1-REE-01` (W3 Sat) → `A-W3-C1-REE-02` (W3 Sun)
    - `A-W5-C2-REE-01` (W5 Fri) → `A-W5-C2-REE-02` (W5 Sat)

    Three further consecutive-day same-engine pairs change format between the two days and are lower risk:
    B W2 Thu→Fri (C3), B W4 Fri→Sat (C2), B W5 Wed→Thu (C1).
14. **No breakout replication.** No sequel, "part 2", re-cut or same-subject follow-up to any post that
    outperformed, for the duration. A breakout may be supported inside that day's single scheduled Story and
    by replying to comments. That is all.

---

## 4. Explicitly permitted

Both accounts covering the same brand, silhouette family or news week · both using the identical house
template (**required**, not duplication) · both using the same public data source · recurring weekly formats
within an engine · the same visual system, palette and typography across all 84 posts.

---

## 5. The constrained topic-selection mechanism

This is what lets slot assignment stay frozen while news-sensitive subjects are chosen near publication,
**without** letting subject choice track early performance.

### 5.1 Check-out deadlines, measured from the slot's 16:00 UTC publish instant

| Engine | Latest check-out | Why |
|---|---|---|
| **C1** Release & Verdict | **T − 48 h** | The engine is defined as reacting within 24–48 h of news breaking |
| **C3** Market & Price | **T − 7 d** | Research- and fact-check-heavy |
| **C2** Rankings · **C4** Meme | **T − 10 d** | Evergreen-capable; no reason to bind late |

### 5.2 The queue rule — the anti-cherry-pick mechanism

The backlog is a **queue**. The person checking out a slot takes the **top eligible item**. There is no
discretionary choice.

- **C1:** eligible items ordered by **nearest confirmed release/news date** within the slot's window; ties
  broken by earliest backlog entry timestamp.
- **C2, C3, C4:** strict **FIFO** by backlog entry timestamp.
- New items may be added at any time and enter at their entry timestamp. Only C1's release-date ordering can
  move an item forward, and only on an objective date.

### 5.3 The blind-to-performance rule

**Subject selection may not reference performance data from any published experiment post.** Stated as a rule
so that a breach is a loggable protocol violation rather than a judgement call.

### 5.4 Audit trail

Each check-out logs: **slot ID · timestamp · item · rule applied · the item's queue position at check-out.**

At the mid-test checkpoint, verify that **every** check-out took the top eligible item. Any exception is
logged as a deviation.
