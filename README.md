# LLM Loop Project Template

[日本語ガイド](README.ja.md) · [Quickstart: adopting / uninstalling this template](QUICKSTART.md)
 · [Changelog](CHANGELOG.md)

**Contract edition: v2.2.0.** The operating contract in this repository is
versioned — an adopting project can install and cite a specific edition. See
[CHANGELOG.md](CHANGELOG.md) for what an edition covers.

## Project direction

This project is a **counter-validation project against the human-intervention
model**.

Under the conventional model, a human sits at two points in the development
loop: the initial *BigDecide* — the framing decision about what to build and
under which constraints — and the feedback given on each deliverable the
agents produce. That model treats standing human judgment as the thing that
keeps generated work correct.

This project removes human presence from the development *loop*. Not from the
project — from the loop.

**Where the human is.** The Director states the direction for a work plan,
builds the detailed plan with the Planner persona through dialogue, and
reaches an explicit design agreement that closes the design phase. Planning is
a conversation, not a review of a finished artifact, and the agreement is
mutual: the Director agrees the plan describes what they want built, and the
AI agrees it is executable without further interpretation. The Director is
present again once, at the work plan's close: reading the AI-approved result
and stating the next direction, in the same action.

**Where the human is not.** Between those two points. No phase-transition
approval, no per-issue test review, no per-deliverable sign-off. An issue's
phase transitions are self-reviewed by the Implementer; once every issue in
the work plan is done, one Reviewer pass in a separate context covers the
whole plan. The loop does not stop for a human until that close. It stops
early only to reopen the design agreement, naming what is unsettled.

The claim under test is that correctness in AI-assisted development comes from
the written contract and its verification, not from a human standing in the
loop. If a closed loop produces work that holds up, the human-intervention
model is not the necessary condition it is assumed to be. If it does not, the
failure modes are the finding — and they have to be visible in the artifacts
rather than absorbed by a human patching them in real time.

### What keeps AI self-approval honest

An AI approving its own work is worthless unless it is constrained. Every
approval — self-review within an issue, or the Reviewer's approval of a whole
work plan — must satisfy two constraints, and the Reviewer's approval must
satisfy a third that self-review is deliberately exempt from:

1. **Context separation.** The Reviewer runs in a context separate from the one
   that produced the work, and receives only artifacts, specifications,
   contracts, and tool output. The Implementer's reasoning is not admissible as
   justification. Waived only for an Implementer's self-review of its own
   phase transitions inside a work plan — never for the Reviewer's
   work-plan-level approval, and never for changes to the contract itself.
2. **Deterministic precondition.** No approval without recorded deterministic
   verification output. AI judgment is additive to tests, linters, and boundary
   checks — never a substitute for them.
3. **Falsification burden.** Approval requires naming the failure scenarios
   searched for and the grounds on which each does not occur, at either layer.
   "No problems found" is not an approval.

Self-review trades context separation for review frequency — the Implementer
reviews its own work at every phase transition instead of a separate context
reviewing it once, less often, at the work-plan's close. See
[ADR 0014](docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md)
for the tradeoff this accepts and why.

### What did not change

Three invariants carry over from `llm-project-template` unchanged, and removing
human approval raises rather than lowers their cost — no human downstream will
reconstruct missing rationale:

1. **Every decision produces a document.**
2. **Every executed fact leaves evidence.**
3. **Every claim states its grounds.**

The governing decision is
[ADR 0001](docs/architecture/adr/0001-director-centered-planning-and-closed-loop.md).
The operating model is defined in
[ai-human-scheme.md](docs/collaboration/ai-human-scheme.md),
[personas.md](docs/collaboration/personas.md), and
[design-agreement.md](docs/collaboration/design-agreement.md).

---

This repository is a starter template for a **Clean Architecture + AT-TDD**
development workflow where a human Director and one or more AI coding agents
(Claude, Copilot, Codex, Grok, Cursor, etc.) work under a shared, written
operating contract.

In this repository, **AT-TDD** is a local shorthand for an **ATDD + TDD hybrid
workflow**: acceptance specifications drive failing tests, reviewed tests drive
minimal implementation, and refactoring happens only after verified Green. It
is not used here as a claim that "AT-TDD" is a separate industry-standard
method name.

Everything here is process and collaboration scaffolding. It contains no
application domain logic, stack decision, datastore decision, provider choice,
or product specification. Those belong to the repository where this template is
installed.

## What this template gives you

- A **phase-gated workflow** (Design Intake -> Red -> Green -> Refactor) that
  every agent must follow, self-reviewed at each phase and reviewed once by
  the Reviewer, in a separate context, at the work plan's close.
- A **Director-bounded collaboration scheme**: the human sets direction, plans
  through dialogue, and reaches one design agreement per work plan, closed by
  one combined checkpoint; the loop between those two points runs on named
  personas that produce reviewable, minimal, phase-correct artifacts.
