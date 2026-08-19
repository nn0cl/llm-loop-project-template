# Backlog item: item-0012-document-and-log-lifecycle-management

## Metadata

- Item ID: item-0012
- Title: Document and log lifecycle management — Entry/Canonical/Evidence/
  Archive layering, consolidation rules, and review-summary packets
- Status: promoted
- Created: 2026-08-19
- Updated: 2026-08-19
- Priority hint: high
- Suggested planning size: XL
- Owner/agent (optional): unassigned

## Summary

External feedback from an adopting project (`qpex`, a separate local
repository at `/Users/nn0cl/Documents/git/qpex`), relayed by the Director.
The core observation: this template's growing volume of documents and logs
(ADRs, issues, work plans, traces, review records, backlog items) is not
itself the problem — the problem is that no record currently states, for
itself: is this current or historical; when can it be consolidated or
compressed; which document should its content move to; how can the
original record be restored. The proposal is to give documents and logs an
explicit **lifecycle**, not simply to write fewer of them.

`qpex` has already implemented parts of this and offers concrete artifacts
as evidence:
`/Users/nn0cl/Documents/git/qpex/docs/work-plans/WP-0090-documentation-canonicalization.md`,
`/Users/nn0cl/Documents/git/qpex/docs/work-plans/WP-0091-decision-theme-canonicalization.md`,
`/Users/nn0cl/Documents/git/qpex/docs/architecture/trace-topic-register.md`,
`/Users/nn0cl/Documents/git/qpex/docs/collaboration/doc-audit-2026-07-23.md`.
These are a different repository's files, outside this one — read them as
supporting evidence when planning, don't assume this template's own
structure already matches them.

### Six proposed facets (the Director's own framing; Design & Review may
regroup these into however many work plans it judges appropriate — this is
one cohesive proposal, not six independent ones)

**1. Four-layer document model.**

| Layer | Role | Principle |
|---|---|---|
| Entry | First thing a developer reads | Kept small and fixed |
| Canonical | Current spec, decisions, open work | One per theme |
| Evidence | Grounds for decisions, review results | Only what current decisions actually need |
| Archive | Completed / superseded / historical | Off the normal reading path, but restorable |

Governing rule (quoted from the proposal): content with current meaning
lives in exactly one Canonical document — the same current-state fact
should not be duplicated across an ADR, an issue, a work plan, and a trace.

**2. Explicit document status vocabulary and consolidation conditions.**
`draft | active | canonical | superseded | archived`. Example consolidation
triggers: a decided ADR gets summarized into a Decision Theme document,
original moves to Archive; a closed issue keeps only its result in an Open
Work Register, detail moves to history; a closed work plan compresses once
there is no further action; a trace with no unresolved decision, approval,
or reproduction step merges into a representative record; duplicate
documents get one designated canonical, others become merge targets.
Deletion/move requires a restoration ledger entry:
`source_path, source_commit, source_tag, canonical_destination,
classification, reason` — the working tree shrinks, but everything stays
recoverable from git history.

**3. Apply the same lifecycle to work traces.** One representative trace
per topic/issue/work-plan; duplicate traces get merged into it; the
consolidation ledger records the merged-from paths; a new trace is not
created when a representative one already exists and the new session found
no unresolved obligation, no new approval boundary, and no unique review
evidence — the existing representative trace gets updated instead. A trace
should never be a verbatim chat transcript; it should keep only: what was
decided, why, what was verified, what remains unresolved, what happens
next.

**4. Single-source multi-agent contract sync.** Split rules explicitly into
Template-owned (shared path/phase/review/sync/logging conventions) versus
Target-owned (adopter-specific language/domain/architecture/ADRs). Syncing
should not mean "make every mirror file textually identical" — it should
produce a diff record naming: the template's own change, the target's own
change, any conflict, and the adopt/reject/defer decision for each. Where
per-agent-tool differences are intentional (this template's own
`CLAUDE.md` vs `AGENTS.md` already have some), record which rule applies to
which agent in a canonical document rather than treating the difference as
an error.

**5. Prevent spec drift from stale documents.** Entry documents should
always show: the Current/Historical distinction, which documents are
canonical, an old-to-new terminology migration table, the standard agent
reading order, and which areas must not be entered from an old ADR
directly. Proposed deterministic (CI) checks: no retired terminology
remains in current documents; no Archive document is referenced from an
Entry document; no more than one document claims to be "current" for the
same theme; issue status and its owning work plan's status agree (this
template already has this one, per item-0009/WP-0007's
`check_issue_status_sync` — note the overlap explicitly during planning,
don't rebuild it); every Canonical document carries a source/evidence link.

