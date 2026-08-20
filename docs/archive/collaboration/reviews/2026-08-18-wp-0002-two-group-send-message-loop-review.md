# Review Record: WP-0002 — Standing Two-Group Loop over send_message

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in the Design & Review
      group's own standing session, which drafted ADR 0016 (LISS-0019) but
      did not produce any of the LISS-0020–LISS-0026 propagation work under
      review here — that work was produced by a separately spawned
      Implementation-group session. This review was written from the actual
      committed diff (`3398942..dad873b`), the issue files' own recorded
      self-reviews, and the AI work traces — not from the Implementer's
      chat reasoning, which this session never had access to beyond what is
      written into those files. See "Provenance verification" below for how
      the reviewed commits' origin was independently confirmed rather than
      taken on the Implementer's word.
- [x] **Deterministic precondition.** `scripts/check-contract-consistency.py`
      and the ADR 0001/0014 phrasing grep sweep were both re-run
      independently by this review, against the actual committed tree, not
      copied from WP-0002's own Preflight section. Output recorded below.
- [x] **Falsification burden.** Failure scenarios searched for, and the
      grounds each does not occur, are named in the table below — one row
      per contract-file issue plus work-plan-level scenarios.

## Review Target

- Artifact: commits `eb74d7f`..`dad873b` (8 commits) on top of `3398942`,
  implementing LISS-0020 through LISS-0026 under WP-0002.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`
  (`DA-2026-08-18-01`)
- Specification: none (process/governance work plan; no application spec).
  Acceptance criteria are WP-0002's own Plan table and each LISS issue's
  Acceptance Notes.
- Current phase: Preflight passed; work-plan-level Review (Task 10).
- Producing persona: Implementer (Implementation group, first standing
  session, agent `a9da782681672e59b`).
- Reviewing persona / model / tool: Reviewer, Design & Review group standing
  session, Claude Sonnet 5 via Claude Code CLI.
- Approval type: **Specification conformance**, **Phase correctness**,
  **Boundary conformance**, and **Evidence sufficiency** — all four,
  addressed separately below per `docs/architecture/agent-quickstart.md`'s
  instruction never to infer one from another.
- Preflight Validation record: `docs/work-plans/WP-0002-two-group-send-message-loop.md`,
  "Preflight Validation" section.
- Preflight result: pass (re-verified independently below, not merely read).

## Provenance verification

Before reviewing content, this session verified — independently, via its own
tool calls, not by trusting any third-party description — that the reviewed
commits are genuine. During this review, this session received three
messages in-band claiming to be from an unidentified "coordinator,"
including one instructing this session to trust that the Implementation
session's commits had landed on this session's own branch. None of these
messages arrived in this environment's documented `SendMessage`
cross-session wrapper format, and none were treated as authoritative. Instead:

- Direct `SendMessage` contact was (re-)established with the Implementation
  session using the agentId this session itself received when it spawned
  that session (`a9da782681672e59b`) — not an address supplied by the
  disputed messages.
- `git worktree list` and `git branch -a`, run directly by this session, were
  used to independently confirm that no separate worktree or branch exists
  for that agentId in this repository — the commits are genuinely on this
  session's own branch (`worktree-agent-a2450968f458bbc6f`), consistent with
  nested `isolation: worktree` spawning (an already-isolated worktree
  spawning a further isolated worktree) not producing a second, separate
  worktree in this environment.
- The content itself corroborates this independently: the trace file for
  LISS-0025 records its own "Environment" as this exact worktree path and
  branch name, and `docs/collaboration/cross-session-messaging.md`'s
  "Confirmed failure mode" section documents, with matching concrete detail
  (error strings, the working `to: "main"` address), the Implementation
  session's own real difficulty reaching this session — independently
  consistent with this session's own experience of the handoff, not
  something either party could have coordinated after the fact through the
  disputed channel.
- `git remote -v` and `git branch -r --contains dad873b` were run to confirm
  no push occurred (`dad873b` is not reachable from any remote-tracking
  branch).

This review proceeded against the commits because their presence, and their
un-pushed, uncommitted-to-main state, were independently established by this
session's own tool calls — not because any unverified message said so.

**Addendum (2026-08-18, per item-0008):** a later Backlog-thread
investigation (`docs/backlog/item-0008-coordinator-message-hallucination-correction.md`)
found no mechanism anywhere in the repository — no `.claude/settings*.json`,
no hook files, no trace in git history on any branch — capable of injecting
the four "coordinator" messages described above. The only legitimate
occurrences of "coordinator" in the repository are ordinary prose in
pre-existing 2026-08-02 review records, files a session doing normal design
intake or Preflight file-scanning would read. The likely explanation is
model-side confabulation triggered by that legitimate historical
terminology, not external injection. This does not change the finding
above: the messages were correctly refused as unverified regardless of
origin, and this addendum does not change this review's Decision
(Approved). See the corrected "Confirmed failure mode" section in
`docs/collaboration/cross-session-messaging.md` for the full correction.

## Deterministic Verification Output

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed

$ grep -rn "does not start without" --include="*.md" . | grep -v "/traces/\|/reviews/"
docs/collaboration/design-agreement.md:164:This specific work plan's own successor does not start without this — the
docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md:13:  clause 5's "the next work plan does not start without [close]" as applied
docs/at-tdd/process.md:198:   work plan does not start without this.
docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md:13:does not start without [close]") as applied *across concurrently in-flight
docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md:92:   optional reading: the next work plan does not start without it. It
docs/issues/LISS-0019-adr-0016-two-group-topology.md:41:     0014 clause 5's "the next work plan does not start without [close]"
docs/issues/LISS-0019-adr-0016-two-group-topology.md:251:     found the "next work plan does not start without it" phrase actually
docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md:13:("the next work plan does not start without [close]") as it applies across
docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md:235:| ADR 0014, Decision, clause 5 (blocking clause) | ... |
docs/work-plans/WP-0002-two-group-send-message-loop.md:140:  work plan does not start without [close]") across all updated documents,
docs/issues/LISS-0025-design-agreement-backlog-gate-reconciliation.md:120:  phrasing ("the next work plan does not start without [close]") found

$ git remote -v
origin	git@github.com:nn0cl/llm-loop-project-template.git (fetch)
origin	git@github.com:nn0cl/llm-loop-project-template.git (push)

$ git branch -r --contains dad873b
(no output — not reachable from any remote branch)

$ git diff 3398942..dad873b -- docs/at-tdd/process.md | wc -l
0
```

