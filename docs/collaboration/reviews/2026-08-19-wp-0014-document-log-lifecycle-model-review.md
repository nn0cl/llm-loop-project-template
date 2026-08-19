# Review Record: WP-0014 — Document and Log Lifecycle Model (ADR 0020)

Use this when the Reviewer persona issues a decision inside the execution loop.

A review that does not satisfy all three constraints below does not count as an
approval, whatever this record says.

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in a context with no prior
      memory of this work plan: no chat transcript from the Design & Review
      or Implementation sessions was read or trusted. This reviewing
      worktree started on a stale branch (`worktree-agent-a513cb4479089d476`,
      missing all WP-0014/item-0012/item-0013 artifacts entirely — a `git
      diff` against the target branch showed 19 files, mostly deletions);
      it was reset with `git checkout -B review-wp-0014
      origin/process/backlog-item-0012-and-0013` before any file was read,
      confirmed clean (`git status`) and at commit `e2052da` (`git log
      --oneline -1`) before proceeding. Everything stated below was
      independently re-derived from the repository artifacts listed in
      "Review Target": the backlog item, the spike, the design agreement
      (current, amended version), the work plan, the local issue (including
      its self-review and correction-cycle Work Notes), the AI work trace,
      the actual landed files, `git log`/`git show` on the actual commits,
      and a command re-run in this reviewing session's own worktree. The
      Implementer's and Design & Review group's own self-review/Preflight
      claims were read only as claims to falsify, not as evidence — every
      quantitative claim below (file diffs, commit contents, ancestry) was
      independently re-derived from `git`, not copied from any party's
      report.

      During this review, an earlier stage of this same work plan's history
      (visible in `docs/work-plans/WP-0014-document-log-lifecycle-model.md`'s
      own Preflight section and commit `3d23c6d`'s message) recorded that an
      in-band message claiming "coordinator" relay authority had arrived and
      was refused, per `docs/architecture/agent-quickstart.md`'s Session
      Entry item 6 and `docs/collaboration/cross-session-messaging.md`'s
      "Confirmed failure mode" section — no persona named "coordinator"
      exists in this project's model. This review encountered no such
      message directly, but treats that refusal as correctly handled
      (verified independently through git tooling by the party that
      encountered it, per its own commit message) rather than as an
      unverified claim to carry forward.
- [x] **Deterministic precondition.** `scripts/check-contract-consistency.py`
      was re-run independently in this reviewing session, against the
      actual current tree at commit `e2052da` (not copied from WP-0014's
      own Preflight section, which was recorded against an earlier commit,
      `3d23c6d`, before WP-0013's Director-close was merged in). Output
      recorded below.
- [x] **Falsification burden.** Sixteen scenarios searched — ten mechanical/
      process, six substantive (the ADR's own reasoning) — each with grounds
      and a not-reproduced/reproduced result, in the Falsification Search
      table below.

## Review Target

- Artifact: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
  (new), `docs/collaboration/restoration-ledger.md` (new),
  `docs/collaboration/local-issue-planning.md` (one paragraph added),
  `README.md`/`QUICKSTART.md`/`QUICKSTART.ja.md` (ADR-range statement
  updates), at commit `e2052da` on `origin/process/backlog-item-0012-and-0013`
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-19-document-log-lifecycle-model.md`
  (`DA-2026-08-19-06`) — current, amended version (amended once mid-work-plan
  at commit `be1d857`, after Preflight caught two gaps; this review reads
  and holds the work to the current, corrected text, not the original)
- Specification: none — documentation/process-governance change (a new
  ADR), per `DA-2026-08-19-06`'s own "Specifications" section
- Current phase: Architecture Path, docs-only (content fully pre-specified
  in the design agreement; Implementer transcribed rather than designed)
- Producing persona: Implementer (Implementation group, branch
  `process/document-log-lifecycle-model`, commits `874c6ce` and `1d177d2`,
  merged via `8b296ec`); Design & Review group (Planner/Specifier) authored
  the design agreement, work plan, and issue (`0a38d6c`, `be1d857`) and
  recorded Preflight (`3d23c6d`)
- Reviewing persona / model / tool: Reviewer, Claude Sonnet 5 via Claude
  Code, separate context/worktree from every session above
- Approval type: specification-conformance (mechanical transcription
  against "Exact Content to Produce"), boundary-conformance
  (scope/Rule 7/CLAUDE.md-mirror boundaries), evidence-sufficiency
  (Preflight fail-then-fix cycle traceability). Also, per this work plan's
  own Plan Task 7, substantive soundness of the ADR's own reasoning —
  broader than the four standard approval types alone cover, since this is
  a genuine new architecture decision, not a mechanical doc edit.
- Preflight Validation record: `docs/work-plans/WP-0014-document-log-lifecycle-model.md`,
  "Preflight Validation" section
- Preflight result: pass (re-verified independently below, against the
  actual current tree, not trusted from the pasted record)

## Deterministic Verification Output

Re-run independently in this reviewing worktree, reset to
`origin/process/backlog-item-0012-and-0013` (`e2052da`) before running:

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
```

Exit code: 0.

Supporting re-verification commands also run independently in this session:

```text
$ git diff 0a38d6c..HEAD --stat
 QUICKSTART.ja.md                                   |   6 +-
 QUICKSTART.md                                      |   6 +-
 README.md                                          |   6 +-
 .../adr/0020-document-and-log-lifecycle-model.md   | 272 ++++++++++++++++++
 .../2026-08-19-document-log-lifecycle-model.md     |  65 ++++-
 docs/collaboration/local-issue-planning.md         |   6 +
 docs/collaboration/restoration-ledger.md           |  46 +++
 ...08-19-liss-0043-document-log-lifecycle-model.md | 320 +++++++++++++++++++++
 .../LISS-0043-document-log-lifecycle-model.md      | 159 ++++++++++
 .../WP-0013-prevent-direct-to-main-commits.md      |  20 +-
 .../WP-0014-document-log-lifecycle-model.md        |  52 +++-
 11 files changed, 935 insertions(+), 23 deletions(-)

$ find docs/archive
find: docs/archive: No such file or directory

$ diff <(sed -n '/### File 1/,/### File 2/p' \
    docs/collaboration/agreements/2026-08-19-document-log-lifecycle-model.md \
    | sed -n '/```markdown/,/```/p' | sed '1d;$d') \
    docs/architecture/adr/0020-document-and-log-lifecycle-model.md
(no output — byte-identical)

$ diff <(sed -n '/### File 2/,/### File 3/p' \
    docs/collaboration/agreements/2026-08-19-document-log-lifecycle-model.md \
    | sed -n '/```markdown/,/```/p' | sed '1d;$d') \
    docs/collaboration/restoration-ledger.md
(no output — byte-identical)

$ git merge-base --is-ancestor 2b98f29 3d23c6d && echo ancestor || echo not-ancestor
not-ancestor
```

## Falsification Search

### Mechanical / process

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | `docs/architecture/adr/0020-*.md` diverges from `DA-2026-08-19-06`'s current "Exact Content to Produce" -> "File 1", including the corrected Rule 4 citation | Extracted File 1's text programmatically from the agreement file and diffed byte-for-byte against the landed file — no output, identical. Confirmed the corrected form is present: `` `/Users/nn0cl/Documents/git/qpex/docs/architecture/trace-topic-register.md` `` (full external absolute path), not the original bare `` `trace-topic-register.md` `` backtick reference. | not reproduced |
| 2 | `docs/collaboration/restoration-ledger.md` diverges from File 2, or its Ledger table contains a data row | Diff against the agreement's own File 2 text: no output, identical. `tail` of the Ledger table shows only the header, separator, and literal placeholder row `_(no entries yet ...)_`. | not reproduced |
| 3 | `docs/collaboration/local-issue-planning.md` changed anywhere other than the one specified paragraph | `git diff 0a38d6c..HEAD -- docs/collaboration/local-issue-planning.md` shows exactly one hunk, six inserted lines, immediately after the `wont_do` bullet and before `## Phase Values` — matching File 3's specified insertion point and text exactly. No other line in the file touched. | not reproduced |
| 4 | `README.md`/`QUICKSTART.md`/`QUICKSTART.ja.md` changed anywhere beyond the specified ADR-range string replacements | `git diff 0a38d6c..HEAD` on all three files shows exactly the 7 specified old-text -> new-text replacements (2+1 in README, 3 in QUICKSTART, 3 in QUICKSTART.ja) named in the amended agreement's "File 4," and nothing else. | not reproduced |
| 5 | An existing `docs/issues/`, `docs/work-plans/`, `docs/collaboration/traces/`, `docs/collaboration/reviews/`, `docs/collaboration/agreements/`, or other `docs/architecture/adr/` file was moved, archived, deleted, or content-edited by **this work plan** | `git diff 0a38d6c..HEAD --name-status` restricted to those directories shows: the new ADR 0020, the design agreement's own amendment, the new trace, and LISS-0043's own Work Notes append (all in-scope, produced by this work plan) — plus `docs/work-plans/WP-0013-prevent-direct-to-main-commits.md`, modified. Read that diff in full: it is WP-0013's own Director-close entry (Work-Plan Close section filled in), authored on a separate line of history (commit `2b98f29`) and confirmed by `git merge-base --is-ancestor 2b98f29 3d23c6d` to be **not** an ancestor of WP-0014's own Preflight commit — i.e., a concurrently in-flight, unrelated work plan's own record on the shared branch, per ADR 0016's "multiple work plans in flight" model, not an edit WP-0014 made. No `docs/architecture/adr/0001`-`0019` file was touched. | not reproduced |
| 6 | `CLAUDE.md` or one of its four mirrors (`AGENTS.md`, `.github/copilot-instructions.md`, `.grok/rules/*.md`, `.cursor/rules/*.mdc`) was touched | `git diff 0a38d6c..HEAD --stat` lists 11 files total; none is `CLAUDE.md` or a mirror path. | not reproduced |
| 7 | A `docs/archive/` directory was created, or the restoration ledger was backfilled with any row, by this work plan | `find docs/archive` returns "No such file or directory." Ledger table confirmed empty (scenario 2). | not reproduced |
| 8 | The AI work trace omits or smooths over the Preflight fail-then-fix cycle, rather than leaving both the original and corrected state visible (Invariant 2) | Read the trace in full. Its original Verification entry records the pre-correction `check-contract-consistency.py` output verbatim (9 findings) with the Implementer's original "pre-existing/anticipated" judgment; a later "Correction cycle" section is appended, not substituted, explicitly stating "Row 7's original 'not reproduced' verdict is superseded by this entry... left in place above rather than edited." Cross-checked against actual git history: `874c6ce` (original ADR text, bare `` `trace-topic-register.md` `` citation, no README/QUICKSTART edits) exists as its own commit, distinct from `1d177d2` (the correction, `+4/-2` on the ADR file, `+6/-3` on each of the three README/QUICKSTART files) — both states are independently recoverable from git history, not only from the trace's own prose. | not reproduced |
| 9 | The 9 original `check-contract-consistency.py` findings, or the corrected re-run, are misreported anywhere in the trace, LISS-0043's Work Notes, or WP-0014's Preflight section | Compared the pasted original 9-finding output across the trace and LISS-0043 Work Notes — identical text in both. Compared the corrected re-run's "all checks passed, exit code: 0" across the trace, LISS-0043 Work Notes, and WP-0014's Preflight section — identical in all three, and independently reproduced by this review's own re-run above. | not reproduced |
| 10 | WP-0014's own Preflight scope-check claim ("exactly 10 files") is stale, wrong, or was never independently accurate | Re-ran `git diff 0a38d6c..3d23c6d --stat` (the commit at which WP-0014's Preflight section was authored, not today's `HEAD`): exactly 10 files, matching the claim precisely at authorship time. The 11th file this review sees today (`WP-0013-...md`) arrived only via `e2052da`, a merge that post-dates `3d23c6d` (scenario 5) — the claim was accurate when made, and the later, unrelated WP-0013 merge does not falsify it. | not reproduced |

### Substantive (ADR 0020's own reasoning)

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 11 | Selection (Option B: adapt, not adopt `qpex` wholesale) overreaches or underreaches the spike's own comparison evidence | Read case-0001's Comparison table and Selection rationale in full. The rationale is grounded in a directly-checked, quantitative fact (19 ADRs here vs. 186 at `qpex` before its own WP-0091), an explicit recovery-friction comparison (plain-file read under `docs/archive/` vs. `git show <tag>:<path>`-only), and a direct citation of item-0012's own explicit warning against wholesale adoption. It neither imports `qpex`'s aggressive mechanics (which the evidence shows solve a differently-scaled problem) nor discards `qpex`'s evidence entirely (Option C, explicitly rejected for exactly that reason). Proportionate to the evidence gathered. | not reproduced |
| 12 | Rule 2's ADR archival trigger ("every Decision clause explicitly named superseded") is internally broken by ADR 0016's own partial supersession of ADR 0001/0014, in a way the Consequences section understates | Read ADR 0016's own "Supersession, precisely" table directly: it names only three specific clauses (ADR 0001 Decision point 2; ADR 0014 clauses 1 and 5) as superseded, and explicitly states ADR 0014's clause 6 is "Not superseded, and cited here to foreclose a misreading." Under Rule 2's "every clause" test, this correctly means ADR 0001 and ADR 0014 remain **not** eligible for archival (a partial supersession does not clear the bar) — which is exactly what ADR 0020's own Negative Consequences bullet 1 already states, citing this precise example ("this template's own supersession style is usually partial (see ADR 0016's own precedent, superseded only specific clauses of ADR 0001/0014)"). The rule behaves as designed against the one real example checked, and the ADR is already explicit that this is a deliberate trade, not an oversight. | not reproduced |
| 13 | Rule 3's in-tree `docs/archive/` mechanism silently reintroduces a duplicate-content or dangling-reference problem via `scripts/check-contract-consistency.py`'s other checks, unacknowledged by ADR 0020's Consequences section | **Reproduced.** Read `scripts/check-contract-consistency.py` directly. Its `RECORD_DIRS` constant (`docs/collaboration/traces/`, `reviews/`, `agreements/`, `docs/issues/`, `docs/work-plans/`, `docs/spike/`, `docs/backlog/`) is the checker's own list of "[d]irectories holding records rather than contract. Their contents are dated statements about the past and are not held to present-tense consistency" (its own comment, verbatim) — and `check_references` skips scanning any file under one of these for dangling links. `docs/archive/` is not in this list, even though ADR 0020's own Rule 1 defines Archive-layer content as exactly this kind of dated, historical record ("Off the normal reading path, but restorable"). Since Rule 3 requires archived files to be moved "verbatim (no content rewriting)," any internal link an archived file already contained (to another document that is later renamed, moved, or itself archived) will be scanned by `check_references` as if it were still a live, present-tense document, producing dangling-reference noise the checker's own design principle says archived content should be exempt from. (`check_id_range_collisions` was separately checked and is **not** vulnerable to the analogous ID-reuse gap — it compares against full `git log --all` history, not current directory listings, so number reuse after an archive move is still caught.) ADR 0020's Consequences section names three other negative consequences with comparable specificity (conservative ADR trigger, illustrative Rule 2 triggers, no Entry-layer discoverability yet) but does not name this one, even though it is concretely checkable by reading the one script this repository's own Preflight already runs. See "Reasons" below for why this is recorded as non-blocking rather than a rejection basis. | reproduced |
| 14 | Rule 4's citation and paraphrase of `qpex`'s `trace-topic-register.md` misquotes or misapplies the rule the spike's own Research Log recorded | Compared ADR 0020 Rule 4's text ("a new trace is not created when the same `LISS-*`/`WP-*` topic already has a current representative trace... update the existing representative trace instead") against case-0001's Research Log entry for `trace-topic-register.md` ("States the reuse rule directly: 'A new phase trace is not added when the same topic already has a current representative... Update the representative... instead.'"). Direct, faithful paraphrase. The additional conditions Rule 4 layers on ("no unresolved obligation, no new approval boundary, no unique review evidence") are item-0012's own facet-3 wording, not `qpex`'s, and ADR 0020 does not attribute them to `qpex` — no misattribution. | not reproduced |
| 15 | ADR 0020 silently includes or forecloses content that belongs to facets 4 (contract-sync diff record), 5 (drift-prevention/CI), or 6 (review-summary packets) | Read the Status, Context, and Decision sections in full for any contract-sync, CI-check, or review-packet content. None appears; the Status section explicitly names facets 4-6 as out of scope and defers them to later, separate work plans per the spike's decomposition table, and Rule 2/Consequences explicitly defer CI-check-driven discoverability to facet 5 without pre-deciding its design. | not reproduced |
| 16 | Rule 7's "no retroactive application" boundary is violated by some file this work plan actually touched, not merely unstated | Same evidence as scenario 5: no existing repository document outside the one named paragraph was moved, archived, deleted, or content-edited; no `docs/archive/` directory exists; the ledger has zero data rows. Held throughout, not merely asserted. | not reproduced |

## Scenarios Not Searched

- Whether every one of ADR 0020's specific quantitative claims about `qpex`
  (e.g., "185 of 186 ADR files," "7 theme documents") is independently
  correct against the actual external `qpex` repository files — this
  review did not re-open `/Users/nn0cl/Documents/git/qpex`; it relied on
  the spike's own Research Log, which states each file was "read in full."
  Re-verifying an external repository's exact file contents from a
  different local repository is judged low-risk and out of this review's
  practical scope, and the claims are attributed consistently across the
  backlog item, spike, and ADR rather than introduced fresh by the ADR.
- Whether `docs/collaboration/restoration-ledger.md`'s conservative
  treatment as an ADR-0006 contract file (Settled Ambiguities table) is the
  only defensible reading — confirmed it is *a* correct reading against the
  letter of `docs/collaboration/prompt-instruction-change-control.md`'s
  contract-file list (`docs/collaboration/*.md` except the three named
  record directories, which does not include a `restoration-ledger.md`
  exemption), but this review did not search for a case where the
  conservative choice itself causes a problem, since erring toward more
  trace/review coverage does not weaken this work plan's evidence.
- Whether Rule 2's per-type triggers, once actually applied by the later
  retroactive-application work plan, will need refinement — explicitly
  named by ADR 0020's own Consequences section as an open risk not yet
  testable against real cases; not this review's job to pre-resolve.
- Long-term stylistic clarity of ADR 0020's prose to a future reader
  unfamiliar with this session — a judgment call beyond the falsification
  criteria this review is scoped to test.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked
      in (Architecture Path documentation/ADR work only — no application
      code, no test changes, content fully pre-specified by the design
      agreement).
- [x] Every `Then` clause in the specification is asserted by the work —
      not applicable; no specification exists for this documentation-only
      change, per `DA-2026-08-19-06`'s own "Specifications" section.
- [x] The dependency rule and port boundaries hold — not applicable; no
      application architecture touched.
- [x] No boundary named in the design agreement was crossed — verified
      directly (scenarios 1-7, 16).
- [x] Specifications and accepted tests were not modified to make work
      pass — not applicable; no tests exist for this change.
- [x] Every claim in the artifact states its grounds — ADR 0020 cites the
      covering design agreement, the spike, and item-0012 throughout; the
      one place a claim's downstream consequence is not fully stated is
      scenario 13, recorded as a non-blocking finding below.
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

- All of `DA-2026-08-19-06`'s explicit Falsification Criteria were
  independently tested and none reproduced: no existing repository
  document outside the one named paragraph was moved, archived, deleted,
  or content-edited by this work plan (scenario 5); the restoration
  ledger's Ledger table has zero data rows (scenario 2); ADR 0020's
  content matches "Exact Content to Produce" byte-for-byte, including the
  corrected Rule 4 citation (scenario 1); `CLAUDE.md` and its four mirrors
  were not touched (scenario 6); the required AI work trace is present and
  accurately documents the fail-then-fix Preflight cycle without smoothing
  it over (scenario 8).
- `scripts/check-contract-consistency.py` passes, re-run independently in
  this session against the actual current tree at `e2052da`, not trusted
  from WP-0014's own Preflight section (which was itself correctly
  point-in-time accurate — scenario 10).
- The mechanical transcription is exact across all four touched files
  (scenarios 1-4), and the Preflight fail-then-fix cycle (bare `qpex`
  citation + stale ADR-range strings, corrected via the amended
  `DA-2026-08-19-06`) is genuine, correctly scoped, and fully traceable
  through both the trace and actual git history (scenarios 8-9).
- Substantively, the ADR's central decision — adapting rather than
  wholesale-adopting `qpex`'s model, given this template's much smaller
  ADR count and existing per-work-plan consolidation checkpoints — is
  soundly grounded in the spike's own comparison (scenario 11), the
  conservative ADR-archival trigger is deliberately self-aware and
  correctly predicts the one real precedent checked (ADR 0016's partial
  supersession of ADR 0001/0014 — scenario 12), the trace-lifecycle rule
  faithfully adapts `qpex`'s own stated rule with correct attribution
  (scenario 14), and the ADR holds its own stated facet 1-3 scope boundary
  throughout, both textually and in what was actually touched (scenarios
  15-16).
- One real, substantive gap was found (scenario 13): ADR 0020's Consequences
  section does not acknowledge that `scripts/check-contract-consistency.py`'s
  `RECORD_DIRS` exclusion list — which exists precisely to exempt
  historical/record content from present-tense consistency checks — does
  not include the new `docs/archive/` directory this ADR's Rule 3
  introduces, so a later archive move risks dangling-reference noise on
  content that is, by this ADR's own definition, no longer supposed to be
  held to present-tense consistency. This is real and worth carrying
  forward, but it does not trigger any of `DA-2026-08-19-06`'s four
  explicit Falsification Criteria, does not misstate anything ADR 0020
  currently claims as true (no `docs/archive/` directory exists yet under
  this work plan's own Rule-7-enforced scope), and is a natural, better fit
  for facet 5 (drift-prevention entry documents and CI checks — the
  work plan ADR 0020 itself already defers exactly this class of
  checker-tooling gap to) or the retroactive-application work plan, both of
  which are the first to actually create `docs/archive/` content. Recorded
  as non-blocking below, per this repository's own precedent
  (`docs/collaboration/reviews/2026-08-19-wp-0013-prevent-direct-to-main-commits-review.md`'s
  Non-Blocking Observations) for a real finding that is not itself a
  rejection basis.

## Non-Blocking Observations

- **(Scenario 13, actionable — recommend a `Type: review-finding` local
  issue.)** `scripts/check-contract-consistency.py`'s `RECORD_DIRS`
  constant should very likely gain a `docs/archive/` entry (or an
  equivalent, more targeted exclusion for archived-file *internal* links,
  since an inbound reference *to* an archived file from a still-current
  document is exactly what Rule 3 already requires updating, and should
  probably still be checked) before or as part of whichever later work
  plan first actually creates content under `docs/archive/` — the
  retroactive-application work plan named in item-0012's Promotion notes,
  or facet 5 (drift-prevention entry documents and CI checks), whichever
  lands first. `docs/collaboration/findings-reuse.md`'s "must change the
  system or be explicitly declined" rule applies to this once it is
  actionable; since no `docs/archive/` content exists yet, it is not
  actionable against this work plan today, but should not be left as an
  unrecorded verbal note either. This review deliberately does not open
  that `Type: review-finding` issue itself (creating a new durable
  artifact goes beyond "review WP-0014 and produce a review record," and
  the finding's real target is a work plan that has not started), but
  recommends the Design & Review group open one — linked to this review
  record — at or before the retroactive-application/facet-5 design intake,
  so the gap does not depend on someone rereading this file to be
  rediscovered.
- Rule 1's Canonical-layer row phrasing ("Any ADR with Status `Accepted`
  and not fully superseded (Rule 3)") cites "(Rule 3)" (Archive mechanism)
  where the actual eligibility test it is invoking is Rule 2's
  (Consolidation trigger conditions); read charitably, "(Rule 3)" points to
  the archival *move* being the act that actually exits an ADR from the
  Canonical layer, with Rule 2 defining eligibility for that move — a
  defensible reading once Rule 2 and Rule 6 are read alongside it, and not
  a claim this review found to be actually wrong anywhere it was traced
  through. A future editor could make the cross-reference read "(Rule 2,
  enacted per Rule 3)" for clarity. Not required for this work plan's Done.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
