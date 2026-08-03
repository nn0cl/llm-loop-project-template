# Review Record: Contract Consistency Checker, Round 4 (PR #8, `539453d`)

Reviewing persona: Reviewer.
Model / tool: Claude Sonnet 5, via a fresh Claude Code agent session with no
memory of the producing session's reasoning. Read the round-4 diff (a
deletion, not a patch), the round-4 Preflight record, and my own round-3
rejection only as statements of what was claimed — every claim independently
re-tested. Confirmed `git merge-base --is-ancestor 5790808
origin/process/contract-consistency-check` is true.

Note: this review resumes after a session-limit interruption on the first
attempt at round 4, per the coordinator's message. No commands ran and no
findings were produced in that attempt; this record starts from a clean read
of `539453d` and is not a continuation of partial state.

## Constraints (all three must hold)

- [x] **Context separation.** Did not produce the fix; producing context's
      reasoning not supplied or relied on.
- [x] **Deterministic precondition.** All checks below re-run in this
      session, against the real branch and a disposable scratch copy for
      destructive defect injection.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below. The round-3 false positive is confirmed gone; the disclosed
      multi-line gap is confirmed to still exist (correctly, as disclosed);
      one new, natural-language-reachable gap is confirmed in the surviving
      same-line range rule, which the disclosure does not adequately cover.

## Method

Copied the full tree (`git archive HEAD` + `.git`) into a fresh scratch
directory, confirmed a clean baseline, then re-ran the round-3 false-positive
and false-negative cases against the new code, attacked the two surviving
range rules (especially the separator whitelist, per the coordinator's own
stated distrust of it), verified the corrected failure message's advice is
achievable, and checked for regressions in everything the first three rounds
established. Reverted each injected defect via `git checkout` before the
next.

## Review Target

- Artifact: branch `process/contract-consistency-check` / commit `539453d`,
  pull request #8.
- Covering design agreement: DA-2026-08-02-07.
- Producing persona: Implementer, responding to my round-3 rejection.
- Reviewing persona / model / tool: Reviewer / Claude Sonnet 5 / Claude Code.
- Approval type: specification-conformance, boundary-conformance,
  evidence-sufficiency.
- Preflight (round 4):
  `docs/collaboration/reviews/2026-08-02-contract-consistency-preflight-4.md`
  — pass, independently re-verified below. Its own negative test used a
  standard dash-separated wrong range (correctly caught); it did not test any
  other separator, which is exactly where this round's finding lives.

## Deterministic Verification Output

**Baseline and CI:**

```text
$ python3 scripts/check-contract-consistency.py --repo .   # real branch
contract consistency: all checks passed

$ gh pr checks 8
Repository sanity   pass   10s   .../actions/runs/30743881008/job/91486001665
$ gh pr view 8 --json headRefOid
{"headRefOid":"539453d5d22e2d7eedd848f8b9a9482d6cd64179"}

required_files: 69, missing: []
py_compile: OK / bash -n: OK / conflict markers: none
copy-script target: checker runs clean inside it
```

**The diff itself** (`git diff 5790808 539453d -- scripts/check-contract-consistency.py`):
confirms the entire "both ends" block (`if re.search(r"\bADR|adr/", text, ...)`
through its `failures.add` call) is deleted outright, not modified; the
disclosure section gained the exact replacement text the commit message
describes; and the version-claims message's advice changed from "say on that
line that it is unreleased" to "link to CHANGELOG.md instead of naming a
version this repository cannot show." No other code changed.

### Item 1 — the deletion: is the false positive gone, and did it take more than the disclosed case with it?

```text
$ # round-3 false positive: README.md with the range-describing paragraph
$ #   replaced by generic prose, leaving only the pre-existing, unrelated
$ #   "[ADR 0001](...)" citation at line 72
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Confirmed gone.**

```text
$ # round-3 false negative, re-run verbatim: QUICKSTART.md's range statement
$ #   split across two lines with a wrong endpoint (0011 instead of 0013)
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Confirmed still open, and correctly disclosed** — the docstring's new
"A range spread across a sentence" bullet names this exact shape
("split over two lines") and states plainly that the earlier attempt to
cover it was removed rather than patched. This is not a hidden hole; it is
what the round says it did.

