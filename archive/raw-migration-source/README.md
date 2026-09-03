# Raw Migration Source — Provenance

This directory preserves the two hand-off packages **exactly as the founders delivered them**. Nothing here
has been edited, renamed, trimmed, reordered, or deduplicated.

**Do not modify anything in this directory.** If you need to work with a document, read the organized copy
under `strategy/`, `experiment/` or `evidence/` instead. This directory is the fallback of record: if any
organized copy is ever wrong, these files settle it.

**Line endings are protected.** The repository's `.gitattributes` marks everything under this directory
`-text`, so Git performs no line-ending conversion on checkout. Without that rule, a clone on a machine with
`core.autocrlf` enabled would rewrite these files to CRLF and the checksum verification below would fail.
**Do not remove those rules.**

---

## Contents

| Path | What it is |
|---|---|
| `instagram_media_migration_bundle.zip` | The first package, as delivered |
| `instagram_media_migration_bundle/` | Its extracted tree (57 files) |
| `instagram_media_supplemental_artifacts.zip` | The second package, as delivered |
| `instagram_media_supplemental_artifacts/` | Its extracted tree (7 files) |

Both packages were extracted into `_migration_inbox/` before migration. `_migration_inbox/` still exists on
the migrating machine but is gitignored, because everything in it is preserved here byte-for-byte.

---

## Integrity verification (performed 2026-09-02, during migration)

**Package checksums**

```
d2077228aed1c6f1fdba94f6eb48b9e0a5638f00b756e6dbf492d0fe85b7a794  instagram_media_migration_bundle.zip
26327fcb9eb9c4dfda0bfb6453867f8eb16ad56beddb7784255a2891f583ac2c  instagram_media_supplemental_artifacts.zip
dfac65b3447e2e3abec032f9a0b854dc3b889be6c744d8a3e2bc15a6e2ba19e8  instagram_media_migration_bundle/01_ORIGINAL_CLAUDE_PACK/original_pack.zip
```

**Checks run and their results**

1. `sha256sum -c` against the supplemental package's own `SHA256SUMS.txt` → **6/6 OK**.
2. `diff -r` of `instagram_media_migration_bundle.zip` against its extracted tree → **IDENTICAL**.
3. `diff -r` of `instagram_media_supplemental_artifacts.zip` against its extracted tree → **IDENTICAL**.
4. `diff -r` of both archived trees against the `_migration_inbox/` originals → **IDENTICAL**.
5. `diff` of every document re-filed into `strategy/` and `experiment/` against its source here → **all VERBATIM**.

---

## Known duplication — preserved deliberately, not deduplicated

`instagram_media_migration_bundle/01_ORIGINAL_CLAUDE_PACK/` contains **both**:

- `original_pack.zip`, and
- `Instagram_Media_Business_Claude_Pack/`, the extracted contents of that same zip.

`diff -r` confirms these are byte-identical to each other. The duplication was present in the package as
delivered and is kept on purpose. Do not remove either copy.

The 42 evidence images and the recovered strategy documents also exist as organized copies elsewhere in the
repository. That is intentional: `archive/` is the pristine record, the organized copies are the working
surface. Neither is authoritative over the other on *content* — they are byte-identical — but this directory
is authoritative on *provenance*.

---

## Provenance notes carried from the packages

- **Files `01`–`04` of the supplemental package** are preserved copies of full generated markdown artifacts
  from the project conversation / file library.
- **File `05` (`05_FINAL_METHODOLOGY_PATCH_MATRIX_FROZEN.md`) is a reconstruction**, not a verbatim export.
  Its package README states it was rebuilt from the founder-supplied final methodology-patch transcript, with
  an explicit later-supersession warning appended for migration safety. Treat its wording as faithful in
  substance but not as a byte-exact original. This distinction matters if the original transcript is ever
  recovered.
- **Files `01`, `02` and `03` open with a line or two of stray chat preamble** (e.g. "I'll do this properly.
  Starting with first-party platform documentation…"), confirming they are transcript exports. This is
  harmless and has been left in place rather than cleaned, per the verbatim rule.

---

## Sensitive-data status

Both packages were scanned during migration for passwords, tokens, API keys, GitHub PATs, AWS keys, private
keys, auth cookies, session secrets, 2FA recovery codes, and email addresses. **Nothing was found.** The 42
JPEGs carry small EXIF segments with **no GPS data**.

The single near-match is item 2 of the Week 0 checklist in `REVIVAL_EXPERIMENT_FINAL_LOCK.md`, which
*instructs* that 2FA recovery codes be stored somewhere both founders can reach. That is an instruction; no
code is present.

**Recovery codes, passwords and account credentials must never be committed to this repository.**
