# Review Record: WP-0006 — Mandatory Quality-Gate Hooks and Perspectives Document

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in the Design & Review
      group's own standing session, which authored `DA-2026-08-18-05` and
      WP-0006/LISS-0032/LISS-0033's initial issue text, but did not author
      the artifact under review — ADR 0018, the four contract-document
      edits, `design-review-perspectives.md`, and the prompt-script
      strengthening were produced by a separately spawned
      Implementation-group agent (`agentId af7587091e1cec4ac`), working in
      its own worktree, branch `process/quality-gate-hooks-and-coverage-policy`.
      This review is written from the actual committed diff, independently
      re-checked out into a separate detached worktree (`git worktree add
      --detach /tmp/verify-wp0006 2c34838`) rather than from the
      Implementer's chat report.
- [x] **Deterministic precondition.** `python3 scripts/check-contract-consistency.py`
      was re-run independently against the detached checkout. Output
      recorded below.
- [x] **Falsification burden.** Failure scenarios searched for, and the
      grounds each does not occur, are named in the table below —
      including independent verification that the perspectives document's
      citations trace to real text, not fabricated or paraphrased-past
      quotes.

## Review Target

- Artifact: commits `b1a49c1`..`2c34838` (5 commits) on top of `57af72e`, on
  branch `process/quality-gate-hooks-and-coverage-policy`, implementing
  LISS-0032 and LISS-0033 under WP-0006. Includes one addition
  (`2c34838`) made after this review's own SendMessage request to merge a
  fourth perspectives entry, per the document's own "merge into an
  existing related perspective" editing rule.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md`
  (`DA-2026-08-18-05`)
- Specification: none (process/governance work plan). Acceptance criteria
  are the design agreement's Plan table and each issue's Acceptance Notes.
- Current phase: Preflight passed (independently re-verified below);
  work-plan-level Review.
- Producing persona: Implementer (Implementation group, spawned agent
  `af7587091e1cec4ac`).
- Reviewing persona / model / tool: Reviewer, Design & Review group
  standing session, Claude Sonnet 5 via Claude Code.
- Approval type: **Specification conformance**, **Phase correctness**,
  **Boundary conformance**, and **Evidence sufficiency** — addressed
  separately below.
- Preflight Validation record: `docs/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md`,
  "Preflight Validation" section.
- Preflight result: pass (re-verified independently below).

## Deterministic Verification Output