**Whether the disclosure understates what was lost — yes.** Round 3's "both
ends" rule, unsound as it was, still provided *some* protection for a
same-line, non-whitelisted-separator wrong range: it caught that case
whenever the document did not happen to restate the correct value elsewhere
(verified directly in my round-3 record). That partial backstop is now gone
with no replacement, and the disclosure's specific wording and example
("split over two lines") does not signal that same-line statements using an
uncommon connector are also unprotected — see Item 2, where this turns out to
be reachable with ordinary English, not just contrived multi-line splitting.

### Item 2 — the two surviving range rules, independently

**Token-existence rule** (any ADR-shaped token on an ADR-mentioning line must
name a real ADR):

```text
$ # a token that is not a valid ADR number at all
$ #   "The ADRs, including a stray reference to ADR 0099, describe the ..."
$ python3 scripts/check-contract-consistency.py --repo .
ADR range:
  README.md:235 names ADR 0099, which the repository does not have. ...
exit: 1
```
**Sound** — not reproduced as a hole. A token naming a nonexistent ADR is
caught regardless of surrounding phrasing, which is the property this rule
claims.

**Same-line range rule** (two numbers with nothing but a dash or a bare range
word between them) — attacked the separator whitelist directly, per the
coordinator's own stated distrust of it:

```text
$ # off-whitelist punctuation, WRONG range, single line, not split at all:
$ for sep in "/" ", " " .. " ": "; do
    # (0001{sep}0011) -- wrong, should be 0001-0013
    python3 scripts/check-contract-consistency.py --repo .
  done
"/"   -> contract consistency: all checks passed
", "  -> contract consistency: all checks passed
" .. "-> contract consistency: all checks passed
": "  -> contract consistency: all checks passed
"-- " -> ADR range: ... states the range 0001-0011 ...   # only this one caught (still just dashes)
```
**Reproduced, blocking.** More significantly, ordinary English connectives
outside `to`/`through`/`まで` also evade it:

```text
$ # "The ADRs 0001 up to 0011 describe the ..." (wrong -- should be 0013)
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed

$ # "0001 up through 0011", "numbered 0001 up to and including 0011",
$ #   "0001 all the way to 0011" -- all four pass clean, all wrong
```
**This is the material finding of this round.** "0001 up to 0011" is not a
contrived edge case or a split-across-lines construction — it is a compact,
single-line, entirely ordinary way to state a range, exactly the kind of
prose a human editor or a future agent would write without any intent to
evade anything, in the same register as round 1's "0001 to 0011" and round
2's "starting from 0012." The regex's fullmatch requires the connective to be
built *only* from `to`/`through`/`まで` plus dash/whitespace characters — "up
to," "through to," "all the way to," and punctuation like `/`, `,`, `..`, `:`
all fall outside it. The commit's own code comment claims this layer "catches
an understated range on a line even when another line names the true last
ADR" — true only for the narrow set of connectives it recognizes, not for
range statements generally.

### Item 3 — the corrected failure message: is the advice achievable?

```text
$ grep -n "CHANGELOG.md" README.md
4: · [Changelog](CHANGELOG.md)
8:version. See [CHANGELOG.md](CHANGELOG.md) for what an edition covers.

$ # a hedge that follows the advice literally: link to CHANGELOG.md,
$ #   name no version token at all
$ #   "See `CHANGELOG.md` for the next edition in progress."
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed

$ # positive control: a real false claim still fails, with the new message
$ #   "**Contract edition: v1.1.0.**" (wrong, untagged)
$ python3 scripts/check-contract-consistency.py --repo .
version claims:
  README.md:6 names v1.1.0, which has no git tag. Tag it, or link to
  CHANGELOG.md instead of naming a version this repository cannot show.
```
**Not reproduced — genuinely fixed.** `README.md` already links to
`CHANGELOG.md` twice; the advice is both true and already practiced in this
repository. The message change is accurate.

### Item 4 — regressions against what the first three rounds established

