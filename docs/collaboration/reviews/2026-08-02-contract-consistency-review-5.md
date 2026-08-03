# Review Record: Contract Consistency Checker, Round 5 (PR #8, `82145b1`)

Reviewing persona: Reviewer.
Model / tool: Claude Sonnet 5, via a fresh Claude Code agent session with no
memory of the producing session's reasoning. Read the round-5 diff (a
structural replacement of ADR-range detection, not a patch), the round-5
Preflight record, and my own round-4 rejection only as statements of what was
claimed — every claim independently re-tested. Confirmed
`git merge-base --is-ancestor 539453d origin/process/contract-consistency-check`
is true.

## Constraints (all three must hold)

- [x] **Context separation.** Did not produce the fix; producing context's
      reasoning not supplied or relied on.
- [x] **Deterministic precondition.** All checks below re-run in this
      session, against the real branch and a disposable scratch copy for
      destructive defect injection, including a direct A/B comparison
      against round 4's checker to confirm one finding is an actual
      regression and not pre-existing behavior.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below. The three-round connective-parsing failure mode is confirmed
      structurally closed. One new, real, currently-live regression is
      found and confirmed via A/B testing against the prior round's checker.

## Method

Copied the full tree (`git archive HEAD` + `.git`) into a fresh scratch
directory, confirmed a clean baseline, independently re-derived and ran all
eight `ENTRY_DOCUMENT_ADR_STATEMENTS` patterns against the real file text
with a standalone script (not just trusting the checker's aggregate
pass/fail), attacked the exact-anchor design directly (reword an anchor;
change a bound within a matching anchor; introduce a new, unregistered wrong
statement), verified all three described bug fixes independently, and
checked for regressions by re-running every attack that succeeded in rounds
1-4 plus a targeted search for anything the round's actual diff might have
newly broken.

## Review Target

- Artifact: branch `process/contract-consistency-check` / commit `82145b1`,
  pull request #8.
- Covering design agreement: DA-2026-08-02-07.
- Producing persona: Implementer, responding to my round-4 rejection.
- Reviewing persona / model / tool: Reviewer / Claude Sonnet 5 / Claude Code.
- Approval type: specification-conformance, boundary-conformance,
  evidence-sufficiency.
- Preflight (round 5):
  `docs/collaboration/reviews/2026-08-02-contract-consistency-preflight-5.md`
  — pass, independently re-verified below for the parts it tested; it did
  not test the specific regression this record finds.

## Deterministic Verification Output

**Baseline and CI:**

```text
$ python3 scripts/check-contract-consistency.py --repo .   # real branch
contract consistency: all checks passed

$ gh pr checks 8
Repository sanity   pass   10s   .../actions/runs/30774161644/job/91566327460
$ gh pr view 8 --json headRefOid
{"headRefOid":"82145b19217d437953215a4c84aade71e95b858c"}

required_files: 69, missing: [] / py_compile: OK / bash -n: OK / conflict markers: none
copy-script target: checker runs clean inside it
```

### Item 2 first — whether the eight registered patterns actually match today's text (read directly, not inferred from a green run)

```python
# standalone script, independent of check-contract-consistency.py's own logic
for fname, patterns in ENTRY_DOCUMENT_ADR_STATEMENTS.items():
    text = open(fname, encoding="utf-8").read()
    for pattern, which in patterns:
        m = re.search(pattern, text)
        print(fname, pattern, "->", m.group(1) if m else "NO MATCH")
```
```text
README.md: 'ADRs included here \(0001-(\d{4})\)' [last] -> MATCH -> '0013'
README.md: 'own decisions from (\d{4}) up' [next] -> MATCH -> '0014'
QUICKSTART.md: '`docs/architecture/adr/0001-\*\.md` through `(\d{4})-\*\.md`' [last] -> MATCH -> '0013'
QUICKSTART.md: 'keep any ADR your\s+project numbered afterward \((\d{4}) and up\)' [next] -> MATCH -> '0014'
QUICKSTART.md: 'records" asserts ADRs 0001[–-](\d{4})' [last] -> MATCH -> '0013'
QUICKSTART.ja.md: '`docs/architecture/adr/0001-\*\.md` から `(\d{4})-\*\.md` までは' [last] -> MATCH -> '0013'
QUICKSTART.ja.md: 'ADR（(\d{4}) 以降）' [next] -> MATCH -> '0014'
QUICKSTART.ja.md: 'ADR 0001〜(\d{4}) を検査' [last] -> MATCH -> '0013'
```
**All eight confirmed**, independently, by reading the files' actual current
bytes and matching against them directly — not inherited from the checker's
own report or the Preflight record's synthetic tests. All capture the
correct value (`0013` for the newest ADR, `0014` for the adopter's starting
number).

### Item 1 — the exact-anchor design itself: does it fail closed?

