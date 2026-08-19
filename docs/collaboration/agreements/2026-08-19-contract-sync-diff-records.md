# Design Agreement: Contract-Sync Diff Records and Per-Agent-Tool Rule Registry

## Identity

- Agreement ID: DA-2026-08-19-07
- Date: 2026-08-19
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
(`Status: promoted`) facet 4 ("Single-source multi-agent contract sync"),
whose Promotion notes are this agreement's Director authorization under
ADR 0016 Rule 2: research showed `docs/architecture/adr/0008-template-update-propagation.md`'s
Tiered Sync Policy already implements facet 4's Template-owned vs
Target-owned split (Tier 1: template-owned, template wins outright; Tier
2: the five agent-persona contract files, adopter-owned placeholders,
AI-assisted reconciliation via `docs/templates/contract-file-sync-prompt.md`).
This agreement closes the two genuinely missing pieces facet 4 also asks
for: a structured Sync Diff Record (naming the template's own change, the
target's own change, each conflict, and the adopt/reject/defer decision)
and a canonical Per-Agent-Tool Rule Applicability Registry — without
rebuilding the already-working mechanism.

## Scope

- In scope:
  - `docs/templates/sync-diff-record.md` (new), with exactly the content
    specified in "Exact Content to Produce" below.
  - `docs/collaboration/prompt-instruction-change-control.md`: a new
    "Per-Agent-Tool Rule Applicability Registry" section, plus shortening
    the existing Review Rule bullet to cross-reference it instead of
    restating the Cursor union-vs-mirror explanation inline — exact text
    specified below.
  - `docs/templates/contract-file-sync-prompt.md`: one new cross-referencing
    paragraph after the intro, and an expanded Step 6 — exact text
    specified below.
  - The required AI work trace under `docs/collaboration/traces/` (all
    three touched/created files are ADR-0006 contract files).
- Explicitly out of scope:
  - Any edit to `docs/architecture/adr/0008-template-update-propagation.md`
    itself — its Tiered Sync Policy already covers what this agreement
    builds on; a forward-pointer note there is judged unnecessary (see
    Settled Ambiguities) since both edited files already cross-reference
    it directly.
  - Any change to `scripts/update-ai-collaboration-files.sh` or
    `scripts/copy-ai-collaboration-files.sh` — this agreement is
    documentation/template layer only, no script behavior change.
  - Any edit to `CLAUDE.md` or its four mirrors — neither touched file is
    listed in CLAUDE.md's "Use `docs/templates/...`" enumeration today
    (`contract-file-sync-prompt.md` itself is not listed there either),
    so adding `sync-diff-record.md` does not create an inconsistency to
    fix.
  - Facets 5 (drift-prevention entry documents and CI checks) and 6
    (review-summary packets) — later, separate work plans.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Create `docs/templates/sync-diff-record.md` | Implementer | Architecture Path (new contract template; content fully specified below) | Matches "Exact Content to Produce" verbatim | read-through diff |
| 2 | Add the Per-Agent-Tool Rule Applicability Registry section and shorten the Review Rule bullet in `prompt-instruction-change-control.md` | Implementer | Architecture Path | Matches "Exact Content to Produce" verbatim; no other part of the file changes | read-through diff |
| 3 | Add the cross-referencing paragraph and expand Step 6 in `contract-file-sync-prompt.md` | Implementer | Architecture Path | Matches "Exact Content to Produce" verbatim; no other part of the file changes | read-through diff |
| 4 | AI work trace | Implementer | Architecture Path | States which three contract files changed, why, and what agent behavior changes | trace file present |
| 5 | Self-review | Implementer | Architecture Path | Short-form self-review per `docs/templates/self-review.md` (size `M`, short form default per ADR 0015 unless escalation criteria apply — none do here, a single cohesive doc-only change), recorded in LISS-0046 Work Notes | self-review record |
| 6 | Preflight Validation | Implementer / deterministic tool | Architecture Path | `pass` recorded with `scripts/check-contract-consistency.py` output and an explicit scope check | Preflight section in WP-0015 |
| 7 | Work-plan-level Reviewer pass | Reviewer (Design & Review group, separate context) | Architecture Path | Review record confirms mechanical accuracy, that the new pieces genuinely extend rather than duplicate ADR 0008, and that the trace is present and accurate | review record under `docs/collaboration/reviews/` |

Sequencing: Tasks 1, 2, and 3 may proceed in any order (independent
files). All three block Task 4. Task 4 blocks 5. Task 5 blocks 6. Task 6
blocks 7.

## Exact Content to Produce

### File 1: `docs/templates/sync-diff-record.md` (new)

```markdown
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
```

### File 2: `docs/collaboration/prompt-instruction-change-control.md` — new section and shortened bullet

Insert this new section immediately after the existing `## Review Rule`
section's list of bullets and before `## Traceability Rule`:

```markdown
## Per-Agent-Tool Rule Applicability Registry

Not every rule in this contract applies identically to every agent tool's
own mirror file. Record every *intentional* difference here — a
difference that exists on purpose, not one this document's own
mirror-consistency requirement above would otherwise flag as a defect.
Consult this table before treating an agent-tool difference as an error.

| Sync mode | Agent tool(s) | What it means |
| --- | --- | --- |
| Literal full mirror | `CLAUDE.md`, `.github/copilot-instructions.md`, `.grok/rules/*.md` | Effective content matches `AGENTS.md` word-for-word (`CLAUDE.md` joined this group on 2026-07-25, when the `@AGENTS.md` import was dropped after an adopter showed the import resolved correctly and still did not produce adherence). |
| Union (complement + native auto-apply) | `.cursor/rules/*.mdc` | Cursor's effective content is the union of `.cursor/rules/*.mdc` (Cursor complements only — not a full restatement) and Cursor's own native root `AGENTS.md` auto-apply (Cursor reads `AGENTS.md` directly; the `.mdc` files add only what Cursor-specific behavior requires and do not `@AGENTS.md`-import it). |
| Canonical source | `AGENTS.md` | The literal-full-mirror group's source of truth; edited first, then propagated to the mirrors listed above. |

Add a new row here, with its own reason, the first time an intentional
per-agent-tool difference is introduced — do not fold a new difference
into prose scattered across this document or a PR description where a
later reader would not think to look for it.
```

Replace the existing Review Rule bullet (currently reading, in full):

```markdown
- confirmation that `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
  `.cursor/rules/*.mdc` still agree with each other in effective content
  after the change, when the change touches shared phase, dependency, or
  read-order rules. Per ADR 0006: agreement means equivalent effective
  content, not a literal text match — Cursor's effective content is the union of
  `.cursor/rules/*.mdc` (Cursor complements only) and Cursor's native root
  `AGENTS.md` auto-apply (no `@AGENTS.md` inside `.mdc`), while `CLAUDE.md`,
  `.github/copilot-instructions.md`, and `.grok/rules/*.md` are literal full
  mirrors. `CLAUDE.md` joined that group on 2026-07-25, when the
  `@AGENTS.md` import was dropped after an adopter showed the import
  resolved correctly and still did not produce adherence.
```

with exactly:

```markdown
- confirmation that `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
  `.cursor/rules/*.mdc` still agree with each other in effective content
  after the change, when the change touches shared phase, dependency, or
  read-order rules. Per ADR 0006: agreement means equivalent effective
  content, not a literal text match — see this document's own
  "Per-Agent-Tool Rule Applicability Registry" section below for exactly
  which sync mode applies to which agent tool, and to record any new
  intentional difference rather than treating it as an error.
```

Do not change anything else anywhere in this file.

### File 3: `docs/templates/contract-file-sync-prompt.md` — new paragraph and expanded Step 6

Insert this new paragraph immediately after the existing intro paragraph
(the one ending "...that a text merge or a blind overwrite can silently
destroy or bury.") and before the "Do not run this as a mechanical text
merge." paragraph:

```markdown
This Tier 1 (template-owned, template wins outright) / Tier 2
(adopter-owned, needs reconciliation) split is this template's own answer
to keeping template-owned process/methodology conventions and
target-owned project-specific facts separate — see
`docs/architecture/adr/0008-template-update-propagation.md`'s Tiered Sync
Policy. "Syncing" here never means making every mirror file textually
identical to the template's own copy; it means keeping each file's
effective rules current while preserving what the adopting project
actually owns.
```

Replace the existing Step 6 (currently reading, in full):

```markdown
6. Once approved, write the file and record the change like any other
   contract-file edit: a stated reason, and an AI work trace under
   `docs/collaboration/traces/` (see
   `docs/collaboration/prompt-instruction-change-control.md`).
```

with exactly:

```markdown
6. Once approved, write the file and record the change like any other
   contract-file edit: a stated reason, and an AI work trace under
   `docs/collaboration/traces/` (see
   `docs/collaboration/prompt-instruction-change-control.md`). Also
   produce a Sync Diff Record — `docs/templates/sync-diff-record.md`,
   stored at `docs/collaboration/sync-records/YYYY-MM-DD-<file-slug>.md`
   in the adopting project's own repository — naming the template's own
   change, the target's own change, each conflict, and the
   adopt/reject/defer decision for it; the fields in this prompt's own
   "Output" section above map directly onto that record's sections. The
   Sync Diff Record and the AI work trace are both required; neither
   substitutes for the other.
```

Do not change anything else anywhere in this file.

## Specifications

- None. Documentation/process-governance change; no application
  specification.

## Boundaries

- All three touched/created files are ADR-0006 contract files — trace and
  separate-context Reviewer approval are mandatory.
- No edit to `docs/architecture/adr/0008-template-update-propagation.md`,
  any sync script, `CLAUDE.md`, or its four mirrors.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` (in the
  Director-facing sense) until the Director's own work-plan-close action.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does facet 4 need a new ADR? | No — it refines an already-Accepted ADR's (0008) mechanism by adding a record-keeping artifact and formalizing existing prose into a registry, rather than introducing a new architectural concept. Matches item-0013's own precedent (a process-rule addition needed no new ADR). | Design & Review group (Planner) |
| Does ADR 0008 itself need a forward-pointer edit for discoverability? | No — both new/edited files already cross-reference ADR 0008 directly by name; a reader is more likely to land on `prompt-instruction-change-control.md` or `contract-file-sync-prompt.md` first (they are read far more often than a specific old ADR), so the added discoverability from an ADR 0008 edit is marginal against the cost of touching another file. | Design & Review group (Planner) |
| Should `CLAUDE.md` reference the new `sync-diff-record.md` template? | No — `CLAUDE.md`'s own template enumeration is not exhaustive today (`contract-file-sync-prompt.md` itself, the template this new one directly supports, is not listed there either); adding one without the other would be inconsistent, and neither omission is a defect under the existing convention. | Design & Review group (Planner) |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should the Per-Agent-Tool Rule Applicability Registry table gain automated drift-checking (e.g., a CI check that the table's claims match the actual mirror files)? | Only if facet 5 (drift-prevention entry documents and CI checks, a later work plan) judges it in scope — not assumed necessary now; the registry is a documentation aid, not itself a new enforcement mechanism. |

## Verification

- `scripts/check-contract-consistency.py`.
- Read-through diff confirming all three changes match "Exact Content to
  Produce" verbatim, and that no other repository file changed.
- Work-plan-level Reviewer approval, separate context.

## Falsification Criteria

- Any existing repository document outside the three named files/sections
  is edited.
- `docs/architecture/adr/0008-template-update-propagation.md` itself,
  any sync script, `CLAUDE.md`, or a mirror file is edited.
- The new registry table restates the Cursor union-vs-mirror explanation
  in two places instead of one (duplication the Settled Ambiguities and
  Plan both intend to avoid).
- No AI work trace is recorded for this contract-file-touching work plan.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0012-document-and-log-lifecycle-management.md`,
      `Status: promoted`, Promotion notes, per ADR 0016 Rule 2.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Made fresh by the Design & Review group
      against this actual plan.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
