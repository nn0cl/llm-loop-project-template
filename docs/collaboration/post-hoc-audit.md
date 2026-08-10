# Post-Hoc Audit

Inside a work plan the Director is not a gate. Correctness depends on the
written contract and on artifacts that remain after the session ends. This
document states what "later confirmation" requires.

Governed settings: `docs/collaboration/loop-settings.toml` → `[audit]`.
Policy overview: `docs/collaboration/loop-settings.md`.

## Principle

If a fact exists only in a chat transcript, it did not happen for audit
purposes. A later reader (human or agent) must be able to answer:

1. What was agreed to be built?
2. What was actually changed?
3. What was verified, with command output?
4. What was rejected or found wanting, and what was done about it?
5. What remains open?

without access to the original LLM session.

## Minimum artifact set

| Question | Where to look |
| --- | --- |
| Direction and boundaries | `docs/collaboration/agreements/` |
| Behavior promised | `docs/specs/` |
| Structure/policy decisions | `docs/architecture/adr/` |
| Work breakdown | `docs/work-plans/`, `docs/issues/` |
| Uncertainty closed by research | `docs/spike/case-*/` |
| Candidates not yet promised | `docs/backlog/` |
| Phase work and routing | `docs/collaboration/traces/` |
| Self-review / phase gates | issue body, trace, or short-form self-review record |
| Independent review | `docs/collaboration/reviews/` |
| Findings and fixes | `docs/issues/LISS-*` with `Type: review-finding` |
| Settings (language, audit flags) | `docs/collaboration/loop-settings.toml` |
| Code and tests | git history, branch, PR |

## Rules for agents

1. **Write for the absent reader.** Prefer complete sentences in records;
   name persona, phase, agreement, and verification commands.
2. **Paste deterministic output** when `[audit].require_verification_output`
   is true (default). "Tests passed" without output is not evidence.
3. **Trace M+ and second attempts** when
   `[audit].require_traces_for_m_plus` is true (default). See
   `docs/collaboration/ai-work-trace-log.md`.
4. **No chat-only continuity.** When
   `[audit].artifact_only_continuity` is true (default), resume only from
   repository artifacts (`docs/collaboration/session-start-and-resume.md`).
5. **Language.** Write new record bodies in `[docs].language`.
6. **Findings.** Apply or formally decline; never leave actionable findings
   as session asides (`docs/collaboration/findings-reuse.md`).

## Rules for later human confirmation

At work-plan close (or any audit), prefer this order:

1. Open the design agreement and the Reviewer record.
2. Walk each issue: status, self-review evidence, verification output.
3. Confirm every finding from the review is `closed` or `wont_do` with
   Arbiter grounds.
4. Spot-check that spike selections match what landed in Spec/ADR/code.
5. Re-run named deterministic commands if trust in recorded output is low.

Reading in-progress chat is optional and never authoritative.
