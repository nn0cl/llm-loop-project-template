# Design Agreement: Document and Log Lifecycle Model

## Identity

- Agreement ID: DA-2026-08-19-06
- Date: 2026-08-19
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
(`Status: promoted`), whose Promotion notes are this agreement's Director
authorization under ADR 0016 Rule 2, and the required-first spike this
agreement itself closes the loop on
(`docs/spike/case-0001-document-log-lifecycle-management/case.md`, `Status:
closed`, Selection: Option B): create ADR 0020, covering facets 1-3 of
item-0012's six-facet proposal (four-layer document model, status
vocabulary and consolidation trigger conditions, trace lifecycle), plus an
empty restoration ledger and a small disambiguating cross-reference in
`docs/collaboration/local-issue-planning.md`. This is the first of several
work plans for item-0012, per the spike's own "Decomposition and
sequencing" table; facets 4-6 are out of scope here and get their own
design agreements when reached. Retroactive application of these rules to
this repository's own existing document history is explicitly out of
scope here, per the Director's own sequencing decision at item-0012's
promotion.

## Spike Result (run by the Design & Review group before this agreement)

`docs/spike/case-0001-document-log-lifecycle-management/case.md`,
Selection: **Option B (adapt)**. This template's own current state (19
ADRs; existing per-work-plan consolidation via ADR 0014/ADR 0016) does not
exhibit the duplication problem `qpex`'s aggressive canonicalization
(WP-0090/WP-0091: mass ADR deletion, tag-only recovery) was built to fix.
The actual, narrower gap: no Archive layer, no document-status vocabulary,
no restoration ledger. Restoration ledger location/format settled:
`docs/collaboration/restoration-ledger.md`, schema
`date, source_path, source_commit, source_tag, canonical_destination,
classification, reason`. Archive mechanism settled: in-tree move to
`docs/archive/<original-dir>/<filename>`, not `qpex`-style working-tree
deletion.

## Scope

