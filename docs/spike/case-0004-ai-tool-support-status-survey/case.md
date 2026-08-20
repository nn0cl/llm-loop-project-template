# Spike Case: case-0004-ai-tool-support-status-survey

## Metadata

- Case ID: case-0004
- Title: Support status survey across Claude Code, Codex, Cursor, Grok,
  and Antigravity
- Status: closed
- Created: 2026-08-20
- Closed: 2026-08-20
- Owner/agent: Design & Review group (Planner), standing session
- Related work plan: none yet
- Related local issue (LISS): LISS-0069 (status report + update proposal
  this spike opens, see Next action)
- Related backlog item:
  `docs/backlog/item-0021-ai-tool-support-status-survey.md`
- Supersedes case: none
- Superseded by case: none

## Question

Is `docs/architecture/adr/0017-...md`'s existing Codex/Grok/Copilot
research still current, and — for Antigravity, which this repository has
never investigated — what instruction-file convention, subagent/worktree
model, and peer-messaging capability does it actually have, per its own
primary-source documentation?

## Why a spike (not immediate implementation)

`docs/backlog/item-0021-...md` explicitly requires this: confirm existing
research is current (not redo from scratch) for Codex/Grok/Copilot, and
fully investigate Antigravity from primary sources, since this repository
has zero existing coverage of it. The item's own Known Constraints
explicitly forbid fabricating a tool's capabilities from general
knowledge — every claim needs a stated source.

## Constraints

- Must remain free of mandatory paid spend unless justified below: yes —
  all research used public documentation, no paid API/subscription
  required to read it.
- Architecture / port boundaries to respect: none — no application
  architecture touched.
- Out of scope for this spike:
  - Redesigning ADR 0016/0017's own topology (per the backlog item's own
    boundary note).
  - Live-testing inside any of the four non-Claude tools (this session
    only has Claude Code available to run in) — noted as a limitation on
    every finding below, not silently glossed over.
  - Antigravity's A2A (Agent2Agent) protocol's own full implementation
    detail — confirmed to exist and be documented, but a deep dive into
    its wire protocol is out of scope; what matters for this survey is
    whether it constitutes a `SendMessage`/`ListAgents`-equivalent for
    two independently-started local CLI sessions, which this spike
    investigated to the extent primary sources allow and reports with
    its own residual uncertainty named explicitly.

## Candidates

Not a vendor/library selection — the five "candidates" are the five AI
coding tools the backlog item names, each evaluated against the same
fixed criteria (instruction-file convention, subagent+worktree model,
peer-messaging equivalent, existing mirror-file currency).

| ID | Tool | Existing coverage in this repo | Notes |
| --- | --- | --- | --- |
| A | Claude Code | Full (this is the reference implementation) | No new research required per the backlog item's own text |
| B | Codex CLI | ADR 0017 (2026-08-18 primary-source fetch) | Re-verify currency |
| C | Cursor | ADR 0017 (secondary sources only, plus `.cursor/rules/*.mdc` mirror) | Re-verify currency; upgrade to a primary source if found |
| D | Grok Build | ADR 0017 (2026-08-18 primary-source fetch), plus `.grok/rules/*.md` mirror | Re-verify currency |
| E | Antigravity | None | Full primary-source investigation required |

## Evaluation criteria

| Criterion | Why it matters | How measured |
| --- | --- | --- |
| Instruction-file convention | Determines whether this repo's existing mirror-file model (`AGENTS.md`/`CLAUDE.md`/`.github/copilot-instructions.md`/`.grok/rules/*.md`/`.cursor/rules/*.mdc`) actually reaches each tool | Primary-source doc fetch naming the exact file(s)/directory the tool reads |
| Subagent + worktree model | Confirms or updates ADR 0017 Rule 2's own portable-baseline claim | Primary-source doc fetch: parent-child only, nesting depth, worktree opt-in vs. automatic |
| Peer-messaging equivalent | Confirms or updates ADR 0017's own claim that no tool examined has a `SendMessage`/`ListAgents` equivalent | Primary-source doc fetch, specifically checking for independently-started-session discovery/messaging, not just parent-child |
| Existing mirror-file currency | Item-0021's own second deliverable — update what can be updated | `scripts/check-contract-consistency.py`'s own mirror-parity check (deterministic, already exists) plus direct content comparison |

