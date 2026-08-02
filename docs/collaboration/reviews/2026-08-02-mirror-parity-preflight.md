# Preflight Validation Record

Per ADR 0013. This is **not an approval**. It permits submission to an
independent Reviewer and nothing else. It cannot establish specification
conformance, and it cannot set `wont_do` or `closed`.

## Target

- Change: mirror parity for Minor Fix Path and Preflight Validation, plus the
  process-ADR range correction.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-mirror-parity-and-adr-range.md`
  (DA-2026-08-02-06).
- Branch: `process/mirror-new-rules-and-adr-range`.
- Producer of this Preflight: Implementer, Claude Opus 5 via Claude Code.
  Per ADR 0013 this producer **cannot** review the same change.

## Result

**pass** — submit to an independent Reviewer.

## Checks

| # | Check | Command | Result |
|---|---|---|---|
| 1 | Contract-file parity for both new rules | per-file `grep -ci` matrix over the nine contract files | pass |
| 2 | No stale process-ADR range statement | `grep -rIn '0001-0011\|0001–0011\|0001〜0011'` excluding record directories | pass — 0 hits |
| 3 | ADR existence | loop over `0001`–`0013` | pass |
| 4 | CI required files | existence check over the list in `ci.yml` | pass — 64 entries, 0 missing |
| 5 | Script syntax | `bash -n` on all four scripts | pass |
| 6 | Conflict markers | `git grep -n -E '^(<<<<<<<\|=======\|>>>>>>>)'` | pass — none |
| 7 | Dangling references | link audit over every `.md`, `.mdc`, `.sh`, `.yml`, `.py` | pass — 5 hits, all the known `docs/templates/examples/` false positives, 0 defects |
| 8 | Dangling anchors | anchor audit | pass — 0 |
| 9 | Distribution | copy smoke test into a temp target | pass |

## Command Output

Parity matrix (`Minor Fix Path` / `Preflight` occurrence counts):

```text
AGENTS.md                                          MinorFix:1 Preflight:2
CLAUDE.md                                          MinorFix:1 Preflight:2
.github/copilot-instructions.md                    MinorFix:2 Preflight:3
.grok/rules/01-quickstart.md                       MinorFix:0 Preflight:0
.grok/rules/02-architecture-boundaries.md          MinorFix:0 Preflight:0
.grok/rules/03-collaboration-and-completion.md     MinorFix:2 Preflight:3
.cursor/rules/01-quickstart.mdc                    MinorFix:0 Preflight:0
.cursor/rules/02-architecture-boundaries.mdc       MinorFix:0 Preflight:0
.cursor/rules/03-collaboration-and-completion.mdc  MinorFix:2 Preflight:3
```

The zero rows are the two multi-file rule sets. ADR 0006 requires the
*effective union* of `.grok/rules/*` and of `.cursor/rules/*` to match
`AGENTS.md`, not each file individually; both rules live in each set's
`03-collaboration-and-completion` file.

Remaining checks:

```text
=== stale ADR range ===        none
ADR OK
required_files: 64, missing: []
bash -n OK
no conflict markers
5 dangling reference(s)   (all known false positives; 0 defects)
0 dangling anchor(s)
```

Copy smoke test — the distributed target after `--project-name`,
`--domain-summary`, `--stack`:

```text
smoke test OK; target has Preflight in:
AGENTS.md
CLAUDE.md
.github/copilot-instructions.md
.grok/rules/03-collaboration-and-completion.md
.cursor/rules/03-collaboration-and-completion.mdc
```

## Scope Result

Within the agreement's scope. No specification, ADR, port, data model,
dependency, or architecture boundary was changed. The wording mirrored into
the seven files is the wording already accepted in `AGENTS.md`.

## Routing and Compatibility

- Capability class: deterministic tools for every check above; strong reasoning
  agent (Claude Opus 5) for the audit that located the defects and for the
  mirroring decision.
- Displayed model / reasoning setting: Claude Opus 5, default.
- Compatibility state: default routing; nothing here depends on a non-default
  setting.
- Escalation reason: the change touches the agent operating contract file set,
  which is Architecture Path by
  `docs/collaboration/prompt-instruction-change-control.md`.

## Next Action

Submit to an independent Reviewer in a separate context. A Reviewer decision is
still required; this record does not substitute for one.

Note the outstanding obligation this record does not discharge: the `v1.0.1`
fixes merged in pull request #6 were never re-verified. The re-review
terminated on a session limit before reaching a decision.
