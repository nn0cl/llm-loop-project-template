# Session Start and Resume

This guide covers how humans and AI agents begin work in a new LLM session.
It applies after the collaboration template is already present in the
repository. It does not replace `docs/collaboration/adoption-guide.md` for
first-time template installation.

For project-level startup (placeholders, first spec, domain modeling), see
`docs/collaboration/project-start-guide.md`.

## Core Idea

Each new LLM session has no prior chat context. The operating contract
(`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, and
`.grok/rules/*.md` when present) is reloaded from the repository, but
in-flight decisions from a previous session are not.

Continuity must come from repository artifacts:

1. handoff note or trace cited in the task message.
2. local issue or work plan.
3. accepted specification under `docs/specs/`.
4. feature branch, PR, or changed files on disk.
5. `docs/collaboration/loop-settings.toml` (language, audit, findings flags).
   Create with `scripts/init-loop-settings.sh` if missing.
6. prior `Type: review-finding` issues that affect the area
   (`docs/collaboration/findings-reuse.md`).

Do not treat chat memory, an old session summary, or README prose as
authoritative state. Write new collaboration record bodies in
`[docs].language` from loop-settings. Prefer post-hoc reconstructability
(`docs/collaboration/post-hoc-audit.md`).

## Four Session Types

### 1. First Session After Template Adoption

Use once, right after `scripts/copy-ai-collaboration-files.sh` completes.

Director:

1. Run `scripts/init-loop-settings.sh --language <en|ja|…>` so
   `docs/collaboration/loop-settings.toml` exists. Paste the printed
   **tooling-setup** prompt into an agent when linters / static analysis /
   loop tools are not yet configured for the stack (`--prompt-only` to
   reprint).
2. Run `scripts/init-llm-context.sh <repo>` (add `--tooling` to append the
   same tooling prompt) or use the Initial Assessment Prompt in
   `docs/templates/examples/adoption-prompts.md`.
3. Paste the output into the first agent session.
4. Expect assessment, placeholder identification, and optional tooling
   setup — not product feature implementation.

Agent:

1. Read `AGENTS.md` and `docs/architecture/agent-quickstart.md`.
2. Read `docs/collaboration/loop-settings.toml` and
   `docs/collaboration/adoption-guide.md` before changing target-owned
   files.
3. Stop when target specification, phase, or project boundaries are missing.

`init-loop-settings.sh` and `init-llm-context.sh` are bootstrap aids for this
session type. CI does not require running the LLM prompt script; it does
require the settings *template* and init script to ship with the template.

### 2. New Session, Same Task (Resume)

Use when continuing work that already has specs, a branch, or a handoff.

The task message should include:

- covering design agreement path under `docs/collaboration/agreements/`.
- active persona for this task.
- operating path: Fast, Feature, or Architecture.
- phase: Phase 0, 1, 2, or 3 when applicable.
- authoritative spec or ADR path.
- issue or work-plan ID when applicable.
- branch name.
- handoff or trace path when resuming mid-task.
- scope and out of scope.

Minimal example:

```markdown
Feature Path / Phase 2 (Green).

Spec: docs/specs/<feature>.md
Issue: docs/issues/LISS-00xx.md
Branch: feature/<name>
Handoff: <paste or path to handoff note>

Phase 1 Red is complete and reviewed. Implement the minimum code to pass the
existing tests. Do not refactor.
```

Agent:

1. Read the task message for the covering agreement, persona, path, phase,
   spec, issue, and branch.
2. If a handoff or trace is cited, read it before other documents.
3. Recover progress from repository artifacts, not from assumed chat history.
4. If the covering agreement, persona, path, phase, or authoritative spec is
   missing, stop after design intake and return a reopening request.

### 3. New Session, New Task

Use for a different feature or process task.

The task message should include the covering agreement, persona, path, phase,
spec or ADR, issue link, branch, scope, and out of scope. No handoff is
required.

Agent follows the selected operating path in
`docs/architecture/agent-quickstart.md` and reads only the documents that path
requires.

### 4. Standing Two-Group Pair

Use for the two standing AI session groups introduced by
`docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
(ADR 0016): the Design & Review group (Planner, Specifier, Reviewer, Arbiter)
and the Implementation group (Implementer).

Director, at first start of each group's session (once per group, not once
per work plan):

1. Start the Design & Review group session and the Implementation group
   session separately, each as its own standing session.
2. In each session's first message, state which group it is and which
   persona set operates in it, per the Session Entry Checklist below —
   exactly as any other session's first message would name its persona and
   operating path.

Agent, in either standing session, at its own start (same as any other
session type):

1. Read `AGENTS.md` / `CLAUDE.md` and
   `docs/architecture/agent-quickstart.md`.
2. Read `docs/collaboration/loop-settings.toml` and the normal recovery-order
   documents ("Agent Recovery Order" below) — a standing session's first
   start is not exempt from the same repository-artifact recovery every
   other session type uses.

Ongoing operation, once both standing sessions are running:

- Both sessions communicate using the handoff protocol defined in
  `docs/collaboration/cross-session-messaging.md` (LISS-0022) — this
  document does not restate that protocol's content; see it for the
  concrete `SendMessage` / `ListAgents` contract between the two groups.
- The Director does not restate a full task message per work plan the way
  Session Type 3 above would. Work arrives through the backlog-item gate and
  the handoff protocol instead (ADR 0016 Rules 2 and 4).

When a standing session ends (process restart, crash, manual stop): the
Director, or the other group sending a message that finds no session via
`ListAgents` (per `docs/collaboration/cross-session-messaging.md`'s
`ListAgents` handling), re-establishes it. Re-establishing a standing
session is not a new continuity mechanism — it follows the same
artifact-only continuity rule as any resumed session under "Core Idea"
above: the re-established session recovers state from repository artifacts
(the covering design agreement, work plan, issues, branch, changed files,
`docs/collaboration/loop-settings.toml`), never from assumed chat memory of
the session that ended.

## Session Entry Checklist

Before sending the first message in any session, confirm:

- [ ] A recorded design agreement covers the task.
- [ ] The active persona is named.
- [ ] Operating path is stated or obvious from the request type.
- [ ] Phase is stated for Feature Path work.
- [ ] An authoritative spec, ADR, or explicit Architecture Path scope exists.
- [ ] Branch and issue links are present for feature work.
- [ ] A handoff or trace is attached when resuming incomplete work.

## Agent Recovery Order

When the task message references ongoing work, read in this order:

1. cited handoff note or trace under `docs/collaboration/traces/`.
2. cited issue or work plan.
3. cited specification or ADR.
4. branch diff or changed files if needed to confirm current state.
5. documents required by the selected operating path in agent-quickstart.

Skip documents not required by the path. Do not reread the entire repository by
default.

## Stopping Before the Next Session

When work pauses before completion, leave resumable evidence:

- use `docs/templates/agent-handoff.md` in the final response, or
- add or update a trace under `docs/collaboration/traces/` when the trace
  policy requires it.

A good handoff states current phase, completed artifacts, changed files,
verification status, blockers, and the next safe action.

## Prompt and Tooling Aids

| Situation | Aid |
|-----------|-----|
| First session after adoption | `scripts/init-llm-context.sh` |
| Deeper first assessment | `docs/templates/examples/adoption-prompts.md` |
| Daily resume or new task | This guide plus a short task message |
| Contract reload only | No script required; contract files load per tool |

Generic chat environments that do not auto-load repository contracts still
need `init-llm-context.sh` output or an equivalent first message pasted in by
whoever starts the session.

## Related Documents

- Adoption: `docs/collaboration/adoption-guide.md`
- Project startup: `docs/collaboration/project-start-guide.md`
- Handoff template: `docs/templates/agent-handoff.md`
- Collaboration loop: `docs/collaboration/ai-human-scheme.md`
- Agent entry: `docs/architecture/agent-quickstart.md`