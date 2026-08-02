# Review Record: Mirror Parity Round 2 (PR #7, 21a6c17) and the v1.0.1 Gap on `main`

Reviewing persona: Reviewer.
Model / tool: Claude Sonnet 5, via a fresh Claude Code agent session with no
memory of the producing session's reasoning. This session read the round-2
commit (`21a6c17`), the round-2 Preflight record
(`docs/collaboration/reviews/2026-08-02-mirror-parity-preflight-2.md`), the
updated trace, the updated `CHANGELOG.md`, and my own prior review record
(`docs/collaboration/reviews/2026-08-02-mirror-parity-and-v101-review.md`) —
the last one read only as a statement of what I previously found and decided,
not re-trusted; every claim in the round-2 commit message and Preflight record
was independently re-executed rather than accepted. `main` was re-checked
directly at its current tip.

This is a new record. The prior record
(`docs/collaboration/reviews/2026-08-02-mirror-parity-and-v101-review.md`) is
left unmodified.

## Constraints (all three must hold)

- [x] **Context separation.** This session did not produce the round-2 fixes
      and was not given the producing context's reasoning — only the commit,
      the Preflight record, and the trace as artifacts to check, not to trust.
- [x] **Deterministic precondition.** All checks below were re-run in this
      session against the actual current state of both the PR branch and
      `main`; output is recorded, not summarized from the Preflight record.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below for both targets. One new non-blocking finding surfaced; no
      blocking defect reproduced in either target's round-2/current state.

---

# Target (A): PR #7, `process/mirror-new-rules-and-adr-range` at `21a6c17`

## Review Target

- Artifact: branch `process/mirror-new-rules-and-adr-range` / commit
  `21a6c17`, open as pull request #7 against `main` (`3ba0219`).
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-mirror-parity-and-adr-range.md`
  (DA-2026-08-02-06) — unchanged by round 2, correctly (no boundary or
  decision in it needed to change to fix these two defects).
- Specification: none new; same as round 1.
- Current phase: Architecture Path.
- Producing persona: Implementer, responding to my round-1 rejection.
- Reviewing persona / model / tool: Reviewer / Claude Sonnet 5 / Claude Code.
- Approval type: specification-conformance, boundary-conformance,
  evidence-sufficiency.
- Preflight Validation record (round 1):
  `docs/collaboration/reviews/2026-08-02-mirror-parity-preflight.md` — `pass`,
  and my round-1 review still rejected on it, which is itself now cited in the
  round-2 commit message as evidence for ADR 0013's own stated risk.
- Preflight Validation record (round 2):
  `docs/collaboration/reviews/2026-08-02-mirror-parity-preflight-2.md`.
- Preflight result (round 2): pass — independently re-verified below, not
  inherited.

## Deterministic Verification Output

**Defect 1 re-check — reading-sequence references, byte-for-byte and by
occurrence count:**

```text
$ for f in AGENTS.md CLAUDE.md .github/copilot-instructions.md .grok/rules/01-quickstart.md; do
    echo "$f  ext-res:$(grep -c external-resource-adoption-contract "$f") \
failrec:$(grep -c ai-failure-recovery "$f") runner:$(grep -c runner-cli-contract "$f")"
  done