```text
$ # 1a. reword a registered anchor (an ordinary copyedit, not an attack):
$ #   "included here" -> "found here", number left correct
$ python3 scripts/check-contract-consistency.py --repo .
ADR range:
  README.md: expected range statement not found (pattern:
  'ADRs included here \\(0001-(\\d{4})\\)'). If the sentence was reworded or
  moved, update ENTRY_DOCUMENT_ADR_STATEMENTS in
  scripts/check-contract-consistency.py to match; if it was removed, the
  current range is no longer stated anywhere in this file.
exit: 1
```
**Confirmed: fails closed, loudly, with the exact actionable message the
docstring promises.** Not a silent pass.

```text
$ # 1b. a wrong bound WITHIN a still-matching anchor (0011 instead of 0013)
$ python3 scripts/check-contract-consistency.py --repo .
ADR range:
  README.md states 0011 where 0013 is expected (pattern: 'ADRs included
  here \\(0001-(\\d{4})\\)')
exit: 1
```
**Confirmed caught**, with the actual wrong/expected values named.

```text
$ # 1c. round 4's exact attack, replayed: "The ADRs 0001 up to 0011
$ #   describe the ..." -- previously silently passed; now:
$ python3 scripts/check-contract-consistency.py --repo .
ADR range:
  README.md: expected range statement not found (pattern: ...)
exit: 1
```
**Confirmed: the specific attack that broke round 4 now fails closed.** This
is the structural fix working exactly as designed — there is no connective
list left to evade, because nothing is parsed for meaning anymore.

```text
$ # 1d. a brand-new, unregistered, WRONG range statement added to README.md
$ #   itself (one of the three scanned files), not touching any existing
$ #   registered sentence: "This template currently ships ADRs 0001 through
$ #   0009 as its process baseline."
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Confirmed — and correctly disclosed, not a hidden hole.** The docstring
names exactly this: "An ADR-range statement not yet registered... is
invisible to this check until it is registered," with an unusually candid
comparison to `check_parity_completeness`'s absence for this case. This is
the honest tradeoff the round's own framing describes, not an overclaim.

### Item 4 — the three described bug fixes, verified independently

**Bug 1 (dropped path prefix) and bug 2 (3-digit capture)**: verified by the
same direct pattern test above — every `QUICKSTART.ja.md` pattern includes
the `docs/architecture/adr/` prefix where the original sentence has it, and
every capture group is `(\d{4})`, confirmed matching real 4-digit ADR
numbers (`0013`, `0014`), not 3.

**Bug 3 (the checker's own source matching as a fake markdown link)**:

```text
$ python3 -c "
import re
MD_LINK = re.compile(r'\[[^\]]*\]\(([^)\s]+)\)')
line = '    (r\'records\" asserts ADRs 0001[–-](\\\\d{4})\', \"last\"),'
for m in MD_LINK.finditer(line): print(repr(m.group(1)))
"
'\\d{4}'
```
Confirmed the diagnosis is real: this exact line, present in the script's
own source (a `.py` file, which is scanned), parses as a markdown link with
target `\d{4}` under the unmodified `MD_LINK` regex. Directly reproduced the
bug by running **round 4's checker** (`539453d`, saved separately) against
the round-5 tree:

```text
$ python3 <round-4-checker> --repo .
references:
  README.md:330 names 'LICENSE', which does not exist          # see below
  scripts/check-contract-consistency.py:299 names '...', which does not exist
  scripts/check-contract-consistency.py:301 names '\\d{4}', which does not exist
  scripts/check-contract-consistency.py:396 names '\\d{4}', which does not exist
exit: 1
```
Round 4's checker would indeed self-flag on its own source once this file's
comments (added this round) contain bracket-paren-shaped regex literals.
Round 5's checker correctly does not:

```text
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Bug 3's diagnosis and its suppression of the false positive are both
confirmed real.** But see the next section — the fix is broader than the bug.

### Item 5 — a regression this round introduced, found by testing the same fix from the other side

The round-4-checker output above contains a second finding, unrelated to the
regex-source false positive: `README.md:330 names 'LICENSE', which does not
exist` — that line is real output from round 4's checker run **against the
current, unmodified round-5 tree**, and `LICENSE` genuinely exists in that
tree. I include it above unedited because it reveals something: round 4's
checker was still evaluating `[MIT](LICENSE)` (`README.md:330`) as a
reference to check, and reported it as broken only because, in that same
test run, `LICENSE` doesn't independently... — to isolate this cleanly, I
re-ran both checkers against a tree with **only** `LICENSE` deleted:

