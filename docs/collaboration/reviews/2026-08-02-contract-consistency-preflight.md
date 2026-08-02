# Preflight Validation Record

Per ADR 0013. **Not an approval.** It permits submission to an independent
Reviewer and nothing else.

## Target

- Change: `scripts/check-contract-consistency.py`, its CI wiring and
  distribution, and the three defects its first run found.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-contract-consistency-check.md`
  (DA-2026-08-02-07).
- Branch: `process/contract-consistency-check`, stacked on
  `process/mirror-new-rules-and-adr-range` (pull request #7).
- Producer of this Preflight: Implementer, Claude Opus 5 via Claude Code.
  Per ADR 0013 this producer cannot review the same change.

## Result

**pass** — submit to an independent Reviewer.

## Checks

| # | Check | Result |
|---|---|---|
| 1 | Checker passes on the template repository | pass |
| 2 | Checker passes inside a fresh copy-script target | pass |
| 3 | Checker detects every defect class it claims to cover | pass — negative test below |
| 4 | CI required files | pass — 65 entries, 0 missing |
| 5 | ADR existence `0001`–`0013` | pass |
| 6 | Script syntax `bash -n` | pass |
| 7 | Conflict markers | pass — none |
| 8 | Distribution: the checker ships and CI asserts it runs in the target | pass |

## Command Output

Negative test — a copy of the tree with one defect of each class injected:

```text
mirror parity:
  copilot does not state 'Prime Directive' (no match for /No execution without a
  recorded design agreement/)

parity completeness:
  AGENTS.md section 'A Brand New Rule' is not classified. Add it to
  MIRRORED_SECTIONS with a pattern, or to AGENTS_ONLY_SECTIONS with a reason.

references:
  docs/collaboration/definition-of-done.md:116 names
  'docs/collaboration/does-not-exist.md', which does not exist

ADR range:
  README.md states ADRs 0001-0011; the repository has 0001-0013

version claims:
  CHANGELOG.md heading 'v9.9.9' has no matching git tag. Mark the section
  unreleased, or tag it.

contract consistency: 5 failure(s)
exit=1
```

Clean tree, and a fresh target produced by the copy script:

```text
contract consistency: all checks passed     (template repo)
contract consistency: all checks passed     (copy-script target)
```

Remaining:

```text
required_files: 65, missing: []
ADR OK
bash -n OK
no conflict markers
```

## Defects the Checker Found on Its First Run

All three were reproduced by hand before being fixed. None was allowlisted.

1. `docs/collaboration/reviews/` — the directory every review record must live
   in — was named in **one of nine** contract files. An agent under any other
   tool knew which template to use and not where to put the result.
2. `.github/copilot-instructions.md` had **no Prime Directive at all**. It
   opened at "Role and Context" and never stated the five directive lines.
3. `CLAUDE.md` and the Grok and Cursor sets likewise lacked the review-record
   location.

A fourth reported failure was a defect in the checker, not the tree: the
version-banner pattern captured a trailing sentence period. Fixed in the
checker.

## Scope Result

Within the agreement's scope. No specification, ADR, port, data model,
dependency, or architecture boundary changed. The checker encodes rules the
contract already states; it introduces none.

One boundary deserves the Reviewer's attention: the checker crashed on its
first run inside a copy-script target, because `README.md` and `CHANGELOG.md`
are not distributed. It now skips template-only files there. That fix is the
kind that can silently disable a check — verify that the skipping is confined
to files an adopting project genuinely does not receive.

## Routing and Compatibility

- Capability class: deterministic tooling for all verification; strong
  reasoning agent (Claude Opus 5) for the checker's design and the parity
  classification.
- Displayed model / reasoning setting: Claude Opus 5, default.
- Compatibility state: default routing; stdlib-only Python 3.
- Escalation reason: the agent operating contract file set changed, and a new
  script joins the distribution.

## Next Action

Submit to an independent Reviewer. Still open and **not** discharged here: an
approving review of this branch, of pull request #7 beneath it, and of the
`v1.0.1` fixes already on `main`.
