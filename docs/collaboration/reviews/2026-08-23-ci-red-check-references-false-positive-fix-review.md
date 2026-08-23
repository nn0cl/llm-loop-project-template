# Review Record: CI-Red `check_references` False-Positive Fix

Minor Fix Path separate-context Reviewer confirmation, per `CLAUDE.md`'s
"Minor Fix Path" and "Bug Triage" (`docs/architecture/agent-quickstart.md`)
sections.

## Constraints (all three must hold)

- [x] **Context separation.** Fresh session, no prior chat memory of this
      fix or how it was produced. Nothing read from a chat transcript or
      trusted from any agent's own description of the fix — every claim
      below is independently re-derived by this session, reading the actual
      current file content and running the actual commands, in a worktree
      isolated from whoever authored commit `403ff02`.
- [x] **Deterministic precondition.** `python3 scripts/check-contract-consistency.py`
      re-run independently, twice: once against a freshly created detached
      `git worktree add` checkout of `origin/main` with only the fixed
      script copied in (not the Implementer's own pasted output, not this
      review's own branch history), and once more after a synthetic
      regression probe was added and removed.
- [x] **Falsification burden.** Searched, with constructions different from
      the fix's own commit message: a repo-wide grep for coincidental reuse
      of the 3 newly allowlisted exact strings outside their intended
      target; a synthetic genuinely-broken reference injected into a
      different document than the fix's own regression test used, to
      confirm the general check is not weakened; a read of the exact-match
      code path to rule out substring/regex over-matching; and independent
      re-reading of the cited 2026-08-20 review record to confirm its
      content actually supports the fix's docstring claims.

## Review Target

- Branch: `process/fix-ci-red-checker-false-positives`, commit `403ff02`
  (single commit, on top of `main` at `74004cc`).
- File touched: `scripts/check-contract-consistency.py` only.
- Problem: CI on `main` (`74004cc`) is red — `check_references` flags 3
  lines in `docs/architecture/ai-tool-support-status.md` (67, 91, 110) as
  dangling references, claimed as false positives.
- Producing persona: Implementer (Minor Fix Path, per the commit's own
  design note: planning size S, no specification/ADR/port/data-model/
  boundary change, resolved in one attempt).
- Reviewing persona / model / tool: Reviewer, Claude Sonnet 5 via Claude
  Code, separate context/session from whoever authored `403ff02`.
- Approval type: boundary-conformance (does the fix stay inside its
  claimed narrow scope) and evidence-sufficiency (are the 3 targets
  genuinely non-local, and does the fix genuinely not weaken the general
  check).

## Scope Conformance

```text
$ git fetch origin && git log --oneline -1
74004cc Merge branch 'process/item-0021-status-survey' (item-0021: AI tool support status survey)

$ git diff 74004cc..process/fix-ci-red-checker-false-positives --name-status
M       scripts/check-contract-consistency.py

$ git log 74004cc..process/fix-ci-red-checker-false-positives --stat
403ff02e1afe58e77182602384a3802696034986 ... (single commit)
 scripts/check-contract-consistency.py | 38 +++++++++++++++++++++++++++++++++--
 1 file changed, 36 insertions(+), 2 deletions(-)
```

One file, one commit. Reading the full diff confirms it is exactly: a new
module-level `NON_LOCAL_PROSE_MENTIONS = {...}` set with 3 exact strings,
each with an inline comment naming the reason; one new `if target in
NON_LOCAL_PROSE_MENTIONS: continue` line inside `check_references`,
placed alongside (not replacing) the existing `EXAMPLE_DOCUMENT_NAMES`
check; and a docstring update on `check_references` naming the new set.
No other function, regex, heuristic, or file is touched. This does not
touch any specification, ADR, port, data model, or architecture boundary
— confirmed both by the diff itself (checker-script-only, additive
allowlist) and by checking `docs/collaboration/prompt-instruction-change-
control.md`'s own "Agent Operating Contract Files" list, which does not
include `scripts/*.py` — so this fix is correctly scoped as Minor Fix
Path / Bug Triage, not an Architecture Path escalation.

## Deterministic Verification — Fresh `origin/main` Checkout

```text
$ rm -rf /tmp/reviewer-main-check
$ git worktree add --detach /tmp/reviewer-main-check origin/main
Preparing worktree (detached HEAD 74004cc)
HEAD is now at 74004cc Merge branch 'process/item-0021-status-survey' ...

$ cd /tmp/reviewer-main-check && git log --oneline -1
74004cc Merge branch 'process/item-0021-status-survey' (item-0021: AI tool support status survey)

--- baseline: unfixed main is genuinely red ---
$ python3 scripts/check-contract-consistency.py --repo .
references:
  docs/architecture/ai-tool-support-status.md:67 names '.cursor/worktrees.json', which does not exist
  docs/architecture/ai-tool-support-status.md:91 names 'github.com/xai-org/grok-build/.../16-subagents.md', which does not exist
  docs/architecture/ai-tool-support-status.md:110 names 'ANTIGRAVITY.md', which does not exist
contract consistency: 3 failure(s)
$ echo $?
1

--- fixed: branch's script copied onto real main content ---
$ git show process/fix-ci-red-checker-false-positives:scripts/check-contract-consistency.py > scripts/check-contract-consistency.py
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
$ echo $?
0
```

Confirms the fix resolves CI red against real `origin/main` content, not
merely relative to the fix's own branch history.

## Falsification Search

| # | Failure scenario searched for | Method (independent of the fix's own commit message) | Result |
|---|---|---|---|
| 1 | The allowlist coincidentally suppresses a genuine dangling reference elsewhere in the repo that happens to share one of the 3 exact registered strings | `grep -rn` for each of the 3 exact strings across the whole repository (including `RECORD_DIRS`-exempt paths, not just current-contract docs) | not reproduced — see below |
| 2 | The general `check_references` logic is weakened for real cases (the fix accidentally broadens what gets skipped) | Injected a synthetic, genuinely broken reference (`docs/architecture/reviewer-synthetic-check-9f3a2b.md` — a filename not used by the fix's own regression test) into `docs/architecture/testing-strategy.md`, a current-contract file outside `RECORD_DIRS`, and re-ran the checker | not reproduced — still caught, exit 1, exactly 1 failure reported at the injected line |
| 3 | The new allowlist match is a substring/regex match rather than exact string equality, which could over-match unrelated targets | Read the code path directly (`scripts/check-contract-consistency.py:541`): `if target in NON_LOCAL_PROSE_MENTIONS: continue` — `NON_LOCAL_PROSE_MENTIONS` is a `set` of complete strings, membership test is exact equality, not `re.search`/substring | not reproduced — confirmed exact-match only |
| 4 | The fix's docstring/comment claims (e.g. "confirmed against `docs/collaboration/reviews/2026-08-20-wp-0025-...`") misstate what that review record actually says | Independently read `docs/collaboration/reviews/2026-08-20-wp-0025-ai-tool-support-status-survey-review.md` in full | not reproduced — that record's own "Deterministic Verification Output" section independently re-ran the checker, got the identical 3 failures at the identical lines, and its own "direct inspection of each of the 3 failures" explicitly confirms: line 67 describes Cursor's own external config file in prose; line 91 is a citation URL with a literal `...` elision; line 110 explicitly states `ANTIGRAVITY.md` was searched for and not found. The fix's comments accurately restate this record, not more than it supports |

### Probe #1 detail — repo-wide grep for the 3 exact strings

All non-`RECORD_DIRS` occurrences of the 3 strings, across the whole
repository:

- `.cursor/worktrees.json`: only in `docs/architecture/ai-tool-support-
  status.md:67` (the fix's intended target). Every other occurrence is
  inside `docs/collaboration/reviews/`, `docs/work-plans/`, `docs/issues/`,
  or `docs/spike/` — all `RECORD_DIRS`, already unconditionally exempt
  from `check_references` before this fix (`rel.startswith(RECORD_DIRS)`
  at line 491), so the new allowlist entry changes nothing there.
- `github.com/xai-org/grok-build/.../16-subagents.md`: same pattern — the
  intended target at line 91, plus one occurrence in `docs/architecture/
  adr/0017-...md` carrying an `https://` prefix, which was already exempt
  via the pre-existing `target.startswith(("http://", "https://", ...))`
  skip (line 498) before this fix existed. The remaining occurrences are
  all inside `RECORD_DIRS`.
- `ANTIGRAVITY.md`: only in `docs/architecture/ai-tool-support-status.md:
  110` (the intended target) outside `RECORD_DIRS`.

No occurrence of any of the 3 strings, anywhere in the repository, is a
document that both (a) is subject to `check_references` (i.e. outside
`RECORD_DIRS`) and (b) uses the string as a claim that a same-repo file
must exist. The allowlist entries suppress exactly the 3 lines they were
registered for and nothing else currently in the repository.

### Probe #2 detail — synthetic broken-reference regression, different construction

```text
$ printf '\nSee `docs/architecture/reviewer-synthetic-check-9f3a2b.md` for details.\n' >> docs/architecture/testing-strategy.md
$ python3 scripts/check-contract-consistency.py --repo .
references:
  docs/architecture/testing-strategy.md:165 names 'docs/architecture/reviewer-synthetic-check-9f3a2b.md', which does not exist
contract consistency: 1 failure(s)
$ echo $?
1

$ git checkout -- docs/architecture/testing-strategy.md
$ git status --porcelain
 M scripts/check-contract-consistency.py
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
$ echo $?
0
```

(The one remaining `M` is this review's own intentional copy of the fixed
script into the throwaway `origin/main` worktree, not a leftover from the
synthetic probe. `docs/architecture/testing-strategy.md` itself is
confirmed restored to its exact original content.) The fix's own
regression test (per its commit message) used a different filename,
`docs/architecture/this-file-does-not-exist-regression-check.md`; this
review deliberately used a different filename and a different host
document than that test, per this task's own falsification requirement,
and got the same result: the general check still fires.

## Scenarios Not Searched

- Behavior of `check_references` on operating systems other than the
  sandboxed macOS/Linux environment this review ran in (not expected to
  differ; `os.path.exists` and `os.walk` are not platform-conditional in
  this script).
- Whether a future edit to `docs/architecture/ai-tool-support-status.md`
  that moves or rewords lines 67/91/110 would silently stop matching the
  registered exact strings and reopen the false positive — this is an
  inherent, accepted property of exact-string registration (the same
  property `EXAMPLE_DOCUMENT_NAMES` already has), not a new gap this fix
  introduces, and the module's own docstring explains why a shape-based
  heuristic was rejected instead.

## Observation (not a blocking condition)

The fix's self-review is recorded entirely inside the commit message
(`403ff02`), not as a separate file under `docs/collaboration/traces/` or
using `docs/templates/self-review.md`'s short form as a standalone
document. A commit message is a durable, auditable repository artifact
(satisfies "every decision produces a document" — it is not a session-
transcript-only claim), and `scripts/check-contract-consistency.py` is
not an agent-operating-contract file under `docs/collaboration/prompt-
instruction-change-control.md`'s own definition, so no trace is
independently required by that document either. This is noted for the
record, not treated as a defect.

## Decision: **Approved**

The fix resolves the documented CI-red defect, verified independently
against real `origin/main` content (exit 0, "all checks passed", not
merely relative to the fix's own branch history). Scope is confirmed
minimal: one file, one function's allowlist, no specification/ADR/port/
data-model/architecture-boundary change — Minor Fix Path was the correct
path. The falsification search, using constructions different from the
fix's own commit message, found no coincidental over-suppression
anywhere in the current repository, confirmed the allowlist match is
exact-string (not pattern-based), confirmed the general check still
catches a genuinely broken reference injected elsewhere, and confirmed
the fix's citation of the 2026-08-20 review record accurately reflects
that record's own content. No condition is attached beyond the
non-blocking observation above.