**6. Review records as summary packets.** Making a Reviewer read every
trace raises cognitive load. Give the Reviewer, as the canonical review
input, only a small packet: `scope, current canonical documents, changed
files, findings, disposition, remaining blockers, verification result,
next approval required`. Detailed traces are linked as evidence, not used
as the review's entry point.

## Why it might matter

This template's own repository, over the course of item-0004 through
item-0011 in this same session, produced 40+ new local issues, a dozen
review records, a dozen AI work traces, and a dozen work plans in about a
day — direct, first-party evidence that the growth pattern this feedback
warns about is real and already happening here, not just in `qpex`. Without
an explicit lifecycle, a later reader (human or agent) has no way to tell
which of two similarly-named review records is the one that matters now, or
whether an old ADR is safe to read as a starting point.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes — this is a documents/
  process convention change, no new paid tooling implied.
- Boundaries or non-goals:
  - Facet 5's issue-status-sync CI check already exists
    (`check_issue_status_sync`, item-0009/WP-0007) — extend or reuse it,
    don't duplicate.
  - Facet 1's four-layer model and facet 2's status vocabulary are a
    structural change to how `docs/architecture/adr/`, `docs/issues/`,
    `docs/work-plans/`, `docs/collaboration/traces/`, and
    `docs/collaboration/reviews/` relate to each other — this is squarely
    Architecture Path work and will likely need its own ADR, given the
    precedent this repository already set with ADR 0016/0019.
  - Do not treat `qpex`'s own files as authoritative for this template —
    they are one adopter's implementation of a similar idea; verify the
    proposal's reasoning independently before adopting its specifics
    wholesale.
  - This item is large (XL) by this repo's own sizing criteria
    (architecture boundaries, multiple dependent facets, meaningful
    uncertainty) — expect Design & Review to decompose it into several
    work plans rather than one, and to treat facet ordering/sequencing as
    its own judgment call.

## Uncertainty

- [ ] Spec can be written now
- [x] Spike required first (options, feasibility, or quality unknown) —
      read the four `qpex` files cited above in full before designing
      this template's own version; decide whether the four-layer model
      maps cleanly onto this template's existing five-artifact-type
      structure (ADR/issue/work-plan/trace/review) or needs its own
      taxonomy; decide the restoration-ledger's storage location and
      format.
- [x] Human decision required (value, policy, budget, legal) — **settled**
      at promotion time: sequence this as two separate work plans, not
      one. First, design and land the lifecycle rules themselves (the
      four-layer model, status vocabulary, consolidation conditions,
      restoration ledger format, trace-lifecycle rules, contract-sync diff
      record, drift-prevention CI checks, review-summary-packet template)
      as a complete document/spec, with no retroactive work performed yet.
      Only after that rule-set is Director-closed does a second,
      independent work plan apply it retroactively to this repository's
      own existing history (today's WP-0002 through WP-0012 and everything
      before). Do not blend rule-definition and retroactive application
      into one work plan.

## Links

- Spike case: none yet
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: none yet — related: `docs/collaboration/findings-reuse.md`,
  `docs/collaboration/design-review-perspectives.md` (item-0006),
  `docs/collaboration/post-hoc-audit.md`,
  `scripts/check-contract-consistency.py`'s `check_issue_status_sync`
  (item-0009); external reference (different repository, read-only
  evidence, not part of this template):
  `/Users/nn0cl/Documents/git/qpex/docs/work-plans/WP-0090-documentation-canonicalization.md`,
  `/Users/nn0cl/Documents/git/qpex/docs/work-plans/WP-0091-decision-theme-canonicalization.md`,
  `/Users/nn0cl/Documents/git/qpex/docs/architecture/trace-topic-register.md`,
  `/Users/nn0cl/Documents/git/qpex/docs/collaboration/doc-audit-2026-07-23.md`

## Promotion notes

- Date: 2026-08-19
- Decision: Promoted, in the Backlog-layer thread. The Director explicitly
  settled the retroactive-application question at promotion time (see
  Uncertainty above): "ドキュメントとして完成させた後に本プロジェクトへの
  適用WPを実行する" — build and close the lifecycle rules as their own
  work plan first; retroactive application to this repository's own
  history is a distinct, later work plan, not bundled into the first. Per
  ADR 0016 Rule 2, Design & Review proceeds autonomously from here on
  everything else (facet decomposition, sequencing within Phase 1,
  taxonomy mapping onto this template's existing artifact types, spike
  execution against the cited `qpex` files).
- Reason: XL-sized, multi-facet proposal with one Director-settled
  sequencing constraint; ready to run under that constraint.
