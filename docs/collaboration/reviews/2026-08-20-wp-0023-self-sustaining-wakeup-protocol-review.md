# Review Record: WP-0023 (check-and-spawn wake protocol, ADR 0016 Rule 7)

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in the Design & Review
      group's standing session, which produced the work plan, design
      agreement, and issue text (including the exact verbatim insertion
      text), but did not perform the file edits itself — that was
      executed by a separate Implementation-group subagent session in
      its own dedicated worktree/branch (`wp-0023-execution`, spawned off
      `process/promote-item-0020`). This review does not rely on that
      Implementer session's own reasoning as justification; every claim
      below is independently re-run against the actual committed tree by
      this review itself.
- [x] **Deterministic precondition.** Deterministic verification was run,
      independently, by this review — including a full second pass after
      this review's own finding (LISS-0064) was corrected, using a fresh
      `git archive` extraction each time, not the Implementer's own
      pasted output.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below, each with the grounds it does not occur. One genuine
      scenario *was* reproduced on the first pass (see row 5) and is
      recorded honestly, not omitted — the same class of defect as
      `LISS-0060`, now confirmed a third time this session.

## Review Target

- Artifact: `wp-0023-execution` branch (commits `6125931`..`4c4d861`), to
  be merged into `process/promote-item-0020`.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-20-self-sustaining-wakeup-protocol.md`
  (`DA-2026-08-20-06`)
- Specification: none (a process/contract documentation change; no
  `docs/specs/` file covers this work plan).
- Current phase: Architecture Path (content fully specified verbatim by
  the design agreement/issue — no design judgment exercised by the
  Implementer). Preflight Validation recorded as pass in
  `docs/work-plans/WP-0023-...md`, re-confirmed by this review after the
  LISS-0064 correction landed.
- Producing persona: Implementer (Implementation group, separate context).
- Reviewing persona / model / tool: Reviewer (Design & Review group,
  standing session).
- Approval type: boundary-conformance (did the edit land exactly the text
  specified, touching nothing else — per ADR 0006's own governance for
  contract-file changes) and evidence-sufficiency (does the trace
  correctly document both edits) — the two types the work plan's own
  Review Summary Packet names as at stake.
- Preflight Validation record: `docs/work-plans/WP-0023-...md`'s own
  "Preflight Validation" section.
- Preflight result: pass (independently confirmed by this review after
  correction; the pre-correction claim for check #1 was not reproducible
  — see Falsification Search row 5 — and is the subject of the resolved
  finding below).

## Deterministic Verification Output

All commands below were run independently by this review, against fresh
`git archive` extractions of `wp-0023-execution` at its final state — not
pasted from the Implementer's own record.

```text
--- contract-file insertion, word-for-word match check ---
$ git diff process/promote-item-0020...wp-0023-execution -- docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md
(full diff independently read; every line matches LISS-0063's own
Acceptance Notes fenced-code-block text exactly -- Rule 7 body, the
Status-section sentence, and both Enforcement bullets, verbatim, no
paraphrase, no dropped or altered word)

$ git diff process/promote-item-0020...wp-0023-execution -- docs/collaboration/cross-session-messaging.md
(full diff independently read; direction 1's replaced Message bullet,
direction 2's new Wake mechanic bullet, and the new "Queue continuation
and resume-before-duplicate-spawn" section all match LISS-0063's own
specification exactly)

--- Rule 1-6 untouched, confirmed ---
$ git diff process/promote-item-0020...wp-0023-execution -- docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md | grep -E "^-[^-]" 
(no output -- the diff contains only additions, zero deletions, in ADR
0016; Rules 1-6 are provably untouched, not merely unmentioned)

--- fresh full checker run, post-correction ---
$ git archive wp-0023-execution | tar -x -C /tmp/wp23-verify2
$ python3 /tmp/wp23-verify2/scripts/check-contract-consistency.py --repo /tmp/wp23-verify2
contract consistency: all checks passed

--- Issue Graph sync (post-LISS-0064 correction) ---
$ git show wp-0023-execution:docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md | grep -n "LISS-0063 |"
48:| LISS-0063 | done | M | M | N/A | LISS-0062 | - | process/promote-item-0020 |
(correctly synced to 'done')

--- full diff scope ---
$ git diff process/promote-item-0020...wp-0023-execution --stat
 ...wo-group-topology-and-backlog-gated-autonomy.md |  70 ++++++
 docs/collaboration/cross-session-messaging.md      |  59 ++++-
 .../2026-08-20-check-and-spawn-wake-protocol.md    | 256 +++++++++++++++++++++
 .../LISS-0063-check-and-spawn-wake-protocol.md     |  66 +++++-
 .../LISS-0064-wp-0023-issue-graph-status-sync.md   |  22 +-
 .../WP-0023-self-sustaining-wakeup-protocol.md     |  86 +++++--
 6 files changed, 531 insertions(+), 28 deletions(-)
(exactly the 6 files the design agreement's Boundaries section
authorizes: the two contract files, the new trace, LISS-0063, LISS-0064,
and WP-0023 itself -- no other file touched, no new script/helper/hook)

