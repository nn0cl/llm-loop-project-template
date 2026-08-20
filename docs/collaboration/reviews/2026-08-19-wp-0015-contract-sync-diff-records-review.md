# Review Record: WP-0015 — Contract-Sync Diff Records and Per-Agent-Tool Rule Registry

Use this when the Reviewer persona issues a decision inside the execution loop.

A review that does not satisfy all three constraints below does not count as an
approval, whatever this record says.

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in a context with no prior
      memory of this work plan: no chat transcript from the Design & Review
      or Implementation sessions was read or trusted. The reviewing worktree
      was reset to `origin/process/item-0012-remaining-facets` at commit
      `6d3b24d` (`git checkout -b review/wp-0015-inspect
      origin/process/item-0012-remaining-facets`, confirmed via `git log
      --oneline -3` and `git rev-parse HEAD`) before any file was read.
      Everything stated below was independently re-derived from repository
      artifacts read in full: the backlog item, ADR 0008, the design
      agreement, the work plan, the local issue (including its self-review
      Work Notes), the AI work trace, the three actual landed files, `git
      diff`/`git log`/`git show` on the actual commits, and a re-run of the
      deterministic check in this reviewing session's own worktree. The
      Implementer's, Design & Review group's, and design agreement's own
      claims (including the central "ADR 0008 already implements facet 4's
      split" research claim) were read only as claims to falsify, not as
      evidence.
- [x] **Deterministic precondition.** `scripts/check-contract-consistency.py`
      was re-run independently in this reviewing session, against the actual
      current tree at commit `6d3b24d` — not copied from WP-0015's own
      Preflight section. Output recorded below, identical result.
- [x] **Falsification burden.** Fourteen scenarios searched — 9 mechanical/
      process, 5 substantive (whether ADR 0008 and the two new artifacts
      actually deliver what facet 4 asks for) — each with grounds and a
      not-reproduced/reproduced result, in the Falsification Search table
      below.

## Review Target

- Artifact: `docs/templates/sync-diff-record.md` (new),
  `docs/collaboration/prompt-instruction-change-control.md` (new "Per-Agent-Tool
  Rule Applicability Registry" section + shortened Review Rule bullet),
  `docs/templates/contract-file-sync-prompt.md` (new cross-referencing
  paragraph + expanded Step 6), at commit `6d3b24d` on
  `origin/process/item-0012-remaining-facets`
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-19-contract-sync-diff-records.md`
  (`DA-2026-08-19-07`)
- Specification: none — documentation/process-governance change; no
  application specification, per `DA-2026-08-19-07`'s own "Specifications"
  section
- Current phase: Architecture Path, docs-only (content fully pre-specified
  in the design agreement; Implementer transcribed rather than designed)
- Producing persona: Implementer (Implementation group, branch
  `process/contract-sync-diff-records`, commit `10b19df`, fast-forward
  merged into `process/item-0012-remaining-facets`); Design & Review group
  (Planner/Specifier) authored the design agreement, work plan, and issue
  (`a68563d`) and recorded Preflight (`6d3b24d`)
- Reviewing persona / model / tool: Reviewer, Claude Sonnet 5 via Claude
  Code, separate context/worktree from every session above
- Approval type: specification-conformance (mechanical transcription
  against "Exact Content to Produce"), boundary-conformance (Scope/no-ADR-0008-edit
  boundaries), evidence-sufficiency (Preflight/trace traceability). Also,
  per this work plan's own Plan Task 7 ("that the new pieces genuinely
  extend rather than duplicate ADR 0008"), substantive soundness of the
  design agreement's central research claim.
- Preflight Validation record:
  `docs/work-plans/WP-0015-contract-sync-diff-records.md`, "Preflight
  Validation" section
- Preflight result: pass (re-verified independently below, against the
  actual current tree, not trusted from the pasted record)

## Deterministic Verification Output

Re-run independently in this reviewing worktree, at commit `6d3b24d`:

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
```

Exit code: 0.

Supporting re-verification commands also run independently in this session:

```text
$ git diff a68563d..6d3b24d --stat
 .../prompt-instruction-change-control.md           |  30 ++-
 ...6-08-19-liss-0046-contract-sync-diff-records.md | 231 +++++++++++++++++++++
 ...ontract-sync-diff-records-and-agent-registry.md |  45 ++++
 docs/templates/contract-file-sync-prompt.md        |  20 +-
 docs/templates/sync-diff-record.md                 |  77 +++++++
 .../WP-0015-contract-sync-diff-records.md          |  30 ++-
 6 files changed, 420 insertions(+), 13 deletions(-)

$ git diff a68563d..6d3b24d --name-status
M	docs/collaboration/prompt-instruction-change-control.md
A	docs/collaboration/traces/2026-08-19-liss-0046-contract-sync-diff-records.md
M	docs/issues/LISS-0046-contract-sync-diff-records-and-agent-registry.md
M	docs/templates/contract-file-sync-prompt.md
A	docs/templates/sync-diff-record.md
M	docs/work-plans/WP-0015-contract-sync-diff-records.md

$ git diff a68563d..6d3b24d --name-only | grep -iE "adr/0008|update-ai-collaboration|copy-ai-collaboration|^CLAUDE\.md$|AGENTS\.md|copilot-instructions|grok/rules|cursor/rules"
(no output, exit 1 — none touched)

$ git show --stat 10b19df
 .../prompt-instruction-change-control.md           |  30 ++-
 ...6-08-19-liss-0046-contract-sync-diff-records.md | 231 +++++++++++++++++++++
 ...ontract-sync-diff-records-and-agent-registry.md |  45 ++++
 docs/templates/contract-file-sync-prompt.md        |  20 +-
 docs/templates/sync-diff-record.md                 |  77 +++++++
```

## Falsification Search

### Mechanical / process

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | `docs/templates/sync-diff-record.md` diverges from `DA-2026-08-19-07`'s "Exact Content to Produce" -> "File 1" | Read the landed file and the agreement's File 1 code block side by side, line for line (intro paragraphs, Metadata/Template's Own Change/Target's Own Change/Conflicts/Result/Verification sections, the Conflicts table header and its one placeholder row). Identical. | not reproduced |
| 2 | `docs/collaboration/prompt-instruction-change-control.md`'s new "Per-Agent-Tool Rule Applicability Registry" section or shortened Review Rule bullet diverges from File 2, or another part of the file changed | `git diff a68563d..6d3b24d -- docs/collaboration/prompt-instruction-change-control.md` shows exactly two hunks: the Review Rule bullet replacement (old prose removed, new cross-reference text inserted) and the new section inserted immediately after the "self-review" paragraph and before "## Traceability Rule." Both hunks match File 2's specified text character for character; no other line in the file is touched. | not reproduced |
| 3 | `docs/templates/contract-file-sync-prompt.md`'s new paragraph or expanded Step 6 diverges from File 3, or another part of the file changed | `git diff a68563d..6d3b24d -- docs/templates/contract-file-sync-prompt.md` shows exactly two hunks: the new paragraph inserted after the intro paragraph and before "Do not run this as a mechanical text merge," and Step 6 replaced. Both match File 3's specified text character for character; no other line touched. | not reproduced |
| 4 | `docs/architecture/adr/0008-template-update-propagation.md`, any sync script, `CLAUDE.md`, or a mirror file was touched | `git diff a68563d..6d3b24d --name-only \| grep -iE "adr/0008\|update-ai-collaboration\|copy-ai-collaboration\|^CLAUDE\\.md$\|AGENTS\\.md\|copilot-instructions\|grok/rules\|cursor/rules"` returns no output (exit 1). | not reproduced |
| 5 | Some repository document outside the plan's own scope (2 edited contract files, 1 new template, the trace, LISS-0046's Work Notes, WP-0015's own Preflight recording) was moved, archived, deleted, or edited | `git diff a68563d..6d3b24d --name-status` lists exactly 6 files: the 2 edited contract files, 1 new template file, 1 new trace file, LISS-0046 (Work Notes append), and WP-0015 itself (Preflight section filled in — expected, since `a68563d` is the design-intake commit predating Preflight). No other file appears. | not reproduced |
| 6 | `scripts/check-contract-consistency.py` fails, or WP-0015's pasted Preflight output is stale relative to the actual current tree | Independently re-run at `HEAD` (`6d3b24d`): `contract consistency: all checks passed`, exit 0 — identical to WP-0015's own pasted claim, and this review does not merely trust that claim; it reproduces it. | not reproduced |
| 7 | The AI work trace's claimed file list or commit contents are inaccurate | `git show --stat 10b19df` (the Implementer's actual commit) shows exactly the 5 files the trace's own Verification section claims: `prompt-instruction-change-control.md`, the trace file itself, LISS-0046, `contract-file-sync-prompt.md`, `sync-diff-record.md` — byte-identical stat output to what the trace pastes. | not reproduced |
| 8 | The three touched/created files are not actually ADR-0006 "agent operating contract" files, so the trace/Reviewer-pass requirement the design agreement invokes would not actually apply | `docs/collaboration/prompt-instruction-change-control.md`'s own "Agent Operating Contract Files" list names `docs/templates/*.md` and `docs/collaboration/*.md` (except the three named record directories) as contract files. `sync-diff-record.md` and `contract-file-sync-prompt.md` are both `docs/templates/*.md`; `prompt-instruction-change-control.md` is itself `docs/collaboration/*.md` and not one of the three exempted record directories. All three are contract files; the trace requirement correctly applies. | not reproduced |
| 9 | The "no new ADR needed... matches item-0013's own precedent" claim in Settled Ambiguities is fabricated or misattributed | Read `docs/work-plans/WP-0013-prevent-direct-to-main-commits.md`: it made a process-rule change (branch-protection/direct-to-main prevention) while explicitly stating "no specification/ADR/port/data-model/architecture-boundary change" and citing no new ADR. The precedent is real and matches the cited pattern (a process-rule addition landing without a new ADR). | not reproduced |

### Substantive (does the work genuinely close what facet 4 asks for)

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 10 | ADR 0008's Tier 1/Tier 2 Tiered Sync Policy genuinely implements facet 4's "split rules explicitly into Template-owned... versus Target-owned" | **Reproduced.** Read ADR 0008's "Tiered Sync Policy" section and item-0012 facet 4's own paragraph side by side. ADR 0008's Tier 1/Tier 2 is a **whole-file authority** classification (Tier 1: template wins outright, no merge attempted; Tier 2: the five persona files, needs AI-assisted reconciliation because they *may* carry adopter placeholders) — a per-file, decided-once split (`is_contract_persona_file`). Facet 4's own wording asks for a **content-level** split within files — its own examples ("shared path/phase/review/sync/logging conventions" vs. "adopter-specific language/domain/architecture/ADRs") describe kinds of content that coexist inside a single Tier-2 file such as `CLAUDE.md` (e.g., its Phase Discipline section vs. its Selected Stack section), not which whole files differ. No standing document in this repository declares, ahead of any specific sync, which specific rule/paragraph is template-owned vs. target-owned. The actual content-level separation happens dynamically, per sync event, via `contract-file-sync-prompt.md`'s Steps 2-4 (diff-and-judge), with the outcome now recorded post-hoc by the new Sync Diff Record — neither is a standing, explicit split document as facet 4's own wording ("split rules explicitly") calls for. Opened as `docs/issues/LISS-0047-facet-4-template-target-split-granularity.md`. | reproduced |
| 11 | The new Sync Diff Record's own sections fail to map onto facet 4's exact four-part ask (template's own change / target's own change / any conflict / adopt-reject-defer decision for each) | Read `docs/templates/sync-diff-record.md` section by section: "Template's Own Change" = facet 4's "the template's own change"; "Target's Own Change" = "the target's own change"; "Conflicts" (with an explicit `Adopt (take template) / Reject (keep target) / Defer` column and a required Reason column) = "any conflict" + "the adopt/reject/defer decision for each." Clean 1:1 match, no gap. | not reproduced |
| 12 | The new Per-Agent-Tool Rule Applicability Registry is too coarse to function as "which rule applies to which agent" — i.e., it records which *sync mode* a file uses in general, not which *specific rule* differs | Read the registry table: 3 rows, keyed by sync mode (Literal full mirror / Union / Canonical source) and which files use each. This is coarser than a per-rule mapping — it does not, by itself, enumerate individual rule-level differences beyond the one concrete historical fact it does capture (`CLAUDE.md`'s 2026-07-25 `@AGENTS.md`-import removal, folded into the "Literal full mirror" row's parenthetical). However, the table's own closing instruction ("Add a new row here, with its own reason, the first time an intentional per-agent-tool difference is introduced") is written to scale toward per-difference granularity as new intentional differences actually arise, rather than claiming false completeness today. Real gap in current granularity, but self-correcting by design and not a misrepresentation of what exists now — judged non-blocking, distinct from and lesser than scenario 10. | reproduced (non-blocking; see Reasons) |
| 13 | Judging "no new ADR is needed" understates that this work plan crosses into a new architectural decision (a new required artifact type, a new canonical registry) that CLAUDE.md's "capture it as an ADR" rule would require | The two new artifacts (Sync Diff Record, Registry) do not introduce a new mechanism, external dependency, or architecture boundary — they add record-keeping and cross-referencing scaffolding around ADR 0008's already-Accepted Tier 1/Tier 2 mechanism, which is unchanged (no edit to ADR 0008 itself, confirmed in scenario 4). This is the same kind of change as the cited WP-0013 precedent (scenario 9): a process-rule/artifact addition, not a new architectural concept. | not reproduced |
| 14 | The Sync Diff Record's positioning (stored in the *adopting* project's repository, never this template repository) makes the whole mechanism unenforceable/unverifiable from inside this repository in a way this work plan fails to disclose, or that newly contradicts the template's own architecture | `scripts/check-contract-consistency.py` contains no reference to `sync-diff-record` or the new registry (confirmed by direct grep of the script's ~1071 lines and its function list) — the work plan makes no false claim of CI enforcement for either new artifact. This limitation is an already-accepted property of ADR 0008's own Decision section (item 5: "The template repository does not maintain a registry of adopting repositories and does not push updates to them"), not something newly introduced or concealed by WP-0015. The Deferred Questions table in `DA-2026-08-19-07` explicitly leaves automated drift-checking of the registry to a possible future facet-5 decision, rather than claiming it already exists. | not reproduced |

