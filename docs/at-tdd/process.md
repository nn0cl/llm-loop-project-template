# AT-TDD Process

This project uses **AT-TDD** as a repository-local name for an
**ATDD + TDD hybrid workflow**.

AT-TDD is not treated here as a separate industry-standard method name. In this
template, it means:

- acceptance specifications drive the first tests.
- self-reviewed failing tests drive the minimum implementation.
- refactoring happens only after verified Green.
- phase transitions within an issue are self-reviewed by the Implementer, not
  approved by a separate-context Reviewer or by a human; the Reviewer
  operates once, over the whole work plan, at its close. See
  `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`.

The workflow combines:

- **ATDD**: EARS/Gherkin acceptance behavior, external dependencies, data
  ownership, and out-of-scope behavior are clarified before implementation.
- **TDD**: Red, Green, and Refactor phases are kept separate and verified by
  deterministic tools when available.

## Inputs

Each feature starts with an EARS and/or Gherkin specification.

The specification must identify:

- Preconditions.
- Trigger.
- Expected observable result.
- External dependencies.
- Data ownership.
- Out-of-scope behavior.

## Phase 0: Design Intake

Every user request starts with design intake before tests, implementation,
migrations, or UI changes. The intake may be compact for Fast Path work and
complete for Feature Path or Architecture Path work.

Purpose: select only the necessary context, identify lightweight design
decisions, and route work to the appropriate model, assistant, or deterministic
tool.

Required output for Feature Path and Architecture Path:

- target behavior.
- local issue or work plan reference when applicable.
- phase to execute next.
- context to include in AI requests.
- context to omit from AI requests.
- value object or DTO candidates that are clear enough to define now.
- ports and adapters involved.
- suggested task routing.
- input, output, and reasoning evidence contracts when AI or model output is
  involved.
- ambiguity boundaries.
- reopening request needed or not needed.

Fast Path output may be a compact design note that states:

- target scope.
- context included and omitted.
- deterministic checks to run.
- why no feature phase, architecture decision, VO/DTO, port, adapter, or AI
  output contract is involved.

Rules:

- Do not include the whole repository, full source documents, full private
  data exports, or secrets when a smaller payload is enough.
- Lightweight value objects may be named during design, but implementation
  still waits for the requested AT-TDD phase.
- AI output must be treated as untrusted until it satisfies the declared output
  and reasoning evidence contracts.
- Deterministic tools should be used instead of AI for formatting, linting,
  dependency checks, migration ordering checks, and test execution.
- Phase transitions within an issue require self-review, issued under two of
  the three constraints: deterministic precondition and falsification burden
  (context separation is waived at this layer). The work plan as a whole
  requires Reviewer approval, once, under all three constraints, before it
  closes.

## Mandatory `[DESIGN CHECK]`

Before Feature Path or Architecture Path work, agents must output:

1. Preconditions, triggers, and expected results.
2. Existing or new target components.
3. Ambiguous boundaries that must not be guessed.
4. AI payload context to include and omit.
5. Suggested model, assistant, or deterministic tool routing.
6. Input, output, and reasoning evidence contract for AI-assisted tasks.

For Fast Path work, agents may output a compact design note instead of the full
`[DESIGN CHECK]` scaffold.

The design check is concise, auditable decision metadata. It must not expose
hidden chain-of-thought. Scope approval, architecture approval, technology
selection approval, phase approval, and implementation approval remain
separate decisions. A proposed ADR does not authorize implementation.

## Phase 1: Red

Purpose: convert acceptance criteria into failing tests.

Allowed:

- Test files.
- Test fixtures.
- Test-only interface declarations when the language requires a compile target
  for mock types and the design agreement has accepted this convention.

Forbidden:

- Production implementation.
- Database migrations.
- UI components.
- Framework controllers.
- Real network, file-system, or external provider calls.

Red may mean:

- Compile failure because production types do not exist yet.
- Failing assertions against intentionally empty skeletons.

Phase 1 exit gate:

- The Implementer self-reviews the failing tests before Phase 2 starts,
  naming the failure scenarios looked for and citing the deterministic
  verification output showing the Red state. Not a separate-context review —
  see
  `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`.

## Phase 2: Green

Purpose: pass the tests with the minimum production code.

Allowed:

- Domain objects required by tests.
- Use cases required by tests.
- Ports required by tests.
- Minimal adapters only when a test requires an integration boundary.

Forbidden:

- Changing the tests to pass.
- Adding speculative behavior.
- Adding persistence, UI, or provider details not required by tests.

Phase 2 exit gate:

- Deterministic verification is run when available.
- The agent reports whether tests were changed. They should not be.
- Self-review, same terms as Phase 1.

## Phase 3: Refactor

Purpose: improve design while preserving test behavior.

Allowed:

- Rename for clarity.
- Extract domain concepts.
- Move logic out of adapters.
- Reduce duplication.
- Improve test readability without changing assertions.

Required final output:

```markdown
### 変更の要約 (PR Summary)
- **何を目的として何を変更したか**: ...

### 残存リスク・検証の溝 (Verification Gap)
- **AIが推測で補った部分、またはハルシネーションが発生しやすい箇所**: ...
- **work-plan-level Reviewer が反証を試みるべきポイント**: ...
```

Phase 3 exit: self-review, same terms as Phase 1 and 2.

## Work-Plan Review and Close

Once every issue in the work plan has reached self-reviewed completion:

1. Run Preflight Validation over the whole work plan (per
   `docs/architecture/adr/0013-preflight-validation-before-independent-review.md`).
2. On `pass`, submit the work plan to the Reviewer persona, in a separate
   context, for one review covering the whole plan. This is the only
   separate-context review inside a work plan.
3. Findings become `Type: review-finding` local issues, resolved through
   Minor Fix Path or an escalation, as sized.
4. Once the Reviewer approves, the Director reads the result and states the
   next direction — or ends the engagement — in the same action. The next
   work plan does not start without this.
