# Route X — the permission request, the reply that counts, and the record

**Who sends it:** a founder, from a **personal e-mail address or personal account** — never from
`thestreetwearofficial` or `sneakerbong` (both are frozen; neither carries any outreach during the test).
**Who receives it:** the **photographer or rights holder** only — the person whose own photograph it is.
Never a repost page, a fan account, an aggregator, a retailer or a brand.

**What is never offered:** a tag, an @-mention, a Collab, a link, a fee, a product, a shout-out, a follow,
or anything else in return. Those would breach the locked no-Collab / no-outreach rule and the caption
policy. Plain-text credit in the caption is the only thing the desk can give, and only if the grantor wants it.

**What is never claimed:** that the desk is affiliated with any brand, that the post is sponsored, or that
the grantor endorses anything.

---

## The message (send as written; fill the brackets; keep it short)

> Subject: Permission to use your photograph of the [model] '[colorway]'
>
> Hi [name],
>
> I'm [founder first name], one of two people running a small independent sneaker editorial account on
> Instagram ([@thestreetwearofficial] / [@sneakerbong]) — rankings and reviews, unsponsored, nothing for sale.
>
> I'd like to ask your permission to use your photograph of the [model] '[colorway]' — this one:
> [URL of the exact photo] — as one of seven product images in a ranking post.
>
> Specifically:
> – one feed post (a Reel, carousel or single image) on either of those two accounts, within six months;
> – non-exclusive, no fee either way; the image stays yours;
> – I'd credit you in the caption as "[name as you'd like it]" if you'd like (we don't tag or @-mention
>   accounts, so it would be plain text);
> – the post is editorial and implies no endorsement by you or by any brand;
> – it's possible the post ends up not being published at all — I'll only ever use it once, within that scope.
>
> If you're happy with that, could you reply to confirm that you took the photograph and that this is OK?
> If not, no problem at all — thank you for reading.
>
> [founder first name]

## The reply that counts

A permission is **logged as CLEARED only if the written reply, in the grantor's own words, does all of these**:

1. confirms **they took the photograph** (or otherwise hold the rights to it);
2. agrees to the **scope** above (or a narrower one — log exactly what was agreed);
3. states the **credit** they want, or that they want none.

A reply of "sure, just credit me" satisfies 2 and 3 and implies 1 if they are plainly the photographer;
follow up once with "thanks — just to confirm, it's your own shot?" if there is any doubt. **A "like", a
follow-back, silence, or a credit given without any reply is not permission.** Permission from someone who
turns out not to be the photographer is void — reject the candidate (`LAUNDERED`).

## The record

- Archive the **whole thread** — screenshot and text, with dates — at
  `local://permissions/YYYY-MM-DD-<grantor>.pdf` (the local asset store, never this repository).
- `candidates_log.csv`: `route = X`, `permission_requested_date`, then `permission_reply_date`,
  `clearance_status = CLEARED`, `evidence_archived_at = <that path>`, `attribution_required = Y/N`.
- `provenance_register.csv`: `class = PERMISSIONED`, `source_name = <grantor>`,
  `licence_or_permission = Written permission <date>`, `licence_text_archived_at = <that path>`,
  `permitted_use = One feed post on either account within 6 months of <date>; editorial; non-exclusive`,
  `restrictions = No tag / @-mention / Collab; plain-text credit only if requested; single use`,
  `expiry = <date + 6 months>`, `attribution_text = Photo: <name>` if requested.
- `timing_log.csv`: the active minutes (finding the person, writing, logging the reply) under
  `PERMISSION_REQUEST`; the wait under `PERMISSION_WAIT`, `PASSIVE`.

## Timing for the stress test

Send every route X request on **day 1** of the run, in one batch, for every item route F could not supply.
Keep working the other routes meanwhile. A request unanswered after **7 days** lapses for the test: log
`clearance_status = LAPSED`, `rejection_reason = NO_REPLY`, and let the item fall through to route S (or
swap to an alternate, logged). A "yes" that arrives after the lapse is still a permission — bank it for a
future piece with its own six-month window.