- **Persona definitions** (Planner, Specifier, Implementer, Reviewer, Arbiter)
  with responsibilities, admissible inputs, required outputs, and rules for
  adding task-specific personas.
- **Anti-rubber-stamp constraints** on AI approval: context separation, a
  deterministic-verification precondition, and a falsification burden on the
  reviewer.
- **Agent operating contract files** (`AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/`, `.cursor/rules/`) kept
  in sync by a documented change-control rule and a CI check. Codex reads
  `AGENTS.md` directly and needs no dedicated file. Cursor and Grok Build
  also read `AGENTS.md` natively as a fallback, but this template keeps
  dedicated `.cursor/rules/*.mdc` and `.grok/rules/*.md` files since each
  tool's own rule surface binds more strongly than generic `AGENTS.md`
  fallback reading.
- **Local issue and work-plan planning** under `docs/issues/` and
  `docs/work-plans/`, usable before or alongside GitHub Issues.
- **Three record directories** that make the loop auditable: design agreements
  under `docs/collaboration/agreements/`, Reviewer decisions under
  `docs/collaboration/reviews/`, and AI work traces under
  `docs/collaboration/traces/`.
- **Reusable templates** for design agreements, review records, self-review,
  design intake, agent handoff, work traces, local issues, work plans,
  Gherkin features, and
  ADRs.
- A **CI skeleton** that checks the contract files exist, checks that
  ADRs are numbered, and enforces that contract-file changes come with a
  trace.
- A **contract consistency checker** (`scripts/check-contract-consistency.py`,
  run by CI) for the drift a link check cannot see: a rule that reaches
  some tool files and not others, a stated ADR range that no longer matches
  the ADRs, a version claimed as released with no tag behind it.
- A **copy script** for rolling the collaboration files into a new or existing
  repository without overwriting existing target files by default.
- An **LLM setup prompt script** that prepares a compact first message for a
  new AI session after installation.
- A **target-local adoption guide** that can be copied without replacing an
  existing product README.
- A **project start and development guide** for moving from template adoption
  to target-owned specifications, domain modeling, and phase-gated work.
- A **lightweight cost/reasoning control ledger** for checking whether strong
  LLM reasoning was actually needed.

## Why use it?

Use this template when you want AI-assisted development to be reviewable,
phase-correct, and cheaper to reason about.

It helps reduce:

- guessed implementation before accepted specs.
- AI agents skipping from vague requests to production code.
- hidden business logic in adapters, UI, provider clients, or persistence.
- oversized prompts and unnecessary strong-model reasoning.
- dependency choices made without security, version, troubleshooting, test, or
  POC evidence.
- handoff gaps when another human or agent continues the work.

The benefits depend on using the process consistently; the template is not an
automatic productivity guarantee. See
`docs/collaboration/template-benefits.md` for the detailed rationale.

## Install into another repository

From this template repository:

```bash
scripts/copy-ai-collaboration-files.sh --target /path/to/target-repo
```

The copy script skips existing files by default. This is intentional: when the
template is introduced into an existing project, the target project's
architecture documents, specifications, README, and application files remain
owned by that project.

Optional placeholder replacement:

```bash
scripts/copy-ai-collaboration-files.sh \
  --target /path/to/target-repo \
  --project-name "Example Product" \
  --domain-summary "one-line target project summary" \
  --stack "backend language, frontend framework, package manager"
```

Use `--dry-run` to preview actions. Use `--force` only when you intentionally
want to replace files that are part of this template.

## Initialize an LLM session

After copying the template into the target repository, run:

```bash
cd /path/to/target-repo
scripts/init-llm-context.sh .
```

Paste the generated prompt into the first LLM session for that repository. The
prompt tells the agent which operating documents to read, which phase gates to
respect, how to choose Fast Path / Feature Path / Architecture Path, and when
to return a reopening request. It does not select the target project's stack,
datastore, LLM provider, external APIs, or domain behavior.

Target-local onboarding lives in
`docs/collaboration/adoption-guide.md` after the template is copied.

## What you must fill in

This template deliberately avoids naming a stack, a domain, or concrete
architecture layers. Before using it on a real project:

1. Fill target-specific placeholders in `AGENTS.md`, `CLAUDE.md`,
   `.github/copilot-instructions.md`, `.grok/rules/*.md`,
   `.cursor/rules/*.mdc`, and `docs/architecture/README.md`. The copy
   script can fill the project name, domain summary, and stack placeholders
   when `--project-name`, `--domain-summary`, and `--stack` are provided;
   runtime boundaries, datastore, migration tool, external resources, and
   stack-specific architecture documents still need target facts settled in a
   design agreement with the Director.
