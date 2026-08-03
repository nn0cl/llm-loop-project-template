# Model and Tool Capability Matrix

Use this matrix to route AI-TDD collaboration tasks. It does not name specific
commercial models; it defines capability classes.

## Capability Classes

### Deterministic Tool

Use for:

- formatting.
- linting.
- dependency checks.
- tests.
- container/infra config validation.
- YAML parsing.
- import-boundary checks.

Reviewer approval:

- not required unless the tool changes files beyond the task scope.

### Code Assistant

Use for:

- small code completions.
- narrow test skeletons from clear Gherkin.
- mechanical edits with obvious local context.
- renaming within one module.

Reviewer approval:

- self-review required before an issue-level phase transition (not for every
  completion); work-plan-level Reviewer approval is required once, at the
  work plan's close.

### Lightweight Reasoning Model

Use for:

- design intake drafts.
- VO/DTO naming review.
- checklist completion.
- summarizing changed files.
- drafting handoff notes.

Reviewer approval:

- required when the output changes process rules or accepted tests. A change to
  process rules is also a reopening request to the Director.

### Strong Reasoning Agent

Use for:

- architecture boundary analysis.
- ambiguous requirements.
- ADR drafting.
- cross-file refactor planning.
- privacy-sensitive routing.
- resolving conflicts between instructions.

Reviewer approval:

- self-review required for issue-level phase transitions; work-plan-level
  Reviewer approval required once, at the close. ADR acceptance is a
  design-phase decision the Director takes part in, not a Reviewer approval.

## Compatibility State

Routing by capability class assumes the chosen provider, model, or tool
configuration actually works as expected. Record that assumption explicitly
using one of three states, per `docs/architecture/adr/
0010-ai-failure-recovery-and-runner-cli-contract.md`:

- **Verified**: the specific configuration was actually exercised and its
  behavior confirmed, not merely assumed from documentation.
- **Inferred**: the configuration is assumed to work based on documentation,
  a model/provider card, or general knowledge, without direct confirmation.
- **Unknown**: compatibility has not been checked at all.

Do not treat `inferred` or `unknown` as equivalent to `verified` when a
routing or recovery decision depends on the configuration actually working
(for example, automatic resume of an unconfirmed run in
`docs/collaboration/ai-failure-recovery.md`, which requires `verified`
idempotency/safe-retry support before it may proceed automatically).
Escalate to a human decision instead of assuming `inferred` or `unknown`
compatibility is safe to act on automatically.

## Routing Table

| Task | Preferred route | Reviewer approval |
| --- | --- | --- |
| Mechanical file or wording edit | Deterministic tool or code assistant | not normally |
| One-file local code change with clear spec | Code assistant plus deterministic tests | after verification |
| Design intake | Lightweight reasoning model | before next phase |
| Phase 1 Red tests | Code assistant or strong reasoning agent | before Phase 2 |
| Phase 2 Green implementation | Code assistant with deterministic tests | after verification |
| Phase 3 refactor | Strong reasoning agent plus deterministic tests | before merge |
| Instruction changes | Strong reasoning agent | required, plus a covering design agreement |
| Prompt/template changes | Strong reasoning agent | required, plus a covering design agreement |
| YAML validation | Deterministic tool | not normally |
| Dependency checks | Deterministic tool | not normally |
| Privacy-sensitive context routing | Strong reasoning agent | required; reopening request if the agreement does not cover it |
| Review-finding extraction and ISSUE drafting | Lightweight reasoning model | required when evidence is ambiguous |
| Review-finding metadata/state synchronization | Code assistant or deterministic tool | required when a transition is disputed |
| Minor Fix Path implementation | Code assistant or lightweight reasoning model | required when it changes a specification, ADR, port, data model, dependency, architecture boundary, leaves size S, or needs a second attempt |
| Minor Fix Path closure review | Strong reasoning agent in a separate context | always required |
| Disputed finding / Arbiter decision | Strong reasoning agent | reopen when neither position is grounded |
| Preflight Validation | Deterministic tool first; lightweight reasoning model for checklist assistance | never issue approval; fail returns to Implementer |
| Preflight deterministic checks | Deterministic tool | any failing signal returns to Implementer |
| Preflight document-consistency checklist | Lightweight reasoning model | ambiguity or semantic judgment |

## Escalation Rules

Start with the cheapest safe route.
When a trace is required, record the starting route and escalation reason using
the cost/reasoning control fields in `docs/templates/ai-work-trace.md`.

Escalate to a stronger reasoning agent when:

- requirements are ambiguous or conflict with an accepted spec.
- more than one architectural boundary is touched.
- agent instructions, collaboration rules, or ADRs change.
- private or large context may be needed.
- deterministic verification contradicts the current plan.

Stay with a code assistant or deterministic tool when:

- the task touches one module or document section.
- the target behavior is already specified.
- no external provider, datastore, or architecture decision is needed.
- verification can be done by tests, linting, parsing, or search.

## Privacy Constraints

Use local or deterministic tools when:

- local-only mode applies.
- the content involved is private user data.
- excerpts contain personal or confidential notes.
- provider terms are unknown.

Return a reopening request to the Director before using external AI with
sensitive context that the design agreement does not cover.
