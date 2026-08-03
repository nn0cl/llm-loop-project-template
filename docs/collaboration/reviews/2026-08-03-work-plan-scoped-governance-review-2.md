# Review Record: Work-Plan-Scoped Governance, Follow-Up on Findings 1 and 2

Reviewing persona: Reviewer.
Model / tool: Claude Sonnet 5, via a fresh Claude Code agent session with no
memory of the producing session's reasoning — same reviewing identity as
`2026-08-03-work-plan-scoped-governance-review.md`, which this record answers
and does not edit. Only the two findings from that record and the commit that
claims to fix them are in scope here; the original approval's other
conclusions are re-checked only where the branch could plausibly have moved
under them.

## Constraints (all three must hold)

- [x] **Context separation.** Did not write the fix commit or the new
      Preflight records. Re-derived every claim below independently by
      running commands against the branch myself, not by trusting the fix
      commit's message or the Preflight record's narrative.
- [x] **Deterministic precondition.** All checks below re-run in this
      session, including reproducing my own original evasion against the
      fixed regex and constructing new adversarial cases against it.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below.

## Review Target

- Artifact: branch `process/work-plan-scoped-governance`, commit `9a87e44`
  (PR #10). Confirmed via `gh pr view 10`: `headRefOid` = `9a87e44...`, CI
  check `Repository sanity` = `SUCCESS`.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-03-work-plan-scoped-governance.md`
  (DA-2026-08-03-01) — unchanged, same agreement as the original review.
- Specification: none (governance/process change), unchanged from original.
- Current phase: Architecture Path, documentation/tooling only.
- Producing persona: Implementer, responding to Findings 1 and 2 of the
  original review.
- Reviewing persona / model / tool: Reviewer / Claude Sonnet 5 / Claude Code.
- Approval type: specification-conformance, boundary-conformance,
  evidence-sufficiency.
- Preflight Validation record:
  `docs/collaboration/reviews/2026-08-03-work-plan-scoped-governance-preflight.md`
  (retroactive, written for this fix commit).
- Preflight result: pass (as recorded); independently re-verified below
  rather than accepted on the record's word.

## Deterministic Verification Output

**Diff scope confirmation** — the fix commit touches only what it claims to:

```text
$ git diff 2c6f219 9a87e44 --stat
 .../2026-08-03-work-plan-scoped-governance-preflight.md |  98 +++++++
 scripts/check-contract-consistency.py                    |   7 +-
 2 files changed, 104 insertions(+), 1 deletion(-)

$ git diff 2c6f219 9a87e44 -- docs/collaboration/agreements docs/architecture/adr \
    AGENTS.md CLAUDE.md .github .grok .cursor
(no output — none of these changed)
```

This confirms the fix did not touch anything the original review already
approved; only the two findings' targets moved.

**The regex change itself:**

```diff
-    "Work-plan-level Reviewer (ADR 0014)": r"work.plan.level Reviewer|"
-        r"whole (?:completed )?work plan",
+    # Not just "whole work plan" alone: that phrase can appear with no
+    # connection to review at all. Require "Reviewer" within the same
+    # neighborhood as "whole ... work plan", or the compound phrase
+    # "work-plan-level Reviewer" directly.
+    "Work-plan-level Reviewer (ADR 0014)": r"work.plan.level Reviewer|"
+        r"Reviewer.{0,80}whole (?:completed )?work plan|"
+        r"whole (?:completed )?work plan.{0,80}Reviewer",
```

**Test A — reproducing my original evasion against the fix, verbatim:**

```text
$ # scratch copy: delete every line in CLAUDE.md tying "Reviewer" to "work
$ # plan", leave one unrelated "whole work plan" sentence
$ python3 scripts/check-contract-consistency.py --repo .

mirror parity:
  CLAUDE.md does not state 'Work-plan-level Reviewer (ADR 0014)' (no match
  for /work.plan.level Reviewer|Reviewer.{0,80}whole (?:completed )?work
  plan|whole (?:completed )?work plan.{0,80}Reviewer/)

contract consistency: 1 failure(s)
```

Fails correctly now. Confirmed fixed.

**Test B — new evasion, forward order, unrelated content within the 80-char
window:**

```text
$ # scratch copy: same deletion as Test A, then inject:
$ #   "The Reviewer persona uses a red pen. Incidentally, the whole
$ #    work plan document is fourteen pages long this quarter."
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```

**Test C — new evasion, reverse order, unrelated content within the 80-char
window:**

```text
$ # scratch copy: same deletion, then inject:
$ #   "The whole work plan folder was reorganized. A Reviewer noticed
$ #    the new layout."
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```

**Sanity: the fix does not regress the real branch or a fresh target:**

```text
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```

**Preflight record's cited commit hash — checked for existence:**

```text
$ git cat-file -t 1152e73
fatal: Not a valid object name 1152e73
$ git log --oneline --all | grep 1152e73
(no output)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur / occurs | Result |
|---|---|---|---|
| 1 | The fix does not actually catch my originally-reported evasion (fix is cosmetic, e.g. only in a comment, or the regex has a syntax error that silently no-ops) | Reproduced Test A verbatim against the fixed script: the exact scratch-copy evasion from my first review now produces `mirror parity: CLAUDE.md does not state 'Work-plan-level Reviewer (ADR 0014)'` and a non-zero exit. Fixed. | not reproduced (fix confirmed effective) |
| 2 | The fix regresses the real repository content (the tightened proximity requirement is too strict for how the rule is actually phrased in the nine contract files) | `python3 scripts/check-contract-consistency.py --repo .` on the real branch: `all checks passed`. No regression. | not reproduced |
| 3 | The 80-character proximity window still admits a false negative — "Reviewer" and "whole work plan" occurring near each other but describing unrelated things | **Reproduced**, twice (Test B, forward order; Test C, reverse order). Both pass the checker while containing no actual statement of the work-plan-level Reviewer rule. The fix narrows the evasion surface from "the phrase appears anywhere in the file" to "the two terms happen to sit within 80 characters of each other," which is a real reduction in likelihood but not a closure of the gap. | **reproduced** (residual, narrower) |
| 4 | The retroactive Preflight record misrepresents itself as having existed at submission time, rather than disclosing it was written after the Reviewer's finding | Read the record in full. Its opening line states: "Written after the fact, in response to the Reviewer's finding that this submission skipped it." Its "Known Gap" section states plainly: "This change was submitted for independent review... without a Preflight record — a real process miss, not a judgment call," and explicitly: "this one is written to close that gap for the record, not to pass off a late addition as if it were always there." This is honest disclosure, not backdating. | not reproduced (record is honest) |
| 5 | The Preflight record's evidentiary claims (command output, checks) are fabricated or do not match what the branch actually does | Independently re-ran every check the record claims: Test A's exact evasion output matches what the record quotes almost verbatim; `all checks passed` on working tree and copy-script target confirmed independently; `bash -n` and ADR-existence not independently re-run here (already verified in the original review and nothing touching them changed — see diff-scope confirmation above). One exception: see Finding 3 below. | reproduced as accurate, except one citation |
| 6 | The commit hash the Preflight record cites for "the fixes below" is real and correctly identifies where the fix landed | `git cat-file -t 1152e73` — not a valid object in this repository, at any point in its history (`git log --oneline --all` contains no such hash). The actual fix landed in `9a87e44`. The record's own hash citation does not correspond to any real commit. | **reproduced** (factual error) |
| 7 | The rest of the original review's conclusions (nine-file consistency, ADR-count bump, ADR 0006 exclusion, tradeoff disclosure) could have been disturbed by this commit | `git diff 2c6f219 9a87e44` touches only `scripts/check-contract-consistency.py` and the two new review-directory files. None of the nine contract files, `docs/architecture/adr/*`, `ai-human-scheme.md`, `personas.md`, `design-agreement.md`, `README*.md`, or `QUICKSTART*.md` changed. Nothing from the original review's scope needed re-checking beyond confirming this. | not reproduced (nothing else moved) |

## Scenarios Not Searched

- Whether the 80-character window could be tightened further (e.g., to
  same-sentence) without breaking legitimate phrasing across the nine
  contract files — not attempted; would require testing every current
  legitimate occurrence, which is more effort than this residual finding's
  severity currently justifies.
- Whether a LISS-tracked review-finding issue should have been opened for
  these two findings, matching the precedent set by LISS-0003 for the prior
  round's non-blocking findings, instead of fixing directly on the same
  branch/PR. Not evaluated — a process-consistency question, not a
  correctness one, and this PR has not merged yet, unlike the LISS-0003
  precedent which followed a merge.
- Independent re-verification of `required_files` count, ADR-existence loop,
  and `bash -n` beyond confirming the diff does not touch anything those
  checks cover — deemed unnecessary given the diff-scope confirmation above.

## Checklist

- [x] The artifact belongs to the phase that was run — Minor-Fix-Path-shaped
      correction (regex fix, S-sized; retroactive record, no code behavior
      change beyond the fix), consistent with what the original review
      suggested.
- [x] Every `Then` clause is asserted — N/A, no application specification.
- [x] The dependency rule and port boundaries hold — N/A, no code beyond the
      one script changed; no port/boundary touched.
- [x] No boundary named in the design agreement was crossed — confirmed via
      diff-scope check: no spec, ADR, port, data model, or architecture
      boundary changed.
- [x] Specifications and accepted tests were not modified — N/A.
- [x] Every claim in the artifact states its grounds — mostly true; **one
      exception found and named** (Finding 3, the `1152e73` citation).
- [x] The record would let a third party re-run this same search — every
      command above is reproducible verbatim.

## Decision

- [x] **Approved** — specification-conformance, boundary-conformance, and
      evidence-sufficiency, with two findings carried forward as tracked,
      non-blocking follow-up (one substantially mitigated, one new and minor).

## Reasons

**Why approved.** Both of the original review's findings were addressed in
good faith, not cosmetically. Finding 1's exact reported evasion is now
caught — verified by reproducing my own attack verbatim against the fixed
regex and watching it fail correctly. Finding 2's Preflight record is honest
about being retroactive and names the gap as a real process miss rather than
presenting a late addition as routine — exactly what I asked for, and
independently confirmed against the record's own text, not just its framing.
Nothing else the original review approved was disturbed: the diff is
confined to the checker script and the two new review-directory documents.

**Why not rejected, despite two remaining issues.** Finding 3 (Test B/C, the
narrower residual proximity-based evasion) is real, but it is a much smaller
surface than what it replaced: before the fix, any unrelated occurrence of
"whole work plan" anywhere in a several-hundred-line document would mask a
genuine gap; after the fix, only a coincidental or contrived co-occurrence of
"Reviewer" and "whole work plan" within an 80-character window does. This is
the same category of "presence, not meaning" limitation the script's own
docstring already discloses as structural (unsolvable by regex alone,
belonging to "the Reviewer persona" to catch by reading) — the fix moved this
specific rule from "clearly unsound" to "as sound as every other entry in
`EXTRA_MIRRORED_RULES` already was," not from "sound" to "unsound." It is
worth a future hardening pass (e.g., anchoring to sentence boundaries), but
holding this PR hostage to a residual instance of an already-accepted,
already-disclosed general limitation would be inconsistent with how every
other mirrored rule in this same script is already scoped.

Finding 6 (the nonexistent `1152e73` commit hash in the Preflight record) is
a genuine citation error and, in a document whose entire purpose is
evidentiary precision, worth taking seriously — but it is isolated (checked:
the hash appears exactly once, nowhere else in the changed files), does not
affect any of the actual reproducible command output in the same record
(independently re-verified above), and does not misstate the state of the
real branch (which is at `9a87e44`, correctly identified everywhere else).
Read most charitably, it looks like a leftover reference to an intermediate,
never-created commit from drafting. It should be corrected — to `9a87e44`,
or removed — but a single wrong hash in an otherwise independently
verified record is a documentation defect, not evidence that the fix itself
is unsound.

## Findings (tracked, non-blocking)

**Finding 3 (residual, narrower version of original Finding 1) — proximity
window still admits an unrelated co-occurrence.**

- File: `scripts/check-contract-consistency.py`, `EXTRA_MIRRORED_RULES`.
- The `.{0,80}` window between "Reviewer" and "whole ... work plan" does not
  require the two to be part of the same clause or sentence. Reproduced with
  two constructed sentences (Test B, Test C above) that satisfy the pattern
  without ever stating the work-plan-level Reviewer rule.
- Suggested correction (optional, low priority given the reduced surface):
  anchor within a single sentence (e.g., split on `[.!?]` before matching,
  or require no sentence-ending punctuation between the two terms) rather
  than a raw character window.

**Finding 6 — nonexistent commit hash cited in the Preflight record.**

- File:
  `docs/collaboration/reviews/2026-08-03-work-plan-scoped-governance-preflight.md`,
  line 12-14: "`1152e73` and later carry the fixes below."
- `1152e73` is not a valid git object in this repository at any point in its
  history. The actual fix landed in `9a87e44`.
- Suggested correction: replace `1152e73` with `9a87e44`, or remove the
  intermediate-commit framing if it does not correspond to anything real.

## Falsification Criteria Check (from the covering design agreement)

Re-checked, not just carried over: none of the four falsification criteria
in the design agreement are newly met by this commit (no stale per-phase
Reviewer language reintroduced, no self-review of a contract-file change, no
split human checkpoint, no missing tradeoff disclosure) — the commit does not
touch any file where those criteria could be tripped.
