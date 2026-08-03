# Review Record: Contract Consistency Checker, Round 3 (PR #8, `5790808`)

Reviewing persona: Reviewer.
Model / tool: Claude Sonnet 5, via a fresh Claude Code agent session with no
memory of the producing session's reasoning. Read the round-3 diff, the
round-3 Preflight record, and my own round-2 rejection only as statements of
what was claimed — every claim independently re-tested. Confirmed
`git merge-base --is-ancestor d479308 origin/process/contract-consistency-check`
is true, so the fixes I am reviewing build on the commit my round-2 record
covered.

## Constraints (all three must hold)

- [x] **Context separation.** Did not produce the fix; producing context's
      reasoning not supplied or relied on.
- [x] **Deterministic precondition.** All checks below re-run in this
      session, against the real branch and a disposable scratch copy for
      destructive defect injection.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below. Three are reproduced as blocking, two of them against the
      round's own centerpiece redesign (the ADR-range "both ends" rule), one
      of those confirmed a second time in an independent file to rule out
      coincidence.

## Method

Copied the full tree (`git archive HEAD` + `.git`) into a fresh scratch
directory, confirmed a clean baseline, then attacked each of the five items
in the coordinator's list plus the "also worth attacking" note, one defect at
a time, reverting via `git checkout` between tests.

## Review Target

- Artifact: branch `process/contract-consistency-check` / commit `5790808`,
  pull request #8.
- Covering design agreement: DA-2026-08-02-07.
- Producing persona: Implementer, responding to my round-2 rejection.
- Reviewing persona / model / tool: Reviewer / Claude Sonnet 5 / Claude Code.
- Approval type: specification-conformance, boundary-conformance,
  evidence-sufficiency.
- Preflight (round 3):
  `docs/collaboration/reviews/2026-08-02-contract-consistency-preflight-3.md`
  — pass, independently re-verified below; its own negative test and the
  "0006 and 0013" false-positive check both reproduce as claimed, but a
  second false-positive/false-negative pair in the same mechanism was not
  found by it.

## Deterministic Verification Output

**Baseline and CI:**

```text
$ python3 scripts/check-contract-consistency.py --repo .   # real branch
contract consistency: all checks passed

$ gh pr checks 8
Repository sanity   pass   9s   .../actions/runs/30743535696/job/91485083766
$ gh pr view 8 --json headRefOid
{"headRefOid":"57908084e9b4085289024f5b75421657eb29fd93"}

required_files: 69, missing: []
py_compile: OK / bash -n: OK / conflict markers: none
```

### Item 1 — bare filenames: root, sibling, unique-match

```text
$ # confirmed the disclosed sibling case still resolves (not re-litigated as
$ #   a finding — the coordinator already told me this one is disclosed):
$ #   docs/collaboration/personas.md referencing bare `design-agreement.md`,
$ #   which is a sibling of that very file (docs/collaboration/design-agreement.md)
$ #   -> still resolves, matches the disclosure.

$ # NEW test: a wrong reference resolved via the "unique file anywhere" leg,
$ #   not the sibling leg -- inserted into .grok/rules/01-quickstart.md
$ #   (NOT a sibling of docs/templates/):
$ #   "When recording an architecture decision, use `review-record.md` as the
$ #    template." (wrong -- should be docs/templates/adr.md; review-record.md
$ #    is the Reviewer's template, unrelated to recording a decision)
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Reproduced, but judged as underdisclosed rather than a new hole.** The
docstring's disclosed limit reads "it cannot know that a sentence meant
`docs/templates/review-record.md` and said
`docs/templates/design-agreement.md`, **when both exist**" — phrasing that
reads as scoped to the ambiguous/duplicate-name case. My test shows the same
failure mode when the wrongly-named file is the *unique* file of that name in
the whole repository, which is a broader blast radius than "when both
exist" suggests. This is the same underlying, disclosed limitation (the
reference check resolves names, not intent), just wider than the literal
wording implies — I fold it into the disclosure judgment (below) rather than
counting it as an independent blocking finding, since the coordinator's own
framing already treats this class as "disclosed, not claimed."

### Item 2 — the range rule's two layers, attacked independently

**2a. Same-line separator whitelist, evaded with an off-whitelist separator,
masked by a coincidentally-correct mention elsewhere in the same document:**

```text
$ # README.md line 235: "The thirteen ADRs included here (0001-0013)..."
$ #                  -> "The eleven ADRs included here (0001 / 0011)..."
$ #   (WRONG -- should be 0001-0013 -- using "/" as separator, which is not
$ #    in the whitelist [\s\-–—〜~]*(?:to|through|まで)?[\s\-–—〜~]*)
$ #   README.md:288 still correctly says "(0001-0013 = process ADRs)"
$ #   elsewhere, unrelated to the wrong statement.
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Reproduced, blocking.** Isolated re-test, removing the other `0013`
mention too, confirms the "both ends" layer *can* catch this class in
isolation:

