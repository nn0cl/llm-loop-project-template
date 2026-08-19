# LISS-0030: Propagate portable three-layer loop wording to contract mirrors

## Metadata

- Local issue ID: LISS-0030
- GitHub issue: none
- Status: done
- Phase: phase-0-design (contract-file propagation, no application code)
- Type: contract-propagation
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/mirror-portable-loop-wording

## Summary

- Add equivalent-effective-content, portable wording to `AGENTS.md`,
  `CLAUDE.md`, `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
  `.cursor/rules/*.mdc` (per ADR 0006's mirror-parity rule) stating: the
  three-layer concept from ADR 0016 (Backlog / Design & Review /
  Implementation); the portable baseline handoff (parent-child subagent
  spawn, dedicated worktree per child, native completion signal); that the
  live-session `SendMessage`/`ListAgents` handoff and Director intervention
  channel are Claude-Code-specific, described in full only in
  `docs/collaboration/cross-session-messaging.md`; and that the default
  intervention-channel fallback everywhere else is the
  `docs/collaboration/handoffs/WP-NNNN-status.md` file convention ADR 0017
  defines. Cross-reference ADR 0017 by path from each mirror.

## Acceptance Notes

- `scripts/check-contract-consistency.py` passes.
- Read-through confirms all five files carry equivalent effective content
  on this new section (not necessarily identical text — Cursor's own
  effective-content composition rule from
  `docs/collaboration/prompt-instruction-change-control.md` still applies).
- No existing rule in any of the five files is weakened, removed, or
  contradicted.
- New section is proportionate to each file's existing style/length (do not
  import the full ADR 0016 text into each mirror — a compact pointer plus
  the portable rule statement is sufficient, mirroring how these files
  already summarize other ADRs rather than reproducing them).
- AI work trace exists under `docs/collaboration/traces/` naming all five
  files, the reason, and the expected agent-behavior change.
- Self-review recorded (short form is appropriate — one cohesive
  propagation change across five files, same pattern in every file).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0007-multi-agent-tool-loop-portability.md
- Depends on: LISS-0029 (cites ADR 0017 by number/path)
- Blocks: none
- Related: `docs/architecture/adr/0006-prompt-instruction-change-control.md`
  (governs the mirror-parity rule itself)

## Decisions Not Settled by the Design Agreement

- Exact prose/wording per file is left to the Implementer, bounded by the
  acceptance criteria above and the "equivalent effective content" rule —
  this is execution-level phrasing, not a planning ambiguity, per
  `docs/collaboration/design-agreement.md`'s existing pattern of leaving
  "exact SendMessage template wording" etc. to Implementer discretion.

## Context

- Included: ADR 0017 (once LISS-0029 lands), `DA-2026-08-18-03`, all five
  mirror files' current content, `docs/collaboration/prompt-instruction-change-control.md`.
- Omitted: the full text of ADR 0016 and `cross-session-messaging.md` —
  mirrors point at them, they do not reproduce them.
- Assumptions: none beyond LISS-0029's ADR 0017 existing and being stable
  before this issue starts editing (enforced by the dependency above).

## AI Planning Records

### AIP-0030-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Sonnet 5 via Claude Code, Design & Review
    group standing session
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: not surfaced in this environment
- Created at: 2026-08-18
- Planning size: M
- Intended execution route: Implementation-group agent, Architecture Path,
  five coordinated file edits plus one trace
- Compatibility state: Verified — confirmed via `grep` that none of the
  five files currently mention the two-group topology at all, so this is a
  pure addition, not a reconciliation of drifted content
- Intended scope: `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md` (3 files),
  `.cursor/rules/*.mdc` (3 files) — effectively up to 9 files depending on
  which `.grok`/`.cursor` rule file is the right home for this content;
  Implementer decides, consistent with how those directories are already
  organized (01-quickstart / 02-architecture-boundaries /
  03-collaboration-and-completion)
- Estimated token range: 6,000-15,000 tokens
- Estimated token midpoint: 10,000
- Token metric: approximate output tokens across all edited files plus the
  trace
- Estimation basis: WP-0002's own mirror-parity precedent
  (`docs/collaboration/agreements/2026-08-03-work-plan-scoped-governance.md`,
  Task 4, "propagation across nine contract files") as an order-of-magnitude
  reference, scaled down since this is one small section, not a full
  propagation pass
- Assumptions: single execution attempt
- Confidence: medium
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/collaboration/prompt-instruction-change-control.md`
- `docs/architecture/adr/0006-prompt-instruction-change-control.md`
- `docs/collaboration/agreements/2026-08-03-work-plan-scoped-governance.md`
  (mirror-propagation precedent)

## Work Notes

- 2026-08-18 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0007-*.md`'s promotion. Confirmed via
  `grep -rln "session group\|two-group\|cross-session-messaging\|SendMessage\|ListAgents" AGENTS.md CLAUDE.md .github/copilot-instructions.md .grok/rules/ .cursor/rules/`
  (no matches) that none of the five files currently describe the
  two-group topology — this issue is a pure addition. Dispatched to the
  Implementation group together with LISS-0029.
- 2026-08-18 (Implementation group, Implementer): read all three
  `.grok/rules/*.md` and all three `.cursor/rules/*.mdc` files in full
  before choosing a home. `03-collaboration-and-completion.md`/`.mdc`
  matched this content's subject best (Design Intake, Reopening Gates,
  Minor Fix Path/Preflight, Handoff and Completion — session-mechanics
  topics, not phase or dependency-boundary rules, which live in
  `02-architecture-boundaries`), and using the same file in both
  directories keeps the two tool-specific mirror sets structurally
  parallel, per the issue's own guidance. Added one new `##` section,
  "Session Topology Across AI Coding Tools," with equivalent content
  (same four points: layer concept is tool-agnostic per ADR 0016; portable
  parent-child-plus-worktree baseline handoff; SendMessage/ListAgents and
  the Director's live intervention channel scoped to Claude Code and
  `cross-session-messaging.md`; the ADR-0017-defined
  `docs/collaboration/handoffs/WP-<NNNN>-status.md` file as the default
  fallback everywhere else, read during ordinary session-start recovery)
  to all five files: `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`,
  `.grok/rules/03-collaboration-and-completion.md`,
  `.cursor/rules/03-collaboration-and-completion.mdc`. Each mirror points
  at ADR 0016 and ADR 0017 by path rather than reproducing their content,
  per this issue's own Acceptance Notes; the Grok and Cursor copies add one
  tool-specific sentence each (Grok Build's own parent-child completion
  wording; Cursor's own worktree-per-agent model) without changing the
  four core points. Registered the new `AGENTS.md` section in
  `scripts/check-contract-consistency.py`'s `MIRRORED_SECTIONS`, anchored
  on the ADR 0017 filename, so `check_parity_completeness` and
  `check_mirror_parity` both cover it. `git diff --stat` confirmed every
  changed mirror file is insertion-only (no line removed or reworded) —
  no existing rule was touched. Created
  `docs/collaboration/traces/2026-08-18-liss-0030-mirror-portable-loop-wording.md`
  naming all five files, the reason, and the expected agent-behavior
  change, per the traceability rule this contract-file change is subject
  to. Status moved to `review`.

## Self-Review (short form, per `docs/templates/self-review.md`)

Phase / finding: Architecture Path contract-file propagation across five
mirror files (single cohesive change, same new section in each).

Command run: `python3 scripts/check-contract-consistency.py`

Result:

```
contract consistency: all checks passed
```

Risks considered:

- One of the five mirrors drifts from "equivalent effective content" —
  stating the four required points differently enough that a reader of one
  mirror would reach a different operational conclusion than a reader of
  another (the specific risk this work plan's own "Risks" section names,
  and the reason this issue's Acceptance Notes call for an explicit
  read-through, not just the automated check).
- The new section accidentally weakens, removes, or contradicts an existing
  rule already present in one of the five files (for example, implying
  `SendMessage`/`ListAgents` is available in a tool that does not have it,
  which `DA-2026-08-18-03`'s own Falsification Criteria names explicitly).
- `scripts/check-contract-consistency.py`'s automated parity check passes
  while the content still differs in substance — the check confirms a
  pattern string is present in each file, not that the surrounding
  sentence means the same thing (a limitation the script's own docstring
  states directly under "What this cannot check... Meaning").
- The new `AGENTS.md` `##` heading is left unclassified in
  `MIRRORED_SECTIONS`/`AGENTS_ONLY_SECTIONS`, which would fail
  `check_parity_completeness`.
- Cursor's copy, which the automated `check_mirror_parity` check does not
  cover (`.cursor/rules/*` is deliberately outside `FULL_MIRRORS`, per ADR
  0006), silently ends up unequal to the other four despite that gap.

Why each does not occur:

- Side-by-side read-through (performed directly, not only via the script)
  confirms all five copies state the same four points in the same order:
  layer concept tool-agnostic (ADR 0016 pointer); portable
  parent-child-plus-worktree baseline; SendMessage/ListAgents and the
  Director's intervention channel scoped to Claude Code
  (`cross-session-messaging.md` pointer); the ADR-0017 handoff-file
  fallback as the default elsewhere, read during ordinary session-start
  recovery. The Grok and Cursor additions are the only per-file variation
  (one extra sentence each naming that tool's own native completion/
  worktree behavior), and neither changes any of the four points.
- `git diff --stat` (recorded in Work Notes above) shows every changed
  mirror file's diff is insertion-only — 0 deletions across all five —
  so no pre-existing sentence was reworded or removed to make room for the
  new section.
- Because the script's own docstring names "meaning" as something it
  cannot check, this self-review does not treat the `all checks passed`
  result as sufficient by itself — it is combined with the direct
  read-through above,
  which is the human-level check the script's docstring says belongs to
  the Reviewer persona (also to be exercised again, independently, at the
  work-plan-level Reviewer pass).
- The new heading was added to `MIRRORED_SECTIONS` in the same change that
  added the heading to `AGENTS.md` (see Changed Files in the trace); the
  full run of `check-contract-consistency.py` above — which runs
  `check_parity_completeness` — passed, confirming no unclassified
  heading remains.
- The Cursor file was edited in the same change as the other four, with the
  same four-point content, specifically because the automated check does
  not cover it — the read-through above was performed against all five
  files, not only the four the script verifies, for exactly this reason.

## Verification

- `python3 scripts/check-contract-consistency.py` — `contract consistency:
  all checks passed`.
- `git diff --stat` — insertion-only across all five mirror files and the
  consistency-script registration; no existing line removed or reworded.
- Direct side-by-side read-through of all five files' new section,
  confirming equivalent effective content (see Self-Review above).
- `docs/collaboration/traces/2026-08-18-liss-0030-mirror-portable-loop-wording.md`
  exists, naming all five files, the reason, and the expected
  agent-behavior change.
