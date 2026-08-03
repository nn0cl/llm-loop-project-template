# Preflight Validation Record

Per ADR 0013. **Not an approval.** It permits submission to an independent
Reviewer and nothing else.

## Target

- Change: `LISS-0003` — give `CODE_PATH` its own reference filter, and name
  the reference checker's self-reference history in the module disclosure.
- Local issue: `docs/issues/LISS-0003-code-path-filter-and-disclosure-history.md`.
- Originating review record:
  `docs/collaboration/reviews/2026-08-02-contract-consistency-review-6.md`.
- Branch: `process/review-issues-minor-fix-path`.
- Producer of this Preflight: Implementer, Claude Opus 5 via Claude Code.
  Per ADR 0013 this producer cannot review the same change.

## Result

**pass** — submit to an independent Reviewer.

## Checks

| # | Check | Result |
|---|---|---|
| 1 | `CODE_PATH` rejects a regex-noise self-reference independently of the `*` filter | pass |
| 2 | `CODE_PATH` still accepts a real reference (`docs/foo.md`-shaped) | pass |
| 3 | Disclosure names the self-reference history | pass — read-through |
| 4 | Negative test, six classes together | pass — 6 failures, exit 1 |
| 5 | Clean tree | pass |
| 6 | Fresh copy-script target | pass |
| 7 | CI required files | pass — 69, 0 missing |
| 8 | ADR existence `0001`-`0011` | pass |
| 9 | `bash -n` | pass |

## Command Output

`CODE_PATH` filtering in isolation, without the `*` filter in the path at all:

```text
'`docs/foo.md`'    -> target='docs/foo.md'     accepted=True
'`\d{4}.md`'        -> target='\d{4}.md'        accepted=False
'`0001-\*\.md`'    -> target='0001-\*\.md'     accepted=False
```

Negative test, six classes together (including the round-5/6 `LICENSE` and
version-claim regressions this fix does not reopen):

```text
mirror parity:      copilot does not state 'Prime Directive'
parity completeness: AGENTS.md section 'A Brand New Rule' is not classified.
references:          README.md:330 names 'LICENSE'
                     docs/collaboration/personas.md:171 names 'does-not-exist-anywhere.md'
ADR range:           README.md: expected range statement not found (...)
version claims:      README.md:6 names v9.9.9, which has no git tag.

contract consistency: 6 failure(s)
```

Clean tree, target, CI:

```text
contract consistency: all checks passed     (template repo)
contract consistency: all checks passed     (copy-script target)
required_files: 69, missing: []
ADR OK
bash -n OK
```

## Scope Result

Within scope. Planning size S, single attempt, no specification, ADR, port,
data model, dependency, or architecture boundary changed. Confined to
`scripts/check-contract-consistency.py`: one shared filter function replacing
two inline copies, and one paragraph added to the module docstring.

## Routing and Compatibility

- Capability class: deterministic tooling for verification; lightweight
  reasoning for the narrow, mechanical correction itself.
- Displayed model / reasoning setting: Claude Opus 5, default.
- Compatibility state: default routing; stdlib-only Python 3.
- Escalation reason: none — this is Minor Fix Path, not Architecture Path.

## Next Action

Submit to an independent Reviewer for separate confirmation, per ADR 0012's
Minor Fix Path requirement.