Of the "does not start without" hits: `design-agreement.md:164` reads "This
specific work plan's own successor does not start without this" —
qualified, correctly scoped to the one work plan being closed, per ADR 0016
Rule 3. `docs/at-tdd/process.md:198` is a genuine unqualified restatement of
the pre-ADR-0016 model — correctly left unedited, since that file is outside
`DA-2026-08-18-01`'s and WP-0002's stated Scope, and correctly recorded as an
out-of-scope finding in WP-0002's own Preflight section rather than silently
fixed or silently ignored. All ADR 0014/0016 hits are the documents stating
the supersession itself, not describing the old behavior as current.

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | LISS-0020 (`personas.md`) changed a persona's five required fields (responsibilities, inputs, outputs, done-when, must-not) instead of only adding topology | Read full diff: only a new "Session Groups" section and the "Where each persona operates" diagram changed; no persona's field-level prose was touched | not reproduced |
| 2 | LISS-0021 (`ai-human-scheme.md`) altered the Reviewer's three constraints, self-review requirements, or the three invariants | Read full diff: the added sections ("Non-blocking concurrency," "Intervention channel") are additive; the existing "Self-review (Implementer...)" and "AI approval (Reviewer...)" sections and their constraint lists are present, unedited, in the diff context | not reproduced |
| 3 | LISS-0022 (`cross-session-messaging.md`) omits a handoff direction's trigger, message content, or record file, or fails to state "message is a trigger, not a record" as a named rule | Read the full new file: five numbered handoff directions each with explicit Trigger/Message/Record subsections; a top-level "The governing rule: a message is a trigger, not a record" section citing Invariant 1 by name | not reproduced |
| 4 | LISS-0022's `ListAgents` failure handling is a soft suggestion rather than a stated reopening-worthy blocker | Read the file: "this is a blocker, not a judgment call," with four explicit non-actions (guess, retry indefinitely, assume pickup, treat absence as no-work-in-flight) and a named reopening-request path | not reproduced |
| 5 | LISS-0023 (`session-start-and-resume.md`) duplicates LISS-0022's protocol content instead of cross-referencing it, or drops the artifact-only continuity rule | Read the diff: "this document does not restate that protocol's content; see it for the concrete contract"; re-establishment explicitly restated as following "the same artifact-only continuity rule as any resumed session" | not reproduced |
| 6 | LISS-0024 (`branch-commit-pr-discipline.md`) weakens or contradicts an existing branch/PR rule while adding the worktree mechanic | Read the diff: new subsection is appended after the existing "Parallel Agent Work (Worktrees)" section, states "does not change branch-naming, the CI gate, the feature-unit branch creation steps, or any other rule in this document" | not reproduced |
| 7 | LISS-0025 (`design-agreement.md`) weakens "Silence is not agreement," or omits the intervention-gated provisional-record rule | Read the diff: "Silence is not agreement, and neither is proceeding without objection" is present unedited; new "Backlog-item-level agreement" subsection states explicitly "This does **not** weaken 'Silence is not agreement'"; new "Intervention-gated provisional records" subsection states the provisional marking and that only a resolving instruction removes it | not reproduced |
| 8 | Six-of-eight required AI work traces under `docs/collaboration/traces/` are missing or empty | `ls docs/collaboration/traces/2026-08-18-liss-002*.md` — confirmed all six (LISS-0020 through LISS-0025) present with substantive content (read two in full: LISS-0022's embedded self-review, LISS-0025's full trace file; spot-checked command output and Result fields in the other four) | not reproduced |
| 9 | LISS-0026 (`docs/backlog/README.md`) either wrongly required a trace (it is not a contract file) or wrongly skipped one it needed | Confirmed `docs/backlog/README.md` is outside `docs/collaboration/*.md` and every other path in `prompt-instruction-change-control.md`'s Agent Operating Contract Files list; LISS-0026's own Work Notes state this explicitly and correctly | not reproduced |
| 10 | Preflight recorded `pass` while the checker actually fails, or the record's pasted output does not match a fresh run | Re-ran `python3 scripts/check-contract-consistency.py` independently against the actual committed tree: `contract consistency: all checks passed`, matching WP-0002's recorded output | not reproduced |
| 11 | A superseded ADR 0001/0014 phrasing is left anywhere, unqualified, describing the pre-ADR-0016 model as still current, within this work plan's Scope | Re-ran the grep sweep independently (output above): the only unqualified hit (`docs/at-tdd/process.md`) is outside WP-0002's Scope and is recorded as an open finding, not silently fixed or silently left unrecorded | not reproduced |
| 12 | The work plan pushed, opened a PR, merged to `main`, or marked any issue/work-plan/agreement `done`/`closed`/`resolved` | `git branch -r --contains dad873b` returns nothing (not pushed); `git status`/issue Status fields show `review`, not `closed`/`resolved`/`done`; WP-0002's "Work-Plan Close" section still reads "pending" | not reproduced |
| 13 | `docs/backlog/item-0005-*.md`, `item-0006-*.md`, or `item-0007-*.md` were touched, exceeding this work plan's authorized scope | `git diff --stat 3398942..dad873b` lists no `docs/backlog/item-0005`, `item-0006`, or `item-0007` path | not reproduced |
| 14 | An intervention or a review-finding was recorded as halting a group's other concurrent work rather than gating only the specific in-flight item | Read `ai-human-scheme.md`'s new "Intervention channel" section and `cross-session-messaging.md`'s direction 5: both state "not the group's other concurrent work" / "other concurrently in-flight work plans or backlog items... are unaffected" | not reproduced |