## Scenarios Not Searched

- Whether every one of ADR 0008's own prior claims (e.g., the exact date and
  mechanism of `CLAUDE.md`'s 2026-07-25 `@AGENTS.md`-import removal) is
  independently correct against that historical event — this review took
  ADR 0008's and the registry's restated version of that fact as already
  established by ADR 0008 itself (unedited by this work plan, confirmed in
  scenario 4), and did not re-derive the original historical change from
  git history predating this work plan.
- Whether the Deferred Questions table's judgment (automated drift-checking
  of the registry left to a possible facet 5) is the right sequencing call
  — plausible and explicitly named as deferred, not this review's job to
  pre-resolve.
- Long-term stylistic clarity of the new registry table and Sync Diff Record
  template to a future reader unfamiliar with this session — a judgment
  call beyond the falsification criteria this review is scoped to test.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked
      in (Architecture Path documentation/template work only, content fully
      pre-specified by the design agreement).
- [x] Every `Then` clause in the specification is asserted by the work — not
      applicable; no specification exists for this documentation-only
      change, per `DA-2026-08-19-07`'s own "Specifications" section.
- [x] The dependency rule and port boundaries hold — not applicable; no
      application architecture touched.
- [x] No boundary named in the design agreement was crossed — verified
      directly (scenarios 4-5).