## Research log

| Date | Query or source | Finding | URL |
| --- | --- | --- | --- |
| 2026-08-20 | `learn.chatgpt.com/docs/agent-configuration/subagents` (Codex CLI subagents, re-fetched) | Re-confirms ADR 0017's own claim: "Codex handles orchestration across agents, including spawning new subagents, routing follow-up instructions, waiting for results, and closing agent threads." No worktree-isolation detail on this page (same gap ADR 0017 already noted); no peer-to-peer/session-discovery mention. **Still current.** | https://learn.chatgpt.com/docs/agent-configuration/subagents |
| 2026-08-20 | `github.com/xai-org/grok-build/.../16-subagents.md` (Grok Build subagents, re-fetched, primary source) | Word-for-word re-confirms ADR 0017's own exact quotes: "Only the top-level session spawns subagents. A subagent cannot spawn its own subagents: the maximum nesting depth is one." Worktree isolation via `isolation: worktree`, opt-in per call, not automatic. Parent receives child's output "usually a summary" on completion. No peer-messaging/discovery mentioned. **Still current, exact match.** A secondary blog source (`mer.vin`) claimed "worktree is declared as a default isolation mode for personas" — this contradicts the primary source; the primary source (the tool's own repository docs) is treated as authoritative per this spike's own evidence discipline, not the blog. | https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/16-subagents.md |
| 2026-08-20 | `docs.github.com/en/copilot/how-tos/copilot-sdk/features/fleet-mode` (Copilot fleet mode, re-fetched) | Re-confirms ADR 0017's own claim: parent-coordinated worker dispatch ("one parent session should coordinate several workers, collect their results"), using "explicit coordination state" (SQL todos) rather than shared memory or peer messaging. Still no git-worktree detail documented on this page (same gap ADR 0017 already noted). **Still current.** | https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/fleet-mode |
| 2026-08-20 | `cursor.com/docs/configuration/worktrees` (Cursor, primary source — new; ADR 0017 only had secondary sources for Cursor) | "When you start or move an agent into a worktree from the Agents Window, Cursor creates a separate checkout for that agent" — worktree isolation is **opt-in** (via the Agents Window or `.cursor/worktrees.json`), not automatic for every agent by default. No peer-to-peer messaging mentioned. This is a genuine upgrade from ADR 0017's own "secondary/blog sources only, no primary Cursor doc URL fetched" caveat — Cursor now has a confirmed primary source. | https://cursor.com/docs/configuration/worktrees |
| 2026-08-20 | Web search + `cursor.com/docs/rules` region (Cursor instruction files) | Confirms: "Starting with Cursor 0.48, `AGENTS.md` is read in all modes: Chat, Composer, and Agent mode... Cursor reads both [`AGENTS.md` and `.cursor/rules/*.mdc`] and merges their context" — and "Cursor's CLI... reads both `AGENTS.md` and `CLAUDE.md` at the project root and applies them as rules alongside `.cursor/rules`." This **exactly matches** `docs/collaboration/prompt-instruction-change-control.md`'s own existing "Union (complement + native auto-apply)" row for Cursor — no update needed to that table's own description of the mechanism. New, not-previously-recorded detail: Cursor's CLI also reads `CLAUDE.md` directly (redundant with `AGENTS.md`, since `CLAUDE.md` is a literal full mirror of it, but not previously documented in this repo). | web search results citing cursor.com/docs/rules and related guides |
| 2026-08-20 | `ai.google.dev/gemini-api/docs/antigravity-agent` (Antigravity, primary source, Google's own official domain) | "you can mount files like `AGENTS.md` for instructions and skills under `.agents/skills/` directly into the sandbox" — confirms `AGENTS.md` as Antigravity's own project-instruction convention, the same file this repository already maintains as its canonical source. No alternate top-level file name (e.g. `ANTIGRAVITY.md`) found. | https://ai.google.dev/gemini-api/docs/antigravity-agent |
| 2026-08-20 | `antigravity.google/docs/subagents/` (Antigravity, primary source, official product domain) | "A maximum nesting depth of 10 levels... is strictly enforced" — unlike Codex/Grok/Copilot, Antigravity subagents **can** spawn further subagents, up to 10 levels deep. Worktree isolation is opt-in per subagent, one of three explicit modes: `inherit` (same workspace), `branch` (isolated git worktree), `share` (shared directory storage) — closest analog to this repository's own `isolation: worktree` convention is the `branch` mode. On completion, a subagent "sent a result message to its parent agent, and paused execution" (parent-child fan-out, same shape as the other three tools). | https://antigravity.google/docs/subagents/ |
| 2026-08-20 | Same page, targeted re-fetch for peer-messaging | **"Agents can communicate with parent agents, subagents, or peer agents whose ID is known."** This is the one finding among all five tools that goes beyond pure parent-child fan-out — Antigravity's own documentation explicitly names peer-agent communication as a capability, not only parent-child. However, the same page does **not** explain how an agent learns a peer's ID — "known" is stated as a precondition, not resolved by a documented discovery mechanism on this page. Agent lifecycle: task-duration, not indefinitely "standing" — described as `Running`/`Idle`/`Killed`, where an idle subagent "automatically re-awakens... upon receiving a message" (message-triggered wake, not a persistent poll loop — directly relevant to this repository's own item-0020/ADR-0016-Rule-7 work, noted as an interesting cross-reference, not acted on here). | https://antigravity.google/docs/subagents/ |
| 2026-08-20 | `antigravity.google/docs/cli/commands/agents/` (Antigravity `/agents` command, primary source) | The `/agents` panel serves two purposes: (1) listing **available agent role/type definitions** (templates a session can invoke, resolved from `.agents/agents/{name}/agent.md` — analogous to this environment's own `subagent_type` category labels, not live instances), and (2) "Subagent Monitoring & Control" showing **live spawned subagent threads**, "grouped by their triggering prompt" — i.e., the current session's own children, not an arbitrary cross-session live-session list. This directly narrows the peer-messaging finding above: the confirmed discovery/listing mechanism (`/agents`) surfaces a session's own spawned subagents and available role templates, not a general registry of independently-started standing sessions the way this environment's own `ListAgents` is documented to work. | https://antigravity.google/docs/cli/commands/agents/ |
| 2026-08-20 | Web search: Antigravity A2A (Agent2Agent) protocol | A2A is confirmed as a real, documented Antigravity capability, but it is a **cross-vendor, open, HTTP/SSE/JSON-RPC-based protocol** (`a2aproject/A2A` on GitHub, `a2a-protocol.org`) designed for "agents deployed in external systems" advertising capabilities via "Agent Cards" — its own canonical example (a purchasing-concierge agent talking to a remote seller agent) is inter-service integration, not two local CLI sessions on one developer's machine discovering each other. This is a materially different use case from `SendMessage`/`ListAgents`. **Conclusion, stated precisely, not overclaimed**: Antigravity's documented "peer agents whose ID is known" capability inside a single subagent tree is real and is a genuine step beyond Codex/Grok/Copilot's pure one-way parent-child model, but this spike found no primary-source confirmation of a `ListAgents`-equivalent *discovery* mechanism for independently-started, unrelated standing sessions — the closest analog (`/agents`) is scoped to one session's own spawn tree plus static role templates. The A2A protocol is real but aimed at a different (cross-service) integration shape. Report this as "closer than the other three, not confirmed equivalent," not as "Antigravity has ListAgents." | https://github.com/a2aproject/A2A, https://a2a-protocol.org/latest/specification/, https://antigravity.google/blog/introducing-google-antigravity-sdk |
| 2026-08-20 | `python3 scripts/check-contract-consistency.py`, run against this repository's own current tree | `contract consistency: all checks passed` — including the mirror-parity check that specifically compares `.cursor/rules/*.mdc` and `.grok/rules/*.md`'s effective content against `AGENTS.md`. This is direct, deterministic, already-existing evidence that both mirrors are currently in sync with the canonical source — not a claim requiring new manual verification. | local command output, this repository |

## Comparison

| Criterion | Claude Code | Codex CLI | Cursor | Grok Build | Antigravity |
| --- | --- | --- | --- | --- | --- |
| Instruction file(s) | `CLAUDE.md` (native) | `AGENTS.md` (native) | `AGENTS.md` + `.cursor/rules/*.mdc` (union) + `CLAUDE.md` (also read, redundant) | `.grok/rules/*.md` (this repo's mirror; native convention not independently re-verified beyond the existing mirror's own continued checker-parity pass) | `AGENTS.md` (native) |
| Subagent nesting | N/A (this repo's own reference model) | Parent-child only (no re-nesting documented) | Not documented on the worktree page; not independently re-verified for nesting depth this round | Max depth 1 (subagent cannot spawn its own) | Max depth 10 |
| Worktree isolation | Native, per this repo's own convention | Not documented (same gap as 2026-08-18) | Opt-in (Agents Window / `.cursor/worktrees.json`) | Opt-in (`isolation: worktree`) | Opt-in, one of three modes (`inherit`/`branch`/`share`) |
| Peer-messaging equivalent | `SendMessage`/`ListAgents` (native) | None documented | None documented | None documented | Partial — "peer agents whose ID is known," discovery mechanism not confirmed equivalent to `ListAgents`; A2A protocol exists but targets cross-service integration |
| This repo's mirror file | `CLAUDE.md` | `AGENTS.md` (already canonical/shared) | `.cursor/rules/*.mdc` — confirmed current (checker passes; mechanism re-verified against a new primary source) | `.grok/rules/*.md` — confirmed current (checker passes; mechanism re-verified against primary source) | **None exists yet** |

## Cost and quality judgment

- Free / zero-mandatory-spend options considered: all five tools'
  documentation is publicly readable without a paid account; no paid
  spend was required for this research.
- Quality bar applied: primary-source (the tool's own official
  documentation domain) preferred over secondary/blog sources throughout;
  the one place a secondary source was found (a Grok Build blog claiming
  automatic worktree isolation) was explicitly checked against and
  overridden by the primary source, not left unresolved.
- No paid option is in play; not applicable.

## Selection

- Selected: none (this is a status survey, not a technology choice
  between competing options)
- Rationale: N/A — see Next action for the concrete follow-up this
  survey's findings support.
- Discard reasons: N/A

## Evidence

- `docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md`
  (the existing research this spike re-verified)
- `docs/collaboration/prompt-instruction-change-control.md`'s
  "Per-Agent-Tool Rule Applicability Registry" (the existing mirror-mode
  table this spike checked Cursor's own row against)
- `docs/backlog/item-0021-ai-tool-support-status-survey.md`
- Every URL cited in the Research log above
- `python3 scripts/check-contract-consistency.py` output (pasted in the
  Research log; full mirror-parity pass)

## Next action (exactly one)

- [x] Spec + implementation issue: **LISS-0069** — writes the status
      report deliverable (one document covering all five tools, per the
      backlog item's own choice of shape), adds Antigravity to
      `docs/collaboration/prompt-instruction-change-control.md`'s
      "Agent Operating Contract Files" list and "Per-Agent-Tool Rule
      Applicability Registry" (as a "Canonical source" reader, alongside
      `AGENTS.md`, since it needs no separate mirror file — it reads
      `AGENTS.md` natively, the same as Codex), and states explicitly
      that no new `.antigravity/` or similar mirror file is needed for
      that reason. Confirms Cursor's and Grok's existing mirror files
      need no content update (checker-verified current). This is a
      contract-file change (ADR 0006 governance applies in full:
      separate-context Reviewer, mandatory trace).

## Open risks after close

- Antigravity's own peer-messaging capability ("peer agents whose ID is
  known") was investigated to the depth primary sources support within
  this spike's own time budget, but a definitive answer to "is there
  truly no discovery mechanism at all, or does one exist undocumented on
  a page this spike did not find" remains genuinely open — reported as
  "not confirmed," not asserted either way, per this spike's own evidence
  discipline. Worth a note in the status report itself, not silently
  smoothed over.
- No tool besides Claude Code was actually exercised live in this session
  (this is a Claude Code session) — every finding above is documentation-
  based, the same limitation `docs/backlog/item-0021-...md` itself
  anticipated and accepted for the existing `.cursor/`/`.grok/` mirrors.
- Antigravity's own documentation is the newest and least stable of the
  five (the product itself appears to have shipped major features,
  including A2A and Mission Control, only recently per the dated blog
  posts found during research) — a follow-up currency check sooner than
  the other four tools' own re-check cadence would need is a reasonable
  expectation, not a defect in this spike.
