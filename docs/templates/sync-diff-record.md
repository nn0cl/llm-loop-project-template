# Sync Diff Record Template

Use this when `docs/templates/contract-file-sync-prompt.md`'s AI-assisted
reconciliation process runs for a Tier 2 contract file (`AGENTS.md`,
`CLAUDE.md`, `.github/copilot-instructions.md`, `.grok/rules/*.md`,
`.cursor/rules/*.mdc`), per
`docs/architecture/adr/0008-template-update-propagation.md`'s Tiered Sync
Policy. It is the durable record of what the template changed, what the
adopting project changed, and the adopt/reject/defer decision for each
conflict — produced once per synced file, not a substitute for the
required AI work trace (`docs/collaboration/traces/`).

Store the completed record in the *adopting* project's own repository
(this template repository is always the sync source, never a sync
target), at `docs/collaboration/sync-records/YYYY-MM-DD-<file-slug>.md`.

See `docs/collaboration/prompt-instruction-change-control.md`'s
"Per-Agent-Tool Rule Applicability Registry" section for which rule
applies to which agent tool, and
`docs/architecture/adr/0008-template-update-propagation.md` for the
Tier 1 (template-owned, template wins outright) / Tier 2 (adopter-owned
placeholders, needs reconciliation) split this record supports —
"syncing" under this template's own model was never meant to mean making
every mirror file textually identical; it means keeping each file's
*effective* rules current while preserving the adopter's own facts.

## Metadata

- File synced (target-repository-relative path):
- Target repository:
- Old ref (template commit the target last synced against):
- New ref (template's current commit):
- Date:
- Performed by (agent/environment):

## Template's Own Change

What the template changed between the old and new ref, for this file —
new sections, reworded rules, added references. This is the structure and
rules being adopted.

-

## Target's Own Change

What the adopting project changed relative to the template's old ref, for
this file — filled placeholders, added project-specific notes, or
template content intentionally removed. This is the adopter's facts being
preserved.

-

## Conflicts

One row per place where the template's change and the target's change
touch the same content. A conflict that was resolved by guessing is not
a resolved conflict — every row needs a decision and a reason.

| # | What conflicts | Adopt (take template) / Reject (keep target) / Defer (open question, unresolved) | Reason |
| --- | --- | --- | --- |
| 1 |  |  |  |

## Result

- Final file content: written to the target path once the covering design
  agreement (per `contract-file-sync-prompt.md` step 5) is reached.
- Deferred questions carried to the Director: list any `Defer` rows above
  that still need an explicit decision before this sync is done.

## Verification

- `scripts/check-contract-consistency.py` (or the target project's own
  equivalent) passes after the file is written.
- AI work trace recorded under `docs/collaboration/traces/`, per
  `docs/collaboration/prompt-instruction-change-control.md`'s
  Traceability Rule — this record and the trace are both required; this
  record is not a substitute for the trace.
