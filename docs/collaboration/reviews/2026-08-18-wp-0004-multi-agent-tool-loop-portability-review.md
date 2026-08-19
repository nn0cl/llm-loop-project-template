# Review Record: WP-0004 — Multi-Agent Tool Loop Portability

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in the Design & Review
      group's own standing session, which authored `DA-2026-08-18-03`
      (including its primary-source spike) and WP-0004/LISS-0029/LISS-0030's
      initial issue text, but did not author the artifact under review — ADR
      0017, the five mirror-file edits, and the trace were produced by a
      separately spawned Implementation-group agent (`agentId
      aa0b88c1afb374097`), branch `process/adr-0017-portable-loop`. Reviewed
      from an independently checked-out detached worktree (`git worktree add
      --detach /tmp/verify-wp0004 b4e3629`).
- [x] **Deterministic precondition.** `python3 scripts/check-contract-consistency.py`
      re-run independently against the detached checkout. Output below.
- [x] **Falsification burden.** Failure scenarios below.

## Review Target

- Artifact: commits on top of `d9c6e6b` through `b4e3629`, branch
  `process/adr-0017-portable-loop`, implementing LISS-0029 and LISS-0030
  under WP-0004.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-18-multi-agent-tool-loop-portability.md`
  (`DA-2026-08-18-03`)
- Specification: none (process/governance work plan).
- Current phase: Preflight passed; work-plan-level Review.
- Producing persona: Implementer (Implementation group, spawned agent
  `aa0b88c1afb374097`).
- Reviewing persona / model / tool: Reviewer, Design & Review group
  standing session, Claude Sonnet 5 via Claude Code.
- Approval type: **Specification conformance**, **Phase correctness**,
  **Boundary conformance**, **Evidence sufficiency**.
- Preflight result: pass (re-verified below).

## Deterministic Verification Output

```text
$ git worktree add --detach /tmp/verify-wp0004 b4e3629
Preparing worktree (detached HEAD b4e3629)

$ cd /tmp/verify-wp0004 && python3 scripts/check-contract-consistency.py
contract consistency: all checks passed

$ git diff --stat d9c6e6b process/adr-0017-portable-loop -- \
    docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md \
    docs/collaboration/cross-session-messaging.md
(empty -- neither file touched, confirming the design agreement's explicit
non-goal)

$ ls docs/collaboration/traces/2026-08-18-liss-0030*
docs/collaboration/traces/2026-08-18-liss-0030-mirror-portable-loop-wording.md

$ git diff --stat d9c6e6b process/adr-0017-portable-loop
 15 files changed, 851 insertions(+), 22 deletions(-)
(the five mirror-file edits are insertion-only, per LISS-0030's own
Preflight claim -- independently confirmed by reading each mirror's diff:
AGENTS.md, CLAUDE.md, .github/copilot-instructions.md,
.grok/rules/03-collaboration-and-completion.md,
.cursor/rules/03-collaboration-and-completion.mdc all show only "+" lines
for the new section, no removed content)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | ADR 0016 or `cross-session-messaging.md` was edited despite the explicit non-goal | `git diff --stat` scoped to those two files, on this branch, is empty. | not reproduced |
| 2 | The new ADR 0017 overclaims tool support (e.g. asserts a tool has peer-to-peer messaging it does not) | Read ADR 0017 in full: every claim in its Context/Decision sections is attributed to a specific, dated, fetched primary source (or explicitly marked "secondary/blog... corroborating, not conclusive" for Cursor) — matches `DA-2026-08-18-03`'s own Spike Result exactly, not a reworded or stronger claim. | not reproduced |
| 3 | A mirror file's content diverges in substance from the others (violates "equivalent effective content") | Read `CLAUDE.md`'s and `.cursor/rules/03-collaboration-and-completion.mdc`'s new sections side by side: same four points (layer concept, portable baseline, `SendMessage` scoping, file-based fallback), each adapted in wording to the target tool (the Cursor version explicitly ties the portable baseline to "Cursor's own agent isolation model") without changing the substance. | not reproduced |
| 4 | The `docs/collaboration/handoffs/WP-<NNNN>-status.md` fallback is described as, or accompanied by, a new live-notification mechanism | ADR 0017 Rule 4 and its Enforcement section explicitly reject this framing ("not a new automation surface, daemon, or poller"); no new script, workflow, or scheduled job appears in the diff. | not reproduced |
| 5 | A contract-file mirror change (five files) landed without a trace | Trace file confirmed present, naming all five files. | not reproduced |
| 6 | `check_parity_completeness` was left unsatisfied by the new `AGENTS.md`/`CLAUDE.md` "Session Topology Across AI Coding Tools" section | Diff to `scripts/check-contract-consistency.py` shows the new section correctly registered in `MIRRORED_SECTIONS`, and the full consistency run passes with zero failures (a missing classification would fail `check_parity_completeness` by design). | not reproduced |

## Scenarios Not Searched

- Full primary-source verification of Cursor's own subagent/worktree
  mechanics (the spike itself discloses this as secondary-source-only,
  per `DA-2026-08-18-03`'s own Deferred Questions) — not re-attempted by
  this review; treated as a known, disclosed gap rather than a defect.

## Checklist

- [x] Artifact belongs to the phase run (Architecture Path); no later phase
      leaked in.
- [x] Acceptance criteria in `DA-2026-08-18-03`'s Plan table satisfied.
- [x] No boundary named in the design agreement crossed.
- [x] Every claim states its grounds (every ADR 0017 assertion traces to a
      dated, fetched source or is explicitly marked as corroborating-only).
- [x] Record lets a third party re-run this same search.

## Decision

- [x] Approved

## Reasons

- ADR 0016 and `cross-session-messaging.md` are confirmed untouched.
- ADR 0017's claims are traceable to the actual primary-source spike, not
  overstated.
- All five mirror files carry equivalent effective content, each adapted
  appropriately to its target tool.
- The file-based fallback stays a plain repository artifact, not a new
  automation surface, consistent with the design agreement's Falsification
  Criteria.
- Trace present; deterministic precondition satisfied against an
  independently checked-out copy.

## Note on merge-time reconciliation

Landing this branch reintroduces `docs/architecture/adr/0017-*.md`, closing
the temporary numbering gap WP-0006's ADR 0018 disclosed in advance. Once
merged: (a) `README.md`/`QUICKSTART.md`/`QUICKSTART.ja.md`'s ADR-range
statements need to state the combined, now-contiguous `0001-0018` range;
(b) the `.github/workflows/ci.yml` "Check architecture decision records"
step — currently running WP-0007's temporarily-relaxed naming-only check,
per that merge's own commit message — should have its strict
contiguous-sequence version restored, since the sequence will be whole
again. Both are Design & Review's own follow-up at merge time, not a defect
in this branch.

This review does not itself close WP-0004 — Director action, Backlog
layer.
