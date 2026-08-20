# LISS-0029: Write ADR 0017 (portable three-layer loop, file-based intervention fallback)

## Metadata

- Local issue ID: LISS-0029
- GitHub issue: none
- Status: done
- Phase: phase-0-design (produces an Architecture Path artifact, not
  application code)
- Type: architecture-decision
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/adr-0017-portable-loop

## Summary

- Write `docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md`
  stating: (1) the three-layer concept (Backlog / Design & Review /
  Implementation, per ADR 0016 Rule 1) is tool-agnostic; (2) the portable
  baseline handoff across AI coding tools is parent-child subagent spawning,
  each child in its own dedicated `git worktree`/branch, using each tool's
  own native completion signal; (3) `SendMessage`/`ListAgents` remain Claude
  Code's own implementation of the routine handoff and the sole
  implementation of the Director's intervention channel (ADR 0016 Rule 4);
  (4) for tools without an equivalent, the intervention-channel fallback is
  a file-based status signal under `docs/collaboration/handoffs/`, in the
  exact format `DA-2026-08-18-03` pins down (one file per in-flight work
  plan: `docs/collaboration/handoffs/WP-NNNN-status.md`).

## Acceptance Notes

- States which ADR 0001/0014/0016 clauses this ADR adds to versus leaves
  untouched (it should add a portability layer, not supersede anything —
  confirm no supersession language is needed, since this is additive).
- Explicitly states ADR 0016 and `cross-session-messaging.md` are unchanged
  by this ADR.
- Cites the primary-source spike findings recorded in `DA-2026-08-18-03`'s
  "Spike Result" section (Copilot fleet mode, Grok Build subagents.md,
  Codex CLI subagents docs).
- Fixes the `docs/collaboration/handoffs/WP-NNNN-status.md` field list
  exactly as `DA-2026-08-18-03`'s Settled Ambiguities table states.
- Not an ADR-0006 contract file (mirrors ADR 0016's own precedent — no
  trace required for this issue).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0007-multi-agent-tool-loop-portability.md
- Depends on: none
- Blocks: LISS-0030 (mirror wording cites this ADR by number)
- Related: ADR 0016, `docs/collaboration/cross-session-messaging.md`
  (referenced, not edited)

## Decisions Not Settled by the Design Agreement

- The exact ADR number is pinned as 0017 in `DA-2026-08-18-03`, but the
  Implementer must confirm it is still the next-free number at execution
  time (`ls docs/architecture/adr/` before creating the file) in case
  another concurrent work plan has since claimed it — if so, this is a
  reopening-worthy conflict, not a silent renumbering.

## Context

- Included: ADR 0016, `docs/collaboration/cross-session-messaging.md`,
  `docs/collaboration/session-start-and-resume.md`,
  `docs/backlog/item-0007-*.md`, `DA-2026-08-18-03`.
- Omitted: WP-0002's per-issue traces — not needed to write a new,
  additive ADR.
- Assumptions: the spike's primary-source findings (recorded in
  `DA-2026-08-18-03`) are accurate as of 2026-08-18; if the Implementer
  finds reason to doubt them, that is a reopening trigger.

## AI Planning Records

### AIP-0029-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Sonnet 5 via Claude Code, Design & Review
    group standing session
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A (not surfaced in this environment)
  - N/A reason: this environment does not display a reasoning-effort label
    to the session itself
- Created at: 2026-08-18
- Planning size: M
- Intended execution route: Implementation-group agent, Architecture Path,
  single ADR document
- Compatibility state: Verified — ADR template and numbering convention
  read directly from `docs/templates/adr.md` and `docs/architecture/adr/`
  directory listing
- Intended scope: one new file under `docs/architecture/adr/`
- Estimated token range: 3,000-8,000 tokens
- Estimated token midpoint: 5,000
- Token metric: approximate output tokens for drafting one ADR of similar
  length to ADR 0016
- Estimation basis: ADR 0016 itself is roughly 6,000-7,000 tokens rendered;
  ADR 0017 is additive and narrower in scope, expected similar or smaller
- Assumptions: single execution attempt; no major restructuring needed
  after self-review
- Confidence: medium
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
- `docs/backlog/item-0007-multi-agent-tool-loop-portability.md` — cites,
  fetch-verified 2026-08-18: `docs.github.com/en/copilot/how-tos/copilot-sdk/features/fleet-mode`,
  `github.com/xai-org/grok-build/.../16-subagents.md`,
  `learn.chatgpt.com/docs/agent-configuration/subagents`
- `docs/templates/adr.md`

## Work Notes

