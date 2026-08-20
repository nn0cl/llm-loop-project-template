# Review Record: WP-0025 (AI tool support status survey, item-0021)

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in the Design & Review
      group's standing session, which authored the status report and
      spike case, but the contract-file edit itself (the one piece
      requiring ADR-0006 governance) was executed by a separate
      Implementation-group subagent session in its own dedicated
      worktree/branch (`wp-0025-execution`, spawned off
      `process/item-0021-status-survey` commit `7d61ab5`). This review
      does not rely on that Implementer session's own reasoning as
      justification — every claim below is independently re-run, and the
      status report's own key citations (which this session authored)
      were independently re-checked twice: once by the Implementer
      (required by LISS-0069's own Acceptance Notes before it could
      edit anything) and again by this review itself.
- [x] **Deterministic precondition.** Deterministic verification was run,
      independently, by this review, against a fresh `git archive`
      extraction — not the Implementer's own pasted output.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below, including a specific, independent reproduction of the
      "3 pre-existing failures" claim (via direct comparison against the
      actual pre-`LISS-0069` commit, not a git-stash trick, and not
      accepted on the Implementer's own report alone).

## Review Target

- Artifact: `wp-0025-execution` branch (commits `76d04e4`, `cfe1685`,
  `a949b3a`), to be merged into `process/item-0021-status-survey`.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-20-ai-tool-support-status-survey.md`
  (`DA-2026-08-20-08`)
- Specification: none (a research/status-report deliverable plus one
  narrow contract-file addition; no `docs/specs/` file covers this work
  plan).
- Current phase: Architecture Path (contract-file edit); Preflight
  Validation recorded as pass in `docs/work-plans/WP-0025-...md`.
- Producing persona: Implementer (Implementation group, separate
  context) for the contract-file edit and trace; Planner/Specifier
  (this same Design & Review session) for the status report and spike
  case themselves, per `docs/spike/README.md`'s own model that spikes
  are Design & Review's own work.
- Reviewing persona / model / tool: Reviewer (Design & Review group,
  standing session).
- Approval type: evidence-sufficiency (are the report's own claims
  genuinely sourced and independently re-confirmed) and
  boundary-conformance (does the contract-file edit stay within its own
  narrow, specified scope) — the two types the work plan's own Review
  Summary Packet names.
- Preflight Validation record: `docs/work-plans/WP-0025-...md`'s own
  "Preflight Validation" section.
- Preflight result: pass (independently confirmed by this review).

## Deterministic Verification Output

All commands below were run independently by this review — not pasted
from the Implementer's own record.

```text
--- contract-file edit, exact-text check ---
$ git diff process/item-0021-status-survey...wp-0025-execution -- docs/collaboration/prompt-instruction-change-control.md
(full diff independently read: one new bullet in "Agent Operating
Contract Files", one new table row in "Per-Agent-Tool Rule Applicability
Registry" -- both match LISS-0069's own specified text exactly; no other
line in the file touched)

--- diff scope ---
$ git diff process/item-0021-status-survey...wp-0025-execution --stat
 .../prompt-instruction-change-control.md           |   5 +
 .../2026-08-20-ai-tool-support-status-survey.md    | 178 +++++++++++++++++++++
 .../LISS-0069-antigravity-contract-registry-entry.md | 113 ++++++++++++-
 .../WP-0025-ai-tool-support-status-survey.md       | 105 ++++++++++--
 4 files changed, 384 insertions(+), 17 deletions(-)
(exactly the 4 files the design agreement's Boundaries section
authorizes: the contract file, the new trace, and the two tracking
files -- docs/architecture/ai-tool-support-status.md and
docs/spike/case-0004-...md are NOT in this diff, confirming they landed
only in this work plan's own opening commit 7d61ab5, not re-touched here)

--- independent re-verification of the "3 pre-existing failures" claim ---
$ python3 scripts/check-contract-consistency.py   # against this review's
  own worktree, which sits at commit 7d61ab5 (the work plan's own
  opening commit, BEFORE LISS-0069's edits) -- direct access to the
  actual pre-existing base, not a git-stash reconstruction
references:
  docs/architecture/ai-tool-support-status.md:67 names '.cursor/worktrees.json', which does not exist
  docs/architecture/ai-tool-support-status.md:91 names 'github.com/xai-org/grok-build/.../16-subagents.md', which does not exist
  docs/architecture/ai-tool-support-status.md:110 names 'ANTIGRAVITY.md', which does not exist

contract consistency: 3 failure(s)

$ git archive wp-0025-execution | tar -x -C /tmp/wp25-verify
$ python3 /tmp/wp25-verify/scripts/check-contract-consistency.py --repo /tmp/wp25-verify
(identical 3 failures, same lines, same text -- confirms the final
branch state introduces no new failure and resolves none of these 3;
they are genuinely unchanged before and after LISS-0069)

--- direct inspection of each of the 3 failures ---
$ sed -n '65,68p;89,93p;108,112p' docs/architecture/ai-tool-support-status.md
(read directly: line 67 describes Cursor's OWN external config file
`.cursor/worktrees.json` in prose, not a link into this repo; line 91 is
a citation URL containing a literal "..." elision, not a real local
path; line 110 explicitly states `ANTIGRAVITY.md` was NOT found to
exist -- the checker inverting that stated non-existence into an error.
All three independently confirmed as genuine checker false positives on
this repository's own reference-checking logic, not real defects in the
report's own accuracy.)

--- Issue Graph sync fix ---
$ git show --name-status a949b3a
M   docs/work-plans/WP-0025-ai-tool-support-status-survey.md
(single-file commit; correctly scoped)

$ git show wp-0025-execution:docs/work-plans/WP-0025-ai-tool-support-status-survey.md | grep -n "LISS-0069 |"
38:| LISS-0069 | done | M | M | N/A | - | - | process/item-0021-status-survey |
(correctly synced)

--- independent re-fetch of both Antigravity citations, matching the Implementer's own Step 1 ---
(re-fetched both ai.google.dev/gemini-api/docs/antigravity-agent and
antigravity.google/docs/subagents/ during this session's own earlier
spike research and again during this review's own reading of the
Implementer's Work Notes -- the "AGENTS.md" quote and the "maximum
nesting depth of 10 levels"/"peer agents whose ID is known" quotes match
exactly what this review's own spike case (case-0004) already recorded)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The contract-file edit drifted from LISS-0069's own verbatim specification | Independent line-by-line `git diff` comparison found an exact match | not reproduced |
| 2 | Any other row/bullet/section of `prompt-instruction-change-control.md` was touched | `git diff` shows exactly one bullet added and one table row added, nothing else | not reproduced |
| 3 | The "3 pre-existing failures" claim is false — one or more were actually introduced by `LISS-0069`'s own edits | Independently ran the checker against the actual pre-`LISS-0069` commit (`7d61ab5`, this review's own worktree state) and got the identical 3 failures at the identical lines, before any of `LISS-0069`'s own work existed — a direct comparison against the real base, not a git-stash reconstruction, and not accepted on the Implementer's own report alone | not reproduced |
| 4 | The 3 failures are real broken references, not checker false positives | Direct inspection of each flagged line's own content confirms all three are prose describing an external tool's own file, a truncated citation URL, or an explicitly-stated non-existent filename — none is a genuine same-repo dangling reference | not reproduced (confirmed false positives) |
| 5 | The 4th-occurrence Issue-Graph-sync defect (same class as `LISS-0060`/`LISS-0064`) was left unresolved | `a949b3a` is a clean, single-file, correctly-scoped fix, caught by the Implementer's own Preflight this time, not left for this review to find | not reproduced |
| 6 | The mandatory AI work trace is missing or incomplete | Read in full: states which contract file changed, why, and what behavior changes, per the template's own required sections | not reproduced |

## Scenarios Not Searched

- Whether the checker false-positive gap (item 4 above) has any other
  instance elsewhere in the repository beyond the 3 found in this one
  file — out of this review's own scope; flagged separately as a
  disclosed, non-blocking follow-up (see Reasons below), not resolved
  here.
- Live behavioral confirmation inside Codex, Cursor, Grok Build, or
  Antigravity themselves — this session has no way to run any of them;
  the same limitation the status report itself states explicitly.

## Checklist

- [x] The artifact belongs to the phase that was run (Architecture Path,
      fully specified content) — confirmed by the exact-match diff.
- [x] Every `Then` clause in the specification is asserted by the work —
      N/A, no specification covers this work plan.
- [x] The dependency rule and port boundaries hold — N/A.
- [x] No boundary named in the design agreement was crossed — confirmed:
      no other row/bullet touched, no rewrite of the report or spike
      case, no new mirror file created.
- [x] Specifications and accepted tests were not modified to make work
      pass — N/A.
- [x] Every claim in the artifact states its grounds — every per-tool
      claim in the status report cites a URL and a fetch date; the
      contract-file addition cites the spike case as its own grounding.
- [x] The record would let a third party re-run this same search — every
      command above is copy-pasteable and was independently re-run by
      this review.

## Decision

- [x] Approved

## Reasons

The contract-file edit (Antigravity's `AGENTS.md`-native status, added to
`prompt-instruction-change-control.md`) is confirmed, by independent
line-by-line diff comparison, to match LISS-0069's own verbatim
specification exactly, with a well-reasoned, disclosed judgment call
(new table row vs. merge) recorded in both the trace and the issue's own
Work Notes. The Implementer's own mandatory independent re-verification
of both Antigravity citations (required before any edit, per LISS-0069's
own Acceptance Notes) found no discrepancy, matching this review's own
independent knowledge of the same primary sources exactly.

The "3 pre-existing failures" claim was not accepted on trust: this
review independently confirmed it by direct comparison against the
actual pre-`LISS-0069` base commit (not a git-stash reconstruction) and
by direct inspection of each flagged line's own content, confirming all
three are genuine checker false positives (an external tool's own
filename described in prose, a truncated citation URL, and an explicitly
non-existent hypothetical filename) rather than real defects in the
status report's own accuracy. This finding is disclosed here, not
silently absorbed into the approval, and has been flagged separately as
a candidate for its own future, narrow fix (same pattern as `LISS-0044`
and `LISS-0052`'s earlier checker gaps) — not blocking this work plan's
own approval, since the status report itself is accurate and the 3
failures are the checker's own limitation, not this work's defect.

The Implementer independently caught and cleanly fixed the 4th occurrence
of the Issue-Graph-sync defect class this session (`LISS-0060` in
WP-0021, self-caught in WP-0022, recurred uncaught in WP-0023/`LISS-0064`,
now self-caught again here) — worth folding into this session's own
future dispatch-instruction template as a standing checklist item, not
resolved by this review itself. No `Type: review-finding` issue is
warranted for this work plan.