# Design Agreement: Mirror-file parity gaps (item-0022)

Store the completed record at
`docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md`.

See `docs/collaboration/design-agreement.md` for the rules this record
implements.

## Identity

- Agreement ID: DA-2026-08-23-01
- Date: 2026-08-23
- Director: per ADR 0016 Rule 2, backlog-item-level agreement — see
  "Agreement" below.
- Planner / Specifier personas (model or tool used): Design & Review group,
  standing session (Claude Code, Planner/Specifier persona).
- Supersedes agreement (if any): none.

## Direction

`docs/backlog/item-0022-mirror-file-parity-gaps.md` (`Status: promoted`,
"承認" from the Director via the Backlog thread, commit `38fff0c`): fix the
mirror-parity gaps it names between the agent-instruction contract files
and `scripts/init-llm-context.sh`'s required-files check. Per ADR 0016
Rule 2, Design & Review proceeds autonomously from here.

**Independent re-verification against current `main` content (not the
backlog item's own text alone) found the backlog item's own description of
gap 1 partially stale.** This agreement's scope is corrected accordingly —
see "Settled Ambiguities" below for the full account.

## Scope

- In scope:
  1. Add an "External resource adoption contract" cross-reference
     (`docs/architecture/external-resource-adoption-contract.md`) to
     `.cursor/rules/01-quickstart.mdc`'s own reading-list-equivalent
     section ("Cursor-side reminders"). **Not** added to `AGENTS.md`,
     `CLAUDE.md`, `.github/copilot-instructions.md`, or
     `.grok/rules/01-quickstart.md` — independent verification shows all
     four already carry this reference (`AGENTS.md:186`, `CLAUDE.md:130`,
     `.github/copilot-instructions.md:328`, `.grok/rules/01-quickstart.md:204`).
  2. Add the two further bullets `.cursor/rules/01-quickstart.mdc` is
     missing relative to the other four mirrors — "AI failure and
     recovery" (`docs/collaboration/ai-failure-recovery.md`) and "Slow AI
     job runner CLI contract" (`docs/collaboration/runner-cli-contract.md`)
     — to the same "Cursor-side reminders" section, alongside item 1's
     addition (three new bullets total in that section).
  3. Update `.grok/rules/01-quickstart.md` line 14's "prepared for
     multiple AI coding agents (Claude, Copilot, Codex, Grok, etc.)"
     sentence to also name Cursor, matching the equivalent sentence
     already updated in `.cursor/rules/01-quickstart.mdc` itself (which
     already lists all five files including its own).
  4. Add `.cursor/rules/01-quickstart.mdc`,
     `.cursor/rules/02-architecture-boundaries.mdc`, and
     `.cursor/rules/03-collaboration-and-completion.mdc` to
     `scripts/init-llm-context.sh`'s `required_files` array, matching the
     existing three-file treatment already given to `.grok/rules/*.md`.
  5. Fix the six confirmed instances of an inline code span (a
     `` `docs/path/to/file.md` `` reference) split across a Markdown line
     break, in exactly these four files (re-verified directly against
     current content, not assumed from the backlog item's list):
     - `docs/architecture/external-resource-adoption-contract.md`
       (lines 14-15, 106-107, 124-125 — three instances)
     - `docs/architecture/io-reasoning-contracts.md` (lines 25-26)
     - `docs/collaboration/ai-failure-recovery.md` (lines 8-9)
     - `docs/collaboration/model-tool-capability-matrix.md`
       (lines 75-76)
     Fix by rewrapping the surrounding paragraph so the inline code span
     is not split by a hard line break, without changing wording or
     meaning.
- Explicitly out of scope:
  - Any edit to `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
    or `.grok/rules/01-quickstart.md`'s reading-list section for item 1
    (already correct).
  - Any change to `.cursor/rules/02-architecture-boundaries.mdc` or
    `.cursor/rules/03-collaboration-and-completion.mdc`'s own content
    (only their *existence* is checked by item 4's script change).
  - Resurrecting or merging the old deleted branch
    `process/2026-07-13-cross-agent-contract-drift-fix`.
  - Touching `docs/research/` or anything related to the deleted
    `docs/research-rationale-essays` branch.
  - Expanding the line-wrap fix (item 5) to any file beyond the four
    named above, even if a similar defect is noticed elsewhere while
    editing — record it as a new backlog candidate instead of fixing it
    under this agreement's scope.
  - Any change to `docs/architecture/ai-tool-support-status.md` or other
    item-0021 content.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | LISS-0070: add the 3 missing bullets to `.cursor/rules/01-quickstart.mdc`'s "Cursor-side reminders" section; update `.grok/rules/01-quickstart.md`'s "prepared for multiple AI coding agents" sentence to name Cursor | Implementer | Fast Path | `grep` confirms all 3 bullets present in the Cursor file; grok sentence names Cursor | `grep -n` before/after, pasted |
| 2 | LISS-0071: add the 3 `.cursor/rules/*.mdc` entries to `scripts/init-llm-context.sh`'s `required_files` array | Implementer | Fast Path | Script exits non-zero with "Missing required file" when a `.cursor/rules/*.mdc` file is absent from a throwaway target; exits 0 against the real repo | Reproduction against a throwaway copy with one `.cursor` file removed, before/after |
| 3 | LISS-0072: rewrap the 6 split inline-code-span instances in the 4 named files | Implementer | Fast Path | No line in any of the 4 files ends with an unclosed backtick-opened path fragment; rendered meaning unchanged | `grep -n` pattern re-run showing zero matches; `git diff` reviewed for wording-only rewrap |
| 4 | LISS-0073 (added 2026-08-23, see Reopening Log): fix all 4 "ADR 0002" -> "ADR 0003" instances in `docs/architecture/external-resource-adoption-contract.md` only | Implementer | Fast Path | `grep -n "ADR 0002"` on this file returns zero matches; `check-contract-consistency.py`'s broken-reference failure is gone | `grep -n` before/after; `python3 scripts/check-contract-consistency.py` |
| 5 | Preflight Validation over the whole work plan, including `python3 scripts/check-contract-consistency.py` | Implementer | Preflight | All checks pass, pasted | WP-0026's own Preflight Validation section |
| 6 | Work-plan-level Reviewer pass, separate context | Reviewer | Review | Approval record addressing evidence-sufficiency and boundary-conformance | `docs/collaboration/reviews/2026-08-23-wp-0026-....md` |

Sequencing: 1, 2, and 3 may proceed in any order or concurrently (disjoint
files) within the same Implementation-group worktree; all three complete
before step 4; step 4 (`pass`) is required before step 5.

## Specifications

No `docs/specs/` file covers this work plan — mechanical agent-instruction
and script mirror-parity corrections, not application or process behavior
with its own acceptance spec.

## Boundaries

- No edit to `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  or `.grok/rules/01-quickstart.md`'s reading-list section.
- No edit to `.cursor/rules/02-architecture-boundaries.mdc` or
  `.cursor/rules/03-collaboration-and-completion.mdc` content.
- No line-wrap fix outside the four named files and six named instances.
- No change to `check-contract-consistency.py`'s Python logic.
- Every edit to a file on `docs/collaboration/prompt-instruction-change-control.md`'s
  Agent Operating Contract Files list (`.grok/rules/*.md`, `.cursor/rules/*.mdc`,
  `docs/collaboration/ai-failure-recovery.md`,
  `docs/collaboration/model-tool-capability-matrix.md`) requires this
  design agreement, a separate-context Reviewer pass, a stated reason, and
  an AI work trace under `docs/collaboration/traces/` — no exception for
  small size.
- `scripts/init-llm-context.sh` is not itself an ADR-0006 contract file,
  but is treated with the same review rigor per this repository's own
  precedent (item-0017's note on `check-contract-consistency.py`'s review
  history).

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does gap 1 (external-resource-adoption-contract cross-reference) actually affect all 5 mirrors, as the backlog item states? | No — independent `grep` against current `main` content shows `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, and `.grok/rules/01-quickstart.md` already carry this reference. Only `.cursor/rules/01-quickstart.mdc` is missing it. Scope corrected to touch only the Cursor file for this gap. | Design & Review group (Planner/Specifier), verified by direct `grep -n "external-resource-adoption-contract"` across all five files |
| Is gap 3 (grok's "prepared for multiple AI coding agents" sentence) still current? | Yes — `.grok/rules/01-quickstart.md` line 14 still reads "(Claude, Copilot, Codex, Grok, etc.)" with no mention of Cursor, while `.cursor/rules/01-quickstart.mdc`'s own equivalent sentence already names all five tools including itself. Confirmed by direct read of both files. | Design & Review group, verified by direct read |
| Is gap 4 (init-llm-context.sh) still current? | Yes — `required_files` lists `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, all three `.grok/rules/*.md` files, and several `docs/` files, but no `.cursor/rules/*.mdc` entry. Confirmed by direct read of the script (lines 48-62). | Design & Review group, verified by direct read |
| Which exact files/lines still have the item-5 line-wrap defect? | Re-verified directly (not assumed from the backlog item's list): all four files it names still have the defect, totaling six instances — three in `external-resource-adoption-contract.md` (14-15, 106-107, 124-125), one each in `io-reasoning-contracts.md` (25-26), `ai-failure-recovery.md` (8-9), and `model-tool-capability-matrix.md` (75-76). No other file was searched beyond these four, per the backlog item's own scope boundary against expanding this cosmetic fix. | Design & Review group, verified by direct `grep -n` and `Read` of surrounding context in each candidate file |

## Deferred Questions

None — this is a fully bounded, small work plan with every gap concretely
re-verified against current content before this agreement was written.

## Verification

- `grep -n` before/after for each of the three quickstart-file edits
  (items 1-3), pasted.
- Reproduction of `scripts/init-llm-context.sh`'s failure/pass behavior
  before and after the required-files addition (item 4).
- `grep -n` re-run for the line-wrap pattern in all four files, showing
  zero remaining matches after the fix (item 5).
- `python3 scripts/check-contract-consistency.py` (real repository) — no
  regression, pasted.
- `git diff` reviewed per file to confirm each change is confined to its
  stated scope (no unrelated wording change).
- Independent work-plan-level Reviewer approval, in a separate context.

## Falsification Criteria

This design was wrong if, after execution:

- Any of `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, or
  `.grok/rules/01-quickstart.md` turns out to have actually been missing
  the external-resource-adoption-contract reference (meaning this
  agreement's own re-verification in "Settled Ambiguities" was wrong).
- `.cursor/rules/01-quickstart.mdc` still lacks any of the three bullets
  after the fix.
- `.grok/rules/01-quickstart.md`'s sentence still omits Cursor after the
  fix.
- `scripts/init-llm-context.sh` still passes against a target missing a
  `.cursor/rules/*.mdc` file after the fix.
- Any line-wrap instance beyond the six named remains unfixed in the four
  named files, or a fix changes wording/meaning rather than only
  rewrapping.
- `python3 scripts/check-contract-consistency.py` regresses.
- Any file outside this agreement's Scope is touched.
- (Added 2026-08-23, per the Reopening Log entry above) Any "ADR 0002"
  instance in `docs/architecture/external-resource-adoption-contract.md`
  is changed to something other than "ADR 0003", or a change is made
  to any "ADR 0002" reference anywhere else in the repository, or a
  change is made to `docs/architecture/adr/0002-design-first-ai-request-routing.md`
  or `docs/architecture/adr/0003-input-output-reasoning-contracts.md`
  themselves.

## Agreement

- [x] **Director**: this plan and these specifications describe what I
      want built, and the stated boundaries are the right ones. — Per
      ADR 0016 Rule 2's backlog-item-level agreement:
      `docs/backlog/item-0022-mirror-file-parity-gaps.md`'s own Promotion
      notes state "Promoted, in the Backlog-layer thread ('承認')... Design
      & Review proceeds autonomously from here," with every gap
      concretely named with exact files and exact missing content.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Nothing in them requires guessing at a rule
      that was never stated. — Design & Review group (Planner/Specifier),
      2026-08-23. The one correction this scope required (gap 1's actual
      footprint, re-verified against current content) is settled above,
      not left for the Implementer to guess; the exact line numbers and
      exact wording changes for every other gap are settled as well.

If the AI cannot make its statement, the design phase is not finished,
regardless of the Director's readiness to proceed.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
| 2026-08-23 | The Implementation group's LISS-0072 fix (rewrapping `docs/architecture/external-resource-adoption-contract.md:14-15`'s split code span) unmasked a pre-existing, previously-undetectable broken reference: the span names `docs/architecture/adr/0002-input-output-reasoning-contracts.md`, which does not exist — the real file is `docs/architecture/adr/0003-input-output-reasoning-contracts.md` (confirmed: ADR 0002 is actually `0002-design-first-ai-request-routing.md`, a different topic; ADR 0003 itself, line 10, correctly says "ADR 0002 defines design-first payload routing", confirming 0002 and 0003 are distinct, correctly-numbered ADRs and this file's references are the ones that drifted). `check-contract-consistency.py`'s `CODE_PATH` regex does not match a code span split across a newline, so this broken reference was invisible to the checker before LISS-0072's fix, not introduced by it. This is a decision the original agreement does not settle (it authorized only a wording-preserving rewrap, not a reference correction) and is outside `docs/backlog/item-0022-...md`'s own stated scope (line-wrap cosmetics only). Independently re-grepped the same file for every "ADR 0002" mention: 3 more prose instances exist (lines 16, 60, 63, pre-fix numbering), all confirmed to be about the same IO/reasoning-contracts topic (source-reference record shape), i.e. all 4 total instances in this one file are the same drift, not a legitimate reference to the real ADR 0002 (routing). No other file in the repository was found to have this same drift (checked via `grep -rn "ADR 0002"` across `docs/`, `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.grok/`, `.cursor/`). | **Resolution**: scope extended by exactly one bounded addition — LISS-0073, fixing all 4 "ADR 0002" -> "ADR 0003" instances in this one file only, nothing else. Decided by the Design & Review group (Planner/Specifier) under ADR 0016 Rule 2's standing autonomy over this backlog item's execution, on the grounds that the fix is single-file, single-pattern, zero architectural/behavioral risk, and independently fact-verified (file existence and topic match) rather than guessed — not escalated to a fresh Director round-trip given its size and the direct, mechanical verification available. The 4 falsification criteria below are added to cover this extension. If the Reviewer disagrees this was within Design & Review's own autonomy to decide, the Reviewer records that as a rejection reason rather than silently approving. |
