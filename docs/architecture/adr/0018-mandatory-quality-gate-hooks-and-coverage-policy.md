# ADR 0018: Mandatory Quality-Gate Hooks and Branch/Route Coverage Policy

## Status

Accepted. Covered by
`docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md`
(`DA-2026-08-18-05`). Follow-up issues: LISS-0032, LISS-0033
(`docs/archive/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md`).

**Numbering note.** `DA-2026-08-18-05`'s Settled Ambiguities tentatively
named this ADR `0018` because a concurrently in-flight work plan (WP-0004,
`DA-2026-08-18-03`) claims `0017` for its own ADR (portable three-layer loop,
LISS-0029). At the time this ADR was written, `0017` had not yet landed on
this branch: `docs/architecture/adr/` here runs `0001`-`0016`, with no
`0017` file present. `0017` exists on a separate, unmerged branch
(`process/adr-0017-portable-loop`) belonging to WP-0004's own Implementation
session. Per the design agreement's own numbering rule, this is not a
reopening-worthy collision — `0017` is still free and `0018` collides with
nothing else in the repository's history — so this ADR proceeds under
`0018` as tentatively named, leaving a temporary gap at `0017` on this
branch alone. The Design & Review group must confirm no collision (and
reconcile the resulting gap in the entry documents that state the ADR range
— `README.md`, `QUICKSTART.md`, `QUICKSTART.ja.md`, updated below to state
`0018` as the current highest number present on this branch) when merging
this branch with WP-0004's.

## Context

`docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md`,
promoted per ADR 0016 Rule 2, named three related gaps in this template's
own quality-assurance contract, confirmed by direct reading before this
agreement was reached (`DA-2026-08-18-05`'s "Spike Result"):

- `docs/architecture/tooling.md`'s stack-specific table is entirely `_TBD_`
  placeholders — the template states no requirement about *how* a project's
  checks are enforced, only that they exist once filled in.
- `docs/architecture/testing-strategy.md` has no coverage policy of any
  kind.
- `scripts/lib/emit-tooling-setup-prompt.sh` — the tooling-setup prompt
  every adopting project's first session pastes into an agent — already asks
  its Section A to "wire scripts... so one command runs the suite" and
  Section D to "extend CI... so formatter/linter/typecheck/tests run," but
  nowhere requires these to run automatically *before a commit can land
  locally*. CI running after push is not the same guarantee: a commit can
  still land on a shared branch with a broken build, a failing test, or an
  uncovered branch, and the failure is only discovered after the fact.

Separately, no `docs/collaboration/*.md` document exists to generalize
review findings into reusable perspectives (see LISS-0033 and the new
`docs/collaboration/design-review-perspectives.md`); this ADR's own coverage
rule (below) is itself the kind of qualitative, hard-to-automate judgment
that document is meant to preserve across reviews.

The Director's promotion of item-0006 flagged one open question: how strict
the branch/route coverage requirement should be, including whether a
numeric floor is still useful and whether it should apply retroactively to
this template repository's own `scripts/` directory. `DA-2026-08-18-05`'s
Settled Ambiguities narrowed this to its genuinely open sub-part (see
"Decision", rule 3, below) and answered the rest — including the
retroactivity question — by ordinary scoping judgment, not a value call;
this ADR restates that reasoning rather than re-deriving it.

## Dependency Adoption Evidence

Not applicable. This decision selects no library, framework package,
provider SDK, datastore client, build tool, or test helper. It states a
contract-level requirement — that adopting projects must wire *some*
enforcing mechanism appropriate to their own stack — not a specific tool.
Concrete per-stack tool examples named in the strengthened
`scripts/lib/emit-tooling-setup-prompt.sh` (native git hooks, husky or
lefthook for Node/TypeScript, the `pre-commit` framework for Python, a Rust
equivalent) are illustrative starting points for an adopting project's own
tooling-setup session to evaluate, not selections this ADR makes on any
project's behalf.

## Decision

### Rule 1 — Mandatory, commit-blocking pre-commit hooks

An adopting project must wire an actual, commit-blocking pre-commit hook for
each implementation language present in the project. "Wire" means an
enforcement mechanism that runs automatically before a commit is created and
prevents the commit from landing when a check fails — not a documented
command a human or an agent is expected to remember to run manually.

Each language's hook must cover, at minimum:

- lint,
- build or compile (when the language has a separate compile/build step),
- unit tests, and
- coverage (subject to Rule 3 below — a coverage *check* is required; a
  universal numeric *floor* is not).

CI running these same checks after a push does not satisfy this rule by
itself. CI is a second, valuable line of defense — catching what a
contributor's local hook was bypassed or misconfigured for — but it runs
after the commit already exists and, on some workflows, after the commit has
already been shared with collaborators. The local, commit-blocking hook is
what this rule requires; CI is additive to it, not a substitute for it.

This rule is stack-agnostic by design: it states what must be true (an
enforcing, commit-blocking mechanism exists, covering these four categories),
not which hook tool implements it. `docs/architecture/tooling.md` and
`scripts/lib/emit-tooling-setup-prompt.sh` (updated by LISS-0032) name
concrete per-stack examples as a starting point for an adopting project's own
tooling-setup session, without this ADR mandating any one of them.

### Rule 2 — Branch/route coverage anti-gaming rule

A numeric coverage percentage is necessary but never sufficient. The
following rule is mandatory and qualitative, for every adopting project,
regardless of whether Rule 3's numeric floor is adopted locally:

- A test that exercises only one side of a conditional branch does not count
  as covering that branch. Both the true and false paths (and, for a
  multi-way branch, every distinct route) each need their own test.
- Every route through a function or use case needs its own test — a
  representative subset chosen only to make a coverage tool report a
  particular percentage does not satisfy this rule, even when the tool's
  number looks acceptable.
- Implementation must not be shaped merely to make a coverage number pass —
  for example, collapsing branches into a single line to hide them from a
  line-coverage tool's branch detection, or removing a genuine conditional
  in favor of logic that produces the same behavior but reports as fully
  "covered" by an existing test that does not actually exercise the removed
  decision.

This rule exists because a coverage percentage measures *what ran*, not
*what was decided correctly*. A suite that runs every line while asserting
nothing about half of a branch's outcomes reports full coverage and proves
nothing about that branch. Reviewers and self-review records should check
for this rule directly against the diff — reading which routes actually have
their own asserting test — not infer compliance from a coverage tool's
summary percentage alone.

### Rule 3 — No universal numeric coverage floor

This ADR does not mandate one specific numeric coverage floor (for example,
"80% line coverage" or "90% branch coverage") as a hard requirement for
every adopting project's stack.

Grounds, restated from `DA-2026-08-18-05`'s Settled Ambiguities rather than
re-derived: a numeric floor is a useful backstop against a project that
otherwise adds no coverage discipline at all — but it is also exactly the
kind of number Rule 2's anti-gaming rule warns against optimizing toward. A
team under a fixed floor has a direct incentive to shape tests and
implementation to clear that specific number, which is the failure mode Rule
2 exists to name. Mandating one floor at the template level, uniformly
across every possible adopting stack and domain, would assert a value
judgment this template cannot make responsibly for projects it has never
seen — a floor appropriate for a payments-processing core is not
automatically appropriate for a prototype UI layer, and the template has no
basis to pick one over the other.

Instead: each adopting project may choose a local numeric floor (or decline
to set one) as part of its own tooling-setup session (per the strengthened
`scripts/lib/emit-tooling-setup-prompt.sh`), recorded there as a project
decision with its own stated grounds — not fixed by this template's
contract. Rule 2's qualitative anti-gaming requirement applies regardless of
whether a project adopts a local floor.

### Rule 4 — No retroactive application to this template repository's own `scripts/`

This ADR does not require retroactive test or coverage work on this
template repository's own `scripts/` directory.

Grounds: `scripts/` is this repository's own template-native Python
tooling (`check-contract-consistency.py`, `init-loop-settings.sh`, and the
supporting shell/Python helpers), with no test suite today. This ADR
establishes the *contract adopting projects' own stacks must satisfy* once
they select a stack and start writing application code under it — it is not
a retrofit obligation for this template repository's own zero-test-coverage
scripts. Retrofitting `scripts/` with tests and hooks to satisfy a policy
this same ADR just introduced would be a separate, unscoped body of work
that neither `docs/backlog/item-0006-*.md` nor `DA-2026-08-18-05` asked for.
A future backlog item may propose that work on its own merits; this ADR does
not authorize or require it.

## Consequences

Positive:

- Closes the gap named in item-0006's spike: adopting projects are now told,
  at the contract level, that CI-after-push does not satisfy the
  quality-gate requirement — a local, commit-blocking hook is required.
- The anti-gaming rule gives reviewers and self-review records a concrete,
  qualitative check to apply to a diff, independent of whatever number a
  coverage tool reports.
- Leaving the numeric floor as a local, adopter-recorded decision avoids the
  template asserting a one-size-fits-all number that Rule 2's own reasoning
  argues against, while still leaving room for a project that wants one.
- Explicitly scoping out `scripts/` avoids an unscoped, unrequested
  retrofit obligation landing on this template repository as a side effect
  of a contract-level policy change.

Negative:

- "Wire an enforcing, commit-blocking hook per language" is a
  stack-agnostic requirement with no single, template-provided
  implementation; an adopting project's tooling-setup session carries the
  full burden of choosing and wiring the right mechanism for its stack, with
  only illustrative examples from the template to start from.
- No universal numeric floor means two adopting projects can reasonably
  choose very different coverage bars, both compliant with this ADR;
  auditing "is this project's coverage policy adequate" is a per-project
  judgment call, not a single number this ADR lets a checker verify.
- The anti-gaming rule is qualitative and not mechanically checkable by this
  template's own tooling; it depends on reviewer and self-review diligence
  reading the diff, the same way Clean Architecture boundary conformance
  already does.

## Enforcement

Code review and self-review should reject:

- a project's tooling-setup session (or any later phase) that documents
  lint/build/test/coverage commands without wiring an actual, automatically
  running, commit-blocking hook for each — "the command exists and someone
  can run it" is not this rule; "the commit is blocked when it fails" is.
- a claim that CI running after push satisfies Rule 1 by itself.
- a test suite change, or an accompanying implementation change, that raises
  a reported coverage percentage without a corresponding test for each
  previously-uncovered branch or route — reviewers should read which routes
  gained their own asserting test, not accept the percentage alone as
  evidence.
- implementation restructured in a way whose only apparent purpose is to
  make a coverage tool report a higher number, without a corresponding
  behavioral or readability justification.
- a claim that this ADR mandates one specific numeric coverage floor across
  every adopting project's stack — it does not; Rule 3 leaves that as a
  local, project-recorded decision.
- a claim that this ADR requires retroactive test/coverage work on this
  template repository's own `scripts/` directory — it does not; Rule 4
  states this explicitly.