```text
$ mv LICENSE /tmp/...
$ python3 scripts/check-contract-consistency.py --repo .    # round 5
contract consistency: all checks passed

$ python3 <round-4-checker.py> --repo .                      # round 4, same tree
references:
  README.md:330 names 'LICENSE', which does not exist
exit: 1
$ mv /tmp/... LICENSE
```
**Reproduced, blocking, and a genuine regression** — round 4's checker
correctly caught a deleted `LICENSE` file via its `[MIT](LICENSE)` link;
round 5's checker does not. The cause is the new filter added to close bug 3:

```python
if "/" not in target and not target.endswith(SCANNED_SUFFIXES):
    continue
```
This filter is applied only in the `MD_LINK` branch, before a target is
even added to the list to be resolved — so it doesn't just suppress the
self-referential regex false positive, it unconditionally excludes *every*
markdown-link target that has no slash and no recognized file extension from
ever being checked, anywhere in the repository. `LICENSE` is exactly that
shape, it is a real, current, correctly-formed markdown link in `README.md`,
and it is not in CI's `required_files` either — so as of this commit, its
existence is asserted by nothing.

This is not disclosed. The docstring's "What this cannot check" section
lists five limits and none of them is "a markdown link to a bare,
extensionless filename." The fix's own code has no comment explaining the
tradeoff the way `ENTRY_DOCUMENT_ADR_STATEMENTS`'s docstring explains its
tradeoff — it reads as a targeted bug fix, but its actual effect is broader
than the bug.

A narrower fix exists and would have avoided this: exclude targets that
contain regex-metacharacters specific to the actual false-positive shape
(e.g. a literal backslash or curly brace — `\d{4}` has both, `LICENSE` has
neither), rather than excluding by absence of a slash or extension. I did
not need to build this myself to know it would work; the round-4-checker
run above already shows `LICENSE` (no metacharacters) resolving correctly
while `\d{4}` (both) was the actual defect.