```text
$ # same edit, but also strip the second "0001-0013" mention at line 288
$ python3 scripts/check-contract-consistency.py --repo .
ADR range:
  README.md describes the ADR set without naming 0013. ...
exit: 1
```
So the vulnerability is specific to, and dependent on, documents that state
the correct range more than once — which is not a corner case. Both
`README.md` and `QUICKSTART.md`, the two real files this check runs against
in this repository, independently do exactly that (see 2b).

**2b. "Both ends" property, both directions:**

*False negative* — the exact split-line attack from my round-2 review,
re-run against the round-3 checker:

```text
$ # QUICKSTART.md, split across two lines (WRONG endpoint, 0011 instead of 0013):
$ #   "`0001-*.md` is where the process ADRs this template ships with begin."
$ #   "The last one it ships is `0011-*.md`; remove only those, ..."
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Still reproduces**, for the same reason as 2a: `QUICKSTART.md` independently
states the correct range a second time, at a different line ("records" asserts
ADRs 0001–0013," line 180), which satisfies "both ends appear somewhere in the
document" even though the actual range-describing sentence I corrupted is
never validated. This is not a new attack — it is my round-2 finding,
confirmed to still reproduce against the mechanism specifically built to fix
it, in the same file, unmodified from my earlier test.

*False positive* — a document with a single, incidental ADR citation and no
attempt to describe a range at all:

```text
$ # README.md: replaced the range-describing sentence with generic prose
$ #   (no digits), and removed the file-tree comment's "0001-0013" mention,
$ #   leaving only the pre-existing, unrelated "[ADR 0001](...)" link at
$ #   line 72 (a completely normal citation of the governing ADR).
$ python3 scripts/check-contract-consistency.py --repo .
ADR range:
  README.md describes the ADR set without naming 0013. The set runs
  0001-0013; a document that states a range must state the current one.
exit: 1
```
**Reproduced, blocking.** A document that never attempts to state a range —
it cites exactly one ADR, in passing, the way `AGENTS.md`, `CLAUDE.md`, and
every contract file in this repository routinely cite specific ADRs — fails
CI solely because the word "ADR" and the token "0001" co-occur somewhere in
it and "0013" does not appear anywhere else. This is a real usability risk in
the current document, not a synthetic one: `README.md` already carries an
incidental "[ADR 0001](...)" link (line 72) alongside its range-describing
paragraph; an editor who simplifies or relocates the range paragraph without
realizing it is load-bearing would hit a confusing, unrelated-looking CI
failure.

### Item 3 — `TEMPLATE_ONLY_FILES`, both halves

```text
$ mv README.md /tmp/...
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed        # checker stays silent, by design
$ python3 -c "... required_files existence check against ci.yml's array ..."
required_files missing: ['README.md']          # CAUGHT, by a different, real check
$ mv /tmp/... README.md
```
```text
$ # fresh copy-script target, which legitimately lacks README.md etc.
$ bash scripts/copy-ai-collaboration-files.sh --target "$tmp" ...
$ (cd "$tmp" && python3 scripts/check-contract-consistency.py --repo .)
contract consistency: all checks passed
$ ls "$tmp/README.md"
No such file or directory                      # confirmed genuinely absent, and clean
```
**Not reproduced — genuinely fixed.** Both halves verified independently: the
checker itself correctly declines to duplicate `required_files`'s job (its
own comment's reasoning — "a checker that both defines what may be missing
and decides whether something is missing has no independent signal" — holds
up), and `required_files` (now listing all four entry documents, confirmed by
direct inspection of `ci.yml`) provides the actual backstop. Deleting any of
the four from this repository now fails CI, and the checker still runs clean
in a target that never had them.

### Item 4 — the version escape hatch's removal, and whether it broke a
legitimate use

```text
$ # README.md, clearly hedged, truthful, forward-looking sentence:
$ #   "The next edition, v1.1.0, is pending independent review; see CHANGELOG.md."
$ python3 scripts/check-contract-consistency.py --repo .
version claims:
  README.md:6 names v1.1.0, which has no git tag. Tag it, or say on that
  line that it is unreleased.