- In scope:
  - `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
    (new), with exactly the content specified in "Exact Content to
    Produce" below.
  - `docs/collaboration/restoration-ledger.md` (new, empty — header,
    schema documentation, and an empty Ledger table only), with exactly
    the content specified below.
  - `docs/collaboration/local-issue-planning.md`: exactly one new
    paragraph added to its "Status Values" section (specified below); no
    other part of this file changes.
  - **Addendum (added after `scripts/check-contract-consistency.py`'s
    `check_adr_range` correctly failed on the first Implementation
    attempt):** `README.md`, `QUICKSTART.md`, and `QUICKSTART.ja.md`'s
    existing ADR-range statements, updated from "0001-0019"/"0020 and
    up"/"0020 以降" to "0001-0020"/"0021 and up"/"0021 以降" — exact
    old/new text pairs specified in "Exact Content to Produce" -> "File 4"
    below. This is routine, pre-existing, checker-enforced maintenance
    that applies to any new ADR (not specific to item-0012's lifecycle
    rules, and not "retroactive application" of those rules to existing
    history) — every prior ADR addition in this repository's history did
    the same. None of these three files is an ADR-0006 contract file or a
    `CLAUDE.md` mirror, so this addendum does not change the trace/mirror-
    sync obligations stated elsewhere in this agreement.
  - The required AI work trace under `docs/collaboration/traces/`
    (`local-issue-planning.md` is an ADR-0006 contract file, so a trace is
    required for this work plan regardless of the ADR itself not being on
    that list).
- Explicitly out of scope:
  - Any move, archive, deletion, or content edit of an existing
    `docs/issues/`, `docs/work-plans/`, `docs/collaboration/traces/`,
    `docs/collaboration/reviews/`, `docs/collaboration/agreements/`, or
    other `docs/architecture/adr/` file (ADR 0020's own Rule 7).
  - Facets 4 (contract-sync diff record), 5 (drift-prevention entry
    documents and CI checks), and 6 (review-summary packets) — later,
    separate work plans, per the spike's decomposition table.
  - Any edit to `CLAUDE.md` or its four mirrors — ADR 0020 is
    self-contained, following ADR 0018's own precedent (no companion
    policy doc, no required-reading-list entry); confirmed by grep that
    no mirror file references ADR numbers directly, so no discoverability
    obligation is raised by this specific ADR.
  - Creating a `docs/archive/` directory itself, populating it, or backfilling
    the restoration ledger with any row — the ledger starts empty; population
    is the later retroactive-application work plan's job.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Create `docs/architecture/adr/0020-document-and-log-lifecycle-model.md` | Implementer | Architecture Path (a new ADR; content fully specified below, so Implementer transcribes rather than designs) | Matches "Exact Content to Produce" verbatim | read-through diff |
| 2 | Create `docs/collaboration/restoration-ledger.md` | Implementer | Architecture Path | Matches "Exact Content to Produce" verbatim; Ledger table has no data rows | read-through diff |
| 3 | Add the one cross-reference paragraph to `docs/collaboration/local-issue-planning.md`'s "Status Values" section | Implementer | Architecture Path | Matches "Exact Content to Produce" verbatim; no other part of the file changes | read-through diff |
| 3b | Update `README.md`/`QUICKSTART.md`/`QUICKSTART.ja.md`'s ADR-range statements (0019 -> 0020) | Implementer | Architecture Path | Matches "Exact Content to Produce" -> "File 4" exactly; `check_adr_range` passes | `scripts/check-contract-consistency.py` |
| 4 | AI work trace | Implementer | Architecture Path | States which contract file changed (`local-issue-planning.md`), why, and what agent behavior changes; also names the two new non-contract files for completeness | trace file present |
| 5 | Self-review | Implementer | Architecture Path | Short-form self-review per `docs/templates/self-review.md` (size `L` — full form per ADR 0015, since `L` exceeds the `S` short-form default), recorded in LISS-0043 Work Notes | self-review record |
| 6 | Preflight Validation | Implementer / deterministic tool | Architecture Path | `pass` recorded with `scripts/check-contract-consistency.py` output and an explicit scope check confirming no existing document was moved/edited beyond the one named paragraph | Preflight section in WP-0014 |
| 7 | Work-plan-level Reviewer pass | Reviewer (Design & Review group, separate context) | Architecture Path | Review record confirms the ADR's substantive soundness (not only mechanical transcription accuracy), the scope boundary held, and the trace is present and accurate | review record under `docs/collaboration/reviews/` |

Sequencing: Tasks 1, 2, and 3 may proceed in any order (independent files).
All three block Task 4. Task 4 blocks 5. Task 5 blocks 6. Task 6 blocks 7.

## Exact Content to Produce

### File 1: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`

```markdown
# ADR 0020: Document and Log Lifecycle Model

## Status

Accepted. Covered by
`docs/collaboration/agreements/2026-08-19-document-log-lifecycle-model.md`
(`DA-2026-08-19-06`). This ADR is additive: it supersedes nothing in ADR
0001-0019. Follow-up issue: LISS-0043
(`docs/work-plans/WP-0014-document-log-lifecycle-model.md`).

`Accepted` status requires a design agreement with the Director covering the
decision. That agreement is `DA-2026-08-19-06`, whose Direction section rests
on `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
(`Status: promoted`) and the required-first spike,
`docs/spike/case-0001-document-log-lifecycle-management/case.md` (`Status:
closed`, Selection: Option B).

This ADR covers facets 1-3 of item-0012's six-facet proposal only: the
four-layer document model, the status vocabulary and consolidation
conditions, and applying the same lifecycle to work traces. Facets 4
(contract-sync diff record), 5 (drift-prevention entry documents and CI
checks), and 6 (review-summary packets) are sequenced as later, separate
work plans — see the spike's own "Decomposition and sequencing" table.

## Context

External feedback from an adopting project (`qpex`), relayed by the
Director: this template's growing volume of documents and logs (ADRs,
issues, work plans, traces, review records, backlog items) does not itself
cause the problem `qpex` observed — the actual problem is that no record
states, for itself, whether it is current or historical, when it can be
consolidated, which document its content should move to, or how to
restore it. `qpex` closed this gap for its own repository with a four-layer
model (Entry/Canonical/Evidence/Archive) and aggressive canonicalization:
`qpex`'s WP-0090/WP-0091 deleted 185 of 186 ADR files from its working
tree, replacing them with 7 theme documents, recoverable only through a
baseline git tag and commit hash.