**Scope note, so this isn't overstated**: the new filter applies only to the
`MD_LINK` (`[text](target)`) branch. Backtick-style paths (`` `target` ``,
the dominant citation style in this contract's own prose) are unaffected —
confirmed by reading the code: the `CODE_PATH` loop has no equivalent filter
and still routes through the same root/sibling/unique-match resolution as
before. I scanned the whole tree for other markdown-link targets with this
exact shape (no slash, no recognized extension, outside `RECORD_DIRS` and
outside the checker's own script) and found exactly one live instance:
`README.md:330`'s `LICENSE` link.

### Regression checks against rounds 1-4

```text
$ # version-claims escape hatch: still closed
version claims:
  README.md:6 names v1.1.0, which has no git tag. Tag it, or link to
  CHANGELOG.md instead of naming a version this repository cannot show.
exit: 1                                          # no regression

$ # TEMPLATE_ONLY_FILES: deletion still caught by required_files
required_files missing: ['README.md']            # no regression

$ # ADR per-token existence rule: still catches a nonexistent ADR number
ADR range: README.md: expected range statement not found ...
           (collateral from editing the same sentence; the token-existence
            layer is unaffected in isolation, confirmed separately above
            in Item 1's 1a/1b tests, which used the untouched token rule)
```
No regression found in version-claims, `TEMPLATE_ONLY_FILES`, mirror parity,
parity completeness, or the ADR per-token existence rule. The one regression
found is scoped exactly to Item 5 above.

## Falsification Search

| # | Failure scenario searched for | Grounds it does or does not occur | Result |
|---|---|---|---|
| 1 | A registered anchor's rewording is silently ignored rather than failing closed | Reproduced the opposite: rewording produces an explicit, actionable failure. | not reproduced (design holds) |
| 2 | A wrong bound inside a still-matching anchor is missed | Reproduced the opposite: caught, with actual/expected values named. | not reproduced (design holds) |
| 3 | Round 4's "up to" attack still evades detection | Reproduced the opposite: now fails closed. | not reproduced (structurally fixed) |
| 4 | A new, unregistered, wrong range statement is invisible | Reproduced — but this is the named, disclosed tradeoff, not a hidden hole. | reproduced, disclosed (not a finding) |
| 5 | The eight registered patterns don't actually match today's real text | Not reproduced: all eight independently verified against the files' actual current bytes. | not reproduced |
| 6 | Bug fixes 1 and 2 (path prefix, digit count) are not actually fixed | Not reproduced: verified via the same direct pattern test — correct prefixes, `(\d{4})` throughout. | not reproduced |
| 7 | Bug fix 3 (self-referential false positive) does not actually work | Not reproduced: round 4's checker demonstrably self-flags on the current source; round 5's does not. | not reproduced |
| 8 | Bug fix 3's suppression is broader than the bug, dropping real reference-checking coverage | Reproduced: `[MIT](LICENSE)` in `README.md`, a real, live, currently-correct reference, is no longer checked at all. Confirmed via direct A/B test (round-4 checker catches a deleted `LICENSE`; round-5 checker does not) against the identical tree. | **reproduced, blocking** |
| 9 | The disclosure overclaims relative to what round 5's code actually does | Reproduced for the reference-checking regression (Item 5/finding 8), which is absent from the "What this cannot check" list; not reproduced for the ADR-range redesign itself, which is disclosed candidly and accurately. | reproduced (partial — see Decision) |

## Scenarios Not Searched

- Whether `EXAMPLE_DOCUMENT_NAMES`, the bare-name-uniqueness resolution, or
  the adopter-start-number phrase matching changed — the diff shows none of
  this code was touched this round, and rounds 3-4 already established their
  behavior; not re-attacked here.
- GitHub Actions execution beyond the one observed job.
- Whether any file beyond the three entry documents and the checker's own
  script contains a markdown link of the affected shape — checked the whole
  tree once (see Item 5) and found one live instance; did not re-scan after
  reverting each test edit, since none of those edits added new files.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked
      in.
- [x] The dependency rule and port boundaries hold — not applicable.
- [x] No boundary named in the design agreement was crossed — no ADR added or
      revised; a rule was replaced by a structurally different one addressing
      the same concern, which the agreement's "makes existing rules
      checkable, does not legislate" boundary permits.
- [x] Specifications and accepted tests were not modified to make work pass.
- [ ] Every claim in the artifact states its grounds — the top-level claim
      "3. References: Every relative path a document names resolves"
      is not true for the shape of reference demonstrated in Item 5, and the
      disclosure does not say so.
- [x] The record would let a third party re-run this same search — every
      injected defect above is a short, literal reproduction against
      `82145b1`, including the round-4-vs-round-5 A/B comparison.

## Decision

- [ ] Approved
- [x] **Rejected** — reasons and the specific artifact change required below
- [ ] Deadlocked — escalate to Arbiter
- [ ] Reopening request

### Approval type outcomes

- **Specification-conformance**: **Rejected**, on one narrow ground only.
  The ADR-range redesign is a genuine, verified success: the three-round
  connective-parsing failure mode is structurally eliminated, not patched
  again, and every claim made about it (fails closed on rewording, catches a
  wrong bound, the "up to" attack no longer works, the registration gap is
  disclosed) is independently confirmed. The rejection is entirely due to
  Item 5/finding 8: fixing the self-referential false-positive bug
  (genuinely real, genuinely fixed) came bundled with an unrelated,
  undisclosed narrowing of what the reference checker validates, which drops
  real coverage for a real, currently-correct reference in this repository
  today.
- **Boundary-conformance**: **Approved.** No ADR touched; deleting an unsound
  rule and replacing it with a differently-shaped one addressing the same
  concern is within the agreement's scope; nothing here legislates a new
  rule the contract does not already state.
- **Evidence-sufficiency**: **Rejected**, on the same narrow ground. The
  Preflight tested that the self-referential false positive is gone and did
  not test whether the fix's blast radius extended past that specific case —
  the A/B comparison in Item 5 is exactly the test that would have caught it,
  and it is a single, mechanical `mv LICENSE /tmp && rerun` check.

## Reasons

1. **(Blocking)** Narrow the `MD_LINK` false-positive filter to the actual
   shape of the bug rather than to "any target without a slash or a known
   extension." A minimal, verifiable fix: exclude targets containing
   characters that cannot appear in a real filename but are common in regex
   literals — a backslash, or an unescaped `{`/`}` — rather than excluding by
   absence of a slash or extension. Re-run the exact test in this record
   (`mv LICENSE`, then both the self-referential-source check and a
   `[MIT](LICENSE)`-still-resolves check) as the acceptance test for the
   fix, since both directions need to hold simultaneously and neither was
   tested together before this round shipped.

This is the narrowest-scoped rejection of the five rounds: one filter, one
line of reasoning, one currently-live instance, with a specific, small,
already-sketched fix and an exact regression test to verify it. Everything
else in this round — the entire ADR-range redesign, all eight registered
patterns, both other bug fixes, the disclosure's treatment of the
registration-gap tradeoff, and the absence of any other regression — is
independently confirmed sound and would not by itself withhold approval.

---

## Verification Environment

- Real branch inspected directly (`process/contract-consistency-check`,
  `82145b1`); destructive defect injection in a disposable scratch copy
  (`git archive HEAD` + `.git`), reverted via `git checkout` between tests.
- Round 4's checker (`539453d`) extracted via `git show` into a standalone
  file and run directly against the round-5 tree for the A/B comparison in
  Item 5 — the only way to distinguish "this was already broken" from "this
  round broke it."
- `gh pr checks 8` and `gh pr view 8` queried live GitHub state at review time
  (2026-08-02, this session).
- Model: Claude Sonnet 5. Tool: Claude Code, fresh session, no access to any
  producing session's reasoning.