exit: 1

$ # tried the error message's own suggested fix -- literally add "unreleased":
$ #   "The next edition, v1.1.0, is currently unreleased and pending
$ #    independent review; see CHANGELOG.md."
$ python3 scripts/check-contract-consistency.py --repo .
version claims:
  README.md:6 names v1.1.0, which has no git tag. Tag it, or say on that
  line that it is unreleased.
exit: 1                                          # the suggested fix does not work
```
**Reproduced, non-blocking but real.** The design itself — no README may name
an untagged `vX.Y.Z` token at all, full stop, forcing indirection through the
changelog for any forward-looking mention — is a defensible, conservative
trade-off given two rounds of escape-hatch exploitation; it closes the
smuggling vulnerability completely rather than trading it for a narrower one.
But the failure message is now false: it tells the author "say on that line
that it is unreleased" as a working remedy, and that remedy does nothing —
the code has no such exception anymore (confirmed by reading it: the
`unreleased`/`CHANGELOG` regex skip was fully deleted, and the comment above
the loop says so explicitly). An author following the tool's own advice would
retry the identical failure. This is the same "claims a capability it doesn't
have" pattern that drove earlier rejections, now inside an error string
rather than a docstring or a check's coverage claim — smaller in
consequence (it misleads about the *fix*, not about whether a real defect was
caught), so I judge it non-blocking, but it should not ship uncorrected.

### `EXAMPLE_DOCUMENT_NAMES` — did the tightened bare-name rule create a live instance?

```text
$ for n in backend-architecture.md frontend-architecture.md persistence.md rust-clean-architecture.md; do
    find . -name "$n" -not -path "./.git/*"
  done