```text
$ # version escape hatch: still fully closed (round-3 fix untouched this round)
$ #   "**v1.1.0 is now released** (see CHANGELOG.md for details)."
version claims:
  README.md:6 names v1.1.0, which has no git tag. ...
exit: 1                                          # still caught, no regression

$ # bare-name wrong-but-unique-elsewhere reference: still resolves, as
$ #   disclosed (not a regression -- this was never claimed fixed)
$ #   .grok/rules/01-quickstart.md: "use `review-record.md` as the template"
$ #   for recording an architecture decision (wrong; unique name elsewhere)
contract consistency: all checks passed          # unchanged from round 3

$ # TEMPLATE_ONLY_FILES: deletion still caught by required_files
$ mv README.md /tmp/... ; required_files check
required_files missing: ['README.md']            # still caught, no regression
```
**Not reproduced.** Every previously-established fix (version smuggling
closed, `TEMPLATE_ONLY_FILES` protected via `required_files`, the false
positive on unrelated ADR citations gone) still holds. The only thing that
changed in scope beyond the two targeted fixes is the removal of "both ends,"
which is the intended, disclosed change, not an accidental regression — my
Item 1 finding is about the *disclosure's precision*, not about an
undisclosed loss.

### Judging the disclosure against what the script does today

The docstring names five limits now: meaning drift, reference-intent
ambiguity, "a range spread across a sentence," the adopter-start-number
phrasing, and target-project skips. Four of five are accurate as far as I
tested them. The "range spread across a sentence" bullet is the one that
does not match the code: its prose and its one example (`"from 0001 onward;
the last one is 0011", split over two lines`) both describe multi-line
spreading, and say nothing about a same-line statement using a connective
other than the three the regex recognizes. A reader relying on this section
to know what is and is not protected would reasonably conclude "0001 up to
0011" is caught (it is compact, one line, not "spread across a sentence")
and would be wrong.

The top-of-file claim list is unchanged: "4. ADR range: Every stated
process-ADR range matches the ADR files" remains a flat, unqualified
sentence, exactly as in every prior round, with the actual boundary of what
"matches" means left to a disclosure section that — as shown above — is
itself imprecise about this specific rule.

**Judgment: improved, but still not accurate to the code, in the same
direction as every previous round's disclosure — narrower than the actual
gap.** This is a smaller miss than rounds 1-3 (no false positive, no
regression, no smuggling route, one rule's boundary described too narrowly)
but it is the same category of miss: a claim (here, a disclosure meant to
bound a claim) that does not match what independent testing finds.

## Falsification Search

| # | Failure scenario searched for | Grounds it does or does not occur | Result |
|---|---|---|---|
| 1 | The round-3 false positive (single incidental ADR citation) still fires | Not reproduced: the triggering rule is deleted. | not reproduced (fixed) |
| 2 | The round-3 false negative (split-line wrong range) still evades detection | Reproduced — but this is the disclosed, accepted gap, not a hidden one. | reproduced, disclosed (not a new finding) |
| 3 | The disclosure understates what protection was lost by removing "both ends" | Reproduced: round 3's rule provided partial protection for same-line, odd-separator wrong ranges (when the doc didn't restate the value elsewhere); that is gone now, and the disclosure's "split over two lines" framing does not signal it. | **reproduced** |
| 4 | The token-existence range rule is unsound | Not reproduced: a nonexistent ADR token is caught regardless of phrasing. | not reproduced |
| 5 | The same-line range rule's separator whitelist is evaded by ordinary punctuation | Reproduced four ways (`/`, `,`, `..`, `:`), all on a single, un-split line. | **reproduced, blocking** |
| 6 | The same-line range rule's separator whitelist is evaded by ordinary English connectives, not just symbols | Reproduced: "up to," "up through," "up to and including," "all the way to" all evade it, none split across lines or otherwise contrived. | **reproduced, blocking** |
| 7 | The corrected version-claims message gives advice that cannot actually be followed in this repository | Not reproduced: `README.md` already links to `CHANGELOG.md`; a hedge with no literal version token passes clean. | not reproduced |
| 8 | Any of the three prior rounds' fixes (version smuggling, `TEMPLATE_ONLY_FILES`, the false positive on unrelated citations) regressed | Not reproduced for any of the three. | not reproduced |

## Scenarios Not Searched

- The adopter's-starting-number phrase-matching gap — unchanged this round,
  already disclosed and verified in round 3; not re-attacked here since
  nothing in this round touched that code path.
