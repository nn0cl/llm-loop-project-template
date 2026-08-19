# Review Record: WP-0011 — Deterministic Gate for Open Review-Finding Issues

## Constraints (all three must hold)

- [x] **Context separation.** Reviewed from an independently checked-out
      detached worktree (`git worktree add --detach /tmp/verify-wp0011
      process/ci-open-finding-gate`, resolved to `d53f6f4`), produced by a
      separately spawned Implementation-group agent (`agentId
      adc03600efbdf5f54`).
- [x] **Deterministic precondition.** `python3 scripts/check-contract-consistency.py`
      re-run independently; and — going beyond re-reading the Implementer's
      pasted synthetic tests — this review constructed its own independent
      synthetic failure and pass cases, using the real `LISS-0003`
      (`Status: resolved`) scenario named in the design agreement's own
      spike, injected into a copy of the actual `WP-0003` file rather than
      a fabricated fixture. See below.
- [x] **Falsification burden.** Failure scenarios below.

## Review Target

- Artifact: commit `d53f6f4` on top of `6161241`, branch
  `process/ci-open-finding-gate`, implementing LISS-0039 under WP-0011.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-19-ci-open-finding-gate.md`
  (`DA-2026-08-19-03`)
- Specification: none.
- Current phase: Preflight passed; work-plan-level Review.
- Producing persona: Implementer (Implementation group, spawned agent
  `adc03600efbdf5f54`).
- Reviewing persona / model / tool: Reviewer, Design & Review group
  standing session, Claude Sonnet 5 via Claude Code.
- Approval type: **Specification conformance**, **Phase correctness**,
  **Boundary conformance**, **Evidence sufficiency**.
- Preflight result: pass (re-verified below).

## Deterministic Verification Output

```text
$ git worktree add --detach /tmp/verify-wp0011 process/ci-open-finding-gate
Preparing worktree (detached HEAD d53f6f4)

$ cd /tmp/verify-wp0011 && python3 scripts/check-contract-consistency.py
contract consistency: all checks passed

Independent synthetic-failure test, using the REAL LISS-0003 scenario named
in DA-2026-08-19-03's own spike (not a fabricated fixture, not reusing the
Implementer's own test artifacts):

$ cp -r /tmp/verify-wp0011 /tmp/verify-wp0011-synth
$ python3 -c "... inject '| LISS-0003 | resolved | injected synthetic test row |' \
    into WP-0003's real (already-closed, Date: 2026-08-18) findings table ..."
injected
$ cd /tmp/verify-wp0011-synth && python3 scripts/check-contract-consistency.py
open findings gate:
  docs/work-plans/WP-0003-coordinator-message-correction.md lists LISS-0003
  in its Work-Plan Review findings table, but
  docs/issues/LISS-0003-code-path-filter-and-disclosure-history.md states
  Status: 'resolved' -- neither 'closed' nor 'wont_do'
contract consistency: 1 failure(s)
(correctly caught)

Independent synthetic-pass test (same injected row, flag set to false):
$ python3 -c "... set block_work_plan_done_on_open_findings = false in the \
    same synthetic copy's loop-settings.toml ..."
flag set to false
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
(correctly stands down when the setting is disabled -- proves the flag is
actually read, not hardcoded)

$ rm -rf /tmp/verify-wp0011-synth
(cleanup; the real reviewed worktree at /tmp/verify-wp0011 was never
modified by this test, only its copy)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The check does not actually catch a real open finding in a closed work plan | Constructed an independent test using the real `LISS-0003` scenario, injected into the real (already Director-closed) `WP-0003` file's findings table — caught correctly, with an accurate message naming both files and the actual status. | not reproduced |
| 2 | The `[findings].block_work_plan_done_on_open_findings` flag is not actually read (hardcoded true or false) | Independently flipped it to `false` in the same synthetic fixture that triggered a failure with it `true`; the failure disappeared. Proves the flag is read, not hardcoded either way. | not reproduced |
| 3 | The check infers a finding-to-work-plan link from free text instead of the structured findings table | Read `check_open_findings_gate`'s code: it anchors strictly on `^\| (LISS-\d{4}) \|` rows under the literal `## Work-Plan Review` heading — no free-text search. | not reproduced |
| 4 | The "closed" work-plan signal is too loose (e.g. treats a placeholder as a real date) | Read `_block_work_plan_done_on_open_findings` and the date-match logic: requires `\d{4}-\d{2}-\d{2}` — `_pending Director action_` does not match, correctly excluding every still-open work plan. Confirmed no false positive on the current, clean `HEAD` run, where several work plans (WP-0007, WP-0011 itself, etc.) are not yet Director-closed. | not reproduced |
| 5 | The check was built as a separate script instead of extending `scripts/check-contract-consistency.py` | Diff confirms the only functional change is inside that one script; no new file. | not reproduced |
| 6 | The module docstring was not updated to reflect the ninth check | Docstring's numbered list now includes item 9, "Open findings gate," matching the actual function added. | not reproduced |

## Scenarios Not Searched

- Multiple simultaneous open findings across several closed work plans in
  one run (only a single-injection case was tested) — judged low-risk
  given the per-row loop structure has no shared state between iterations
  that a multi-row case would exercise differently.

## Checklist

- [x] Artifact belongs to the phase run (Architecture Path).
- [x] Acceptance criteria in `DA-2026-08-19-03`'s Plan table satisfied.
- [x] No boundary crossed (no `findings-reuse.md` edit; `LISS-0003` not
      retroactively modified; no separate mechanism built).
- [x] Every claim states its grounds.
- [x] Record lets a third party re-run this same search — the exact
      injection method (real file, real scenario) is reproducible against
      commit `d53f6f4`.

## Decision

- [x] Approved

## Reasons

- Independently constructed, not merely re-read, synthetic failure and pass
  cases both behaved correctly, using a real repository scenario rather
  than an invented one.
- The check stays within the anchored/structural-comparison design
  discipline this script's other checks (and its own docstring's
  documented history of rejecting meaning-inference) require.
- No false positive against the current, real, mixed-state repository
  (several closed and several still-open work plans coexist on `HEAD`).

This review does not itself close WP-0011 — Director action, Backlog
layer.
