# Backlog item: item-0021-ai-tool-support-status-survey

## Metadata

- Item ID: item-0021
- Title: Survey this template's support status across Claude Code, Codex,
  Cursor, Grok, and Antigravity, and update what can be updated
- Status: promoted
- Created: 2026-08-20
- Updated: 2026-08-20
- Priority hint: medium
- Suggested planning size: L
- Owner/agent (optional): unassigned

## Summary

Director request: produce a status report covering how well this
repository's AI-agent collaboration model (personas, phase discipline,
ADR 0016's standing two-group topology, ADR 0017's portable baseline
handoff and file-based intervention fallback, ADR 0006's mirrored
instruction files) is actually supported by five specific AI coding
tools — **Claude (Code)**, **Codex**, **Cursor**, **Grok**, and
**Antigravity** — and then update whatever instruction files, mirror
files, or settings can be updated to close gaps found, for each tool
where that is actually feasible.

Two deliverables, both explicitly requested:

1. A status report document (one document covering all five tools,
   or one section per tool — Design & Review's call on shape) stating,
   per tool: which instruction-file convention it reads (if any), whether
   it supports the parent-child subagent + per-child worktree isolation
   baseline ADR 0017 describes, whether it has any equivalent to
   `SendMessage`/`ListAgents` peer-to-peer messaging, and whether this
   repository's existing mirror file for it (if one exists) is accurate,
   stale, or missing.
2. Instruction-file / mirror-file / settings updates, applied where the
   survey finds a real, fixable gap — not a redesign of the collaboration
   model itself, and not a promise to make every tool fully equivalent to
   Claude Code (ADR 0017 already establishes that peer-to-peer messaging
   is Claude-Code-specific and other tools use the portable baseline
   instead).

## Current state (what already exists, to avoid re-deriving from scratch)

- `docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md`
  already documents, from primary-source research conducted this session
  (item-0007 / `WP-0004-multi-agent-tool-loop-portability.md`), that Codex
  CLI, GitHub Copilot, and xAI Grok Build support only parent-child
  subagent fan-out with per-child worktree isolation — not
  `SendMessage`/`ListAgents`-style peer messaging. That research is
  existing ground truth for **Codex** and **Grok**; this item's own spike
  should re-check it is still current (tool capabilities change), not
  necessarily redo it from zero.
- Existing mirror files, per
  `docs/collaboration/prompt-instruction-change-control.md`'s own
  ADR-0006 contract-file list: `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`,
  `.cursor/rules/*.mdc`. So **Cursor** already has a mirror file
  (`.cursor/rules/*.mdc`) and **Grok** already has one
  (`.grok/rules/*.md`) — the survey's job for these two is to confirm
  each file is still accurate against the current `CLAUDE.md`, not to
  create it from nothing.
- **Codex**: `AGENTS.md` is Codex CLI's own standard instruction-file
  convention (and is also the generic multi-tool file this repository
  already maintains) — confirm this mapping is still correct and the
  content is current.
- **Antigravity**: not covered anywhere in this repository today. No
  existing research, no mirror file, no confirmed instruction-file
  convention. Full spike required for this one specifically — do not
  assume it follows any other tool's convention without checking a
  primary source (its own documentation).
- **Claude (Code)**: the reference implementation this whole contract is
  written against (`CLAUDE.md` itself, `SendMessage`/`ListAgents`,
  `docs/collaboration/cross-session-messaging.md`). Include it in the
  report for completeness/baseline comparison, but it needs no new
  research — it is what the other four are being compared against.

## Why it might matter

This repository is explicitly designed to be adopted by teams using
different AI coding tools (`docs/collaboration/adoption-guide.md`,
ADR 0017's own stated goal). A stale or missing mirror file for a tool a
new adopter actually uses means that adopter's agent either ignores this
repository's own governance model entirely or follows an outdated version
of it — silently, with no signal that anything is wrong. A periodic
support-status audit, ideally repeatable (not just a one-time report), is
also the kind of drift this session has repeatedly found and fixed for
other artifact types (contract-consistency checks, document lifecycle) —
worth considering whether this survey's own findings suggest a
lightweight recurring check, though that decision is explicitly left to
Design & Review's own spike/proposal, not decided here.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes — this is
  documentation/research and file updates, no paid tooling required in
  principle; if verifying a specific tool's actual current behavior would
  require a paid subscription or account this session doesn't have,
  name that limitation explicitly in the report rather than guessing past
  it or silently skipping the tool.
- Boundaries or non-goals:
  - Do not redesign ADR 0016's two-group topology or ADR 0017's portable
    baseline as part of this item — the goal is accurate status reporting
    and mirror-file currency, not a new architecture decision. If the
    survey finds something that genuinely requires an architecture
    change, that is a reopening trigger / new backlog item, named in the
    report, not silently decided here.
  - Do not fabricate a tool's capabilities from general knowledge alone —
    per this repository's own established discipline (`Every claim states
    its grounds`), each per-tool claim in the report needs a stated
    source: the tool's own current documentation, a primary-source check,
    or an explicit "could not verify, here is why" note. This is exactly
    the standard item-0007's own spike (case behind WP-0004) already met
    for Codex/Copilot/Grok — match it, don't regress from it.
  - Updating a mirror file for a tool this session cannot directly test
    (most of them — this is a Claude Code session) is expected and fine,
    the same way the existing `.cursor/`/`.grok/` mirrors were produced
    without live-testing inside Cursor or Grok themselves; note this
    limitation in the report rather than treating an untested mirror
    update as equivalent to a verified one.

## Uncertainty

- [ ] Spec can be written now
- [x] Spike required first (options, feasibility, or quality unknown) —
      confirm whether the existing Codex/Grok research in ADR 0017 is
      still current, and fully investigate Antigravity from primary
      sources (no existing research in this repository at all).
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none yet
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: `docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md`
  (existing Codex/Grok/Copilot research this item builds on);
  `docs/architecture/adr/0006-...` — related:
  `docs/collaboration/prompt-instruction-change-control.md` (mirror-file
  list), `docs/collaboration/cross-session-messaging.md`,
  `docs/backlog/item-0007-multi-agent-tool-loop-portability.md` (prior,
  already-done, related work)

## Promotion notes

Filled when status becomes `promoted` or `spiked` or `dropped`.

- Date: 2026-08-20
- Decision: Promoted, in the Backlog-layer thread ("はい。承認"). Per ADR
  0016 Rule 2, Design & Review proceeds autonomously from here, starting
  with the spike (confirming the existing Codex/Grok research is current,
  and fully investigating Antigravity from primary sources).
- Reason: Concrete, well-scoped request with existing ground truth to
  build on for 3 of the 5 tools; ready to begin with the spike.