- `EXAMPLE_DOCUMENT_NAMES` — unchanged this round; not re-attacked, since
  round 3 already established it has no live instance and this round did not
  touch it.
- GitHub Actions execution beyond the one observed job.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked
      in.
- [x] The dependency rule and port boundaries hold — not applicable.
- [x] No boundary named in the design agreement was crossed — no ADR added or
      revised; a rule was deleted, not a new one added.
- [x] Specifications and accepted tests were not modified to make work pass.
- [ ] Every claim in the artifact states its grounds — the same-line range
      rule's code comment ("catches an understated range on a line even when
      another line names the true last ADR") does not hold for connectives
      outside its narrow whitelist, and the disclosure does not say so.
- [x] The record would let a third party re-run this same search — every
      injected defect above is a short, literal reproduction against
      `539453d`.

## Decision

- [ ] Approved
- [x] **Rejected** — reasons and the specific artifact changes required below
- [ ] Deadlocked — escalate to Arbiter
- [ ] Reopening request

### Approval type outcomes

- **Specification-conformance**: **Rejected**, narrowly. The design
  agreement's Falsification Criterion 1 reproduces once more: a stated
  process-ADR range, wrong, phrased in ordinary English ("0001 up to 0011"),
  passes a checker whose top-level claim is that "every stated process-ADR
  range matches the ADR files." The round's two targeted findings — the
  false positive and the split-line false negative that motivated the
  deletion — are both genuinely resolved.
- **Boundary-conformance**: **Approved.** No ADR touched; a rule was removed
  rather than a new one legislated; the change is smaller than what it
  replaced, matching the agreement's boundary that the checker "makes
  existing rules checkable; it does not legislate."
- **Evidence-sufficiency**: **Rejected**, on the same narrow ground. The
  Preflight's negative test used a standard dash-separated wrong range and
  called the same-line rule sound; it did not test a single alternative
  connective. A test suite that only exercises the separators the code
  already whitelists cannot demonstrate the rule is sound "in both
  directions," as both the commit message and the code comment claim.

## Reasons

1. **(Blocking)** Broaden or reframe the same-line range rule. Two paths,
   either acceptable:
   - Broaden the whitelist meaningfully (e.g., match any connective built
     from a bounded set of range-indicating words — "to," "through," "up
     to," "up through," "through to," "and," when NOT preceded by a word
     like "see" that would indicate separate citations — this reintroduces
     some of the ambiguity the "and" exclusion was designed to avoid, so it
     needs care) — or
   - Narrow the claim instead: change the docstring's top-level claim 4 and
     the code comment to state precisely what is checked ("two ADR numbers
     joined by a dash, or by the words 'to'/'through'/'まで', with nothing
     else between them" — not "every stated range"), and extend the "What
     this cannot check" section to say plainly that any other connective,
     even on a single line, is unprotected, not just multi-line splits.
   Given this repository's own history — every attempt to broaden a check by
   guessing more phrasings has produced the next round's gap — the second
   path is likely the safer one, and is consistent with what round 4 already
   did for the "both ends" rule: narrow the claim to what can actually be
   verified, rather than widen the pattern match again.
2. **(Non-blocking)** Once the claim is corrected, the Preflight's negative
   test should include at least one non-whitelisted-connective case (e.g.,
   "0001 up to 0011") alongside the dash-separated one, so a future round's
   "sound in both directions" claim is tested against more than the
   separators already known to work.

This is the narrowest rejection of the four rounds. Three of the round's four
targets — the false positive, the version-message accuracy, and the absence
of any regression — are each independently confirmed sound. The remaining
issue lives entirely inside one regular expression's connective whitelist,
has a small, well-scoped fix, and does not require reopening any design
decision this agreement settled.

---

## Verification Environment

- Real branch inspected directly (`process/contract-consistency-check`,
  `539453d`); destructive defect injection in a disposable scratch copy
  (`git archive HEAD` + `.git`), reverted via `git checkout` between tests.
- `gh pr checks 8` and `gh pr view 8` queried live GitHub state at review time
  (2026-08-02, this session).
- Model: Claude Sonnet 5. Tool: Claude Code, fresh session, no access to any
  producing session's reasoning. This session began after a prior attempt at
  this same round hit a session limit before any command ran; no findings
  from that attempt exist to carry forward.
