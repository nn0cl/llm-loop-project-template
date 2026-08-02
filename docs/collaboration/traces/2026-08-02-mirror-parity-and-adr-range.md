# AI Work Trace

## Request

- Date: 2026-08-02
- User request: check the latest state and carry out the continuation.
- Active persona: Implementer.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-mirror-parity-and-adr-range.md`
  (DA-2026-08-02-06).
- Current phase: Architecture Path.
- Canonical issue or work plan: none.
- AI planning record: the Plan table in that agreement.

## Context Ledger

- Included: the nine contract files; `README.md`; `QUICKSTART.md`;
  `QUICKSTART.ja.md`; `CHANGELOG.md`; `docs/architecture/README.md`; ADRs 0012
  and 0013 and the commit that added them; `.github/workflows/ci.yml`.
- Omitted: the bodies of the agreements, specs, issues, and review records that
  arrived with ADRs 0012 and 0013 — read only far enough to confirm the two
  ADRs are accepted and covered, since this change propagates them rather than
  revising them.
- Assumptions:
  - The parallel work is authoritative. It arrived on `main` with its own
    agreements and review records; this change does not second-guess it.
  - `.grok/rules/*` and `.cursor/rules/*` satisfy parity as a set, per ADR
    0006's effective-union rule, so the mirrored rules belong in each set's
    `03-collaboration-and-completion` file rather than in all three.
- Open decisions: the two rows in the agreement's Deferred Questions.

## Routing

- Model/assistant/tool: Claude Opus 5 via Claude Code; deterministic checks via
  `grep`, `bash -n`, the link and anchor checkers, and the copy smoke test.
- Capability class: deterministic tools for the checks; strong reasoning agent
  for the audit and the parity judgment.
- Reason: the defects were found by comparing files against each other, which
  is what an audit costs; the repairs themselves were mechanical.
- Privacy constraints: none.

## AI Execution Records

### Attempt 1

- Agent: Claude Code
- Environment: local clone, branch `process/mirror-new-rules-and-adr-range`,
  based on `main` at `3ba0219`
- Model as displayed: Claude Opus 5
- Reasoning setting as displayed: default
- Estimated token range: not recorded
- Estimated token midpoint: not recorded
- Actual tokens: unavailable
- Token metric: unavailable
- Token source: unavailable
- Token attribution boundary: unavailable
- Actual token unavailable reason: the harness does not surface per-session
  token counts to the agent.
- Estimate variance: not applicable
- Variance reason: not applicable
- Scope: mirror parity for two rules; the process-ADR range; the changelog
  entry; a Preflight record.
- Result: complete.
- Attempt boundary: single continuous session.
- Notes: the state changed underneath this session. Two ADRs, two agreements,
  two specs, two local issues, three review records, and two traces landed on
  `main` from work outside it while an independent review was running, and
  pull request #6 was merged by someone other than this session. The first
  action was to establish what had changed rather than to continue from
  memory.

## Cost / Reasoning Control

- Operating path: Architecture Path.
- Files read: as listed in the Context Ledger.
- Context intentionally omitted: the record bodies of the parallel work.
- Deterministic checks used: recorded in
  `docs/collaboration/reviews/2026-08-02-mirror-parity-preflight.md`.
- Escalation reason: contract files changed.
- Avoided LLM work: the parity gap was found with a `grep` matrix over nine
  files rather than by reading them; the mirrored text was copied from the
  accepted `AGENTS.md` wording rather than re-authored, so no rule could drift
  in restatement.
- Rework caused by AI output: none in this round.

## Decisions Carried

- Director decisions: check the latest state and continue.
- Implementer decisions: mirror the accepted wording verbatim rather than
  paraphrase; place it in each rule set's `03` file; move the adopter's
  starting ADR number to `0014`; ship one `v1.1.0` rather than tag a `v1.0.1`
  that no commit isolates.
- Reviewer decisions: none. This change has a Preflight `pass`, which is not an
  approval.
- Arbiter decisions: none.

## Verification

- Commands/checks and their output: recorded in the Preflight record at
  `docs/collaboration/reviews/2026-08-02-mirror-parity-preflight.md`.
- Summary: parity matrix passes for all nine contract files as sets; 0 stale
  ADR-range statements; ADRs `0001`-`0013` present; `required_files` 64 with 0
  missing; `bash -n` clean; no conflict markers; link audit 0 defects; anchor
  audit 0; copy smoke test passes and the distributed target carries both rules
  for every tool.
- Not verified: CI itself, and independent review — outstanding for this change
  and, separately, for the `v1.0.1` fixes merged in pull request #6.

## Changed Files

- Added: the covering design agreement, the Preflight record, this trace.
- Updated: `.github/copilot-instructions.md`,
  `.grok/rules/03-collaboration-and-completion.md`,
  `.cursor/rules/03-collaboration-and-completion.mdc`, `README.md`,
  `QUICKSTART.md`, `QUICKSTART.ja.md`, `CHANGELOG.md`.

## Next Safe Action

Independent Reviewer review of this change, in a separate context. Then tag
`v1.1.0`.

The `v1.0.1` fixes on `main` remain unverified by any Reviewer: the
re-verification terminated on a session limit before reaching a decision, and
pull request #6 was merged before it could be restarted. That obligation is
still open and is not discharged by this change.

## Notes

Two rules were added to the contract and reached only two of the nine files
that carry it. An agent running under Copilot, Grok, or Cursor would have had
no way to learn from its own contract that Preflight Validation was mandatory
before review — while the ADR that mandates it sat accepted in the same
repository.

The same audit found the entry documents still telling adopting projects to
number their ADRs from `0012`, in the same commit range where the template took
`0012` and `0013` for itself. Neither defect broke a link or a build. Both were
visible only by holding two documents side by side and asking whether they
still agreed.

---

## Round 2: response to the Reviewer's rejection

The independent Reviewer rejected both this branch and the `v1.0.1` fixes
already on `main`. Both findings were reproduced before being fixed.

- **Mirror obligation half-applied.** The first edition's rejection had named
  three documents unreachable from the contract files, and required the fix in
  `AGENTS.md`, `.github/copilot-instructions.md`, and
  `.grok/rules/01-quickstart.md`. Only `AGENTS.md` was fixed. Copilot and Grok
  are full mirrors and carried none of the three; the gap survived the merge of
  pull request #6 and this branch's first round. Now fixed in both.
  `.cursor/rules/*` is exempt as a complements-only set that receives root
  `AGENTS.md` natively, per ADR 0006.
- **A version claimed as released.** `CHANGELOG.md` said `v1.1.0` "shipped"
  while no such tag existed and both READMEs bannered `v1.0.0` — a direct hit
  on this agreement's own Falsification Criterion 3. The section is now marked
  unreleased and names the condition for tagging.

Round-1 Preflight returned `pass` and the Reviewer still rejected. That is the
concrete case of the risk ADR 0013 states about itself: a checklist that passes
is not evidence that a change is correct. Both Preflight records are kept so the
pair is auditable — `2026-08-02-mirror-parity-preflight.md` and
`2026-08-02-mirror-parity-preflight-2.md`.

Still open after this round: an approving review of this branch, and of the
`v1.0.1` fixes on `main`.
