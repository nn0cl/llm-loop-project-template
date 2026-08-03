# Preflight Validation Record (round 3)

Per ADR 0013. **Not an approval.** Rounds 1 and 2 of this change both returned
`pass` and were both rejected. This record is a submission ticket and carries
no weight beyond that.

## Target

- Change: the four blocking gaps and one non-blocking finding the Reviewer
  found in the redesigned checker.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-contract-consistency-check.md`
- Review record being answered:
  `docs/collaboration/reviews/2026-08-02-contract-consistency-review-2.md`
- Branch: `process/contract-consistency-check`.
- Producer: Implementer, Claude Opus 5 via Claude Code. Cannot review this.

## Result

**pass** — resubmit.

## Defects Addressed

Each reproduced against the shipped checker before any fix was written.

| # | Reviewer finding | Fix |
|---|---|---|
| 1 | Bare-filename resolution accepted any file anywhere with that name, looser than path references | bare names resolve against the repository root, then the referencing file's own directory, then a **unique** file of that name. A name two files answer to now fails and asks for the path |
| 2a | Two ADR numbers on one line were called a range, so a sentence citing two unrelated ADRs failed | the two numbers must be joined by nothing but a dash or a bare range word. `0006 and ADR 0013` is left alone; `0001 to 0011` is not |
| 2b | An understated range split across two lines evaded detection | a document describing the ADR set must name both of its ends, which no line break or rewording evades |
| 3 | `TEMPLATE_ONLY_FILES` exempted the entry documents unconditionally, so deleting `README.md` from this repository produced zero failures | the exemption applies only where the file is genuinely absent. Their existence here is asserted by CI's `required_files`, which now lists all four — the Reviewer's observation that they had no protection anywhere |
| 4 | The version check skipped any line mentioning "unreleased" or "CHANGELOG", so a false release claim could ride on either word | the escape hatch is gone. Any `vX.Y.Z` a README names must be a git tag |
| 5 (non-blocking) | `EXAMPLE_DOCUMENT_NAMES` has the same context-blind shape | unchanged, and now named in the disclosure |

## Disclosure

The Reviewer judged the previous disclosure "honest about the two things it
names but materially incomplete". It now names four limits rather than two,
including the two the Reviewer found: that the reference check cannot know a
sentence meant one document and named another, and that checks over the entry
documents are skipped in an adopting project. It also states plainly that two
rounds of review found holes in this script, and that each was a claimed check
that did not exist rather than a weak one.

## Checks

| # | Check | Result |
|---|---|---|
| 1 | All four blocking gaps closed | pass |
| 2 | No false positive on two unrelated ADRs cited together | pass |
| 3 | Negative test across every claimed class | pass — 6 failures, exit 1 |
| 4 | Clean tree | pass |
| 5 | Fresh copy-script target | pass |
| 6 | Entry-document deletion is caught | pass — by CI `required_files`, verified by deleting two |
| 7 | CI required files | pass — 69, 0 missing |
| 8 | `bash -n` | pass |

## Command Output

Negative test:

```text
mirror parity:
  copilot does not state 'Prime Directive'
parity completeness:
  AGENTS.md section 'A Brand New Rule' is not classified.
references:
  docs/collaboration/personas.md:171 names 'does-not-exist-anywhere.md'
ADR range:
  README.md:235 states the range 0001-0011; the repository has 0001-0013
  QUICKSTART.ja.md tells adopting projects to start at 0012; ... must start at 0014
version claims:
  README.md:6 names v1.1.0, which has no git tag.

contract consistency: 6 failure(s)
```

The same tree also contains `See ADR 0006 and ADR 0013 for details.` — the
Reviewer's false-positive case — and it produces no failure.

Entry-document deletion, now caught by CI rather than by the checker:

```text
required_files missing: ['README.md', 'QUICKSTART.ja.md']  -> CI FAILS
```

Clean tree and a fresh target:

```text
contract consistency: all checks passed     (template repo)
contract consistency: all checks passed     (copy-script target)
required_files: 69, missing: []
bash -n OK
```

## Scope Result

Within scope. No specification, ADR, port, data model, dependency, or
architecture boundary changed.

## Routing and Compatibility

- Capability class: deterministic tooling for verification; strong reasoning
  agent for deciding which checks could be made sound and which had to be
  narrowed and disclosed instead.
- Displayed model / reasoning setting: Claude Opus 5, default.
- Compatibility state: default routing; stdlib-only Python 3.
- Escalation reason: contract files and CI changed.

## Next Action

Resubmit. The remaining known softness is the bare-name uniqueness rule, which
still resolves a name that exists as a sibling of the referencing file even
when the sentence meant a different document — disclosed rather than claimed.
