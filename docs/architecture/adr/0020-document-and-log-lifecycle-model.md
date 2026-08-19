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
addition specific to traces, adapted directly from `qpex`'s own stated
rule — a file named trace-topic-register.md in a different, external
repository, not part of this template (full citation in
`docs/spike/case-0001-document-log-lifecycle-management/case.md`'s
Research Log), quoted and endorsed by item-0012 itself: **a
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
