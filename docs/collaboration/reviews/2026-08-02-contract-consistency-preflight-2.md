# Preflight Validation Record (round 2)

Per ADR 0013. **Not an approval.** Round 1 of this same change returned `pass`
and the Reviewer rejected it anyway, which is the second time that has happened
in this repository. Read this record as a submission ticket, nothing more.

## Target

- Change: the three holes the Reviewer found in
  `scripts/check-contract-consistency.py`, plus the two non-blocking findings.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-contract-consistency-check.md`
  (DA-2026-08-02-07).
- Review record being answered:
  `docs/collaboration/reviews/2026-08-02-contract-consistency-review.md`
- Branch: `process/contract-consistency-check`.
- Producer: Implementer, Claude Opus 5 via Claude Code. Cannot review this.

## Result

**pass** — resubmit.

## Defects Addressed

Each was reproduced against the shipped checker before any fix was written.

| # | Reviewer finding | Root cause | Fix |
|---|---|---|---|
| 1 | Bare filenames in backtick paths were skipped entirely; a dangling `personas.md`-style reference passed clean | the reference check required a `/` in the token | bare names now resolve against every filename in the repository; `@`-prefixed import syntax is stripped first |
| 2 | `0001 to 0011` evaded the ADR range check | the check parsed a fixed set of separator words | it no longer reads separators at all: every ADR-shaped token on an ADR line must name an ADR that exists, and two distinct tokens on one line are treated as a range whose ends must be the set's ends |
| 3 | A reworded false banner (`Now shipping v1.1.0`) passed | the check matched the literal prefix `Contract edition:` | any `vX.Y.Z` a README names must be a git tag, unless that line says it is unreleased |
| 4 (non-blocking) | `AGENTS_ONLY_SECTIONS`'s justification was false for three of four mirrors | the exemption was wrong, not just its wording | the two sections were added to the mirrors and the exemption removed; `AGENTS_ONLY_SECTIONS` is now empty, with the history recorded where a reader meets it |
| 5 (non-blocking) | A reworded-but-present rule evades mirror parity | structural: parity checks presence, not meaning | not fixed — disclosed. See below |

## What the Checker Now Says It Cannot Do

The Reviewer's finding was not only that holes existed, but that the script
claimed coverage it did not have. Its docstring now carries a
"What this cannot check, and who does" section naming two structural limits:
meaning drift in a mirror that keeps the phrase, and the phrasing of the
sentence that tells adopters where to start their ADR numbering. It states
that a green run means "no mechanical drift found", never "the contract is
consistent".

## Checks

| # | Check | Result |
|---|---|---|
| 1 | The three holes are closed | pass — all three now fail the checker |
| 2 | Negative test, seven injected defects across every claimed class | pass — 7 failures, exit 1 |
| 3 | Clean tree | pass |
| 4 | Fresh copy-script target | pass |
| 5 | CI required files | pass — 65, 0 missing |
| 6 | `bash -n` | pass |

## Command Output

Negative test, seven defects injected:

```text
mirror parity:
  copilot does not state 'Prime Directive'
parity completeness:
  AGENTS.md section 'A Brand New Rule' is not classified.
references:
  docs/collaboration/definition-of-done.md:116 names 'docs/collaboration/nope.md'
  docs/collaboration/personas.md:171 names 'does-not-exist-anywhere.md'
ADR range:
  README.md:235 states the range 0001-0011; the repository has 0001-0013
version claims:
  CHANGELOG.md heading 'v9.9.9' has no matching git tag.
  README.md:6 names v1.1.0, which has no git tag.

contract consistency: 7 failure(s)
```

Clean tree, and a fresh copy-script target:

```text
contract consistency: all checks passed     (template repo)
contract consistency: all checks passed     (copy-script target)
```

## What Broadening the Reference Check Surfaced

Six references that had never been checked. Four were false positives and are
handled by rule rather than by silence: `@AGENTS.md` is Claude Code import
syntax, so a leading `@` is stripped; `backend-architecture.md` and its
siblings are names of documents a target project creates, listed in an
explicit `EXAMPLE_DOCUMENT_NAMES` set rather than by a rule about "e.g." lines,
so a genuine dangling reference on such a line is still caught.

Then the checker flagged **itself**: its own docstring names `CHANGELOG.md`,
which does not exist in an adopting project. That produced
`TEMPLATE_ONLY_FILES`, one declaration now used both for skipping absent entry
documents and for not treating their names as dangling.

## Scope Result

Within scope. No specification, ADR, port, data model, dependency, or
architecture boundary changed. Two target-fill sections were added to two
contract files, which the parity model now requires rather than exempts.

## Routing and Compatibility

- Capability class: deterministic tooling for verification; strong reasoning
  agent for the redesign of checks 2 and 3 away from phrase matching.
- Displayed model / reasoning setting: Claude Opus 5, default.
- Compatibility state: default routing; stdlib-only Python 3.
- Escalation reason: contract files changed.

## Next Action

Resubmit to the independent Reviewer, with the specific request that it attack
the *new* rules rather than re-run its previous attacks: the bare-filename
resolution is lenient by construction, and the two-tokens-are-a-range rule will
misfire on a line that legitimately cites two unrelated ADRs.
