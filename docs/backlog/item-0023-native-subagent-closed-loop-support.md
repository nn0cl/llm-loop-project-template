# Backlog item: item-0023-native-subagent-closed-loop-support

## Metadata

- Item ID: item-0023
- Title: Adopt native subagent improvements that demonstrably support the complete backlog-to-close loop
- Status: promoted
- Created: 2026-10-01
- Updated: 2026-10-01
- Priority hint: high
- Suggested planning size: M
- Owner/agent (optional): unassigned
- Active persona at intake: Planner
- Operating path: Architecture Path, design intake only

## Summary

The Director wants recent native subagent improvements incorporated when they actually support the existing loop from approved backlog intake through design, implementation, deterministic tests, independent review, finding correction, and closure. Additional parallelism alone does not meet the desired outcome.

First establish the delta from the existing portable parent-child baseline, support survey, and check-and-spawn protocol. The complete loop is already the project's intended operating design; this item evaluates tool support and necessary compatibility improvements, not construction of a new loop.

Evaluate Codex, Claude Code, Grok Build, Cursor, GitHub Copilot, and Google Antigravity independently, separating each tool surface from the model/API surface. Claude Code is a current comparison target, not an assumed fully compatible baseline. Other relevant agents may be added when primary documentation establishes their relevance. The desired outcome is portable support with optional tool-specific mechanisms, not a Codex-only operating contract.

## Why it might matter

Existing instructions describe orchestration but do not establish that newly released primitives provide reliable execution of the whole loop. A supported path needs completion delivery, continuation, isolated implementation workspaces, artifact-only Reviewer input, recovery, and auditable lifecycle updates together.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes.
- Use the Director's existing billing environment. Cloud environments requiring a different billing arrangement are deferred. Do not assume an API feature is included in a ChatGPT/Codex subscription, or that current billing has been verified.
- Additional paid subscriptions, API consumption outside existing coverage, and hosted orchestration are not authorized by this item.
- Backlog creation alone must not trigger implementation: preserve the existing Director approval/promotion gate.
- Preserve the existing Director work-plan closing checkpoint. Supporting closure includes preparing the approved result and recording the Director's close; automatic removal of this checkpoint is not authorized.
- Preserve Red/Green/Refactor discipline, separate-context Reviewer approval, verification evidence, intervention gates, and resume-before-duplicate-spawn.
- No change to contracts or production orchestration is authorized by capture of this item.

## Evaluation requirements

Before recommending adoption, demonstrate one bounded end-to-end fixture:

1. Approved backlog scope starts or resumes the design layer once; unapproved scope does not execute.
2. Design artifacts and the executable agreement/work plan are recorded before implementation dispatch.
3. Implementation runs in its dedicated branch/worktree and records phase verification and self-review.
4. Child completion reliably reaches the parent and starts the next eligible step, including when the parent's active turn has ended. State any requirement to keep the parent session/client alive.
5. A fresh Reviewer receives only authoritative artifacts and deterministic evidence, excluding producer chat history.
6. A deliberate review rejection generates a finding, correction, re-verification, and independent confirmation before completion.
7. Interruption or failure resumes recorded state without duplicated workers or skipped verification.
8. The approved result reaches the Director's existing closing checkpoint; after the Director closes, backlog disposition and linked lifecycle records are updated consistently.

Record tool/version/surface, supplied inputs, command/event outputs, resulting artifacts, billing prerequisites, and Verified/Inferred/Unknown status. Identify remaining gaps rather than claiming that native delegation proves end-to-end support. Prefer disposable fixture artifacts over exercising an unapproved real implementation item.

Produce a per-tool, per-stage coverage matrix for approved-backlog intake, design dispatch, isolated implementation, tests and evidence, independent review, finding correction, continuation/recovery, and Director close/lifecycle recording. For each cell state: native support, support requiring an auxiliary mechanism, unsupported, or unconfirmed; cite its grounds separately from live verification status. Name what an adopter must configure and what still requires manual relay. Do not reduce coverage to one percentage that conceals a missing mandatory gate. Features unavailable under the existing billing environment remain deferred or documentation-only, with the limitation stated.

## Uncertainty

- [ ] Spec can be written now
- [x] Spike required first (end-to-end feasibility, lifecycle delivery, context isolation, and billing coverage are unverified)
- [ ] Human decision required beyond the existing closing checkpoint; raise one if billing or architecture scope changes