2. Add one architecture document per architectural area you actually have
   (e.g. `backend-architecture.md`, `frontend-architecture.md`,
   `persistence.md`). Use `docs/architecture/project-structure.md` and
   `docs/architecture/testing-strategy.md` as the starting shape and fill in
   real paths. See `docs/templates/examples/` for two filled-in examples
   (Rust/Tauri core, React front-end) — copy the pattern, not the content.
3. Add project-specific "external resources must be ports" entries to
   `CLAUDE.md` / `AGENTS.md` (e.g. payment provider, LLM provider, message
   queue, external API).
4. Write your first EARS/Gherkin specification under `docs/specs/` using
   `docs/templates/gherkin-feature.md`.
5. Update `.github/workflows/ci.yml`'s `required_files` list and add
   stack-specific jobs (lint, test, dependency policy) once those tools
   exist.
6. Renumber/extend `docs/architecture/adr/` as real architecture decisions are
   made. The fifteen ADRs included here (0001-0015) describe the
   collaboration process itself and normally do not need to change; number
   your project's own decisions from 0016 up, so a later template update does
   not collide with them.

## Introduce into an existing repository

For midway adoption, start with a dry run:

```bash
scripts/copy-ai-collaboration-files.sh --target /path/to/existing-repo --dry-run
```

Then run the copy without `--force`. Review skipped files, decide whether any
existing project documents should manually adopt the collaboration wording, and
only then consider targeted overwrites. Do not use this template to replace the
target project's accepted architecture or feature specifications.

## Read order for a new agent

1. `docs/architecture/agent-quickstart.md`
2. Select the smallest safe path: Fast Path, Feature Path, or Architecture
   Path.
3. Read only the documents required by that path.
4. `docs/architecture/implementation-readiness.md` before Phase 1, 2, or 3
   starts.

## Directory Guide

```text
.
├── QUICKSTART.md / QUICKSTART.ja.md  # adoption/uninstall guide, not copied to targets
├── AGENTS.md                       # operating contract (tool-agnostic)
├── CLAUDE.md                       # operating contract (Claude-specific entry point)
├── .gitignore                      # local editor/OS noise ignored by default
├── .grok/
│   └── rules/                      # operating contract (Grok-specific entry point)
├── .cursor/
│   └── rules/                      # operating contract (Cursor-specific entry point)
├── .github/
│   ├── copilot-instructions.md     # operating contract (Copilot-specific entry point)
│   ├── pull_request_template.md
│   ├── ISSUE_TEMPLATE/
│   └── workflows/ci.yml
└── docs/
    ├── at-tdd/process.md           # phase discipline
    ├── collaboration/              # process rules (scheme, personas, DoD, privacy, branching, ...)
    │   ├── agreements/             # design agreement records (human gate 1, per work plan)
    │   ├── reviews/                # Reviewer persona decisions (once per work plan)
    │   └── traces/                 # AI work trace log (per-task audit trail)
    ├── templates/                  # design agreement, review record, design intake, handoff, trace, issue, ADR, Gherkin
    │   └── examples/               # filled-in stack-specific examples, for reference only
    ├── architecture/               # Clean Architecture rules, quickstart, readiness checklist
    │   └── adr/                    # architecture decision records (0001-0015 = process ADRs)
    ├── specs/                      # EARS/Gherkin feature specifications
    ├── issues/                     # local issue files (LISS-0000 style)
    ├── work-plans/                 # multi-issue work plans
    └── evaluation/                 # golden examples and evaluation criteria
└── scripts/
    ├── copy-ai-collaboration-files.sh
    ├── update-ai-collaboration-files.sh
    ├── init-llm-context.sh
    └── lib/collaboration-template-paths.sh
```

### Record state

The record directories in this repository are empty. On 2026-08-02 the
Director reset them: the local issues, work plans, traces, review records,
design agreements, and sample rollout spec accumulated while building the
template were removed from the working tree, so the repository presents the
same initial state an adopting project starts from. Git history was kept
deliberately — every removed record is still reachable there, and the commit
that cleared them is the record of the decision.

The copy/update scripts exclude those paths from adopting projects in any
case. New target repositories receive the empty `.gitkeep` folders and create
their own agreements, reviews, traces, issues, and specs.

## Core rules worth remembering

- No execution without a recorded design agreement.
- No approval without deterministic verification output.
- No approval by the context that produced the work.
- No phase skipping. Only the phase named in the plan runs.
- No hidden business logic in adapters, UI components, or framework handlers.
- Every external resource is represented as a port before it is used.
- Every task starts with path-appropriate design intake: compact note for Fast
  Path, full `[DESIGN CHECK]` for Feature Path or Architecture Path.
- Changing an agent operating contract file requires a stated reason, a
  covering design agreement, Reviewer approval, and a trace under
  `docs/collaboration/traces/` (CI enforced).

## License

[MIT](LICENSE)