(no output for any of the four)
```
**Not reproduced.** None of the four exempted names exist as real files
anywhere in the repository, and the exemption is checked before any
root/sibling/unique-match resolution runs, so the bare-name redesign has no
interaction with it. Still non-blocking, still no live instance, unchanged
from round 2.

### Judging the disclosure (four limits named, up from two)

The four named limits — meaning drift, reference-intent ambiguity, the
adopter-start-number phrasing, and target-project skips — are each real and,
except for the scope note on reference-intent above, accurately described.
To that extent the disclosure is honest.

It remains incomplete, and the omission is the same shape as both previous
rounds': the section says nothing about the two failure modes in Item 2,
even though the "both ends" rule is this round's own new mechanism, built
specifically in response to my prior finding, and preflighted with a targeted
test ("No false positive on two unrelated ADRs cited together: pass" — true,
but narrower than the actual risk surface of the rule it was testing). It
also says nothing about the version-check error message giving advice that
does not work. Neither omission is a rehash of an old, already-disclosed
limit; both are properties of code written in this round.

**Judgment: still materially incomplete, for the same reason each previous
round's was** — the disclosure is written by the context that built the
fix, and it names the limits that context could see, not the ones adversarial
testing finds. That is not a criticism of effort; it is the exact argument
this document has made every round for why the disclosure cannot substitute
for independent review, and it continues to hold here.

## Falsification Search

| # | Failure scenario searched for | Grounds it does or does not occur | Result |
|---|---|---|---|
| 1 | Bare-name resolution accepts a wrong reference via the "unique match anywhere" path, not just the disclosed sibling path | Reproduced (`.grok/rules/01-quickstart.md` citing the wrong template by a uniquely-named bare filename). Judged as broadening, not violating, the existing disclosure. | reproduced, non-blocking (disclosure-scope note) |
| 2a | The same-line separator whitelist is evaded by an off-whitelist separator, and the resulting wrong statement is masked when the document happens to state the range correctly elsewhere too | Reproduced in `README.md`; confirmed the "both ends" backstop *would* catch it if isolated (no other correct mention present), which locates the actual failure in the interaction between the two layers, not either alone. | **reproduced, blocking** |
| 2b-false-negative | A genuinely wrong range split across two lines still evades detection when the document independently states the correct range a second time elsewhere | Reproduced, in `QUICKSTART.md`, with the identical attack from round 2 — this file has its own independent second correct mention ("asserts ADRs 0001–0013," line 180) that masks the corrupted primary statement. | **reproduced, blocking (round-2 finding not actually closed)** |
| 2b-false-positive | A document citing exactly one ADR in passing, with no attempt to state a range, is wrongly forced to also name the last ADR | Reproduced in `README.md`, using its own pre-existing, unrelated `[ADR 0001](...)` citation (line 72) as the trigger. | **reproduced, blocking** |
| 3 | `TEMPLATE_ONLY_FILES` still masks a real deletion in the template repo, or breaks in a legitimate target | Not reproduced for either half: deletion is now caught by `required_files`; the copy-script target still runs clean. | not reproduced (genuinely fixed) |
| 4 | The version-claims redesign broke a legitimate, truthful, hedged use | Reproduced: a hedged, non-false sentence naming an untagged version fails, and the error message's suggested remedy does not work. Judged non-blocking: the underlying design choice is a defensible, conservative trade-off; only the error message is wrong. | reproduced, non-blocking |
| 5 | `EXAMPLE_DOCUMENT_NAMES` gained a live instance from the bare-name redesign | Not reproduced: none of the four names exist as real files; the exemption is unaffected by the resolution-order change. | not reproduced |
| 6 | The disclosure section is complete relative to what this round's code actually does | Not reproduced as complete: the "both ends" rule's two failure modes and the version-message inaccuracy are both absent from it. | reproduced (still incomplete) |

## Scenarios Not Searched

- Whether `QUICKSTART.ja.md` has the same redundant-mention structure that
  makes `README.md` and `QUICKSTART.md` vulnerable to 2a/2b — not checked,
  since two independent confirmations were already sufficient to establish
  the pattern is structural rather than a one-off.
- Full enumeration of separators outside the whitelist beyond "/" — one
  concrete counter-example was judged sufficient to establish the class.
- GitHub Actions execution beyond the one observed job.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked
      in.
- [x] The dependency rule and port boundaries hold — not applicable.
- [x] No boundary named in the design agreement was crossed — no ADR added or
      revised.
- [x] Specifications and accepted tests were not modified to make work pass.
- [ ] Every claim in the artifact states its grounds — the "both ends" rule's
      code comment ("neither rewording nor line breaks evade it") is shown
      above not to hold whenever a document states the range more than once,
      which both real files this check runs against do.
- [x] The record would let a third party re-run this same search — every
      injected defect is a short, literal reproduction against `5790808`.

## Decision

- [ ] Approved
- [x] **Rejected** — reasons and the specific artifact changes required below
- [ ] Deadlocked — escalate to Arbiter
- [ ] Reopening request

### Approval type outcomes

- **Specification-conformance**: **Rejected.** The design agreement's
  Falsification Criterion 1 reproduces twice more against the ADR-range
  check specifically — a false negative that is my exact round-2 finding
  surviving, unresolved, against the mechanism built to close it, and a new
  false positive on an ordinary, correct document. Three of five items
  (bare-name scope, `TEMPLATE_ONLY_FILES`, `EXAMPLE_DOCUMENT_NAMES`) are
  resolved or judged non-blocking; the version-message issue is non-blocking;
  the ADR-range layer is not.
- **Boundary-conformance**: **Approved.** No ADR touched; `required_files`
  additions and the checker's internal redesign both stay within the
  agreement's scope.
- **Evidence-sufficiency**: **Rejected.** The round's own Preflight tested
  the specific false-positive case named in my round-2 rejection ("0006 and
  ADR 0013") and confirmed it fixed — correctly — but did not test the
  interaction between the two new layers, which is where both remaining
  defects live. A green run of a test suite built to check the previously
  found holes is not evidence the new mechanism is sound; it is evidence the
  old holes are closed, which is a narrower claim than the disclosure
  intends "no mechanical drift found" to cover for this check.

## Reasons

1. **(Blocking)** Make the "both ends" rule operate on the sentence or list
   item that actually states a range, not on the whole document's token bag.
   A document-wide check cannot distinguish "this document correctly states
   the range in two places" from "this document states the range once,
   correctly, and once, wrongly" — and both `README.md` and `QUICKSTART.md`,
   the only two files this check runs against in this repository, state it
   more than once. One approach: apply the same-line/short-span range
   detection (already built for 2a) to *every* line, and independently
   require that at least one such detected range statement in the document
   matches the true ends, rather than scanning for the bare tokens
   in isolation from the range-shaped context that introduces them.
2. **(Blocking)** Fix the false positive: a document must only be held to
   the "both ends" rule when it actually contains a range-shaped statement
   (per the same detection used for 2a), not merely because it cites any
   single ADR number anywhere. As shipped, `README.md`'s ordinary,
   unrelated `[ADR 0001](...)` citation is enough to trigger it. Solving
   reason 1 the way described above would likely solve this one too, since
   both come from the same over-broad trigger condition
   (`re.search(r"\bADR|adr/", ...)` over the whole document, rather than
   over range-stating spans).
3. **(Non-blocking)** Update the version-claims failure message. It currently
   tells an author "say on that line that it is unreleased," which no longer
   works — the escape hatch that sentence describes was deleted this round.
   Either restore a narrow, safe version of that escape (e.g., require the
   word to be adjacent to the version token, not merely present on the line —
   which would reopen the smuggling risk this round closed, so likely not
   worth it) or change the message to state the actual remedy: remove the
   literal version token from the line, or tag it.
4. **(Non-blocking)** Extend the disclosure to name the "both ends" rule's
   scope precisely — that it is satisfied by any correct mention anywhere in
   the document, not tied to the statement it is meant to validate — and to
   widen the reference-intent disclosure from "when both exist" to cover the
   unique-but-wrong case demonstrated in Item 1.

This is not a rejection of the direction, and the gap between this round and
approval is narrower than either previous round's: `TEMPLATE_ONLY_FILES` is
solidly fixed, the version escape hatch is solidly closed (its only remaining
issue is a wrong error string), the false positive on two unrelated ADR
citations that this round specifically set out to fix is genuinely fixed, and
the disclosure keeps growing more honest each round even as it keeps trailing
what the code actually does. The two blocking items both live in one
function (`check_adr_range`'s "both ends" block) and share one root cause
(a document-wide token check standing in for a statement-scoped one) — this
reads like a fix that is one more iteration away, not a design that needs to
be abandoned.

---

## Verification Environment

- Real branch inspected directly (`process/contract-consistency-check`,
  `5790808`); destructive defect injection in a disposable scratch copy
  (`git archive HEAD` + `.git`), reverted via `git checkout` between tests.
- `gh pr checks 8` and `gh pr view 8` queried live GitHub state at review time
  (2026-08-02, this session).
- Model: Claude Sonnet 5. Tool: Claude Code, fresh session, no access to any
  producing session's reasoning.
