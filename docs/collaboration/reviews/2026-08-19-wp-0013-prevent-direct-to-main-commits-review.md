# Review Record: WP-0013 — Prevent Direct-to-Main Commits

Use this when the Reviewer persona issues a decision inside the execution loop.

A review that does not satisfy all three constraints below does not count as an
approval, whatever this record says.

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in a context with no prior
      memory of this work: no chat transcript from the Design & Review or
      Implementation sessions was read or trusted. Everything stated below
      was independently re-derived from the repository artifacts listed in
      "Review Target" — the backlog item, the design agreement, the work
      plan, the local issue, the AI work trace, the actual file diffs, and a
      command re-run in this reviewing session's own worktree. The
      Implementer's self-review claims (LISS-0042 Work Notes) were read only
      as a claim to falsify, not as evidence.
- [x] **Deterministic precondition.** `scripts/check-contract-consistency.py`
      was re-run independently in this reviewing session, against the
      current tree at commit `d9b9926` (not copied from WP-0013's own
      Preflight section). Output recorded below.
- [x] **Falsification burden.** Nine scenarios searched, each with grounds
      and a not-reproduced/reproduced result, in the Falsification Search
      table below.

## Review Target

- Artifact: `docs/collaboration/branch-commit-pr-discipline.md` (new
  "Pre-Commit Branch Confirmation" subsection) and
  `docs/collaboration/local-issue-planning.md` (broadened "Dependency
  Rules" sentence), at commit `d9b9926` on
  `origin/process/backlog-item-0012-and-0013`
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-19-prevent-direct-to-main-commits.md`
  (`DA-2026-08-19-05`)
- Specification: none — documentation/process-only change, per
  `DA-2026-08-19-05`'s "Specifications" section
- Current phase: Fast Path (mechanical, narrow, no behavior/architecture
  change)
- Producing persona: Implementer (Implementation group,
  `process/prevent-direct-to-main-commits` branch, commit `37581e1`)
- Reviewing persona / model / tool: Reviewer, Claude Sonnet 5 via Claude
  Code, separate context/worktree from both the Design & Review session
  that wrote `DA-2026-08-19-05` and the Implementation session that made
  the edits
- Approval type: boundary-conformance, evidence-sufficiency (this work has
  no application specification, so specification-conformance does not
  apply; phase-correctness is folded into boundary-conformance since there
  is only one Fast Path phase)
- Preflight Validation record: `docs/work-plans/WP-0013-prevent-direct-to-main-commits.md`,
  "Preflight Validation" section
- Preflight result: pass (re-verified independently below, not trusted from
  the pasted record)

## Deterministic Verification Output

Re-run independently in this reviewing worktree, reset to
`origin/process/backlog-item-0012-and-0013` (`d9b9926`) before running:

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
```

Exit code: 0.

Supporting re-verification commands also run independently in this session:

```text
$ git diff 632a8e4..HEAD --stat
 .../2026-08-19-prevent-direct-to-main-commits.md   | 143 +++++++++++++++++
 docs/collaboration/branch-commit-pr-discipline.md  |  27 ++++
 docs/collaboration/local-issue-planning.md         |  11 +-
 ...iss-0042-pre-commit-branch-confirmation-rule.md | 178 +++++++++++++++++++++
 ...ISS-0042-pre-commit-branch-confirmation-rule.md | 172 ++++++++++++++++++++
 .../WP-0013-prevent-direct-to-main-commits.md      | 120 ++++++++++++++
 6 files changed, 647 insertions(+), 4 deletions(-)

$ git diff 632a8e4..HEAD -- CLAUDE.md AGENTS.md .github/copilot-instructions.md '.grok/rules/*.md' '.cursor/rules/*.mdc' | wc -l
       0

$ git log --oneline 632a8e4..HEAD -- CLAUDE.md AGENTS.md .github/copilot-instructions.md .grok .cursor
(no output — no commits touch these paths)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | New rule states the confirm-before-commit requirement only for AT-TDD "issue work," not Backlog-layer records (the exact gap item-0013 exists to close) | Read the actual added text in `branch-commit-pr-discipline.md`: "Before any `git commit` — for every kind of record this repository's process produces, not only AT-TDD issue work" and its third bullet: "explicitly including Backlog-layer records such as `docs/backlog/item-NNNN-*.md`, local issues, and work plans." Cites the incident by commit (`b6c8961`) as the concrete case. `local-issue-planning.md`'s broadened sentence independently repeats the same scope ("this also covers Backlog-layer records such as backlog items, local issues, and work plans"). Both files name Backlog-layer records explicitly, not implicitly. | not reproduced |
| 2 | The broadened `local-issue-planning.md` sentence accidentally implies Backlog-layer records now require separate-context Reviewer approval (out of scope per `DA-2026-08-19-05`'s own Falsification Criteria) | Read the full added/changed text in both files verbatim. Neither contains the words "review," "approval," or "Reviewer" anywhere in the new/changed sentences. The added text is scoped entirely to branch-checking and commit-timing mechanics ("confirm the current branch," "create or switch to a dedicated branch first"), never to an approval gate. | not reproduced |
| 3 | `CLAUDE.md` or one of its four mirrors (`AGENTS.md`, `.github/copilot-instructions.md`, `.grok/rules/*.md`, `.cursor/rules/*.mdc`) was touched | `git diff 632a8e4..HEAD` against those five path patterns returns zero lines; `git log 632a8e4..HEAD` against those paths returns no commits. Confirmed directly above, not inferred from the trace's claim. | not reproduced |
| 4 | The AI work trace names the wrong contract files, the wrong reason, or the wrong expected-behavior change (Traceability Rule, `prompt-instruction-change-control.md`) | Trace's "Scope" field for Attempt 1 names both changed files and describes insertion points ("immediately after the existing 'automated maintenance branches' bullet and before '## Continuous Integration Gate'" for file 1; the "Dependency Rules" paragraph replacement for file 2). Verified both placements against the actual file contents by line number: `branch-commit-pr-discipline.md` line 38 is the "automated maintenance branches" bullet, the new subsection starts at line 45, "## Continuous Integration Gate" starts at line 72 — exact match. `local-issue-planning.md`'s "## Dependency Rules" section (line 173) contains the replaced paragraph at line 185-194 — exact match. "Why" is carried by reference to the covering design agreement (`DA-2026-08-19-05`) and its Context Ledger's included item-0013, matching this repository's own established trace convention (spot-checked against `docs/collaboration/traces/2026-08-19-liss-0041-branch-worktree-cleanup-rule.md`, which follows the identical by-reference pattern rather than restating incident prose inline). | not reproduced |
| 5 | Scope exceeds what `DA-2026-08-19-05` authorized — an unrelated file was touched | `git diff 632a8e4..HEAD --stat` (re-run independently above) shows exactly 6 files: the design agreement itself, the work plan, LISS-0042, the two edited contract files, and the new trace file. Every file is named in `DA-2026-08-19-05`'s Plan table or is the agreement/work-plan/issue record itself. No file outside that set appears. | not reproduced |
| 6 | The new rule text contradicts or duplicates (rather than cross-references) existing wording elsewhere in either file | `branch-commit-pr-discipline.md`'s pre-existing bullets (lines 23-24, "direct pushes to `main`... are prohibited," and 27-29, "do not implement issue work directly on `main`... even for a single commit") are unchanged by this diff and are not contradicted — the new subsection generalizes them, it does not restate their exact text. `local-issue-planning.md`'s broadened sentence does restate the *scope* claim ("must not commit any repository record directly on `main`... covers Backlog-layer records") in its own words before cross-referencing `branch-commit-pr-discipline.md`'s "Pre-Commit Branch Confirmation" by name for the procedural detail (how to check, when to check). This is a genuine partial overlap with the general rule's substance — more than a bare cross-reference, contrary to the Settled Ambiguities table's stated intent to avoid "duplicating the rule's substance in two places." It is not a contradiction (both statements agree), and it does not trigger any of `DA-2026-08-19-05`'s four explicit Falsification Criteria. Recorded as a non-blocking observation below, not a rejection basis. | not reproduced (as contradiction); reproduced (as a minor, non-blocking substance overlap — see Non-Blocking Observations) |
| 7 | The new rule silently leaves `git push` directly to `main` uncovered, exposing a new unreviewed gap (the original incident was "committed **and pushed**") | Re-read `docs/backlog/item-0013-prevent-direct-to-main-commits.md`'s own incident description: the failure was committing while the local branch was already `main` (the push was the automatic next step of that already-broken state, not an independent bypass). `branch-commit-pr-discipline.md` already states, pre-existing and unchanged by this diff (line 23-24), "direct pushes to `main` or the trunk branch are prohibited; all changes must arrive through a pull request that carries a Reviewer approval record" — a general push-to-main prohibition already exists independently of this change. The new rule's narrower scope (git commit while checked out on `main`) is the specific, previously-uncovered gap item-0013 names; it does not need to restate the pre-existing push prohibition to close that gap. Judged an acceptable, deliberate scope boundary, not a newly-exposed gap. | not reproduced |
| 8 | LISS-0042's self-review does not meet the short-form bar in `docs/templates/self-review.md` (deterministic output + named failure scenarios with grounds) | LISS-0042 Work Notes contains all four required fields: `Phase / finding` (Fast Path, single-attempt), `Command run` (`python3 scripts/check-contract-consistency.py`), `Result` (actual pasted output, not a summary), `Risks considered` (5 named risks) and `Why each does not occur` (5 corresponding grounds, one-to-one). Matches the template's required shape exactly. | not reproduced |
| 9 | LISS-0042's `Status: done` and WP-0013's Issue Graph row (`done`) are premature — set before the work-plan-level Reviewer has approved, contradicting `DA-2026-08-19-05`'s own Boundaries statement ("nothing marked done/closed... until the Director's own work-plan-close action") | That Boundaries sentence itself qualifies the claim: "in the Director-facing sense." WP-0013's own "Work-Plan Review" (`_pending_`) and "Work-Plan Close" (`_pending_`) sections are correctly left unfilled — the Director-facing closure has not happened. The issue-level `Status: done` reflects only that the Implementer's own work on LISS-0042 is complete and self-reviewed, which `CLAUDE.md`'s "Work-Plan Review" section itself describes as the precondition for submission to the Reviewer ("After every issue in the work plan is self-reviewed and complete, run Preflight..."). Cross-checked against two other recently-closed work plans (`WP-0011`, `WP-0012`): both used the identical pattern (`done` at the issue level, set before the plan's own Work-Plan Review/Close sections were filled). `scripts/check-contract-consistency.py` check 7 ("Issue status sync") independently confirms LISS-0042's `Status` field agrees with its Issue Graph row — the two are at least internally consistent with each other, whatever the timing question. | not reproduced |

## Scenarios Not Searched

- Whether `docs/collaboration/local-issue-planning.md`'s new sentence
  interacts correctly with every other place in the repository that quotes
  or paraphrases the old "issue work" sentence (a repository-wide grep for
  quotations of the exact old sentence was not run; only the file's own
  internal consistency and the two design-agreement-named files were
  checked). Low risk: the agreement's own scope names only these two files
  as touched, and `check-contract-consistency.py`'s reference/parity checks
  would likely surface a dangling quote if one existed, but this was not
  independently confirmed by grep.
- Whether the wording is natural-language-unambiguous to every possible
  future reader (a stylistic/clarity judgment beyond the falsification
  criteria this review is scoped to test).
- Whether a git hook or CI check should enforce this rule — explicitly out
  of scope per `DA-2026-08-19-05` and recorded as a Deferred Question there,
  not this review's job to second-guess.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked
      in (Fast Path documentation edit only — no application code, no test
      changes).
- [x] Every `Then` clause in the specification is asserted by the work — not
      applicable; no specification exists for this documentation-only change,
      per `DA-2026-08-19-05`'s own "Specifications" section.
- [x] The dependency rule and port boundaries hold — not applicable; no
      application architecture touched.
- [x] No boundary named in the design agreement was crossed — verified
      directly (scenarios 1, 2, 3, 5 above).
- [x] Specifications and accepted tests were not modified to make work pass —
      not applicable; no tests exist for this change.
- [x] Every claim in the artifact states its grounds — the new rule text
      cites the incident by commit id; the trace and self-review both cite
      command output.
- [x] The record would let a third party re-run this same search — every
      command in this record is copy-pasteable and every file/line reference
      is exact.

## Decision

- [x] Approved
- [ ] Rejected — reasons and the specific artifact changes required
- [ ] Deadlocked — escalate to Arbiter, with both positions stated
- [ ] Reopening request — the design agreement does not settle this; state
      what is unsettled and what the loop needs in order to continue

## Reasons

- All four of `DA-2026-08-19-05`'s explicit Falsification Criteria were
  independently tested and none reproduced: the new rule names Backlog-layer
  records explicitly (scenario 1), the wording does not imply new
  separate-context Reviewer approval for Backlog-layer records (scenario 2),
  neither `CLAUDE.md` nor any mirror was touched (scenario 3), and the
  required AI work trace is present and accurate (scenario 4).
- Scope matches `DA-2026-08-19-05` exactly: 6 files, all named in the
  agreement's Plan table or the agreement/plan/issue record itself
  (scenario 5).
- `scripts/check-contract-consistency.py` passes, re-run independently in
  this session against the current tree, not trusted from WP-0013's own
  Preflight section.
- LISS-0042's self-review meets the short-form bar (scenario 8).
- The one substantive issue found — `local-issue-planning.md`'s broadened
  sentence partially restates the general rule's scope claim rather than
  purely cross-referencing it (scenario 6) — is a real, minor drift from the
  Settled Ambiguities table's stated intent, but it does not contradict
  anything, does not trigger any of the four named Falsification Criteria,
  and does not narrow or misstate the rule's coverage. It is recorded below
  as a non-blocking observation rather than a rejection, per this review's
  own instruction to distinguish blocking problems from wording nits.

## Non-Blocking Observations

- `local-issue-planning.md`'s broadened "Dependency Rules" sentence
  ("Agents must not commit any repository record directly on `main` or the
  trunk branch — issue work included, but not only issue work; this also
  covers Backlog-layer records such as backlog items, local issues, and
  work plans.") restates the general rule's scope-broadening claim in its
  own words before cross-referencing `branch-commit-pr-discipline.md`'s
  "Pre-Commit Branch Confirmation" by name. The Settled Ambiguities table in
  `DA-2026-08-19-05` states the intent was to avoid "duplicating the rule's
  substance in two places." This is a soft miss of that stated intent — not
  a contradiction, not a scope violation, and not a trigger for any of the
  four Falsification Criteria — but a future editor tightening this
  documentation could shorten the `local-issue-planning.md` sentence to
  something closer to "Agents must not commit any repository record
  directly on `main` or the trunk branch; see
  `docs/collaboration/branch-commit-pr-discipline.md`'s 'Pre-Commit Branch
  Confirmation' for the full rule, which also covers Backlog-layer
  records," removing the enumerated repetition of "backlog items, local
  issues, and work plans" that now lives in both files. Not required for
  this work plan's Done.
