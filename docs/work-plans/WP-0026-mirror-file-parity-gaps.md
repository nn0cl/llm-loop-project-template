# Work Plan: Mirror-file parity gaps (item-0022)

## Goal

- Close the 5 mirror-parity gaps `docs/backlog/item-0022-mirror-file-parity-gaps.md`
  names between the agent-instruction contract files (`.cursor/rules/*.mdc`,
  `.grok/rules/*.md`) and `scripts/init-llm-context.sh`'s required-files
  check, and fix a small, re-verified set of Markdown line-wrap defects
  splitting inline code spans across a line break in four docs.

## Scope

- In: see the covering design agreement's own Scope section
  (`docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md`)
  for the exact, re-verified file/line list. Independent re-verification
  found gap 1 (external-resource-adoption-contract cross-reference)
  already fixed in 4 of the 5 mirrors named by the backlog item — only
  `.cursor/rules/01-quickstart.mdc` still needs it.
- Out: any edit to `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, or `.grok/rules/01-quickstart.md`'s
  reading-list section (already correct); any content change to
  `.cursor/rules/02-architecture-boundaries.mdc` or
  `.cursor/rules/03-collaboration-and-completion.mdc`; any line-wrap fix
  outside the four named files; any Python logic change in
  `check-contract-consistency.py`.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0070 | ready | S | S | N/A | - | - | process/promote-item-0022 |
| LISS-0071 | ready | S | S | N/A | - | - | process/promote-item-0022 |
| LISS-0072 | ready | S | S | N/A | - | - | process/promote-item-0022 |
| LISS-0073 | ready | S | S | N/A | LISS-0072 | - | process/promote-item-0022 |

## Recommended Order

1. LISS-0070, LISS-0071, LISS-0072 — disjoint files, no dependency between
   them; may be done in any order or together in one Implementer pass.
2. LISS-0073 — added 2026-08-23 per the design agreement's Reopening Log;
   fixes a pre-existing defect LISS-0072's own fix unmasked. Depends on
   LISS-0072 having landed on the same file first (easiest to locate the
   4 "ADR 0002" instances after the rewrap, though not strictly required).

## Current Next Issue

- Issue: LISS-0070 (also LISS-0071, LISS-0072 — no ordering dependency)
- Reason it is unblocked: no dependency; scope is fully settled by the
  design agreement; every gap independently re-verified against current
  file content before this work plan was written.
- Reopening request needed: no.

## Minor Fix Path

Not used formally (this is new work against a freshly promoted backlog
item, not a correction to previously accepted work), but each issue is
Minor-Fix-Path-shaped in size and risk: planning size `S`, small mechanical
additions/rewraps, one attempt expected, no specification, ADR, port, data
model, or architecture boundary changed. Per the design agreement's own
Boundaries section, the contract-file edits (LISS-0070's `.grok`/`.cursor`
files, LISS-0072's `ai-failure-recovery.md`/`model-tool-capability-matrix.md`
files) still require this covering design agreement, a separate-context
Reviewer pass, a stated reason, and an AI work trace — the Minor Fix Path's
usual self-contained handling does not waive ADR 0006's contract-file rule.

## Preflight Validation

Filled in by the Implementation group once every issue above is
self-reviewed and complete.

## Review Summary Packet

Filled in by the Implementation group once Preflight passes.

## Work-Plan Review

Reviewer's approval record: <link, filled in after the separate-context
Reviewer pass>

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves — not performed
by the Design & Review group itself.

- Date:
- Result read:
- Next direction:
- New design agreement (if any):

## Risks

- The backlog item's own description of gap 1 was stale for 4 of 5 files;
  a similar staleness could affect other unverified assumptions if the
  Implementer trusts the backlog item's text over direct file reads.
  Mitigated: the design agreement's own Settled Ambiguities table already
  states the re-verified, corrected scope; the Implementer must still
  independently confirm each file/line before editing, not merely copy
  this work plan's line numbers without checking.
- `.cursor/rules/*.mdc` files have YAML frontmatter (`---` delimited) at
  the top; a careless edit near that boundary could corrupt Cursor's own
  rule-loading. Mitigated: LISS-0070's acceptance notes point at the
  specific "Cursor-side reminders" section well below the frontmatter.

## Verification Plan

- `grep -n` before/after for each of the three quickstart-file edits.
- Reproduction of `scripts/init-llm-context.sh`'s pass/fail behavior
  before and after the required-files addition.
- `grep -n` re-run for the line-wrap pattern across the four files,
  zero remaining matches.
- `python3 scripts/check-contract-consistency.py` (real repository),
  before and after — no regression.
- `git diff` reviewed per file against the design agreement's Scope.
- Independent work-plan-level Reviewer approval, in a separate context.