AGENTS.md                          ext-res:1 failrec:1 runner:1
CLAUDE.md                          ext-res:1 failrec:1 runner:1
.github/copilot-instructions.md    ext-res:1 failrec:1 runner:1
.grok/rules/01-quickstart.md       ext-res:1 failrec:1 runner:1
```
Matches the Preflight-2 occurrence matrix exactly. Content compared by eye
against `AGENTS.md` lines 99-105: identical prose in all three ("External
resource adoption: ...", "AI failure and recovery: ...", "Slow AI job runner
CLI contract: ..."), differing only in line-wrap style (Copilot keeps each
item on one line; `AGENTS.md`/Grok wrap at ~80 columns) — no meaning drift.

**Defect 1 — testing the `.cursor/rules/*` exemption, not accepting it:**

```text
$ grep -n "External resource adoption\|external-resource-adoption-contract\|ai-failure-recovery\|runner-cli-contract" \
    .cursor/rules/*.mdc
(no hits)

$ grep -n "alwaysApply" .cursor/rules/*.mdc
.cursor/rules/01-quickstart.mdc:alwaysApply: true
.cursor/rules/02-architecture-boundaries.mdc:alwaysApply: true
.cursor/rules/03-collaboration-and-completion.mdc:alwaysApply: true

$ grep -n "Before writing implementation\|Reading Sequence\|read the relevant architecture" \
    .cursor/rules/*.mdc
(no hits — .cursor/rules/*.mdc carries no competing "what to read" list of its
own that could omit the three documents while looking authoritative)
```
The exemption rests on two claims: (a) Cursor auto-loads root `AGENTS.md`
natively, independent of `.cursor/rules/*.mdc`, and (b) `AGENTS.md` itself
carries the three references. (b) is directly confirmed above. (a) is not
something this fix invented — it is ADR 0006's own recorded finding, quoted
verbatim: "Cursor loads root `AGENTS.md` as its own rule type, separately from
`.cursor/rules`" and "A live Cursor session in this repository (2026-07-16)
received root `AGENTS.md` as its own always-applied workspace rule *and* the
three `alwaysApply` `.mdc` files." I cannot re-run a live Cursor session from
here, so (a) itself is taken from the accepted ADR rather than independently
re-tested — but I did check the one thing a fresh fix could get wrong even if
(a) holds: that no `.cursor/rules/*.mdc` file presents its own "documents to
read" list that a Cursor agent might treat as complete and stop at, silently
missing the three. None does — confirmed by grep above.

One asymmetry worth naming, not a defect: the *same* mirror-parity work
(round 1) added the Minor Fix Path / Preflight text to
`.cursor/rules/03-collaboration-and-completion.mdc` directly, redundantly with
`AGENTS.md`'s native loading. Round 2 relies solely on native loading for the
reading-sequence fix and adds nothing to `.cursor/rules/*.mdc`. Both choices
are consistent with ADR 0006 (belt-and-suspenders is allowed, not required),
and both leave Cursor covered either way — but the two rounds justify skipping
`.cursor` on inconsistent grounds (round 1 didn't skip it; round 2 does). This
is a style inconsistency, not a coverage gap.

**Defect 2 re-check — version-claim contradiction:**

```text
$ git tag -l
v0.0.1  v0.1.0  v0.1.1  v1.0.0
# still no v1.1.0 tag.

$ git describe --tags HEAD   # HEAD = 21a6c17
v1.0.0-6-g2d83262
# (git describe reports the nearest tag ancestor; 21a6c17 is 7 commits past
# v1.0.0, same as before — no tag added)

$ grep -n "Contract edition" README.md
6:**Contract edition: v1.0.0.**
$ grep -n "契約バージョン" README.ja.md
6:**契約バージョン: v1.0.0。**

$ sed -n '11,20p' CHANGELOG.md
## v1.1.0 — Independent review, and the rules it produced (unreleased)

**Unreleased.** No `v1.1.0` tag exists yet; the released edition is still
`v1.0.0`, which is what both READMEs banner. This section is tagged only after
an approving independent review, and the README banners move at the same
time. Until then, treat everything below as landed on `main` but unreleased.
...
```
`CHANGELOG.md` now correctly states no tag exists and names `v1.0.0` as the
released edition — matching both README banners (English and Japanese) and
matching `git tag -l`. The contradiction row 6 found in round 1 does not
reproduce.

**One place the old framing still lives, found while checking "did the fix
just move the claim":**

```text
$ sed -n '69p' docs/collaboration/agreements/2026-08-02-mirror-parity-and-adr-range.md
| Should `v1.0.1` be tagged retroactively? | No. It was never released and no
commit contains only those fixes. One `v1.1.0` covers the shipped state, and
the changelog says so. | Planner |
```
This "Settled Ambiguities" row still asserts, in the present tense, that "the
changelog says" `v1.1.0` "covers the shipped state" — which was true when this
row was written (before round 1's rejection) and is no longer true now that
`CHANGELOG.md` says the opposite (unreleased). This is not a new claim
introduced by round 2; it predates round 1 and round 2 did not touch the
agreement file (confirmed: `git diff 2d83262 21a6c17 --name-only` does not
list the agreement). It is not the same failure mode as the original
defect — this line is inside a design agreement's historical decision record,
not a distributed, adopter-facing claim like `CHANGELOG.md` or the READMEs,
and a design agreement is understood in this contract as a record of what was
decided at the time, not a live-synced status page. I am naming it because the
instruction was to check whether the fix "moved the false claim somewhere
else," and, narrowly, an inaccurate echo of it still exists here even though
the operative, reader-facing claim (`CHANGELOG.md`) is now correct.

CI-equivalent checks, re-run on `21a6c17`:

```text
$ required_files (ci.yml): count 64, missing: []
$ for n in 0001..0013: ls docs/architecture/adr/${n}-*.md   -> all OK
$ bash -n scripts/copy-ai-collaboration-files.sh scripts/update-ai-collaboration-files.sh \
    scripts/init-llm-context.sh scripts/lib/collaboration-template-paths.sh
OK
$ git grep -n -E '^(<<<<<<<|=======|>>>>>>>)' -- . ':!.git'
none found
$ grep -rIn '0001-0011|0001–0011|0001〜0011' . | grep -v '\.git/'
# 3 hits, all inside docs/collaboration/{traces,reviews}/*.md (record
# directories, describing historical checks or quoting old text) — 0 hits in
# normative content.
```

Repo-wide dangling-link/backtick-path resolver (82 `.md`/`.mdc` files):

```text
Checked 82 files
Found 3 problems, all inside my own round-1 review record
(docs/collaboration/reviews/2026-08-02-mirror-parity-and-v101-review.md),
flagging `.grok/rules/03-...md` / `.cursor/rules/03-...mdc` — these are
ellipsis-shortened illustrative paths in my own prose, not real links, and not
part of the artifact under review. 0 problems in any contract, README,
CHANGELOG, or record file produced by round 2.
```

Copy smoke test, reproduced locally on `21a6c17` (own temp target, own
`git init`):

```text
$ scripts/copy-ai-collaboration-files.sh --target "$tmp" --project-name "Smoke App" \
    --domain-summary "template smoke test" --stack "Go backend, React frontend, npm"
(exit 0)

$ grep -l "external-resource-adoption-contract" "$tmp"/{AGENTS.md,CLAUDE.md,.github/copilot-instructions.md,.grok/rules/01-quickstart.md}
all four — present in every full-mirror file in the distributed target.

$ grep -R -n -i -E '<PROJECT_NAME: one-line description|<FILL IN: e\.g\. backend' "$tmp"/...
(no hits, exit 1)
```

Real CI, queried live:

```text
$ gh pr checks 7
Repository sanity   pass   8s   .../actions/runs/30742134891/job/91481299141

$ gh pr view 7 --json headRefOid,state,mergeable
{"headRefOid":"21a6c171d756d07724e411731b00678c361566af","state":"OPEN","mergeable":"MERGEABLE"}
```

Traceability `case`-block against this round's actual changed-file list:

```text
$ git diff 2d83262 21a6c17 --name-only
.github/copilot-instructions.md
.grok/rules/01-quickstart.md
CHANGELOG.md
docs/collaboration/reviews/2026-08-02-mirror-parity-and-v101-review.md
docs/collaboration/reviews/2026-08-02-mirror-parity-preflight-2.md
docs/collaboration/traces/2026-08-02-mirror-parity-and-adr-range.md

$ ./case_test.sh "<above>"
contract_changed=true trace_added=true
WOULD PASS CI
```

**PR description currency check:**

```text
$ gh pr view 7 --json body
```
The PR body still describes only round 1: it links the round-1 Preflight
record, states "Known gaps: 1. no Reviewer approval, 2. v1.0.1 unverified,"
and ends "After an approving review, tag `v1.1.0`" — with no mention of the
rejection, the round-2 fixes, or the round-2 Preflight record. A reader
relying only on the GitHub PR page (not the commit log or the trace) would not
learn a rejection and a fix round happened. Non-blocking, but worth naming as
a completeness gap in the review-facing surface, separate from the file
contents themselves (which are correct).

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The reading-sequence fix is incomplete for any of the full-mirror files (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.grok/rules/01-quickstart.md`) | Occurrence-count grep for all three document names returns exactly 1 in each of the four files; content matches `AGENTS.md`'s wording verbatim. | not reproduced |
| 2 | The `.cursor/rules/*` exemption is wrong — a Cursor agent using only `.cursor/rules/*.mdc` would not reach the three documents | No `.cursor/rules/*.mdc` file contains a competing reading-sequence list that would appear complete while omitting the three; the exemption instead rests on ADR 0006's own recorded, previously-tested claim that Cursor auto-loads root `AGENTS.md` (which does carry the three references) independently of `.mdc`. I could not re-run a live Cursor session to re-test the ADR's underlying claim itself, so this is verified against the accepted ADR record, not against live Cursor behavior. | not reproduced (see Scenarios Not Searched for the residual gap) |
| 3 | `CHANGELOG.md` still claims a release that has not happened | `CHANGELOG.md`'s `v1.1.0` section now says "Unreleased," names `v1.0.0` as the released edition, and gives the tagging condition — matching `git tag -l` (no `v1.1.0`) and both README banners (`v1.0.0` in English and Japanese). | not reproduced |
| 4 | The version-claim fix just relocated the false claim to a different document | **Partially reproduced, non-blocking.** The design agreement's Settled Ambiguities table (line 69) still describes the changelog as saying `v1.1.0` "covers the shipped state" — stale since round 2 changed that wording. Not the same severity as the original defect: this line sits in a historical decision record, not in a document a reader would use to determine current release state, and neither README nor `CHANGELOG.md` — the two adopter-facing surfaces — repeat it. | reproduced, non-blocking |
| 5 | CI itself does not pass on the current commit, only local reproductions of its logic do | `gh pr checks 7` at `headRefOid 21a6c17` shows the real GitHub Actions "Repository sanity" job as `pass`. | not reproduced |
| 6 | The round-2 fix broke something the round-1 fix had gotten right (regression) | Full re-run of every round-1 deterministic check (`required_files` 64/0, ADR loop 0001-0013, `bash -n`, conflict markers, stale-range grep, copy smoke test for the two rules added in round 1) against `21a6c17`: all identical results to round 1. | not reproduced |
| 7 | The round-2 commit or its records misrepresent Preflight as approval, given the commit message explicitly discusses "Round-1 Preflight passed and the Reviewer still rejected" | Commit message and Preflight-2 record both explicitly say Preflight "is not an approval" and name two still-open review obligations in Preflight-2's "Next Action." | not reproduced |

## Scenarios Not Searched

- Live Cursor product behavior — whether `.cursor/rules/*.mdc` plus root
  `AGENTS.md` auto-apply actually behaves as ADR 0006 recorded from its
  2026-07-16 test. This review re-verified the *document-side* precondition
  (AGENTS.md carries the content, no competing list exists in `.mdc`) but
  took Cursor's auto-load behavior itself from the ADR rather than
  re-observing it live.
- Whether GitHub Actions would behave identically to the local
  `case`-block reproduction under real merge-commit SHAs rather than the
  synthetic path lists used here (same limitation as round 1).
- A full byte-level parity re-audit of the seven-file set beyond the two
  rules and three document references in scope across both rounds.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked
      in.
- [ ] Every `Then` clause in the specification is asserted — not applicable,
      no Gherkin spec.
- [x] The dependency rule and port boundaries hold — not applicable.
- [x] No boundary named in the design agreement was crossed.
- [x] Specifications and accepted tests were not modified to make work pass.
- [x] Every claim in the artifact states its grounds — the one residual
      exception (agreement line 69) is named above and judged non-blocking.
- [x] The record would let a third party re-run this same search.

## Decision

- [x] **Approved**
- [ ] Rejected
- [ ] Deadlocked — escalate to Arbiter
- [ ] Reopening request

### Approval type outcomes

- **Specification-conformance**: **Approved.** Both defects named in my
  round-1 rejection are independently confirmed fixed. The `.cursor/rules/*`
  exemption for defect 1 is grounded in ADR 0006's own recorded finding and
  the document-side precondition for it was independently checked (no
  competing incomplete list on the Cursor side).
- **Boundary-conformance**: **Approved.** No ADR touched; no specification or
  named boundary crossed; the design agreement was correctly left unedited
  since no decision in it changed.
- **Evidence-sufficiency**: **Approved**, with one named, non-blocking gap:
  the design agreement's Settled Ambiguities row 3 (line 69) still echoes the
  pre-round-2 "the changelog says [v1.1.0] covers the shipped state" framing,
  and the PR description on GitHub was not updated to reflect round 2 (still
  reads as if only round 1 happened). Neither affects an adopter's or a
  future agent's ability to learn the actual, correct release state from
  `CHANGELOG.md` or the READMEs, which are the documents that state it.

## Reasons

Approval, with two non-blocking suggestions for a follow-up Minor Fix Path
change (not required before merge):

1. Update the design agreement's Settled Ambiguities row 3 (line 69) to match
   `CHANGELOG.md`'s current "unreleased" framing, or add a Reopening Log entry
   noting the wording changed in response to review — whichever this
   contract's own precedent treats defect-driven wording fixes as (the
   `v1.0.1` trace treated this class of fix as execution under the existing
   agreement, not a reopening; the same reasoning would apply here).
2. Update pull request #7's description to mention the rejection and the
   round-2 fixes, and link `2026-08-02-mirror-parity-preflight-2.md`, so a
   reader who only opens the PR page (not the commit log) sees the full
   picture.

---

# Target (B): The v1.0.1 gap on `main` (defect 2 from my round-1 review)

## Review Target

- Artifact: `main` at `3ba0219` — **unchanged since my round-1 review.**
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-contract-first-edition.md`
  (DA-2026-08-02-03), per the original v1.0.1 trace's reasoning, as in round 1.
- Approval type: specification-conformance, evidence-sufficiency.

## Deterministic Verification Output

```text
$ git rev-parse origin/main
3ba0219ae89132d5ac92387be823854ddcc0860c
# identical to the commit reviewed in round 1 — main has not moved.

$ grep -c "external-resource-adoption-contract\|ai-failure-recovery\|runner-cli-contract" \
    .github/copilot-instructions.md    # (checked against main's tree via git show)
$ git show main:.github/copilot-instructions.md | grep -c "external-resource-adoption-contract\|ai-failure-recovery\|runner-cli-contract"
0
$ git show main:.grok/rules/01-quickstart.md | grep -c "external-resource-adoption-contract\|ai-failure-recovery\|runner-cli-contract"
0
```
The gap I found in round 1 is **still present on `main` as it stands today.**
It has not been backported or cherry-picked there; it exists only on the PR
branch.

```text
$ git diff main 21a6c17 -- .github/copilot-instructions.md .grok/rules/01-quickstart.md | head -20
(shows the same additions verified under Target A above)
```
If and when pull request #7 (`21a6c17` or a later commit on the same branch)
merges to `main`, `main` would then carry these references in
`.github/copilot-instructions.md` and `.grok/rules/01-quickstart.md`, closing
this specific gap. That is a statement about what merging would do, not a
statement about `main`'s current state.

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The v1.0.1 defect-2 gap (reading-sequence references absent from Copilot/Grok) is closed on `main` as it stands | `main` is unchanged at `3ba0219`; `git show main:<file>` for both `.github/copilot-instructions.md` and `.grok/rules/01-quickstart.md` returns 0 occurrences of all three document names, identical to round 1. | reproduced — gap still open on `main` |
| 2 | The fix on the PR branch, if merged, would fail to close the gap | `git diff main 21a6c17` for both files shows the exact reference text added, matching `AGENTS.md` verbatim (see Target A). A merge would carry these lines into `main` unchanged, since the branch is a fast-forward-compatible descendant of `main` (`git merge-base main 21a6c17` is `3ba0219`, `main`'s own tip). | not reproduced — the pending fix is adequate, contingent on merge |

## Checklist

- [x] Deterministic verification was run against `main`'s actual current tip,
      not assumed unchanged.
- [x] The record distinguishes "fixed on `main` today" from "fixed once this
      branch merges" rather than conflating them.

## Decision

- [ ] Approved
- [x] **Rejected** — `main` itself is unchanged; the defect this rejects for
      still exists there today.
- [ ] Deadlocked — escalate to Arbiter
- [ ] Reopening request

### Approval type outcomes

- **Specification-conformance**: **Rejected**, unchanged from round 1, for
  the same reason: `main` still leaves `.github/copilot-instructions.md` and
  every `.grok/rules/*.md` file without the three reading-sequence
  references.
- **Evidence-sufficiency**: **Rejected** for the same reason — nothing new to
  evidence, since nothing on `main` changed.

## Reasons

1. **(Blocking, specification-conformance)** No new action required beyond
   what is already in motion: merge pull request #7 (approved above at
   `21a6c17` or later on the same branch). Once merged, this specific gap on
   `main` closes — verified directly against the branch's actual diff, not
   asserted. Re-review of `main` after that merge should re-confirm the four
   remaining v1.0.1 defects (1, 3, 4, 5) are still intact post-merge and that
   this fifth one now reads correctly on `main` itself, not just on a branch.

This target's rejection is not a statement that the fix is wrong — Target A
above confirms it is correct — only that a fix which exists on a branch does
not yet exist on `main`, and the review target named by the coordinator was
`main` as merged, not the pending branch.

---

## Cross-Target Observations

- Both of round 1's findings are now correctly and verifiably fixed on the PR
  branch. Neither introduced a new blocking defect. One pre-existing,
  non-blocking staleness surfaced (the design agreement's line 69) that
  neither round touched — worth a follow-up, not a blocker.
- The `v1.0.1` gap on `main` remains open only because `main` has not moved,
  not because the fix is deficient. This distinction matters for anyone
  reading only a decision label: "Target B: Rejected" should not be read as
  "the fix is wrong" — it is "the fix has not landed on the reviewed ref yet."
- Recommend, as before in round 1: once this branch merges, a short follow-up
  re-review of `main` at the merge commit to close out Target B formally,
  since a Reviewer decision against a branch is not a Reviewer decision
  against `main`.

## Verification Environment

- All checks re-run directly against `21a6c17` (PR branch, checked out as the
  working tree) and `main` at `3ba0219` (read via `git show main:<path>`,
  without checking out a second worktree this round, since only two files
  needed direct inspection).
- `gh pr checks 7` and `gh pr view 7` queried live GitHub state at review time
  (2026-08-02, this session).
- Model: Claude Sonnet 5. Tool: Claude Code, fresh session, no access to the
  producing session's reasoning for either round-2 fix.