The required-first spike (`docs/spike/case-0001-document-log-lifecycle-management/case.md`)
compared `qpex`'s actual mechanics against this template's own current
state (19 ADRs, not 186; per-work-plan self-review and consolidation
checkpoints already provided by ADR 0014 and ADR 0016) and found this
template does not exhibit the duplication problem `qpex`'s aggressive
mechanics were built to solve. The concrete gap this template does have,
confirmed by direct inspection of `docs/collaboration/` and
`docs/architecture/adr/`, is narrower: there is no Archive layer, no
document-status vocabulary, and no restoration-ledger mechanism at all.
This ADR closes that specific gap (spike Selection: Option B — adapt, not
adopt wholesale), leaving this template's existing five-artifact-type
structure (ADR / local issue / work plan / trace / review record) intact.

This ADR defines rules only. Per the Director's own sequencing decision at
item-0012's promotion ("build and close the lifecycle rules... as their
own work plan first; retroactive application... is a separate, later work
plan"), no existing repository document is archived, moved, deleted, or
edited by this ADR or its own work plan (WP-0014). The restoration ledger
this ADR creates starts empty.

## Dependency Adoption Evidence

Not applicable. This decision selects no library, framework package,
provider SDK, datastore client, build tool, or test helper. It is a
process/documentation-governance decision.

## Decision

### Rule 1 — Four layers, mapped onto this template's existing artifact types

