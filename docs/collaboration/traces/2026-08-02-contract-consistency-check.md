# AI Work Trace

## Request

- Date: 2026-08-02
- User request: fix it with the recommended approach and get the review to
  pass.
- Active persona: Implementer.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-contract-consistency-check.md`
  (DA-2026-08-02-07).
- Current phase: Architecture Path.
- Canonical issue or work plan: none.
- AI planning record: the Plan table in that agreement.

## Context Ledger

- Included: the nine contract files; `README.md`; the QUICKSTART pair;
  `CHANGELOG.md`; `.github/workflows/ci.yml`;
  `scripts/lib/collaboration-template-paths.sh`; the three review records that
  established the recurring defect class.
- Omitted: ADR bodies, which the checker does not interpret; documents no check
  reads.
- Assumptions:
  - "Get the review to pass" means make the artifact correct enough to survive
    an honest review, not steer the Reviewer. Recorded as a Settled Ambiguity
    because the opposite reading would corrupt the gate this whole contract
    exists to protect.
  - A finding gets fixed or its suppression gets justified in the script.
- Open decisions: the row in the agreement's Deferred Questions.

## Routing

- Model/assistant/tool: Claude Opus 5 via Claude Code; verification by the new
  checker, `bash -n`, the copy smoke test, and a negative test.
- Capability class: deterministic tooling for verification; strong reasoning
  agent for the checker's design, the parity classification, and the reading of
  the Director's instruction.
- Reason: the design question — how a parity list avoids drifting itself — is
  not mechanical; everything downstream of it is.
- Privacy constraints: none.

## AI Execution Records

### Attempt 1

- Agent: Claude Code
- Environment: local clone, branch `process/contract-consistency-check`,
  rebased onto `main` at `c15dcf3`
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
- Scope: the checker, its CI wiring and distribution, and the defects its first
  run found.
- Result: complete.
- Attempt boundary: single continuous session.
- Notes: the checker found three real defects on its first run, and its own
  smoke test found a defect in the checker — it crashed inside a copy-script
  target, because `README.md` and `CHANGELOG.md` are not distributed. A
  checker that cannot run where the contract lands is not a checker.

## Cost / Reasoning Control

- Operating path: Architecture Path.
- Files read: as listed in the Context Ledger.
- Context intentionally omitted: record bodies beyond the three review records.
- Deterministic checks used: recorded in
  `docs/collaboration/reviews/2026-08-02-contract-consistency-preflight.md`.
- Escalation reason: the contract file set changed and a script joined the
  distribution.
- Avoided LLM work: the checker replaces the hand-built grep matrix that had
  been rebuilt from scratch in each of three review rounds. That is the entire
  point of the change — the comparison is now a command instead of an act of
  attention.
- Rework caused by AI output: the version-banner pattern captured a trailing
  sentence period and reported a false failure; the checker crashed in a
  distributed target. Both found by running it rather than reasoning about it,
  and both fixed.

## Decisions Carried

- Director decisions: apply the recommended approach; get the review to pass.
- Implementer decisions: ship the checker to adopting projects rather than keep
  it in the template; Python 3 stdlib; make the rule list self-checking by
  failing on an unclassified `AGENTS.md` section; fix every finding rather than
  allowlist it.
- Reviewer decisions: **approved** the change beneath this one (pull request
  #7, commit `21a6c17`) for specification-conformance, boundary-conformance,
  and evidence-sufficiency, after rejecting its first round. Its non-blocking
  finding about a stale line in that change's design agreement is fixed here,
  so the approved commit stayed the merged one.
- Arbiter decisions: none.

## Verification

- Commands/checks and output: recorded in
  `docs/collaboration/reviews/2026-08-02-contract-consistency-preflight.md`.
- Summary: the checker passes on the template repository and inside a fresh
  copy-script target; a negative test with one defect of each class injected
  produces exactly five failures and a non-zero exit; `required_files` 65 with
  0 missing; ADRs `0001`-`0013` present; `bash -n` clean; no conflict markers;
  CI now runs the checker and the smoke test executes it inside the target.
- Not verified: CI itself, and independent review of this change.

## Changed Files

- Added: `scripts/check-contract-consistency.py`, the covering design
  agreement, the Preflight record, this trace.
- Updated: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `.grok/rules/03-collaboration-and-completion.md`,
  `.cursor/rules/03-collaboration-and-completion.mdc`,
  `.github/workflows/ci.yml`, `scripts/lib/collaboration-template-paths.sh`,
  `README.md`, `QUICKSTART.md`, `QUICKSTART.ja.md`, `CHANGELOG.md`,
  `docs/collaboration/agreements/2026-08-02-mirror-parity-and-adr-range.md`.

## Next Safe Action

Independent Reviewer review of this change. If it approves, tag `v1.1.0` and
move both README banners in the same commit, which is the condition the
changelog states.

## Notes

Three review rounds found the same defect class and each rebuilt the same
comparison by hand. This change makes the comparison a command, and the command
immediately found three more instances of the class — including that
`docs/collaboration/reviews/`, the directory every review record must live in,
was named in one of nine contract files, and that
`.github/copilot-instructions.md` had no Prime Directive at all.

Neither had broken anything. Both had been read past by three reviews.