- [x] Specifications and accepted tests were not modified to make work pass
      — not applicable; no tests exist for this change.
- [x] Every claim in the artifact states its grounds — the three landed
      files and their covering documents cite ADR 0008 and the design
      agreement throughout; the one place a claim (the "already implements
      facet 4's split" research finding) overstates its own grounds is
      scenario 10, recorded as a non-blocking finding below.
- [x] The record would let a third party re-run this same search — every
      command in this record is copy-pasteable and every file/line/commit
      reference is exact.

## Decision

- [x] Approved
- [ ] Rejected — reasons and the specific artifact changes required
- [ ] Deadlocked — escalate to Arbiter, with both positions stated
- [ ] Reopening request — the design agreement does not settle this; state
      what is unsettled and what the loop needs in order to continue

## Reasons

- All of `DA-2026-08-19-07`'s explicit Falsification Criteria were
  independently tested and none reproduced: no repository document outside
  the three named files/sections was edited (scenario 5); ADR 0008, any
  sync script, `CLAUDE.md`, and its mirrors were not touched (scenario 4);
  the registry table does not duplicate the Cursor union-vs-mirror
  explanation in two places — it was moved, not copied (scenario 2); the
  required AI work trace is present and accurate (scenarios 7-8).
- `scripts/check-contract-consistency.py` passes, re-run independently in
  this session against the actual current tree at `6d3b24d`, not trusted
  from WP-0015's own Preflight section.
- The mechanical transcription is exact across all three touched/created
  files (scenarios 1-3), and the new Sync Diff Record's sections map
  cleanly onto facet 4's own four-part ask (scenario 11).
- One real, substantive gap was found (scenario 10): the design agreement's
  (and LISS-0046's, and WP-0015's) claim that ADR 0008's Tier 1/Tier 2
  Tiered Sync Policy "already implements" facet 4's "Template-owned vs
  Target-owned split" overstates what that policy actually does. Tier 1/
  Tier 2 is a whole-file authority classification; facet 4's own wording
  asks for a content-level split within files, which is currently produced
  only dynamically, per sync event, not as a standing document. This is
  real and worth carrying forward — it means item-0012 facet 4 is not yet
  fully closed even after this work plan, contrary to what a surface
  reading of the covering documents would suggest — but it does not
  invalidate anything WP-0015 actually built: the Sync Diff Record and
  Per-Agent-Tool Rule Applicability Registry are both correctly built,
  verbatim to spec, and each closes a real, distinct piece of facet 4 on
  its own merits (scenarios 11-12). It also does not trigger any of
  `DA-2026-08-19-07`'s four explicit Falsification Criteria, none of which
  test this claim. Recorded as non-blocking, per this repository's own
  precedent (`docs/collaboration/reviews/2026-08-19-wp-0014-document-log-lifecycle-model-review.md`'s
  Non-Blocking Observations, scenario 13) for a genuine gap that is not
  itself grounds to reject already-correct, in-scope deliverable work.
- A second, smaller substantive observation (scenario 12): the registry's
  current 3-row, sync-mode-keyed granularity is coarser than a literal
  per-rule "which rule applies to which agent" mapping, though it is
  explicitly designed to grow toward that granularity as new intentional
  differences are recorded. Non-blocking, folded into the same tracked
  finding rather than a second one, since both concern facet 4's residual
  granularity gap.

## Non-Blocking Observations

- **(Scenario 10, actionable now — tracked as `docs/issues/LISS-0047-facet-4-template-target-split-granularity.md`,
  `Type: review-finding`, `Status: proposed`.)** The "ADR 0008 already
  implements facet 4's Template-owned/Target-owned split" claim in
  `DA-2026-08-19-07`, `LISS-0046`, and `WP-0015` should be corrected to
  distinguish ADR 0008's actual whole-file authority split from facet 4's
  content-level rule split, which remains open. See LISS-0047 for the full
  finding, the two candidate resolutions (wording correction vs. a new
  standing rule-level document), and why this should be resolved before
  item-0012 facet 4 is treated as fully closed in any later summary.
- **(Scenario 12, folded into LISS-0047 rather than a separate issue.)**
  The registry's current granularity (sync-mode + file, not per specific
  rule) is real but explicitly designed to self-correct as new differences
  are recorded going forward; not required for this work plan's Done.
- **Delivery note on this review record itself:** this review's own
  investigation (all reading, all `git diff`/`git show` verification, the
  independent `scripts/check-contract-consistency.py` re-run) was completed
  successfully against the reviewing worktree at commit `6d3b24d`. Partway
  through composing this record and the LISS-0047 finding, the reviewing
  worktree (`/Users/nn0cl/Documents/git/llm-loop-project-template/.claude/worktrees/agent-a52df87ff7ea12729`)
  became unreachable to this session's file tools (`EPERM`/working-directory-resolution
  errors on both `Bash` and `Read`/`Write`, persisting across repeated
  retries, and affecting a sibling worktree under the same
  `.claude/worktrees/` path as well — indicating an environment/mount fault,
  not a problem with this review's own file paths). This record and
  LISS-0047 were therefore composed and preserved in the session scratchpad
  instead, and committed to the repository once write access was restored.
  This delivery gap is operational, not a defect in WP-0015 or in this
  review's own findings.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