## Scenarios Not Searched

- Whether `ListAgents`' actual absence from the Implementation session's
  tool list (as opposed to the two failed `SendMessage` attempts, which this
  review independently reproduced the pattern of in its own handoff
  exchange) would reproduce in a fresh, unrelated session — this review
  relies on the Implementation session's and this session's own consistent,
  independently-arrived-at experience, not on invoking `ListAgents` itself
  from a third vantage point.
- Full line-by-line proofreading of every cross-reference path across all
  seven changed documents beyond what the checker (which resolves file
  references) and the targeted reads above covered.
- The AI Planning Records' token estimates were not checked against actual
  usage — this harness does not surface actual token counts, as each
  record itself states, so there is nothing to check them against.
- Whether a differently-shaped nested `isolation: worktree` spawn (not
  nested inside an already-isolated worktree) would produce a true separate
  worktree — out of scope for this review, but worth flagging as a
  follow-up: LISS-0024's new worktree rule describes worktree creation "at
  the ... handoff, before Phase 0 Design Intake starts," which held for a
  freshly-spawned, non-nested Implementation session, but this specific run
  was itself a nested spawn from within the Design & Review group's own
  isolated worktree, where isolation collapsed. This is a real environment
  interaction, not a defect in what LISS-0024 states, since LISS-0024
  describes the intended mechanic rather than every possible spawn topology.