There are four layers. Unlike `qpex`, this template does not introduce new
document *types* for them — each layer is a role a document plays,
determined by its existing type and its existing type-specific status
field (per `docs/collaboration/local-issue-planning.md`'s Status Values,
each ADR's own Status section, `docs/backlog/README.md`'s status flow, and
`docs/collaboration/design-agreement.md`'s work-plan-close state) plus, for
Canonical and Evidence records, whether they have been archived under
Rule 3.

| Layer | Which existing documents play this role | Principle |
| --- | --- | --- |
| Entry | `docs/architecture/agent-quickstart.md`, `CLAUDE.md` and its mirrors, `README.md`/`README.ja.md` | Fixed, small set; not archived; content changes go through ADR-0006 governance, not this ADR |
| Canonical | Any ADR with Status `Accepted` and not fully superseded (Rule 3); every `docs/collaboration/*.md` and `docs/templates/*.md` contract/policy file (current by definition — these are living documents kept in sync, not versioned instances); the current `docs/specs/` file for a behavior | The same current-state fact lives in exactly one Canonical document; a second document restates it only by reference, not by duplication |
| Evidence | Work plans, local issues, traces, review records, design agreements, backlog items, spike cases, while still current (in progress, recently closed, or still needed to explain a live Canonical decision or an unresolved obligation) | Grounds for Canonical decisions; not itself the current source of a rule |
| Archive | Any Evidence-layer or superseded Canonical-layer document that has met a Rule 2 consolidation trigger and been moved under Rule 3 | Off the normal reading path, but restorable — a plain file read under `docs/archive/`, not only a git-history lookup |

### Rule 2 — Consolidation trigger conditions

A document becomes eligible for archival only after its own existing
type-specific terminal status is already reached — this ADR's vocabulary
never substitutes for or skips a type's own required lifecycle. Illustrative
triggers, by type (not exhaustive; the retroactive-application work plan
applies these principles to specific documents and records its own
judgment call for cases not listed here):

- **ADR**: eligible once every one of its Decision clauses has been
  explicitly named as superseded in a later Accepted ADR's own
  Supersession statement (this template's existing convention, e.g. ADR
  0016's "Supersession, precisely" table) — not merely "old." An ADR with
  even one live, unsuperseded clause is not eligible.
- **Work plan**: eligible once Director-closed (per
  `docs/collaboration/design-agreement.md`'s "Closing a work plan"), every
  issue in it is `done` or `wont_do`, and no open `Type: review-finding`
  issue names it.
- **Local issue**: eligible once `done`, `wont_do`, or (for a
  review-finding) `closed`, and its owning work plan is itself archived or
  Director-closed with no remaining dependency on the issue.
- **Trace**: governed by Rule 4 below (the representative-trace rule), not
  by a separate trigger — a trace becomes eligible when it is merged into
  a topic's representative trace.
- **Review record**: eligible once the work plan it reviewed is archived.
- **Backlog item**: eligible once promoted and its resulting work plan is
  Director-closed — the work plan becomes the current record; the backlog
  item becomes historical.
- **Design agreement**: eligible once its work plan is archived, unless a
  later work plan's own agreement explicitly cites it as still-relevant
  precedent (in which case it is not archived while that citation stands).

A document with a still-open `depends_on`, an unresolved `Type:
review-finding`, or content a current Canonical document still references
by more than a passing mention is never eligible, regardless of its own
type's terminal status.

### Rule 3 — Archive mechanism

Archiving a document means an in-tree move, not a working-tree deletion:

- Move the file verbatim (no content rewriting) from its original path to
  `docs/archive/<original-directory-under-docs>/<original-filename>` —
  for example, `docs/issues/LISS-0005-*.md` moves to
  `docs/archive/issues/LISS-0005-*.md`.
- Record one row in `docs/collaboration/restoration-ledger.md` (Rule 5)
  for every moved file, in the same commit as the move.
- Update any live inbound reference in a current Canonical document to
  point at the new `docs/archive/` path (or, preferably, at the
  restoration ledger row, when the reference was only "see the historical
  record" rather than a normative citation) — do not leave a current
  document quietly pointing at a path that no longer exists.
- Do not create a redirect stub at the old path.
- This is a deliberate, evidence-based departure from `qpex`'s own
  approach (full working-tree deletion, recovery only via `git show
  <tag>:<path>`) — chosen in the spike (Option B) because this template's
  own Prime Directive ("no human downstream will reconstruct missing
  rationale") weighs plain-file recovery friction more heavily than
  `qpex`'s own documented priorities required for its use case. Git
  history remains a second, independent recovery path in both cases; it
  is not the only one under this ADR.

### Rule 4 — Trace lifecycle (applying Rules 1-3 to work traces specifically)

The same lifecycle applies to `docs/collaboration/traces/`, with one
addition specific to traces, adapted directly from `qpex`'s own stated rule
(`/Users/nn0cl/Documents/git/qpex/docs/architecture/trace-topic-register.md`,
a different, external repository's file, quoted and endorsed by
item-0012 itself): **a
new trace is not created when the same `LISS-*`/`WP-*` topic already has a
current representative trace, and the new session found no unresolved
obligation, no new approval boundary, and no unique review evidence not
already in the representative.** In that case, update the existing
representative trace instead of adding a new file.

When a later session's trace does carry a genuinely new obligation,
boundary, or evidence item, add it as a new trace as usual — this rule
prevents duplicate restating of the same facts, not recording of new
facts. When a topic accumulates more than one trace before this rule is
applied retroactively (the normal case for this repository's own existing
history), the retroactive-application work plan designates one as
representative and archives (Rule 3) the others, recording each in the
restoration ledger with `classification: consolidated-into-representative`.

### Rule 5 — Restoration ledger

`docs/collaboration/restoration-ledger.md` is the single running record of
every archive move and trace consolidation. One Markdown table, one row
per moved-or-consolidated document, append-only (never reordered or
rewritten in place):

| Column | Meaning |
| --- | --- |
| `date` | Date the row was recorded |
| `source_path` | Original path before the move |
| `source_commit` | Full commit hash of the move |
| `source_tag` | Optional; empty/`N/A` unless the move was also marked with an annotated git tag (not required by default under this ADR, unlike `qpex`'s convention) |
| `canonical_destination` | `docs/archive/...` path, or the representative trace's path for a trace consolidation |
| `classification` | One of: `archived`, `consolidated-into-representative`, `superseded` |
| `reason` | One sentence naming the Rule 2 trigger that applied |

The ledger starts empty (header row only) as of this ADR's own work plan
(WP-0014) — it is populated only by the later retroactive-application work
plan and by ordinary ongoing archival from this point forward, never
backfilled speculatively.

### Rule 6 — Relationship to existing per-type status fields

This ADR's four-layer/five-role model is additive. It does not replace,
rename, or reinterpret any artifact type's own existing status field:
`docs/collaboration/local-issue-planning.md`'s Status Values
(`proposed | ready | in_progress | blocked | review | done | wont_do`),
each ADR's own Status section prose, `docs/backlog/README.md`'s status
flow, or a work plan's own Work-Plan-Close state. "Archived" (Rule 3) is
the one new terminal state this ADR adds, reachable only after a
document's own existing terminal status is already reached — never a
substitute for, or a way to skip, a type's own required lifecycle.

### Rule 7 — Scope boundary: rules only, no retroactive application

This ADR and its own work plan (WP-0014) create the rule set and an empty
restoration ledger. They do not move, archive, delete, or edit any
existing `docs/issues/`, `docs/work-plans/`, `docs/collaboration/traces/`,
`docs/collaboration/reviews/`, `docs/collaboration/agreements/`, or
`docs/architecture/adr/` file. Applying these rules to this repository's
own existing history (WP-0002 through WP-0012 and everything before) is a
separate, later work plan, per the Director's own sequencing decision
recorded in `docs/backlog/item-0012-document-and-log-lifecycle-management.md`'s
Promotion notes.

## Consequences

Positive:

- Gives every future document a clear, checkable answer to "is this
  current or historical, and where would its replacement live" — the gap
  item-0012 exists to close.
- The in-tree `docs/archive/` move (Rule 3) keeps recovery a plain file
  read rather than a git-archaeology exercise, preserving this
  repository's own Prime Directive more directly than `qpex`'s
  tag-and-delete approach.
- Adds no new mandatory field or process step to routine `S`-sized edits —
  the five-value vocabulary is expressed through each type's own existing
  status field plus Rule 3's archival move, not a new metadata block every
  file must carry.
- The restoration ledger (Rule 5) gives a single, append-only place to
  audit every consolidation, rather than scattering that history across
  commit messages.

Negative:

- A conservative archival trigger for ADRs (every clause must be
  explicitly superseded by name) means most ADRs will likely never become
  eligible for archival, since this template's own supersession style is
  usually partial (see ADR 0016's own precedent, superseded only specific
  clauses of ADR 0001/0014) — this is a deliberate trade favoring recovery
  safety over shrinking `docs/architecture/adr/`'s file count, and may
  need revisiting if that directory's size becomes its own problem later.
- Rule 2's per-type triggers are illustrative, not exhaustive; the
  retroactive-application work plan will encounter cases this ADR does not
  explicitly cover and must record its own judgment call for each,
  consistent with these rules' stated principles.
- This ADR alone does not yet give a later reader a way to discover it —
  facet 5's drift-prevention entry-document requirements (a later, separate
  work plan, per the spike's decomposition table) are what will surface
  Canonical-vs-Archive status at the Entry layer; until that work plan
  lands, a reader must already know to check `docs/architecture/adr/0020`
  and `docs/collaboration/restoration-ledger.md` directly.

## Enforcement

Code review should reject:

- an archive move (Rule 3) performed without a corresponding restoration
  ledger row in the same commit.
- a document moved to `docs/archive/` while a `depends_on`,
  `Type: review-finding`, or live Canonical-document reference to it is
  still open.
- a new trace file added for a topic that already has a current
  representative trace, with no unresolved obligation, new approval
  boundary, or unique review evidence named as the reason for the new
  file (Rule 4).
- any edit under this ADR's own work plan (WP-0014) that moves, archives,
  or deletes an existing repository document — out of scope per Rule 7;
  that is the retroactive-application work plan's job, not this one's.
- treating this ADR's five-value vocabulary as a required new metadata
  field on every file — it is expressed through each type's existing
  status field plus archival state, not a new mandatory block (Rule 6).
```

### File 2: `docs/collaboration/restoration-ledger.md`

```markdown
# Restoration Ledger

The single, append-only record of every document archived or consolidated
under `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
(Rules 3 and 5). Every row is added in the same commit as the archive move
or trace consolidation it records. Never reorder or rewrite an existing
row — a correction is a new row, not an edit to an old one.

This ledger starts empty. It is populated only by ordinary ongoing
archival from this point forward, and by the later, separate
retroactive-application work plan referenced in
`docs/backlog/item-0012-document-and-log-lifecycle-management.md`'s
Promotion notes — not backfilled speculatively by ADR 0020's own work plan
(WP-0014).

## How to read a row

- `date` — the date the row was recorded.
- `source_path` — the document's path before the move.
- `source_commit` — the full commit hash that performed the move.
- `source_tag` — optional; an annotated git tag, only when one was also
  created for this move (not required by default under ADR 0020).
- `canonical_destination` — the `docs/archive/...` path the document now
  lives at, or the representative trace's path for a trace consolidation
  (`classification: consolidated-into-representative`).
- `classification` — one of `archived`, `consolidated-into-representative`,
  `superseded`.
- `reason` — one sentence naming the ADR 0020 Rule 2 trigger that applied.

## Recovery

For any row, the current copy is at `canonical_destination`. As a second,
independent recovery path, the original pre-move state is also always
available from git history:

```console
git show <source_commit>^:<source_path>
```

(the parent of `source_commit`, since `source_commit` is the move itself).

## Ledger

| date | source_path | source_commit | source_tag | canonical_destination | classification | reason |
| --- | --- | --- | --- | --- | --- | --- |
| _(no entries yet — see "This ledger starts empty" above)_ | | | | | | |
```

### File 3: `docs/collaboration/local-issue-planning.md` — cross-reference paragraph

Insert this paragraph immediately after the existing `## Status Values`
section's bullet list (`proposed`/`ready`/.../`wont_do`) and before the
next `## Phase Values` heading. Do not change anything else in the file.

```markdown
This is the issue's own lifecycle status, not the same field as the
document-lifecycle role (Entry/Canonical/Evidence/Archive) and status
vocabulary `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
defines. The two are independent: an issue can be `done` long before it is
eligible for archival under ADR 0020's Rule 2.
```

### File 4: ADR-range statement updates (`README.md`, `QUICKSTART.md`, `QUICKSTART.ja.md`)

Routine maintenance `scripts/check-contract-consistency.py`'s
`check_adr_range` requires whenever a new ADR is added — apply each
exact string replacement below (old text -> new text), nowhere else in
each file:

**`README.md`** (two replacements):

1. Old: `` made. The ADRs included here (0001-0019) describe the collaboration ``
   New: `` made. The ADRs included here (0001-0020) describe the collaboration ``
   (line ~250)
2. Old: `` own decisions from 0020 up, so a later template update does not collide ``
   New: `` own decisions from 0021 up, so a later template update does not collide ``
   (line ~252)
3. Old: `` │   └── adr/                    # architecture decision records (0001-0019 = process ADRs) ``
   New: `` │   └── adr/                    # architecture decision records (0001-0020 = process ADRs) ``
   (line ~303 — not required by `check_adr_range`'s anchored patterns, since both 0001 and 0019 remain valid ADR numbers either way, but left stale would misstate the current range; fix for consistency)

**`QUICKSTART.md`** (three replacements):

1. Old: `` - `docs/architecture/adr/0001-*.md` through `0019-*.md` are the process ADRs ``
   New: `` - `docs/architecture/adr/0001-*.md` through `0020-*.md` are the process ADRs ``
   (line ~163)
2. Old: `` project numbered afterward (0020 and up). ``
   New: `` project numbered afterward (0021 and up). ``
   (line ~165)
3. Old: `` records" asserts ADRs 0001–0019. Deleting anything before trimming those ``
   New: `` records" asserts ADRs 0001–0020. Deleting anything before trimming those ``
   (line ~191)

**`QUICKSTART.ja.md`** (three replacements):

1. Old: `` - `docs/architecture/adr/0001-*.md` から `0019-*.md` までは、このテンプレー ``
   New: `` - `docs/architecture/adr/0001-*.md` から `0020-*.md` までは、このテンプレー ``
   (line ~166)
2. Old: `` その後採番した ADR（0020 以降）は残します。 ``
   New: `` その後採番した ADR（0021 以降）は残します。 ``
   (line ~168)
3. Old: `` 「Check architecture decision records」step は ADR 0001〜0019 を検査 ``
   New: `` 「Check architecture decision records」step は ADR 0001〜0020 を検査 ``
   (line ~195)

Line numbers are approximate (as of this agreement's own drafting) — match
by the exact old-text string, not by line number, since a prior edit in
the same file could shift lines.

## Specifications

- None. Documentation/process-governance change (a new ADR); no
  application specification.

## Boundaries

- `local-issue-planning.md`'s edit is an ADR-0006 contract file change —
  trace and separate-context Reviewer approval are mandatory. ADR 0020
  and the restoration ledger are not independently ADR-0006 contract
  files (ADRs and this new ledger file are outside that list — though the
  ledger, being under `docs/collaboration/*.md` and not in an excluded
  record directory, is treated as one out of caution; see Falsification
  Criteria), but both are reviewed for substantive soundness in the same
  Reviewer pass regardless.
- No move, archive, deletion, or content edit of any existing repository
  document (ADR 0020 Rule 7).
- No new `docs/archive/` directory or restoration-ledger data row created
  by this work plan.
- No edit to `CLAUDE.md` or its four mirrors.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` (in the
  Director-facing sense) until the Director's own work-plan-close action —
  this work plan stops at Reviewer approval, on the shared branch
  `process/backlog-item-0012-and-0013`, and reports readiness.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does ADR 0020 need a companion policy doc (like `cross-session-messaging.md` for ADR 0016) or a `CLAUDE.md` required-reading-list entry? | No — follows ADR 0018's own precedent (self-contained ADR, no companion doc, no `CLAUDE.md` reference; confirmed no mirror file references ADR numbers directly today) | Design & Review group (Planner) |
| Is `docs/collaboration/restoration-ledger.md` an ADR-0006 contract file? | Ambiguous by the letter of the rule (it is a `docs/collaboration/*.md` file not under `traces/`, `reviews/`, or `agreements/`) even though it is closer in spirit to a data ledger than a behavior-defining document; resolved conservatively — treat it as a contract file requiring the trace, since over-compliance carries no real cost here and the alternative risks a future Reviewer correctly flagging the omission | Design & Review group (Planner) |
| Should the restoration ledger be backfilled with any row now? | No — starts empty; population is the later retroactive-application work plan's job, per the Director's own sequencing decision | Design & Review group (Planner), directly from item-0012's Promotion notes |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Will ADR 0020's Rule 2 per-type consolidation triggers need refinement? | Settled once the later retroactive-application work plan actually applies them to this repository's own real documents and finds cases the current wording does not clearly cover |
| Should ADRs' conservative archival trigger (every clause explicitly superseded) be loosened later? | Only if `docs/architecture/adr/`'s growing file count becomes its own readability problem — not assumed now |

## Verification

- `scripts/check-contract-consistency.py`.
- Read-through diff confirming all three files/edits match "Exact Content
  to Produce" verbatim, and that no other repository file changed.
- Work-plan-level Reviewer approval, separate context — including
  substantive review of the ADR's reasoning, not only mechanical
  transcription accuracy.

## Falsification Criteria

- Any existing repository document (outside the one named
  `local-issue-planning.md` paragraph) is moved, archived, deleted, or
  content-edited by this work plan.
- The restoration ledger's Ledger table contains a data row.
- ADR 0020's content diverges from "Exact Content to Produce" above in a
  way that changes its substance (not just whitespace).
- `CLAUDE.md` or a mirror file is edited.
- No AI work trace is recorded for this contract-file-touching work plan.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0012-document-and-log-lifecycle-management.md`,
      `Status: promoted`, Promotion notes, per ADR 0016 Rule 2.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Made fresh by the Design & Review group
      against this actual plan and the spike result above.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