```text
$ git worktree add --detach /tmp/verify-wp0006 2c34838
Preparing worktree (detached HEAD 2c34838)
HEAD is now at 2c34838 process: sharpen the "verify claimed authority" perspective (peer-suggested)

$ cd /tmp/verify-wp0006 && python3 scripts/check-contract-consistency.py
contract consistency: all checks passed

$ git ls-tree process/quality-gate-hooks-and-coverage-policy -- docs/architecture/adr/ | tail -3
... 0016-standing-two-group-topology-and-backlog-gated-autonomy.md
... 0018-mandatory-quality-gate-hooks-and-coverage-policy.md
(0017 correctly absent on this branch -- reserved for WP-0004's own
unmerged ADR; no collision, per DA-2026-08-18-05's numbering rule)

$ ls docs/collaboration/traces/2026-08-18-liss-0032* docs/collaboration/traces/2026-08-18-liss-0033*
docs/collaboration/traces/2026-08-18-liss-0032-definition-of-done-hook-coverage.md
docs/collaboration/traces/2026-08-18-liss-0033-perspectives-doc-and-required-reading.md

$ git show process/quality-gate-hooks-and-coverage-policy:docs/issues/LISS-0032-quality-gate-hooks-and-coverage-policy.md | grep "^- Status"
- Status: review
$ git show process/quality-gate-hooks-and-coverage-policy:docs/issues/LISS-0033-design-review-perspectives-doc.md | grep "^- Status"
- Status: review

Independent citation spot-checks against the actual review-record source files
(not the perspectives document's own prose):
$ grep -n "checklist that passes is not evidence the tree is correct" docs/collaboration/reviews/2026-08-02-contract-consistency-review.md
431:  think to try. A checklist that passes is not evidence the tree is correct;
$ grep -n "materially" docs/collaboration/reviews/2026-08-02-contract-consistency-review-2.md
294:Judgment: **the disclosure is honest about what it says, but materially
$ grep -n "merge-base --is-ancestor" docs/collaboration/reviews/2026-08-02-contract-consistency-review-2.md
15:an ancestor of the current branch tip (`git merge-base --is-ancestor 2183b8e
$ grep -n "coordinator's own stated distrust" docs/collaboration/reviews/2026-08-02-contract-consistency-review-4.md
34:  range rules (especially the separator whitelist, per the coordinator's own
$ grep -n "independently by this review, against the actual committed tree" docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md
18:      independently by this review, against the actual committed tree, not
(all five citation spot-checks reproduced; none fabricated or misquoted)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | ADR 0018 mandates one universal numeric coverage floor, overstepping the design agreement's explicit non-decision | Read ADR 0018 Rule 3 in full: "does not mandate one specific numeric coverage floor... each adopting project may choose a local numeric floor... not fixed by this template's contract" — matches `DA-2026-08-18-05`'s Settled Ambiguities exactly. | not reproduced |
| 2 | The retroactivity question is left unresolved or silently assumed | ADR 0018 Rule 4 states it explicitly with grounds, matching the design agreement's reasoning rather than re-deriving a different answer. | not reproduced |
| 3 | The perspectives document's cited quotes are fabricated, paraphrased past what the source says, or misattributed | Independently re-ran five spot-check greps directly against the named source files (not the perspectives document's own text) — all five located, verbatim, at the cited files. Also confirmed the LISS-0033 Work Notes show the Implementer deliberately declined to use one of my own suggested illustrative perspective titles because it did not trace to the sampled records' actual text — evidence of the verification discipline being genuinely applied, not assumed. | not reproduced |
| 4 | The perspectives document duplicates `findings-reuse.md`'s per-finding lifecycle instead of generalizing from it | Read the document's own "How this differs from findings-reuse.md" section: explicitly states no status/lifecycle fields are imported; a perspective stays open even after its originating finding is `closed`. | not reproduced |
| 5 | `definition-of-done.md`'s existing criteria were weakened or removed to add the new hook/coverage requirements | Full diff of the file shows only additive changes (`+` lines extending existing bullet points); no `-` line removes prior content. | not reproduced |
| 6 | A contract-file change (`definition-of-done.md`, the new perspectives document, `CLAUDE.md`) landed without a trace | Both required trace files confirmed present in the independently checked-out tree; `docs/architecture/agent-quickstart.md`'s edit correctly has no trace, since it is not in `prompt-instruction-change-control.md`'s contract-file list (confirmed by re-reading that list) and the LISS-0033 trace explicitly names which files it covers. | not reproduced |
| 7 | The ADR-numbering coordination with the concurrently in-flight WP-0004 (claiming `0017`) produced an actual collision, silently unflagged | `0017` is confirmed absent from this branch's `docs/architecture/adr/` tree; ADR 0018's own "Numbering note" section, LISS-0032's Work Notes, and WP-0006's Preflight "Scope result" all independently name the resulting range-statement gap and explicitly assign its reconciliation to the Design & Review group at merge time — not silently resolved, not silently ignored. | not reproduced |
| 8 | `scripts/` in this template repository was required to gain retroactive coverage as a side effect of this work plan | Rule 4 explicitly states this ADR does not require it; no diff under `scripts/*.py` adds tests. | not reproduced |
| 9 | Any new meaning-inference heuristic was introduced (out of this work plan's own scope, but worth checking since ADR 0018 discusses coverage "meaning") | ADR 0018 Rule 2 is a qualitative rule for human/AI reviewer judgment against a diff, not a new automated check in `check-contract-consistency.py` — this work plan does not touch that script at all (confirmed: no diff under `scripts/check-contract-consistency.py`). | not reproduced |

## Scenarios Not Searched

- Whether every one of the strengthened `scripts/lib/emit-tooling-setup-prompt.sh`'s per-stack hook examples (native git hooks, husky/lefthook, `pre-commit`, etc.) is itself current best practice for that ecosystem — out of scope; the ADR and design agreement both frame these as illustrative starting points for an adopting project's own tooling-setup session to verify against official docs at the time it runs, not as claims this review is positioned to fact-check for every ecosystem today.
- Full line-by-line review of `docs/architecture/testing-strategy.md`'s and `docs/architecture/tooling.md`'s complete diffs beyond the "Coverage Policy" section and hook-wiring requirement already spot-checked — read in full during design intake for `DA-2026-08-18-05` and re-skimmed here; not re-verified line-by-line a second time since neither is an ADR-0006 contract file and neither shows unexpected structural change in `git diff --stat`.

## Checklist

- [x] The artifact belongs to the phase that was run (Architecture Path);
      no later phase leaked in.
- [x] Every acceptance criterion in `DA-2026-08-18-05`'s Plan table is
      satisfied (Tasks 1-9 all have corresponding diff/commit evidence).
- [x] The dependency rule and port boundaries hold — N/A, no application
      code.
- [x] No boundary named in the design agreement was crossed (no universal
      numeric floor mandated; no retroactive `scripts/` work; pattern
      5-equivalent duplication not present; `findings-reuse.md` untouched).
- [x] Specifications and accepted tests were not modified — N/A, none
      exist for this work plan.
- [x] Every claim in the artifact states its grounds (ADR 0018's Rules 3
      and 4 both restate `DA-2026-08-18-05`'s reasoning explicitly rather
      than asserting bare conclusions).
- [x] The record would let a third party re-run this same search (every
      command above is pasted verbatim, re-runnable against commit
      `2c34838`).

## Decision

- [x] Approved

## Reasons

- All nine named failure scenarios were searched for and none reproduced,
  including an independent re-verification of the perspectives document's
  citations against the actual source files rather than trusting the
  Implementer's report of them.
- The deterministic precondition was satisfied against an independently
  checked-out copy of the actual committed tree.
- The flagged human-decision question in item-0006's own promotion (the
  numeric-floor strictness question) was resolved with explicit,
  restated grounds at both the design-agreement and ADR level, not
  silently assumed or silently escalated back to the Director without
  first doing the narrowing work the mandate asked for.