- 2026-08-18 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0007-*.md`'s promotion, after running the primary-source
  spike recorded in `DA-2026-08-18-03`. Dispatched to the Implementation
  group together with LISS-0030.
- 2026-08-18 (Implementation group, Implementer): confirmed `0017` was the
  next-free ADR number by `ls docs/architecture/adr/` (highest existing file
  was `0016-standing-two-group-topology-and-backlog-gated-autonomy.md`) before
  creating the file, per the issue's own "Decisions Not Settled" note.
  Created `docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md`
  stating the four points from this issue's Summary as testable rules (Rules
  1-4), an explicit "what this ADR leaves untouched" statement (Rule 5) per
  the Acceptance Notes, the exact `docs/collaboration/handoffs/WP-<NNNN>-status.md`
  field list from `DA-2026-08-18-03`'s Settled Ambiguities table verbatim, and
  the primary-source spike citations from that same agreement's Spike Result
  section. `scripts/check-contract-consistency.py` failed on first run
  (dangling references to a URL and to the generic handoff-file naming
  pattern; a stale `0001-0016` ADR range in `README.md`, `QUICKSTART.md`,
  `QUICKSTART.ja.md`, and `.github/workflows/ci.yml`'s ADR-existence check,
  all caused directly by adding a 17th process ADR, mirroring the precedent
  set when ADR 0016 itself last bumped that range). Fixed all of the above;
  second run passed clean. Status moved to `review`; Preflight and the
  separate-context Reviewer pass are recorded at the work-plan level
  (`docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md`) after
  LISS-0030 also reaches `review`.

## Self-Review (short form, per `docs/templates/self-review.md`)

Phase / finding: Architecture Path design artifact (new ADR file; no Red/
Green/Refactor phase applies to a documentation-only decision record).

Command run: `python3 scripts/check-contract-consistency.py`

Result:

```
contract consistency: all checks passed
```

(First run, before the fixes below, reported 13 failures: 5 dangling
references inside the new ADR file, and 8 stale-ADR-range statements in
`README.md`/`QUICKSTART.md`/`QUICKSTART.ja.md`. Both categories are fixed in
the working tree; the `all checks passed` result above is the current,
post-fix state.)

Risks considered:

- ADR 0017 rewords, weakens, or silently supersedes an ADR 0016 rule instead
  of staying additive.
- ADR 0017 edits `docs/collaboration/cross-session-messaging.md` or ADR
  0016 itself, which `DA-2026-08-18-03` explicitly puts out of scope.
- The `docs/collaboration/handoffs/WP-<NNNN>-status.md` field list drifts
  from the exact list `DA-2026-08-18-03`'s Settled Ambiguities table pins.
- ADR 0017 is not actually the next-free ADR number (a concurrent work plan
  claimed 0017 first).
- The spike citations in ADR 0017's Context section misstate or invent
  content beyond what `DA-2026-08-18-03`'s own Spike Result section records.
- Adding a 17th process ADR silently breaks the repository's own mechanical
  ADR-range checks or its CI ADR-existence assertion.

Why each does not occur:

- ADR 0017's Status section states explicitly "does not supersede ADR 0016
  or any clause of ADR 0001 or ADR 0014," and Rule 5 ("What this ADR leaves
  untouched") restates this with no reworded ADR 0016 clause anywhere in the
  file; verified by re-reading ADR 0016 alongside ADR 0017's Rules 1-5
  side by side.
- `git status --short` and `git diff --stat` (run before this commit) show
  no modification to `docs/architecture/adr/0016-*.md` or
  `docs/collaboration/cross-session-messaging.md` — only `.github/workflows/ci.yml`,
  `QUICKSTART.ja.md`, `QUICKSTART.md`, `README.md` (modified) and the new
  `docs/architecture/adr/0017-*.md` (untracked) appear in the diff.
- ADR 0017 Rule 4's five fields (`Work plan`, `Current stage`, `Director
  intervention gate`, `Last updated`, `Updated by`) were copied and checked
  word-for-word against `DA-2026-08-18-03`'s Settled Ambiguities row for
  this exact question.
- `ls docs/architecture/adr/` was run immediately before creating the file
  (recorded above); `0016-...md` was the highest existing entry, so `0017`
  was free at that moment. Re-run at self-review time (`ls
  docs/architecture/adr/`) still shows no other `0017-*` file and no `0018-*`
  file, so no concurrent claim landed since.
- Each Context-section bullet in ADR 0017 is a direct quotation of
  `DA-2026-08-18-03`'s own Spike Result bullet for that tool, with the same
  fetch date (2026-08-18) and the same "confirms, rather than overturns"
  conclusion sentence; no new claim was added beyond what that section
  already states.
- `scripts/check-contract-consistency.py`'s own "ADR range" check (which
  reads `docs/architecture/adr/` directly, not a hardcoded number) now
  passes, and `.github/workflows/ci.yml`'s ADR-existence loop was extended
  to include `0017` in the same change, following the precedent set when
  ADR 0016 itself was added (`git log --oneline -- .github/workflows/ci.yml`
  shows commit `6fb7eff` added `0016` to that same loop).

## Verification

- `python3 scripts/check-contract-consistency.py` — `contract consistency:
  all checks passed` (see Self-Review above for the failing first run and
  the fixes applied).
- `ls docs/architecture/adr/` before file creation and again at self-review
  time, confirming `0017` was and remains the next-free number.
