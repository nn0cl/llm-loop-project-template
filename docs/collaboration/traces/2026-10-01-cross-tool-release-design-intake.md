# Cross-tool release research: design intake

## Request and authority

- Date: 2026-10-01 (Asia/Tokyo).
- Active persona: Planner.
- Current phase: design intake only; no implementation phase authorized.
- Operating path: Architecture Path intake, because possible follow-ups affect orchestration, review, and execution boundaries.
- Covering design agreement: none for these new candidates. The Director requested project understanding and a summary of useful recent capabilities, with Codex, Grok, and Cursor portability.
- Planning size: not assigned; candidates need individual sizing during planning.
- Issue/work plan: none created. This record captures research, not promotion or execution authority.

## Inspected context

README.md, agent-quickstart.md, loop-settings.toml, backlog policy, model-tool-capability-matrix.md, ai-request-routing.md, privacy-context-budget-policy.md, runner-cli-contract.md, definition-of-done.md, ADR 0017, backlog items 0007/0020/0021, case-0004, and relevant issue metadata were inspected. No application code or private external account content was needed. Existing findings LISS-0070 through LISS-0073 are marked done; mirror and citation drift remain useful failure scenarios for any future contract change.

The template tests whether written contracts and verification can sustain development without a human inside each work-plan loop. Separate Reviewer context, deterministic evidence, and falsification are essential. Capability-based routing already avoids commercial model names. Prior portability, wakeup, and support-survey work must be reused rather than recreated.

## Source-grounded observations

Retrieved official sources on 2026-10-01:

- [ChatGPT/Codex changelog](https://learn.chatgpt.com/docs/changelog): Sol 6.1 is dated September 29; CLI 0.159.1 adds its default catalog entry; 0.159.0 adds opt-in instant interruption.
- [Weekly product update](https://learn.chatgpt.com/docs/whats-new/september-28-october-2-2026): describes dots, reusable cloud environments, Security Cloud preview, cross-device Work, Space, and Ultrafast. A weekly listing does not establish that every feature launched September 29 or 30.
- [API changelog](https://developers.openai.com/api/docs/changelog): September 29 adds Sol 6.1, Responses multi-agent beta support, Agents API computer use, and Astra Ultrafast. Agents API itself is dated September 10.
- [Responses multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent): model-directed delegation; concurrent agents can increase cost; context propagation is configurable. An independent context window alone does not prove artifact-only Reviewer input.
- [Cursor subagents](https://cursor.com/docs/subagents): clean initial context, parent-supplied task context, editor/CLI/cloud support.
- [Cursor automations](https://cursor.com/docs/cloud-agent/automations): schedule and source-control/event triggers.
- [Grok Build overview](https://docs.x.ai/build/overview): headless execution, streaming JSON, ACP, and configuration inspection. This is not evidence that Grok has dots-equivalent persistent autonomy.
- [Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments) and [Security setup](https://learn.chatgpt.com/docs/security/setup) were retrieved as follow-up references.

Compatibility is Inferred from documentation, not Verified by live execution. Product performance claims are vendor claims, not project measurements. Account availability and paid-plan eligibility were not tested.

## Candidate recommendations, not decisions to adopt

1. High: refresh the existing cross-tool capability survey with version, surface, checked date, source, compatibility state, and a small repeatable smoke-test protocol. Track instruction loading, independent review context, workspace isolation, completion signals, interruption, hooks, and resumption separately.
2. High: validate artifact-only Reviewer handoff across tools. Record the exact supplied artifacts and revision; test that producer chat history is excluded. Worktree isolation and conversation isolation are different properties.
3. High: extend the existing wakeup work with portable event/schedule adapters. Require approved backlog scope, intervention-gate checks, duplicate-execution prevention, bounded cost, and artifact-based recovery. Dots and Cursor Automations are optional implementations, not governing authorities.
4. Medium: benchmark role-based model selection after releases. Measure defect detection, phase/boundary conformance, total cost including rework, and elapsed time against fixed repository tasks. Sol 6.1 is a candidate configuration; do not hard-code it as template policy.
5. Medium: define reproducible execution-environment evidence, including setup revision, tool versions, verification commands/output, and isolation. Reusable cloud environments are optional alongside local worktrees and CI.
6. Medium: import security-scanner findings into the existing review-finding lifecycle, with reproduction and deterministic verification. Scanner output does not constitute Reviewer approval. Start with existing local tools; cloud products remain optional.
7. Medium: test mid-execution Director intervention, distinguishing clarification, scope reopening, cancellation, and resume. Native interruption is a transport; record the governing decision and partial execution evidence.
8. Low / spike first: browser-driven verification and portable workflow skills. Capture reproducible fixtures and evidence; evaluate UI instability and skill distribution separately. Never move template authority into vendor plugins.

Space can be an optional discussion/display surface while Git artifacts remain authoritative. Voice and Ultrafast are lower-priority conveniences; their value is unmeasured and neither is required for the loop.

## Verification and open decisions

Read-only command observations: `git status --short` returned no entries before this record; `git branch --show-current` returned `main`. Relevant issue status searches returned `done` for LISS-0070, LISS-0071, LISS-0072, and LISS-0073. Shell reads completed with exit code 0, except optional absent-file/glob probing; absent probes are not evidence of missing functionality.

No tests, adapters, contracts, settings, schedules, or approvals were changed. No implementation approval or independent Reviewer approval is claimed. Deterministic verification of product capabilities remains a future spike task; web documentation is evidence of documented behavior only.

Next action: Director prioritization of candidates, followed by scoped backlog capture and design planning. Implementation requires its own covering agreement, persona, path, phase, acceptance/evidence contracts, and separate review where required.

## Director clarification and documentation update

The Director clarified that the existing project already defines the complete backlog-to-close loop. The intended improvement is compatibility with new native agent capabilities, not creation of that loop. Candidate [item-0023](../../backlog/item-0023-native-subagent-closed-loop-support.md) captures this scope and comparative coverage of Codex, Claude Code, Grok Build, Cursor, GitHub Copilot, and Antigravity. It remains captured, not promoted. Cloud environments or API adoption requiring a different billing arrangement are deferred; current account coverage is unverified.

The Director subsequently requested explicit Codex update grounds and then authorized updating these documents. The backlog now distinguishes CLI 0.156.0 worktree, completion/interruption preservation, and Plan-mode resumption changes (September 22), CLI 0.159.0 opt-in `instant_interrupt`, and CLI 0.159.1 Sol 6.1 catalog changes (September 29), citing the official changelog. Existing subagent orchestration and the separate Responses API Multi-agent surface are distinguished from these dated updates. No claim of verified end-to-end automation is made.

Scope: research and backlog documentation only; no contract, implementation, billing, or automation change. Active persona remains Planner, phase remains design intake. Verification uses `git diff --check` and a deterministic check of required release/source references in both updated files; output is recorded below after execution.

Verification output (exit code 0; `git diff --check` produced no diagnostics):

```text
PASS: release references, official sources, captured status, and clarification record
```
