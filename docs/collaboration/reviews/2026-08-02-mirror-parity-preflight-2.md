# Preflight Validation Record (round 2)

Per ADR 0013. **Not an approval.** It permits resubmission to an independent
Reviewer and nothing else.

## Target

- Change: the two defects the Reviewer rejected in
  `docs/collaboration/reviews/2026-08-02-mirror-parity-and-v101-review.md`.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-mirror-parity-and-adr-range.md`
  (DA-2026-08-02-06).
- Branch: `process/mirror-new-rules-and-adr-range`.
- Producer of this Preflight: Implementer, Claude Opus 5 via Claude Code.
  Per ADR 0013 this producer cannot review the same change.
- Preceding Preflight: `2026-08-02-mirror-parity-preflight.md` (round 1,
  `pass`). Round 1 passed and the Reviewer still rejected — recorded here
  because it is the evidence for ADR 0013's own stated risk that "a weak
  checklist can create false confidence".

## Result

**pass** — resubmit to an independent Reviewer.

## Defects Addressed

| # | Reviewer finding | Fix | Verification |
|---|---|---|---|
| 1 | The reading-sequence references to `external-resource-adoption-contract.md`, `ai-failure-recovery.md`, and `runner-cli-contract.md` were added to `AGENTS.md` only. Copilot and Grok are full mirrors and carried none of them. | Added to `.github/copilot-instructions.md` and `.grok/rules/01-quickstart.md` | occurrence matrix below |
| 2 | `CHANGELOG.md` said `v1.1.0` "shipped", while no such tag exists and both READMEs banner `v1.0.0`. | The section is marked **unreleased**, states that the released edition is still `v1.0.0`, and names the condition for tagging | `git describe`, README banner, changelog text |

`.cursor/rules/*` is intentionally not in the fix for defect 1: it is a
complements-only set, and ADR 0006 records that Cursor loads root `AGENTS.md`
natively, so the reference reaches Cursor through that path. Copilot and Grok
are full mirrors and must carry it themselves.

## Checks

| # | Check | Result |
|---|---|---|
| 1 | Three documents reachable from every full-mirror contract file | pass |
| 2 | No version claim unsupported by a tag | pass |
| 3 | ADR existence `0001`–`0013` | pass |
| 4 | CI required files | pass — 64 entries, 0 missing |
| 5 | Script syntax `bash -n` | pass |
| 6 | Dangling references | pass — 5 known false positives, 0 defects |
| 7 | Dangling anchors | pass — 0 |

## Command Output

```text
=== reading-sequence references, full-mirror files ===
AGENTS.md                                     ext-res:1 failrec:1 runner:1
CLAUDE.md                                     ext-res:1 failrec:1 runner:1
.github/copilot-instructions.md               ext-res:1 failrec:1 runner:1
.grok/rules/01-quickstart.md                  ext-res:1 failrec:1 runner:1

=== version claims ===
$ git describe --tags HEAD
v1.0.0-6-g2d83262
README.md:6:**Contract edition: v1.0.0.**
CHANGELOG.md: "## v1.1.0 — ... (unreleased)" / "No `v1.1.0` tag exists yet"

=== remaining ===
ADR OK
required_files: 64, missing: []
bash -n OK
5 dangling reference(s)   (known false positives; 0 defects)
0 dangling anchor(s)
```

## Scope Result

Within the agreement's scope. No specification, ADR, port, data model,
dependency, or architecture boundary changed.

## Routing and Compatibility

- Capability class: deterministic tools for every check; strong reasoning agent
  (Claude Opus 5) for classifying the Cursor exemption.
- Displayed model / reasoning setting: Claude Opus 5, default.
- Compatibility state: default routing.
- Escalation reason: the agent operating contract file set changed.

## Next Action

Resubmit to an independent Reviewer. Two obligations remain open and are **not**
discharged by this record: an approving review of this branch, and an approving
review of the `v1.0.1` fixes already merged to `main`, of which four of five
were confirmed fixed and the fifth is fixed here.