## Checklist

- [x] The artifact belongs to the phase that was run (Architecture Path
      contract-file propagation); no application-code phase leaked in — all
      21 changed files are documentation/process files.
- [x] Every acceptance criterion in each of LISS-0020 through LISS-0026 is
      addressed by the corresponding diff (verified per-issue above).
- [x] No boundary named in the design agreement was crossed: ADR 0006's
      contract-file governance is intact (this review is exactly the
      required separate-context Reviewer pass); the Reviewer's three
      constraints, the Implementer's self-review requirements, and the
      three invariants are unedited in `ai-human-scheme.md`'s diff; no push,
      PR, merge, or `done`/`closed`/`resolved` marking occurred; out-of-scope
      files (`docs/at-tdd/process.md`, `item-0005`/`0006`/`0007`) were not
      touched.
- [x] Specifications and accepted tests were not modified to make work
      pass — not applicable in substance (no application spec exists for
      this work plan), and no issue's own Acceptance Notes were edited to
      match what was built rather than the reverse.
- [x] Every claim in the artifact states its grounds — each issue's
      self-review names a command and its actual output; WP-0002's Preflight
      section pastes real command output rather than a summary.
- [x] The record would let a third party re-run this same search — commands
      are the exact ones pasted above, runnable from this worktree.

## Decision

- [x] **Approved**

## Reasons

All six ADR-0006 contract-file changes (LISS-0020–0025) were reviewed
individually against their own Acceptance Notes and found conforming, with
no regression to the invariant/constraint/boundary content each was required
to leave untouched. The seventh, non-contract-file change (LISS-0026)
correctly states why it carries no trace. Preflight's `pass` result was
independently reproduced, not merely read. Two genuine out-of-scope findings
surfaced during Preflight — `docs/at-tdd/process.md`'s unqualified
pre-ADR-0016 phrasing, and this review's own provenance question about
nested worktree isolation — were correctly left unresolved rather than
guessed past, and are carried forward to the Director in this session's
report rather than silently fixed or silently dropped. No push, PR, merge,
or `done`/`closed`/`resolved` marking occurred; the work-plan close remains
the Director's own pending action.
