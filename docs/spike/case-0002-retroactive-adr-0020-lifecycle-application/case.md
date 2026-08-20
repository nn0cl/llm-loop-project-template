# Spike Case: case-0002-retroactive-adr-0020-lifecycle-application

## Metadata

- Case ID: case-0002
- Title: Retroactive ADR 0020 application — batching strategy and
  restoration-ledger scale check
- Status: closed
- Created: 2026-08-20
- Closed: 2026-08-20
- Owner/agent: Design & Review group (Planner), standing session
- Related work plan: none yet — this item's own execution work plan opens
  only after the Backlog-thread check-in this spike's own Next action
  requires (`docs/backlog/item-0016-retroactive-adr-0020-lifecycle-application.md`'s
  Promotion notes)
- Related local issue (LISS): LISS-0055 (human-decision issue this spike
  opens, see Next action)
- Related backlog item:
  `docs/backlog/item-0016-retroactive-adr-0020-lifecycle-application.md`
- Supersedes case: none
- Superseded by case: none

## Question

Given this repository's actual current document population (20 ADRs, 18
work plans, 38 local issues, 28 traces, 50 review records, 16 backlog
items, 25 design agreements), what batching strategy for applying ADR
0020's classification/archival rules is both mechanically sound and
appropriately conservative for a first pass, and does the restoration
ledger's row format actually hold up at this volume?

## Why a spike (not immediate implementation)

item-0016's own Uncertainty section names this a required-first spike
("this repository's own history is large... decide a manageable batching
strategy... before attempting a single sweep, and confirm the
restoration-ledger format actually scales to this volume before
committing to it") and separately flags "how aggressive the initial pass
should be" as a human-decision point the Director may want to weigh in on
once a concrete plan exists — even though ADR 0016's backlog-gate model
would otherwise let this run fully autonomously. Both of item-0016's own
Promotion notes require a check-in with the Backlog thread before any
large first archiving sweep, so this spike closes with a proposal, not an
executed batch.

## Constraints

- Must remain free of mandatory paid spend unless justified below: yes —
  trivially; this is repository document classification, no tooling cost.
- Architecture / port boundaries to respect: none — no application
  architecture is touched; this is process-document classification only.
- Out of scope for this spike:
  - Actually moving, archiving, or editing any existing repository
    document — item-0016's own boundary note and this session's mandate
    both require a Backlog-thread check-in before any real archive move,
    which has not yet happened.
  - Anything from before this repository's own v1.0.0-era consolidation
    (commit `cf9da58`/`9fcb2d2`) — investigated directly below and found
    to be a non-issue for the working tree as it exists today (see
    Research log).
  - Re-deciding ADR 0020's own rules — if this spike had found a real gap
    or ambiguity in ADR 0020 itself, that would be a reopening trigger for
    a new backlog item per item-0016's own boundary note, not something to
    patch here. No such gap was found (see Selection).

## Candidates

Not a vendor/library selection — the "candidates" are three possible
batching postures for the first archival sweep.

| ID | Option | Source | Notes |
| --- | --- | --- | --- |
| A | Single full sweep: classify and archive every eligible document across all types in one pass | item-0016's own Uncertainty section names this as one option ("archive everything that qualifies immediately") | Matches ADR 0020's rules exactly, but is the aggressive posture item-0016's own Promotion notes explicitly ask Design & Review not to execute unprompted |
| B | Conservative first batch, scoped by work-plan range (e.g. WP-0001 through a stated cutoff), later batches as follow-ups | item-0016's own Uncertainty section names this as the alternative option | Matches the batching-strategy pattern this spike's own research (below) found to be the natural grain of this repository's actual document graph |
| C | Batch by artifact type instead of by work-plan range (e.g. archive all eligible traces first, then all eligible reviews, etc., across the whole history at once) | This spike's own comparison, below | Considered because ADR 0020 Rule 2's per-type triggers differ by type; discarded below because it cuts across work-plan boundaries that the actual eligibility evidence (Director-close, issue terminal status, no open finding) is scoped to |

## Evaluation criteria

| Criterion | Why it matters | How measured |
| --- | --- | --- |
| Respects item-0016's own Promotion-notes constraint (propose, don't execute a large first sweep unprompted) | This is a session mandate, not a judgment call this spike can override | Direct compliance check against the Promotion notes' literal wording |
| Matches ADR 0020 Rule 2's actual eligibility grain (work plan is the unit most triggers are defined against — Director-closed, every issue done/wont_do, no open review-finding) | A batching unit that does not match the eligibility unit produces partial, inconsistent archival state | Compare each option's batching unit against Rule 2's own per-type trigger definitions |
| Scales to the restoration ledger's row format without redesign | item-0016's own Uncertainty section requires confirming the ledger format "actually scales to this volume" before committing to it | Draft sample ledger rows for representative candidate documents and check they fit the schema Rule 5/case-0001 already fixed |
| Leaves the v1.0.0-era boundary and the `KNOWN_HISTORICAL_ID_REUSE` registry undisturbed | item-0016's own boundary note requires explicit care here | Direct git-history inspection of the boundary commits and the files the registry names |
| Minimizes risk from already-known, still-open gaps in the drift-prevention checks that will run against real archive content | item-0016 itself names LISS-0044 (resolved) and LISS-0052 (still open) as exactly the kind of gap this application will make concretely testable | Inspect `scripts/check-contract-consistency.py`'s current archive-related checks and the still-open finding's own stated exposure |