--- trace content spot-check ---
$ git show wp-0023-execution:docs/collaboration/traces/2026-08-20-check-and-spawn-wake-protocol.md
(read in full -- states both contract files, the Director's own decision
as the reason, and the two concrete behavior changes: a spawning party
checks ListAgents before spawning, and a standing loop checks its queue
before going idle; covering agreement DA-2026-08-20-06, canonical
issue/work plan LISS-0063/WP-0023, all correctly cited)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The inserted text drifted from LISS-0063's own verbatim specification (paraphrase, dropped clause, reordered sentence) | Independent line-by-line `git diff` comparison against LISS-0063's own fenced code blocks for both files found an exact match, character for character | not reproduced |
| 2 | ADR 0016 Rules 1-6, or any other existing sentence in either file, was altered or removed | `git diff -- <adr-0016-path> \| grep -E "^-[^-]"` shows zero deletion lines in ADR 0016; `cross-session-messaging.md`'s diff shows deletions only inside direction 1's own replaced bullet (the one edit LISS-0063 explicitly authorized), nothing else | not reproduced |
| 3 | A new script, helper, scheduled task, or `.claude/settings.json` hook was added, exceeding the design agreement's documentation-only scope | `git diff --stat` shows exactly 6 files, none under `scripts/` or `.claude/`; the trace itself states no code surface was found or touched | not reproduced |
| 4 | The mandatory AI work trace is missing, or omits which files changed / why / what behavior changes | Trace file exists, read in full, and states all three required facts explicitly and accurately | not reproduced |
| 5 | Preflight's own "all checks passed" claim for check #1 is reproducible against the actual final committed state | **Reproduced on this review's first pass**: independently running `check-contract-consistency.py` against a fresh `git archive` of the pre-correction `wp-0023-execution` (commits `6125931`/`dd5e9f9`) showed a real `issue status sync` failure — WP-0023's own Issue Graph row for LISS-0063 was never updated to `done`. This is the third occurrence of this exact defect class this session (WP-0021: caught as `LISS-0060`; WP-0022: self-caught by the Implementer). Not accepted at face value — opened as `docs/issues/LISS-0064-...md` (`Type: review-finding`), routed back to the Implementation group via the Minor Fix Path, and independently re-verified clean after the correction (commit `4c4d861`) — see the "fresh full checker run" output above | reproduced pre-correction; not reproduced post-correction |
| 6 | The LISS-0064 fix itself touched more than the one authorized table cell | `git diff f5c3423...wp-0023-execution --stat` shows exactly 2 files (`LISS-0064` itself and `WP-0023`'s own file), and direct inspection of `WP-0023`'s diff shows a single-line change | not reproduced |

## Scenarios Not Searched

- Full end-to-end behavioral confirmation that a real spawning party
  (the Backlog thread, or a future Design & Review session) actually
  performs the `ListAgents` check this protocol now documents — this
  work plan documents the rule; it does not add automated enforcement,
  which the design agreement's own Risks section names as an honest,
  accepted limitation, not something this review should treat as a gap
  in the documentation change itself.
- Whether the recurring Issue-Graph-sync defect class (now three
  occurrences) should prompt a change to how future Implementers are
  dispatched (e.g., an explicit checklist item) — noted in `LISS-0064`'s
  own Work Notes as worth flagging, not resolved by this review, which
  stays scoped to confirming this one work plan's own correctness.

## Checklist

- [x] The artifact belongs to the phase that was run (Architecture Path,
      fully specified content) — confirmed by the exact-match diff.
- [x] Every `Then` clause in the specification is asserted by the work —
      N/A, no specification covers this work plan.
- [x] The dependency rule and port boundaries hold — N/A.
- [x] No boundary named in the design agreement was crossed — confirmed:
      Rules 1-6 untouched, no other contract file touched, no new script
      or automation surface.
- [x] Specifications and accepted tests were not modified to make work
      pass — N/A.
- [x] Every claim in the artifact states its grounds — Rule 7 itself
      cites the spike that grounds it; the trace cites the covering
      agreement and canonical issue/work plan.
- [x] The record would let a third party re-run this same search — every
      command above is copy-pasteable and was independently re-run by
      this review.

## Decision

- [x] Approved

## Reasons

Both contract-file insertions (ADR 0016's new Rule 7, plus its
Status-section and Enforcement additions; `cross-session-messaging.md`'s
updated directions and new section) are confirmed, by independent
line-by-line diff comparison, to match this issue's own verbatim
specification exactly — no drift, no paraphrase. Rules 1-6 and all other
existing content in both files are provably untouched (the ADR 0016 diff
contains zero deletion lines). The mandatory AI work trace is present,
accurate, and complete. The diff is confined to exactly the 6 authorized
files; no new script, helper, or automation surface was added, matching
the design agreement's own explicit boundary.

This review's own independent re-verification caught one real defect on
its first pass — the same Issue Graph sync gap class as `LISS-0060`,
recurring a third time this session — and did not accept the
Implementer's own "all checks passed" claim at face value. It was routed
through the proper channel (`Type: review-finding`, `LISS-0064`, Minor
Fix Path) and independently re-verified clean after correction. No
further `Type: review-finding` issue is warranted. `LISS-0064` itself is
`Status: resolved`, closed below alongside this approval.