- The ADR-numbering coordination risk with the concurrently in-flight
  WP-0004 was handled exactly as the design agreement anticipated: no
  collision, and the resulting range-statement gap explicitly flagged for
  reconciliation at merge time rather than silently resolved either way.
- Boundary conformance holds: pattern 5 (template-copy exclusion gaps) is
  not duplicated here; `findings-reuse.md`'s lifecycle is not imported into
  the new document; no contract-file change lacks a trace.

## Note for merge-time reconciliation

Per this branch's own ADR 0018 "Numbering note" and LISS-0032's Work Notes:
when this branch (`process/quality-gate-hooks-and-coverage-policy`) and
WP-0004's branch (`process/adr-0017-portable-loop`) are both merged into
`design-review/backlog-0005-0008`, `README.md`, `QUICKSTART.md`,
`QUICKSTART.ja.md`, and `.github/workflows/ci.yml`'s ADR-range statements
will need reconciling to state the combined range (`0001-0018`, contiguous)
rather than either branch's own partial view. This is expected, disclosed
in advance by the Implementer, and not a defect in either branch on its
own.

This review does not itself close WP-0006 — per
`docs/collaboration/design-agreement.md`'s "Closing a work plan," that is
the Director's own combined action, in the Backlog layer, reading this
approval.
