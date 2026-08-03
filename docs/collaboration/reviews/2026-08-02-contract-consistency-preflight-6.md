# Preflight Validation Record (round 6)

Per ADR 0013. **Not an approval.**

## Target

- Change: the one blocking regression the Reviewer found in round 5 — the
  self-referential-bug fix over-excluded, silently dropping extensionless
  real references like `[MIT](LICENSE)`.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-contract-consistency-check.md`
- Review record being answered:
  `docs/collaboration/reviews/2026-08-02-contract-consistency-review-5.md`
- Branch: `process/contract-consistency-check`.
- Producer: Implementer, Claude Opus 5 via Claude Code. Cannot review this.

## Result

**pass** — resubmit.

## Round 5's Regression, and What Fixing It Broke Next

Round 5 fixed a self-referential false positive (the checker's own regex
literal matching as a fake markdown link) by requiring a `/` or a recognized
extension before treating an `MD_LINK` target as a real reference. That
correctly rejected `\d{4}`, and it also rejected `LICENSE` — a real,
extensionless, currently-correct reference in this repository's own README —
leaving its deletion silently uncaught. Confirmed by the Reviewer's own A/B
test and reproduced here independently: `rm LICENSE` produces no failure on
round 5.

The fix in this round switched from an exclusion list (slash-or-extension) to
an inclusion list (only path-shaped characters, with at least one
alphanumeric). Fixing it exposed a **second** self-reference: the comment
explaining the *first* self-reference illustrates it with the literal text
`[...](...)`, which the new filter accepted (`...` contains no backslash or
brace) and flagged as a dangling reference to a file named `...`. Caught by
re-running the checker on itself, the same way the first two self-references
were — this script cannot be trusted without running it against its own
source.

The filter now additionally requires at least one alphanumeric character in
the target, which rejects `...` while still accepting `LICENSE`,
`docs/foo.md`, and every other real reference.

## Checks

| # | Check | Result |
|---|---|---|
| 1 | `LICENSE` deletion is caught (the Reviewer's exact regression test) | pass |
| 2 | The original self-reference (`\d{4}`) does not resurface | pass |
| 3 | The new self-reference (`...` in this comment) does not occur | pass |
| 4 | Round 4's "up to" attack still fails closed | pass |
| 5 | Round 5's reworded-anchor test ("included here" → "found here") still fails closed | pass |
| 6 | Negative test, six classes together including `LICENSE` deletion | pass — 6 failures, exit 1 |
| 7 | Clean tree | pass |
| 8 | Fresh copy-script target | pass |
| 9 | CI required files | pass — 69, 0 missing |
| 10 | `bash -n` | pass |

## Command Output

The Reviewer's exact regression test:

```text
$ rm LICENSE && python3 scripts/check-contract-consistency.py --repo .
references:
  README.md:330 names 'LICENSE', which does not exist

contract consistency: 1 failure(s)
```

Clean tree, confirming neither self-reference recurs:

```text
contract consistency: all checks passed
```

Combined negative test, six classes:

```text
mirror parity:       copilot does not state 'Prime Directive'
parity completeness: AGENTS.md section 'A Brand New Rule' is not classified.
references:          README.md:330 names 'LICENSE', which does not exist
                     docs/collaboration/personas.md:171 names 'does-not-exist-anywhere.md'
ADR range:           README.md: expected range statement not found (...)
version claims:      README.md:6 names v1.1.0, which has no git tag.

contract consistency: 6 failure(s)
```

Target and CI:

```text
contract consistency: all checks passed     (copy-script target)
required_files: 69, missing: []
bash -n OK
```

## Scope Result

Within scope. No specification, ADR, port, data model, dependency, or
architecture boundary changed. The change is confined to one filter inside
`check_references`.

## Routing and Compatibility

- Capability class: deterministic tooling for verification; strong reasoning
  agent for choosing an inclusion filter over a narrower exclusion list, after
  the exclusion list produced a second, different self-reference.
- Displayed model / reasoning setting: Claude Opus 5, default.
- Compatibility state: default routing; stdlib-only Python 3.
- Escalation reason: contract tooling changed.

## Next Action

Resubmit. Three rounds of this script's own comments and regex literals have
now individually triggered its reference check — the self-inspection this
Preflight repeats every round is not optional ceremony; it has caught a real
defect in three of the last three rounds before submission.
