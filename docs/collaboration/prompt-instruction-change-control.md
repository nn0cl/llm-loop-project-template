# Prompt and Instruction Change Control

Agent behavior depends on prompt and instruction files, not only on
application code. A silent change to these files can silently change how
every AI agent behaves on this repository.

This document defines which files are the agent operating contract, and the
review and traceability rules that apply when they change.

## Agent Operating Contract Files

These files are the agent operating contract:

- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`
- `.grok/rules/*.md`
- `.cursor/rules/*.mdc`
- `docs/at-tdd/process.md`
- `docs/collaboration/*.md` (except the record directories below)
- `docs/templates/*.md`
- `AGENTS.md` is also read natively by Codex CLI and by Google
  Antigravity (confirmed via primary source,
  `docs/spike/case-0004-ai-tool-support-status-survey/case.md`) —
  neither needs its own dedicated mirror file for this reason.

Files under `docs/collaboration/traces/`, `docs/collaboration/reviews/`, and
`docs/collaboration/agreements/` are records produced by following the
contract, not part of the contract itself. Changing one is not a contract
change and does not require its own trace — a review record in particular is
the Reviewer persona's only output, and requiring a trace alongside it would
make the persona's own deliverable unlandable.

New files that define agent behavior, phase rules, or cross-cutting
collaboration rules should be added to this list when they are created.

## Review Rule

A pull request that changes an agent operating contract file requires:

- a design agreement covering the change, recorded under
  `docs/collaboration/agreements/`. Changing an operating contract changes the
  rules the loop runs under, so it is a design-phase decision the Director
  takes part in — not something the loop settles for itself.
- Reviewer approval from a separate context, not only automated CI.
- a stated reason for the change in the PR description.
- confirmation that `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
  `.cursor/rules/*.mdc` still agree with each other in effective content
  after the change, when the change touches shared phase, dependency, or
  read-order rules. Per ADR 0006: agreement means equivalent effective
  content, not a literal text match — see this document's own
  "Per-Agent-Tool Rule Applicability Registry" section below for exactly
  which sync mode applies to which agent tool, and to record any new
  intentional difference rather than treating it as an error.

Do not merge an agent operating contract change based only on an AI agent's
self-review.

**No Director instruction waives this rule.** A Director can decide what to
build and can accept a design agreement's scope and boundaries; a Director
cannot grant an exception to the separate-context Reviewer requirement itself,
because nothing in this contract names that as an authority the design
agreement carries. A Director instruction to skip review is not evidence the
change was safe — it is an unreviewed change, full stop, and must be treated
as such until a separate-context Reviewer actually examines it. This is not a
hypothetical: `docs/architecture/adr/0015-review-cost-discipline.md` was
merged on exactly this instruction, and a later retroactive review rejected
it for that reason among others (see that ADR's own Status section). That
incident is not precedent for a future skip; it is the reason this paragraph
exists.

## Per-Agent-Tool Rule Applicability Registry

Not every rule in this contract applies identically to every agent tool's
own mirror file. Record every *intentional* difference here — a
difference that exists on purpose, not one this document's own
mirror-consistency requirement above would otherwise flag as a defect.
Consult this table before treating an agent-tool difference as an error.

| Sync mode | Agent tool(s) | What it means |
| --- | --- | --- |
| Literal full mirror | `CLAUDE.md`, `.github/copilot-instructions.md`, `.grok/rules/*.md` | Effective content matches `AGENTS.md` word-for-word (`CLAUDE.md` joined this group on 2026-07-25, when the `@AGENTS.md` import was dropped after an adopter showed the import resolved correctly and still did not produce adherence). |
| Union (complement + native auto-apply) | `.cursor/rules/*.mdc` | Cursor's effective content is the union of `.cursor/rules/*.mdc` (Cursor complements only — not a full restatement) and Cursor's own native root `AGENTS.md` auto-apply (Cursor reads `AGENTS.md` directly; the `.mdc` files add only what Cursor-specific behavior requires and do not `@AGENTS.md`-import it). |
| Canonical source | `AGENTS.md` | The literal-full-mirror group's source of truth; edited first, then propagated to the mirrors listed above. |
| Canonical source (also read directly, no mirror needed) | Codex CLI, Google Antigravity | Both tools read `AGENTS.md` natively — confirmed via primary source for Antigravity in `docs/spike/case-0004-ai-tool-support-status-survey/case.md`; no `.antigravity/` or equivalent mirror file exists or is needed for this reason. |

Add a new row here, with its own reason, the first time an intentional
per-agent-tool difference is introduced — do not fold a new difference
into prose scattered across this document or a PR description where a
later reader would not think to look for it.

## Traceability Rule

A pull request that changes an agent operating contract file must include an
AI work trace under `docs/collaboration/traces/` explaining:

- which contract file or files changed.
- why the change was needed.
- what agent behavior is expected to change as a result.

Use `docs/templates/ai-work-trace.md`. This trace is required even for small
wording changes to a contract file; the "tiny documentation-only change"
exception in `docs/collaboration/ai-work-trace-log.md` does not apply to
files in this list.

## Enforcement

CI checks that a pull request touching an agent operating contract file also
adds a trace file under `docs/collaboration/traces/`.

Code review should reject:

- agent operating contract changes without a stated reason.
- agent operating contract changes without an accompanying trace.
- agent operating contract changes that leave `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
  `.cursor/rules/*.mdc` inconsistent with each other in effective content.
- agent operating contract changes merged without a covering design agreement
  or without a Reviewer approval record.
- agent operating contract changes merged on a Director instruction to skip
  review, treated as if that instruction were itself a substitute for
  Reviewer approval. No such substitution exists in this contract.
