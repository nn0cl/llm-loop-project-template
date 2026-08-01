# ADR 0006: Prompt and Instruction Change Control

## Status

Accepted.

## Context

`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
`.grok/rules/*.md`, and `.cursor/rules/*.mdc` are near-duplicate operating
contracts for different AI coding tools, together with
`docs/at-tdd/process.md`, `docs/collaboration/*.md`, and
`docs/templates/*.md`. Agent behavior depends directly on these files. (Codex
reads `AGENTS.md` directly and needs no dedicated file.)

These files can drift from each other silently. One file gains a required read
step the others do not, and nothing forces the contract files themselves to be
reviewed with the rigor applied to application code.

Several tools now also read `AGENTS.md` natively, independent of their own rule
surface, which raises the question of whether a dedicated per-tool file is
still worth its duplication cost. The answer differs per vendor, and the
grounds are recorded below because "we decided this once" is not evidence.

### Per-vendor grounds

**GitHub Copilot** reads `AGENTS.md` natively, but GitHub's documentation
describes that reading as read-and-apply, not strict enforcement. Generic
context loading proving insufficient in practice is the same class of evidence
that justified a dedicated file elsewhere. Keep the full mirror.

**Claude Code** supports `@path` imports that expand inline at session launch.
That mechanism was verified working — an adopter confirmed the day's current
`AGENTS.md` content, including same-day additions, present in a live session's
context. In that same session Claude Code still omitted the mandatory
`[DESIGN CHECK]` scaffold across multiple turns and, once, began Phase 2
implementation without stopping at an open decision point. The import
resolved; the adherence did not follow.

Anthropic's own documentation (fetched 2026-07-25) both supports and
complicates the conclusion:

- Imported content is no more binding than any other prose: "Claude treats
  them \[CLAUDE.md / auto memory] as context, not enforced configuration."
  ([*How Claude remembers your project*](https://code.claude.com/docs/en/memory))
- But the causal story is not confirmed: "Splitting into imports helps
  organization but doesn't reduce context, since imported files load at
  launch." The documented adherence drivers are total line count ("target
  under 200 lines… longer files consume more context and reduce adherence"),
  instruction specificity, and absence of cross-file conflicts — none of which
  a full mirror fixes by itself.
- A stronger mechanism exists and is deliberately not adopted here: "To block
  an action regardless of what Claude decides, use a **PreToolUse hook**
  instead." ([hooks-guide](https://code.claude.com/docs/en/hooks-guide)) A hook
  could gate a decision point, but only after decision points are reshaped into
  a machine-checkable form.

`CLAUDE.md` is therefore a full mirror as a precautionary measure, on the same
footing as Copilot's, with the causal mechanism recorded as unresolved.

**Cursor** loads root `AGENTS.md` as its own rule type, separately from
`.cursor/rules`:

1. Rules types list `AGENTS.md` separately from Project Rules
   ([Rules | Cursor Docs](https://cursor.com/docs/rules.md)).
2. "Create an `AGENTS.md` file in your project root. … Cursor picks it up
   automatically." ([Help: Rules](https://cursor.com/help/customization/rules.md))
3. Nested `AGENTS.md` applies automatically for files in that directory
   ([Rules § AGENTS.md](https://cursor.com/docs/rules.md)).
4. `@filename` inside a rule includes that file in rule context — valid, but
   for root `AGENTS.md` it duplicates (1)–(2) rather than substituting.
5. A live Cursor session in this repository (2026-07-16) received root
   `AGENTS.md` as its own always-applied workspace rule *and* the three
   `alwaysApply` `.mdc` files, while `@AGENTS.md` prose inside `.mdc` bodies
   was not expanded inline.

Omitting shared sections from `.mdc` therefore does not drop them from Cursor's
context while root `AGENTS.md` auto-apply remains in force. Keep `.mdc` for
Cursor-only complements, and watch Cursor's product documentation on upgrade.

**Grok** reads `AGENTS.md` at three levels plus `CLAUDE.md` for compatibility,
but a live `grok inspect` test (2026-07-08) found `.grok/rules/` binds more
strongly. Keep the full mirror.

## Decision

Adopt `docs/collaboration/prompt-instruction-change-control.md` as the
canonical definition of the agent operating contract file set.

- Name the exact files and glob patterns that count as the agent operating
  contract.
- Treat a contract change as a design-phase decision: it requires a covering
  design agreement, because changing the contract changes the rules the loop
  runs under.
- Require Reviewer approval from a separate context, a stated reason, and a
  cross-file consistency check whenever a contract file changes.
- Require an AI work trace under `docs/collaboration/traces/` for every
  contract change, including small wording changes.
- Enforce the trace requirement in CI: a pull request that changes a contract
  file must also add a trace file.
- Consistency means the files resolve to equivalent effective content, not
  that they are literal duplicates. `CLAUDE.md`, `copilot-instructions.md`,
  and `.grok/rules/*.md` are each independently phrased, full-coverage mirrors
  of `AGENTS.md`'s effective content for their own tool; `.cursor/rules/*.mdc`
  plus Cursor's native root `AGENTS.md` loading together supply the shared
  contract for Cursor.

## Consequences

Positive:

- Contract drift becomes visible in review instead of silently changing agent
  behavior.
- Every contract change has a recorded reason and expected behavior change.
- CI gives an automated signal rather than relying on anyone's memory.
- Cursor `.mdc` files carry no redundant shared-section mirrors; shared content
  rides on native `AGENTS.md` auto-apply.

Negative:

- Adds a mandatory trace step even for small wording changes.
- Requires keeping the file list in
  `docs/collaboration/prompt-instruction-change-control.md` current as new
  contract-like files appear.
- The consistency check is a judgment call for Cursor (`.mdc` plus native
  `AGENTS.md`), not a byte comparison.
- `CLAUDE.md`, `copilot-instructions.md`, and `.grok/rules/*.md` are
  hand-maintained duplicates: a change to `AGENTS.md` needs matching edits in
  each.
- The mechanism behind the observed Claude Code adherence gap is unconfirmed.
  If line count and specificity are the real drivers, a full mirror may not
  address the root cause.
- If Cursor stopped auto-applying root `AGENTS.md`, shared rules would vanish
  from Cursor sessions until `.mdc` or another binding was restored.

## Enforcement

Code review should reject:

- agent operating contract changes without a stated reason, a covering design
  agreement, or Reviewer approval from a separate context.
- agent operating contract changes without an accompanying trace under
  `docs/collaboration/traces/`.
- agent operating contract changes that leave `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
  `.cursor/rules/*.mdc` inconsistent with each other in effective content.

CI should reject:

- a pull request that changes a file listed in
  `docs/collaboration/prompt-instruction-change-control.md` without adding a
  trace file under `docs/collaboration/traces/`.
