# Spike Case: case-0001-document-log-lifecycle-management

## Metadata

- Case ID: case-0001
- Title: Document and log lifecycle management — taxonomy mapping and
  restoration-ledger design
- Status: closed
- Created: 2026-08-19
- Closed: 2026-08-19
- Owner/agent: Design & Review group (Planner), standing session
- Related work plan: none yet — this spike's own "Next action" opens the
  first one (see below)
- Related local issue (LISS): none yet
- Related backlog item: `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
- Supersedes case: none
- Superseded by case: none

## Question

Does `qpex`'s four-layer document model (Entry/Canonical/Evidence/Archive)
map cleanly onto this template's existing five-artifact-type structure
(ADR/Issue/Work-Plan/Trace/Review), or does this template need its own
taxonomy — and what storage location and field format should the
restoration ledger use?

## Why a spike (not immediate implementation)

item-0012 explicitly names this a required-first spike ("read the four
`qpex` files... in full before designing this template's own version") and
explicitly warns against adopting `qpex`'s specifics wholesale without
independent verification ("Do not treat `qpex`'s own files as
authoritative for this template — they are one adopter's implementation of
a similar idea"). The right taxonomy and ledger design are not obvious
without first comparing this template's actual current structure against
what `qpex` actually built and why.

## Constraints

- Must remain free of mandatory paid spend unless justified below: yes —
  trivially; this is a documentation/process design question, no tooling
  cost.
- Architecture / port boundaries to respect: none — no application
  architecture is touched by this spike or its resulting facet 1/2 work
  plan; this is process-document design only.
- Out of scope for this spike: retroactive application to this
  repository's own existing history (WP-0002 through WP-0012 and
  everything before) — settled by the Director at item-0012's promotion as
  a separate, later work plan (see item-0012's own Promotion notes). Also
  out of scope: facets 4 (contract-sync diff record), 5 (drift-prevention
  CI), and 6 (review-summary packets) in detail — this spike closes only
  the taxonomy-mapping and restoration-ledger question that facets 1-3
  depend on; facets 4-6 are sequenced as later, separate work plans (see
  "Next action" below) and get their own design intake when reached.

## Candidates

Not a vendor/library selection — the "candidates" are three possible
design postures for adapting `qpex`'s proposal to this template.

| ID | Option | Source | Notes |
| --- | --- | --- | --- |
| A | Adopt `qpex`'s model directly: four layers as a new document-role classification, PLUS `qpex`'s aggressive canonicalization mechanics (delete accepted-ADR bodies into `DEC-*` theme documents backed only by baseline-tag/commit recovery; replace per-issue/per-work-plan status tracking with one consolidated open-work register) | `qpex` WP-0090, WP-0091 | Solves a problem `qpex` had (186 ADRs, "one large ADR/Issue/WP record per decision slice") that this template does not have to the same degree |
| B | Adapt: keep this template's existing five artifact types (ADR/Issue/Work-Plan/Trace/Review) and their current per-type governance fully intact; layer the four-layer *role* classification on top as a `status` field per file (`draft \| active \| canonical \| superseded \| archived`), add the one mechanism this template genuinely lacks — an Archive layer and a restoration ledger — without mandatory theme-document consolidation or a single open-work register | This spike's own comparison, below | Targets this template's actual gap (no Archive mechanism at all) without importing `qpex`'s aggressive compaction, which solves a different-shaped problem |
| C | Design independently: build a lifecycle model from this template's own observed pain points (item-0012's own "40+ issues, a dozen review records, a dozen traces, a dozen work plans in about a day") without using `qpex`'s four-layer terminology or status vocabulary at all | — | Discards evidence item-0012 explicitly asks to read and reason from; more design work for no clear benefit over adapting a working precedent |

## Evaluation criteria

| Criterion | Why it matters | How measured |
| --- | --- | --- |
| Fit to this template's current artifact count and structure | `qpex`'s mechanics were sized for its own scale/history; adopting them wholesale risks solving a problem this template doesn't have while adding process overhead it does not need | Compare ADR/Issue/WP/Trace counts and existing consolidation checkpoints (ADR 0014, ADR 0016) between the two repositories |
| Preserves Invariant 1 ("every decision produces a document") and this template's existing recovery model | Any lifecycle rule that makes past decisions harder to find without replaying a chat session violates this template's own Prime Directive | Compare recovery friction: `git show <tag>:<path>` (qpex, tree deletion) vs. a file still present under `docs/archive/` (in-tree move) |
| Closes the two questions item-0012's own Uncertainty section names | The spike's job is exactly these two questions, not a general redesign | Direct answer recorded in Selection below |
| Minimizes new process weight for an S/M-sized future edit | This template already has ADR 0015 (review-cost discipline) warning against unnecessary process overhead | Count new mandatory steps each option adds to routine document edits |

## Research log

| Date | Query or source | Finding | URL |
| --- | --- | --- | --- |
| 2026-08-19 | `/Users/nn0cl/Documents/git/qpex/docs/work-plans/WP-0090-documentation-canonicalization.md` | Four-layer model (Entry/Canonical decision/Canonical open-work/Evidence/git-history-as-archive) proposed under an Adjudicator-approved "documentation-only compaction" work plan. Explicitly allows deleting Issue/Work-Plan/Trace files from the working tree once a compression-map row records `source_path, source_commit, source_tag, destination, classification, reason`. Recovery is `git show <tag>:<path>` only — nothing stays in the working tree. | local file, read in full |
| 2026-08-19 | `/Users/nn0cl/Documents/git/qpex/docs/work-plans/WP-0091-decision-theme-canonicalization.md` | Completed follow-on: 185 of 186 ADR files were deleted from the working tree entirely, replaced by 7 `DEC-*` theme documents plus a `decision-theme-register.md`. This is the aggressive end of the model — collapsing many historical decision records into few current ones, git-history-only recovery. | local file, read in full |
| 2026-08-19 | `/Users/nn0cl/Documents/git/qpex/docs/architecture/trace-topic-register.md` | One representative trace per `LISS-*`/`WP-*` topic; other same-topic traces deleted from the tree, listed in the register's "Consolidated source paths" column, recoverable only via the same baseline-tag mechanism. States the reuse rule directly: "A new phase trace is not added when the same topic already has a current representative... Update the representative... instead." | local file, read in full |
| 2026-08-19 | `/Users/nn0cl/Documents/git/qpex/docs/collaboration/doc-audit-2026-07-23.md` | A drift audit, not a lifecycle-model document itself — but useful evidence of the underlying problem the lifecycle model was built to solve: stale terminology (`observe` vs `measure`, `span` vs `when`) surviving in old ADRs and examples that a skimming agent could pick up as current. This is the concrete failure mode facet 5 (drift-prevention CI checks) targets. | local file, read in full |
| 2026-08-19 | This template's own `docs/architecture/adr/` directory listing | 19 ADR files (`0001`-`0019`), each already scoped to one cohesive decision (not `qpex`'s pre-WP-0091 "186 ADRs, one per decision slice" problem). `docs/collaboration/design-agreement.md`, ADR 0014, and ADR 0016 already provide per-work-plan and per-item consolidation checkpoints `qpex` apparently lacked before WP-0090/0091. | `ls docs/architecture/adr/` |
| 2026-08-19 | This template's own `docs/collaboration/` directory | No existing Archive mechanism, status vocabulary, or restoration ledger anywhere. `docs/collaboration/findings-reuse.md` and `docs/collaboration/post-hoc-audit.md` assume documents remain readable in place indefinitely; neither states a consolidation or removal condition. Confirms item-0012's own diagnosis: the gap is real and is specifically the Archive layer and status vocabulary, not the whole four-layer idea. | repository read |

## Comparison

| Criterion | A (adopt directly) | B (adapt) | C (independent) |
| --- | --- | --- | --- |
| Fit to current scale/structure | Poor — solves a 186-ADR-scale duplication problem this template's 19 ADRs do not exhibit; would force consolidation this template doesn't need yet | Good — targets exactly the missing Archive/status/ledger mechanism, leaves the already-working five-type structure alone | Good on paper, but re-derives ground `qpex`'s evidence already covers |
| Recovery friction | High — `git show <tag>:<path>` only, no in-tree fallback | Low — archived files stay readable under `docs/archive/`, git history is a second line of defense, not the only one | Depends entirely on what gets designed — unconstrained |
| Preserves Invariant 1 spirit | Weaker — 185 ADR bodies are only reachable through a tag+commit lookup a future human/agent must already know to run | Stronger — the same "every decision produces a document" property holds, with the document just relocated, not removed | Depends on design |
| New process weight for routine S-sized edits | High — theme-document consolidation, register rewriting on every ADR acceptance | Low — a `status` field and, only past a stated consolidation trigger, an archive move + ledger row | Unknown until designed |
| Uses item-0012's own required evidence | Uses it, arguably over-literally (adopts scale-specific mechanics wholesale, which item-0012 explicitly warns against) | Uses it as evidence and precedent while adapting to actual fit | Discards it |

## Cost and quality judgment

- Free / zero-mandatory-spend options considered: all three; none has a
  cost dimension (documentation/process design only).
- Quality bar applied: does the option close the named uncertainty, fit
  this template's actual current scale, and preserve the Prime Directive's
  documentation/evidence invariants at least as well as no lifecycle model
  at all?
- No paid option is in play; not applicable.

## Selection

- Selected: B (adapt)
- Rationale: This template's existing five-artifact-type structure
  (ADR/Issue/Work-Plan/Trace/Review) already has clear, distinct roles and
  is at a scale (19 ADRs, work-plan-scoped self-review per ADR 0014,
  backlog-gated autonomy per ADR 0016) that does not exhibit the
  duplication problem `qpex`'s WP-0090/0091 were built to fix. The actual
  gap, confirmed by directly inspecting this template's own
  `docs/collaboration/` directory, is narrower and specific: **there is no
  Archive layer, no document-status vocabulary, and no restoration-ledger
  mechanism at all** — not that the existing five types are wrong or need
  replacing. Mapping decision:
  - **Entry** — already exists in substance: `docs/architecture/agent-quickstart.md`,
    `CLAUDE.md`/mirrors, `README.md`. No new document type needed; facet 5's
    entry-document requirements (Current/Historical distinction, canonical
    list, terminology migration table, standard reading order) are an
    *addition to* these existing files, not a new layer.
  - **Canonical** — maps to `Accepted` ADRs, `active`/`in_progress` work
    plans and issues, and current `docs/collaboration/*.md` contract
    files. This template does **not** adopt `qpex`'s mandatory `DEC-*`
    theme-document consolidation — an ADR stays the canonical record for
    its own decision; a *future*, explicitly optional theme-consolidation
    step remains available per-theme if a specific theme's ADR count ever
    grows large enough to warrant it, but is not built now and is not
    required by this work plan.
  - **Evidence** — maps to review records (`docs/collaboration/reviews/`),
    traces (`docs/collaboration/traces/`), and self-review records already
    embedded in issue Work Notes. No new type needed; facet 3's
    "one representative trace per topic" rule refines *how many* trace
    files accumulate per topic, not what a trace is.
  - **Archive** — genuinely new. Recommended mechanism: a `status: archived`
    value (see the new status vocabulary work plan, next) plus an in-tree
    move to `docs/archive/<original-type-dir>/<original-filename>`
    (mirroring the source directory structure under `docs/archive/`),
    **not** working-tree deletion relying only on `git show <tag>:<path>`.
    This keeps `qpex`'s "off the normal reading path, but restorable"
    property (item-0012's own Layer table wording) while keeping recovery
    a plain file read instead of a git-archaeology exercise — a
    deliberate, evidence-based departure from `qpex`'s more aggressive
    delete-and-tag approach, chosen because this template's Prime
    Directive ("no human downstream will reconstruct missing rationale")
    weighs recovery friction more heavily than `qpex`'s own documented
    priorities did. Full working-tree deletion (git-history-only recovery)
    remains available as a *later*, separate, more aggressive option if a
    future ADR wants it — not adopted by default here.
- Discard reasons:
  - A (adopt directly): imports scale-specific mechanics (mass ADR
    deletion, single open-work register) this template's own inspected
    state does not need, and increases recovery friction in a way that
    cuts against this repository's own Prime Directive more than `qpex`'s
    priorities required for its own use case.
  - C (independent): would discard the concrete, already-battle-tested
    evidence item-0012 explicitly directs this spike to read, for no
    demonstrated benefit — the actual gap-analysis in Option B already
    derives a template-appropriate answer from that evidence rather than
    from `qpex`'s exact mechanics.

### Restoration ledger — location and format

- **Location**: `docs/collaboration/restoration-ledger.md` — a single,
  append-only running ledger, consistent with this template's existing
  convention of one canonical process-meta file per concern under
  `docs/collaboration/` (parallel to `findings-reuse.md`,
  `post-hoc-audit.md`). Mirrors `qpex`'s single
  `documentation-compression-map.md` file, adapted to this template's
  naming convention.
- **Format**: one Markdown table, one row per archived-or-consolidated
  record, columns exactly matching item-0012's own stated schema (already
  specified by the item, not an open design question):
  `source_path, source_commit, source_tag, canonical_destination,
  classification, reason`, plus one column this template's own convention
  adds: `date` (the date the row was recorded — every other collaboration
  record in this template dates its entries; the ledger should not be the
  exception).
- `classification` values: reuse the status vocabulary's own terms
  (`superseded`, `archived`) rather than inventing a parallel vocabulary —
  settled as part of the status-vocabulary work plan below, not
  re-litigated per row.
- `source_tag`: optional per row (only used when a row corresponds to a
  deliberate baseline tag, which this template does not require by
  default under Option B — most rows will have a `source_commit` and an
  empty/`N/A` `source_tag`, since routine archive moves do not need a new
  annotated tag each time under the in-tree-move design).

## Evidence

- `/Users/nn0cl/Documents/git/qpex/docs/work-plans/WP-0090-documentation-canonicalization.md`
- `/Users/nn0cl/Documents/git/qpex/docs/work-plans/WP-0091-decision-theme-canonicalization.md`
- `/Users/nn0cl/Documents/git/qpex/docs/architecture/trace-topic-register.md`
- `/Users/nn0cl/Documents/git/qpex/docs/collaboration/doc-audit-2026-07-23.md`
- This template's own `docs/architecture/adr/` (19 files) and
  `docs/collaboration/` directory listings, read directly as part of the
  comparison (not assumed).

## Next action (exactly one)

- [x] Open or update an ADR — **ADR 0020: Document and Log Lifecycle
      Model** (four-layer role classification adapted per Option B above,
      status vocabulary, consolidation trigger conditions, and the
      restoration ledger format/location settled above), to be produced
      by the first facet work plan below.

### Decomposition and sequencing for the remaining facets (Design & Review's own judgment, per item-0012's explicit delegation)

Recorded here as the durable record of this spike's own scope boundary
(facets 4-6 are named but not designed by this spike) and as the sequencing
this spike's Selection depends on being read in order:

| Work plan (working title) | Facets covered | Depends on | Rationale |
| --- | --- | --- | --- |
| WP-0014 (next) — Document/Log Lifecycle Model | 1 (four-layer model), 2 (status vocabulary + consolidation rules + restoration ledger), 3 (trace lifecycle — directly reuses facet 1/2's status vocabulary and ledger, no independent design needed) | This spike (case-0001) | The architectural root every other facet depends on; produces ADR 0020 |
| WP-001x — Contract-sync diff record | 4 (Template-owned vs Target-owned split; diff-record sync replacing literal-mirror-sync for non-shared-rule content) | WP-0014 (uses its status vocabulary for "adopt/reject/defer" framing, though the diff-record mechanism itself is otherwise independent) | Changes ADR 0006's mirror-sync mechanics — needs its own ADR; distinct enough concern (multi-agent-tool contract sync, not document archival) to stay a separate work plan |
| WP-001x — Drift-prevention entry documents and CI checks | 5 (entry-document requirements; CI checks for retired terminology, Archive-from-Entry references, single-canonical-per-theme, source/evidence links) | WP-0014 (status vocabulary and canonical/Archive definitions are preconditions for writing these checks) | Implementation-heavy (extends `scripts/check-contract-consistency.py`'s existing `check_issue_status_sync`, per item-0012's own explicit "note the overlap, don't rebuild" instruction) — natural Implementation-group work once the model exists |
| WP-001x — Review-summary packets | 6 (Reviewer input packet: scope/canonical docs/changed files/findings/disposition/blockers/verification/next approval) | WP-0014 (packet's "current canonical documents" field needs the canonical/status vocabulary to mean something) | Small, self-contained template addition; lowest risk, could run concurrently with the CI-checks work plan once WP-0014 closes |

This table is a sequencing record, not a commitment to exact WP numbers —
each later work plan confirms its own true next-free number via
`git log --all` at the time it is actually opened, per this session's
standing mandate.