## Codex update grounds and adoption checks

Source: [official ChatGPT and Codex changelog](https://learn.chatgpt.com/docs/changelog), retrieved 2026-10-01. These are CLI release facts; equivalent availability in the desktop app must be checked separately.

| Release | Documented change | Relevance and remaining check |
| --- | --- | --- |
| 2026-09-22, CLI 0.156.0 | Agent Command Center can create worktree sessions; worktree support enabled by default | Easier workspace isolation. Does not establish automatic worktree isolation for every subagent; verify dispatch configuration. |
| 2026-09-22, CLI 0.156.0 | Preserve streamed answers and plans when turns fail, are interrupted, or receive subagent completion events | Reduces information loss. Does not prove completion starts the next phase or wakes an idle parent; exercise those cases. |
| 2026-09-22, CLI 0.156.0 | Restore Plan mode when resuming sessions | Relevant to recovery. Verify repository phase/persona state from artifacts rather than relying on the UI mode. |
| 2026-09-29, CLI 0.159.0 | Opt-in `instant_interrupt` permits steering during model responses and long-running Code Mode calls | Relevant to Director intervention. Verify partial execution evidence and safe continuation. |
| 2026-09-29, CLI 0.159.1 | Add GPT-6.1 Sol as the default in bundled model catalogs | Model-selection update, not evidence of a new orchestration or automatic-closing capability. |

[Current Codex subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents) describes spawning, follow-up instructions, waiting, and closing agent threads. These capabilities are existing baseline support; the documentation alone does not date them to the recent release. Agent-thread closure is not the repository's backlog disposition or Director work-plan close.

[Responses API Multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent) is a separate API surface with delegation and collaboration primitives, including context propagation controls. Its support for Sol 6.1 does not establish inclusion in the Director's existing Codex billing environment. Defer adoption when it requires a different billing arrangement.

No retrieved source establishes that the entire approved-backlog-to-close loop now runs automatically. The target is to test workspace isolation, completion-triggered continuation, interruption/recovery, and artifact-only Reviewer input against the existing loop. Benefits in the table are candidate applications of documented changes, not measured results.

## Links

- Research intake: ../collaboration/traces/2026-10-01-cross-tool-release-design-intake.md
- Existing portable-loop backlog: item-0007-multi-agent-tool-loop-portability.md
- Existing wakeup backlog: item-0020-self-sustaining-group-wakeup-loop.md
- Existing tool survey: item-0021-ai-tool-support-status-survey.md
- Existing wakeup agreement: ../collaboration/agreements/2026-08-20-self-sustaining-wakeup-protocol.md
- Existing survey spike: ../spike/case-0004-ai-tool-support-status-survey/case.md
- Spike case: ../spike/case-0005-native-subagent-loop-support/case.md
- Work plan (when promoted): ../work-plans/WP-0027-native-subagent-loop-support.md
- Design agreement (when promoted): ../collaboration/agreements/2026-10-01-native-subagent-loop-support.md
- Local issue (LISS): ../issues/LISS-0074-native-subagent-support-research.md; LISS-0075
- Spec: none
- ADR: existing ADR 0016 and ADR 0017; no new ADR adopted
- Current official Codex subagent documentation: https://learn.chatgpt.com/docs/agent-configuration/subagents
- Responses API delegation is a separate surface: https://developers.openai.com/api/docs/guides/responses-multi-agent
- Cursor subagents: https://cursor.com/docs/subagents
- Grok Build: https://docs.x.ai/build/overview

## Promotion notes

- Date: 2026-10-01
- Decision: captured as a conditional adoption request, not promoted.
- Reason: The Director narrowed the desired outcome to complete-loop support and deferred cloud environments that change billing. End-to-end support and existing-plan coverage still need evidence; research findings alone do not authorize implementation.
- Scope clarification: The Director confirmed the existing project already defines the complete loop and requested a comparative assessment of Codex, Claude, and other AI agents. Evaluate compatibility with that existing loop, including the six named tools above; do not assume Claude Code is exempt from current verification.

### Director approval
- Date: 2026-10-01
- Decision: promoted.
- Director statement: “バックログ承認。進めて”.
- Scope: existing-loop compatibility research and necessary support within this item; different billing remains deferred. Earlier captured notes are historical.