## Research log

| Date | Query or source | Finding | URL |
| --- | --- | --- | --- |
| 2026-08-20 | `docs/architecture/adr/0020-document-and-log-lifecycle-model.md` (Rules 1-7) | Fixes the eligibility grain per type: ADR (every Decision clause explicitly superseded by name), work plan (Director-closed + every issue done/wont_do + no open review-finding naming it), local issue (terminal status + owning work plan archived/closed with no dependency), trace (Rule 4's representative-trace rule, not a separate trigger), review record (its work plan is archived), backlog item (promoted + work plan Director-closed), design agreement (its work plan is archived, unless a later agreement still cites it). | local file, read in full |
| 2026-08-20 | `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`, Consequences (Negative) | States directly: "most ADRs will likely never become eligible for archival, since this template's own supersession style is usually partial" — a deliberate trade the ADR itself already anticipated, not a gap this spike needs to escalate. | local file, read in full |
| 2026-08-20 | `docs/architecture/adr/0016-...md`, "Supersession, precisely" table | The only concrete precedent of one Accepted ADR superseding another in this repository is partial: ADR 0016 supersedes specific clauses of ADR 0001 (point 2) and ADR 0014 (clauses 1 and 5), never every clause of either. Neither ADR 0001 nor ADR 0014 has every Decision clause named as superseded, so neither is Rule-2-eligible for archival today. No other ADR in the set (0002-0013, 0015, 0017-0020) is named as superseded, in whole or in part, anywhere in the repository. **Finding: zero ADRs are archival-eligible under Rule 2 in a first pass** — the Canonical/ADR layer is out of scope for any batch until a later ADR fully supersedes an earlier one by name. | repository-wide read of every ADR's own Status section |
| 2026-08-20 | `git log --oneline --all \| grep -i "director close"` and a second pass for phrasing variants (`record work-plan close`) | Explicit Director-close commits found for WP-0002, WP-0003, WP-0004/0005/0007/0008 (closed together), WP-0006, WP-0009, WP-0010/0011 (closed together), WP-0012 through WP-0018 (each individually). WP-0001 has no matching commit-message convention (it predates the standardized "Director close" phrasing) but its own Issue Graph shows its single issue, LISS-0001, at terminal `Status: done`, with "Current Next Issue: none... LISS-0001 is complete" recorded in the file itself. | `git log --oneline --all`, direct file read |
| 2026-08-20 | `- Status:` field, every `docs/issues/LISS-*.md` file (top-level metadata field only, not prose mentions elsewhere in each file) | 38 issues total. Terminal (`done`/`wont_do`/`resolved`/`closed`): LISS-0001, 0002, 0003, 0028-0033, 0035-0045, 0047, 0049-0051, 0054 — the large majority. Non-terminal: LISS-0019 through LISS-0027 (all `review`, WP-0002's own issue set) and LISS-0046, 0048, 0052, 0053 (`ready`/`proposed`, all forward-looking work not yet started). | `grep -H "^- Status:" docs/issues/LISS-*.md` |
| 2026-08-20 | LISS-0019 through LISS-0027 specifically, cross-checked against WP-0002's own Director-close commit (`9721477`/`7f82227`) | **Concrete finding, not an ADR-0020 gap**: WP-0002 (the founding two-group-loop work plan) was recorded as Director-closed, but its own nine issues (LISS-0019-0027) still carry `Status: review` today rather than `done` — i.e., their Status field was never advanced past the Reviewer stage after the work plan's own close. Under ADR 0020 Rule 2's literal reading ("every issue in it is `done` or `wont_do`"), WP-0002 is **not yet archival-eligible**, even though it is Director-closed, until either those nine issues' Status fields are corrected to reflect their actual completion or a documented judgment call treats a Director-closed work plan's frozen `review`-status issues as equivalent to `done` for this purpose. This is exactly the kind of "case not listed here" ADR 0020 Rule 2 itself anticipates the retroactive-application work plan will need to resolve with its own recorded judgment call — not a defect in ADR 0020's rule text itself. | direct file reads, cross-referenced against `git log` close commits |
| 2026-08-20 | `Type: review-finding` issues' `Status:` fields | Two open (non-terminal) review-finding issues exist: none are open — LISS-0044 and LISS-0047 (the only two `Type: review-finding` issues that were also `closed`) are both terminal. **LISS-0052** (`Type: review-finding`, `Status: proposed`) is the one currently-open review-finding issue in the whole repository, and it concerns the drift-prevention checker's own fenced-code-block gap (see below) — directly relevant to this item's own scope, not incidental. | `grep -H "^- Type:" docs/issues/LISS-0044*.md docs/issues/LISS-0046*.md docs/issues/LISS-0047*.md docs/issues/LISS-0048*.md docs/issues/LISS-0052*.md docs/issues/LISS-0053*.md` |
| 2026-08-20 | `docs/issues/LISS-0052-entry-archive-reference-fenced-code-block-gap.md` | `check_no_archive_reference_from_entry` (the ADR-0020 drift-prevention check in `scripts/check-contract-consistency.py`) has a known, still-open, low-priority gap: a `docs/archive/...` reference split across a hard line-wrap **inside a fenced code block** is invisible to both its per-line and cross-line scans. The issue's own Disposition section records this as deliberately deferred (narrow exposure, no Entry document today combines a fenced example with a hard-wrapped archive path, two correction rounds already spent on adjacent gaps LISS-0050/0051). Not a blocker for a first small archive batch, since a first batch produces few new `docs/archive/` paths and none of this repository's Entry documents (`docs/architecture/agent-quickstart.md`, `CLAUDE.md`, `README*.md`) currently reference archived files at all — but worth re-checking once Entry documents start citing specific archived paths. | direct file read |
| 2026-08-20 | `scripts/check-contract-consistency.py`, `RECORD_DIRS` constant (line ~320) | `docs/archive/` is already present in `RECORD_DIRS` (the set of directories excluded from present-tense contract-consistency checks) — confirms LISS-0044's finding (the original `RECORD_DIRS` exclusion gap) is already resolved in the current tree, ahead of any real archive content existing. This is exactly the "confirm the drift-prevention checks... correctly validate the result once real archive content exists" item-0016 itself calls for; the mechanism is present and ready to be exercised, not still missing. | direct file read |
| 2026-08-20 | `git log --oneline cf9da58 -1`, `git show 9fcb2d2 --stat`, `docs/architecture/adr/0020...` boundary note, `scripts/check-contract-consistency.py`'s `KNOWN_HISTORICAL_ID_REUSE` registry | `9fcb2d2` ("chore: reset the repository's record artifacts to the initial state") removed every pre-existing local issue, work plan, trace, review record, design agreement, and sample spec from the working tree ("Removed: 26 traces, 17 local issues, 2 work plans, 2 design agreements, 1 review record, 1 sample rollout spec"), keeping only `.gitkeep` files. `cf9da58` (immediately prior) consolidated the ADR set into its "first edition." **Finding: no Evidence-layer document (issue/work-plan/trace/review/agreement) anywhere in the current working tree predates this boundary** — every one that exists today was created after the reset, by construction. The ADR set (`0001`-`0020`) begins at exactly this boundary (`cf9da58`'s own "first edition"), so no ADR predates it either. item-0016's boundary note ("do not touch anything from before this repository's own v1.0.0-era consolidation... without explicit care") is therefore automatically satisfied for this spike's scope by the fact that nothing pre-boundary exists in the tree to touch — the only live consideration is not to *misread* `KNOWN_HISTORICAL_ID_REUSE`'s five listed files (ADR 0001-0003/0012-0013, LISS-0001-0002/WP-0001-0002... — actually LISS-0001-0003 and WP-0001-0002 per the registry) as if they carried pre-reset history; they are post-reset documents whose *numbers* were reused, not pre-reset survivors. | `git log`, `git show`, direct script read |
| 2026-08-20 | Document population census (`ls`/`wc -l` across each `docs/` subdirectory) | 20 ADRs, 18 work plans, 38 local issues, 28 traces, 50 review records, 16 backlog items, 25 design agreements. Confirms item-0016's own Summary figures ("WP-0001 through WP-0018, 50+ local issues... a dozen-plus review records, a dozen-plus AI work traces, 15 backlog items, 20 ADRs") are accurate as of today, with backlog items now at 16 (item-0016 itself is the 16th). | direct directory listing |

## Comparison

| Criterion | A (single full sweep) | B (conservative, work-plan-scoped batches) | C (batch by artifact type) |
| --- | --- | --- | --- |
| Respects the Promotion-notes constraint | Fails directly — this is exactly the "archive this repository's entire qualifying history in one pass unprompted" the Promotion notes name and reject | Matches — "a conservative first batch... with later batches as follow-ups" is the Promotion notes' own stated alternative | Matches the letter (not a single full sweep) but not clearly the spirit — still touches every work plan's traces/reviews at once, just reordered by type |
| Matches Rule 2's actual eligibility grain | N/A (single pass makes this moot — everything eligible moves at once regardless of grain) | Strong fit — work plan is the unit Rule 2 defines Director-close, issue-terminal-status, and open-finding triggers against; traces/reviews/design-agreements attach to a work plan and inherit its archival state (Rule 2: trace/review/agreement eligibility each ultimately keys off "its owning/reviewed work plan is archived") | Weaker fit — archiving "all traces" independent of which work plan owns them risks archiving a trace whose owning work plan is not yet archival-eligible (e.g., a trace under WP-0002, which this spike found is not yet eligible per the review-finding-issue-status gap above) |
| Scales to the ledger format | Same schema regardless of batch size — not differentiating, but a single sweep produces the largest number of rows in one commit, the least reviewable unit | Same schema; each batch produces a reviewable, bounded set of rows per commit — better matches Rule 5's "one row per moved-or-consolidated document... in the same commit as the move" without producing one enormous commit | Same schema; type-based batches could still produce a very large single-type commit (e.g., "archive all eligible traces across 18 work plans at once") |
| v1.0.0 boundary / `KNOWN_HISTORICAL_ID_REUSE` risk | Same for all three — already a non-issue per Research log (nothing pre-boundary exists in the tree) | Same | Same |
| Drift-prevention-check exposure (LISS-0052) | Same for all three — narrow, already-scoped gap, not batch-size-dependent | Same | Same |

## Cost and quality judgment

- Free / zero-mandatory-spend options considered: all three; none has a
  cost dimension (documentation/process classification only).
- Quality bar applied: does the option comply with item-0016's own
  Promotion-notes constraint, match ADR 0020 Rule 2's actual eligibility
  unit, and produce a reviewable, bounded first commit rather than one
  large undifferentiated sweep?
- No paid option is in play; not applicable.

## Selection

- Selected: B (conservative, work-plan-scoped batches) — recommended
  posture; **not yet authorized to execute**, per this item's own
  Promotion-notes check-in requirement (see Next action).
- Rationale: Option B is the only one of the three that both matches
  ADR 0020 Rule 2's actual eligibility grain (the work plan is the unit
  almost every per-type trigger ultimately resolves against — a trace,
  review record, or design agreement's own eligibility is defined in terms
  of its owning/reviewed work plan's archival state, not independently) and
  satisfies item-0016's own explicit Promotion-notes instruction to
  propose a conservative first batch rather than execute a single full
  sweep. Concretely, based on this spike's own research:
  - **Zero ADRs** are eligible in any batch today (Rule 2's
    all-clauses-superseded trigger has never fired once in this
    repository's history) — the Canonical/ADR layer stays untouched by
    the first batch and likely for a long time after, which is a known,
    already-accepted trade-off from ADR 0020 itself, not a new finding
    this spike needs to escalate.
  - **WP-0001** is the strongest first-batch candidate: Director-close
    convention predates it, but its own file records its one issue
    (LISS-0001) as terminal (`done`) with no further action, and it has no
    known open review-finding naming it. A reasonable first-batch judgment
    call (to be recorded explicitly in the retroactive-application work
    plan, per ADR 0020 Rule 2's own "record its own judgment call for
    cases not listed here" allowance) is to treat WP-0001 as archival-
    eligible despite predating the "Director close" commit-message
    convention, since the terminal-status evidence itself is present in
    the file.
  - **WP-0002** is Director-closed but **not yet eligible** under Rule 2's
    literal "every issue is done or wont_do" wording, because LISS-0019
    through LISS-0027 are still `Status: review`. This is a real,
    concretely-discovered batching consideration (not an ADR 0020 gap):
    the retroactive-application work plan will need to either (a) correct
    those nine issues' Status fields to reflect their actual
    already-reviewed-and-closed reality before archiving WP-0002's
    Evidence-layer documents, or (b) record an explicit judgment call
    treating a Director-closed work plan's frozen pre-terminal issue
    statuses as equivalent to `done` for archival purposes. Either path is
    a defensible, in-scope judgment call for that later work plan to make
    and record — not something this spike or ADR 0020 itself needs to
    resolve now.
  - **WP-0003 through WP-0018** each have their own Director-close commit;
    a full per-work-plan eligibility check (every issue's Status field,
    every review-finding issue naming it) is the retroactive-application
    work plan's own job, not fully re-verified line-by-line here — this
    spike's job was to confirm the batching *unit* and *approach* work,
    not to pre-execute the classification.
  - **Design agreements, review records, and backlog items** naturally
    batch alongside the work plan they belong to (a design agreement moves
    only if its own work plan is archived and no later agreement still
    cites it as precedent; a review record moves only once the work plan
    it reviewed is archived; a backlog item moves once its resulting work
    plan is Director-closed) — confirming Option B's work-plan-scoped
    batching naturally carries these types along without a separate
    per-type sweep.
  - **Traces** follow Rule 4 (representative-trace consolidation) inside
    each batch, not a separate trigger — most topics in this repository
    accumulated more than one trace before ADR 0020 existed (the normal
    case Rule 4 itself anticipates), so each work-plan batch will also need
    to designate one representative trace per topic and consolidate the
    rest, recorded as `consolidated-into-representative` rows.
  - The restoration-ledger format itself (columns
    `date, source_path, source_commit, source_tag, canonical_destination,
    classification, reason`, fixed by case-0001 and ADR 0020 Rule 5) was
    checked against a drafted sample row for the WP-0001 candidate (see
    Evidence) and holds up without modification — confirming the second
    half of item-0016's own required spike question.
- Discard reasons:
  - A (single full sweep): directly contradicts item-0016's own
    Promotion-notes instruction not to "archiv[e] this repository's entire
    qualifying history in one pass unprompted"; also produces the least
    reviewable single commit and the highest risk of missing a
    per-work-plan eligibility gap like the WP-0002 issue-status finding
    above.
  - C (batch by artifact type): technically avoids "one pass" but not the
    Promotion notes' underlying spirit (Director wants graduated,
    checkable batches), and risks archiving a type-level document (e.g., a
    trace) ahead of its owning work plan's own eligibility determination,
    producing an inconsistent intermediate state Option B's work-plan
    grain avoids by construction.

### Sample ledger row (drafted, not committed — format check only)

Drafted against the WP-0001 candidate to confirm the restoration-ledger
schema holds at this repository's actual scale; **not written to
`docs/collaboration/restoration-ledger.md`** — no document has actually
moved yet.

| date | source_path | source_commit | source_tag | canonical_destination | classification | reason |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-08-20 | `docs/work-plans/WP-0001-review-issues-minor-fix-path.md` | `<commit hash of the actual archive-move commit, once executed>` | N/A | `docs/archive/work-plans/WP-0001-review-issues-minor-fix-path.md` | archived | Work plan Director-closed (predates the "Director close" commit-message convention; own file records LISS-0001 at terminal `done` with no further action), per ADR 0020 Rule 2's work-plan trigger |

The row fits the schema cleanly at seven columns with no truncation or
ambiguity; drafting it also surfaced that `source_commit` cannot be filled
in accurately until the archive-move commit itself exists (a chicken-and-
egg the ledger format already handles correctly, since Rule 5 requires the
row "in the same commit as the move" — the row and the commit are written
together, not the row first).

## Evidence

- `docs/architecture/adr/0020-document-and-log-lifecycle-model.md` (Rules
  1-7, Consequences)
- `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
  ("Supersession, precisely" table)
- `docs/backlog/item-0016-retroactive-adr-0020-lifecycle-application.md`
  (Uncertainty and Promotion notes sections)
- `docs/work-plans/WP-0001-review-issues-minor-fix-path.md`,
  `docs/work-plans/WP-0002-two-group-send-message-loop.md`
- `docs/issues/LISS-0019-*.md` through `docs/issues/LISS-0027-*.md`
  (`Status: review`, cross-checked against WP-0002's Director-close commit)
- `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`,
  `docs/issues/LISS-0052-entry-archive-reference-fenced-code-block-gap.md`
- `scripts/check-contract-consistency.py` (`RECORD_DIRS`,
  `check_no_archive_reference_from_entry`, `KNOWN_HISTORICAL_ID_REUSE`)
- `git log --oneline --all` (Director-close commit survey),
  `git show 9fcb2d2 --stat`, `git log --oneline cf9da58 -1` (boundary
  commit inspection)
- Direct census of `docs/architecture/adr/`, `docs/work-plans/`,
  `docs/issues/`, `docs/collaboration/traces/`,
  `docs/collaboration/reviews/`, `docs/backlog/`,
  `docs/collaboration/agreements/`

## Next action (exactly one)

- [x] Human decision issue (`Type: decision`): **LISS-0055** — records
      this spike's proposed batching plan (Option B: conservative,
      work-plan-scoped first batch, oldest-first, starting with WP-0001 and
      WP-0002 once WP-0002's own issue-status question is resolved or
      explicitly judgment-called) and holds the Backlog-thread check-in
      this item's own Promotion notes require before any real archive move
      is dispatched to the Implementation group. No work plan or design
      agreement is opened by this spike — per the item's own mandate, that
      happens only after the Director/Backlog thread responds to LISS-0055.

## Open risks after close

- The WP-0002 issue-status finding (LISS-0019 through LISS-0027 frozen at
  `Status: review` despite the work plan's own Director close) may recur
  across other early work plans not individually re-checked by this spike;
  the retroactive-application work plan's own Preflight should re-verify
  every candidate work plan's issue statuses directly rather than assuming
  this spike's WP-0001/WP-0002 spot-check generalizes.
- LISS-0052's fenced-code-block gap in
  `check_no_archive_reference_from_entry` remains open; low risk for a
  first small batch (no Entry document today references any archived
  path), but should be re-checked before a later, larger batch once Entry
  documents plausibly start citing specific `docs/archive/` files in
  fenced examples.
- This spike did not re-verify per-work-plan eligibility for WP-0003
  through WP-0018 individually (Director-close commits exist for all of
  them, but issue-level and open-review-finding-level detail was not
  re-checked file-by-file the way WP-0001/WP-0002 were) — the
  retroactive-application work plan's own Preflight must do this
  verification directly, not assume this spike's spot-check covers them.

## Addendum (2026-08-20, post-close): WP-0002 issue-status gap resolved; batch authorized

Recorded after this spike's own close, once the Backlog thread responded to
LISS-0055 (see that issue's own Work Notes for the full decision record —
this addendum states only what changes for this spike's own findings above,
not a re-litigation of the batching-posture selection, which stands as
recorded).

- **WP-0002 issue-status gap, closed**: the "Open risks after close" gap
  above (LISS-0019 through LISS-0027 frozen at `Status: review` despite
  WP-0002's own Director close) was resolved by path (a) of the two this
  spike named — the nine issues' `Status` fields were corrected to `done`,
  not judgment-called around. Commit `73ab2ce` ("process: sync WP-0002's
  nine issue statuses to done"), merged to `main` via PR #20 (merge commit
  `6e52ad7`). Independently re-confirmed directly against the files
  themselves in the retroactive-application work plan's own worktree (not
  taken on the commit message's word alone), after merging `main` into
  `process/promote-item-0016` (merge commit `9be0223`):
  `grep -H "^- Status:" docs/issues/LISS-0019-*.md docs/issues/LISS-0020-*.md
  docs/issues/LISS-0021-*.md docs/issues/LISS-0022-*.md
  docs/issues/LISS-0023-*.md docs/issues/LISS-0024-*.md
  docs/issues/LISS-0025-*.md docs/issues/LISS-0026-*.md
  docs/issues/LISS-0027-*.md` shows `Status: done` for all nine. No open
  `Type: review-finding` issue names either WP-0001 or WP-0002 (confirmed by
  `grep -rl "Type: review-finding" docs/issues/` cross-checked against each
  matched file's own `Type:` field — the four incidental text hits for
  "WP-0001"/"WP-0002" are LISS-0022, LISS-0028, LISS-0039, LISS-0055, none of
  which is itself `Type: review-finding`). **WP-0002 is now genuinely
  Rule-2-eligible**, on the same footing as WP-0001, not merely
  judgment-called eligible.
- **New finding this spike did not surface: two of the four candidate
  design agreements are blocked from archival by the general Rule 2 opening
  clause**, independent of the per-type design-agreement trigger this
  spike's Selection section described. A current, Accepted,
  not-fully-superseded Canonical document (an ADR) cites each of WP-0001's
  and WP-0002's own design agreements *normatively* — as the grounding for
  its own Accepted status, not as a passing or historical mention:
  - `docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md`'s
    Status section: "Accepted. Covered by `DA-2026-08-02-04`." — WP-0001's
    own design agreement.
  - `docs/architecture/adr/0016-...md`'s Status section: "`Accepted` status
    requires a design agreement with the Director covering the decision.
    That agreement is `DA-2026-08-18-01`..." — WP-0002's own design
    agreement, additionally quoted from directly in ADR 0016's own Context
    section.

  Rule 2's opening paragraph is explicit that this blocks archival
  regardless of a type's own terminal status: "A document with... content a
  current Canonical document still references by more than a passing
  mention is never eligible." Both citations name the specific agreement ID
  as the ADR's own Accepted-status grounding — this is exactly "more than a
  passing mention," not the "see the historical record" case Rule 3
  reserves for a reference-update instead of a block. **Neither
  `DA-2026-08-02-04` nor `DA-2026-08-18-01` is archived in this batch**;
  both stay in place regardless of their owning work plan's own archival.
  This does not affect WP-0001 or WP-0002's own file-level eligibility, or
  their issues'/traces'/review-records' eligibility — only the two design
  agreements themselves.
- **Confirmed non-blocking, Rule-3 reference-update case**:
  `docs/collaboration/design-review-perspectives.md` (a Canonical contract
  file) cites both of WP-0002's own review records
  (`docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`
  twice, at its "Re-verify state" and "Verify a claimed authority"
  perspective entries) as historical provenance for lessons the document
  already states in full — not as content the document's own validity
  depends on. This is the "see the historical record" case Rule 3 itself
  names: the review records are still archival-eligible once WP-0002 is
  archived, but the retroactive-application work plan must update
  `design-review-perspectives.md`'s two citations to point at the new
  `docs/archive/` paths in the same commit as the move, per Rule 3's own
  requirement not to leave a current Canonical document pointing at a path
  that no longer exists.
- **Decision recorded**: the Backlog thread authorized this spike's own
  Option B first batch as WP-0001 and WP-0002 together (see LISS-0055's
  Work Notes) — the WP-0002 issue-status gap that would otherwise have
  required a judgment call is resolved as ordinary bookkeeping instead, per
  the first of the two paths this spike's Selection section named.
