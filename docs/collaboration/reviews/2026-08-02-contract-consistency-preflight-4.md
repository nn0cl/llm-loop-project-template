# Preflight Validation Record (round 4)

Per ADR 0013. **Not an approval.** Rounds 1, 2, and 3 of this change each
returned `pass` and each was rejected. Three passes and three rejections is the
strongest evidence this repository has produced for ADR 0013's own warning that
a checklist which passes says nothing about whether a change is correct.

## Target

- Change: the two blocking findings in the ADR-range "both ends" rule, and one
  non-blocking wrong-advice message.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-contract-consistency-check.md`
- Review record being answered:
  `docs/collaboration/reviews/2026-08-02-contract-consistency-review-3.md`
- Branch: `process/contract-consistency-check`.
- Producer: Implementer, Claude Opus 5 via Claude Code. Cannot review this.

## Result

**pass** — resubmit.

## What Was Done

The Reviewer's diagnosis was that both findings shared one root cause: the
"both ends" rule read the whole document's token bag rather than the span that
states a range, making it simultaneously too loose — any correct mention
elsewhere masked a wrong one — and too strict, since an ordinary citation of a
single ADR tripped it.

That diagnosis is correct, and the rule was **removed rather than patched**.
This is the third rule in this script that review found unsound. Patching each
one produced the next round's defect; the rule that survives is the one that
compares two things, not the one that infers intent from a document.

What remains for ADR ranges, both sound in each direction:

- every ADR-shaped token on an ADR line must name an ADR the repository has,
  or the number an adopting project starts at;
- two ADR numbers with nothing but a dash or a bare range word between them
  state a range, and its ends must be the set's ends.

What that leaves uncovered is now in the disclosure, in the specific terms the
Reviewer used: a range spread across a sentence or split over two lines is not
caught, and the earlier attempt to cover it was too loose and too strict at
once.

The version failure message told authors to "say on that line that it is
unreleased", which stopped being true when the escape hatch was removed. It now
tells them to link to the changelog instead.

## Checks

| # | Check | Result |
|---|---|---|
| 1 | The false positive on an ordinary ADR citation is gone | pass |
| 2 | The remaining range rules still catch an in-line wrong range | pass |
| 3 | No false positive on two unrelated ADRs cited together | pass |
| 4 | Negative test across every claimed class | pass — 6 failures, exit 1 |
| 5 | Clean tree | pass |
| 6 | Fresh copy-script target | pass |
| 7 | CI required files | pass — 69, 0 missing |
| 8 | `bash -n` | pass |

## Command Output

The Reviewer's false-positive case — `README.md` with every range statement
removed, leaving only an ordinary `[ADR 0001](...)` citation:

```text
contract consistency: all checks passed
```

A wrong in-line range, in a tree that also contains the Reviewer's
false-positive case `See ADR 0006 and ADR 0013 for details.`:

```text
ADR range:
  README.md:235 states the range 0001-0011; the repository has 0001-0013

contract consistency: 1 failure(s)
```

Negative test:

```text
mirror parity:      copilot does not state 'Prime Directive'
parity completeness: AGENTS.md section 'A Brand New Rule' is not classified.
references:         docs/collaboration/personas.md:171 names 'does-not-exist-anywhere.md'
ADR range:          README.md:235 states the range 0001-0011
                    QUICKSTART.ja.md tells adopting projects to start at 0012
version claims:     README.md:6 names v1.1.0, which has no git tag.

contract consistency: 6 failure(s)
```

Clean tree, target, CI:

```text
template: pass
target: pass
required_files: 69, missing: []
bash -n OK
```

## Scope Result

Within scope. No specification, ADR, port, data model, dependency, or
architecture boundary changed. The script is smaller than it was last round.

## Routing and Compatibility

- Capability class: deterministic tooling for verification; strong reasoning
  agent for the decision to delete rather than patch.
- Displayed model / reasoning setting: Claude Opus 5, default.
- Compatibility state: default routing; stdlib-only Python 3.
- Escalation reason: contract tooling changed.

## Next Action

Resubmit. The honest summary of four rounds: every check this script now makes
compares two things that must agree. Every check it tried to make by inferring
what a document meant has been removed, and what those attempts were reaching
for is written down as the Reviewer's work instead.
