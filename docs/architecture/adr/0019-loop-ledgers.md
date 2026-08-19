# ADR 0019: Loop Ledgers

## Status

Accepted. Covered by
`docs/collaboration/agreements/2026-08-19-adr-loop-ledgers.md`
(`DA-2026-08-19-02`). This ADR is additive: it supersedes nothing in ADR
0012-0015 or ADR 0016-0018. Follow-up issue: LISS-0038
(`docs/work-plans/WP-0010-adr-loop-ledgers.md`).

`Accepted` status requires a design agreement with the Director covering the
decision. That agreement is `DA-2026-08-19-02`, whose Direction section rests
on `docs/backlog/item-0002-adr-loop-ledgers.md` (`Status: promoted`).

## Context

Five docs-first process rules already govern this loop in practice — spike
cases, backlog promotion, loop-settings, post-hoc audit, and the
findings-must-apply rule — and each already has its own accepted
collaboration document. None of the five was ever recorded as an ADR: they
exist as collaboration-document policy that `CLAUDE.md` and
`docs/architecture/agent-quickstart.md` point at directly, with no single
architecture decision record an adopter can cite to say "these five rules,
together, are the accepted shape of this repository's ledger system." That
gap makes it harder to reference the ledger system as one settled decision,
and harder for a later reader auditing `docs/architecture/adr/` to see that
the five documents were deliberately adopted as a unit rather than accreting
independently.

## Dependency Adoption Evidence

Not applicable. This decision selects no library, framework package,
provider SDK, datastore client, build tool, or test helper. It formalizes,
as one accepted architecture decision, five collaboration documents already
in force in this repository.

## Decision

The following five ledgers are accepted as one unified process decision.
Each ledger's own document remains the sole source of truth for its
operational detail; this ADR states that the five are adopted together and
does not restate or duplicate that detail, so that a future edit to any one
document's operational rules does not require a matching edit here.

1. **Spike ledger** — `docs/spike/README.md`. Governs how uncertainty is
   closed through investigation before a specification or ADR is written:
   one `docs/spike/case-NNNN-short-slug/` directory per question, a
   free-by-default/quality-required selection policy, and a closing rule
   that a spike's recommendation still needs its own ADR or spec path
   before it counts as settled. See the source document for numbering,
   allowed/forbidden work, and status values.

2. **Backlog ledger** — `docs/backlog/README.md`. Governs candidates that
   are not yet promised under a design agreement: one
   `docs/backlog/item-NNNN-*.md` per candidate, a status
   vocabulary (`captured` through `dropped`), and the rule that no
   Red/Green/Refactor execution starts against a backlog item until it is
   promoted into a covering design agreement and work plan. See the source
   document for the full status table and its relationship to spikes and
   issues.

3. **Loop-settings ledger** — `docs/collaboration/loop-settings.md`.
   Governs the target-owned `docs/collaboration/loop-settings.toml` file:
   how it is created and refreshed
   (`scripts/init-loop-settings.sh`), and the `[docs].language`,
   `[audit]`, `[findings]`, and `[selection]` sections every agent session
   reads before design intake or implementation. See the source document
   for the full section reference.

4. **Post-hoc audit ledger** — `docs/collaboration/post-hoc-audit.md`.
   Governs what a later reader — human or agent, without access to the
   original session — must be able to reconstruct from repository
   artifacts alone: what was agreed, what changed, what was verified with
   command output, what was rejected, and what remains open. See the
   source document for the minimum artifact set and the rules for later
   human confirmation.

5. **Findings-must-apply ledger** — `docs/collaboration/findings-reuse.md`.
   Governs that every actionable Reviewer finding becomes a durable
   `docs/issues/LISS-*.md` entry with `Type: review-finding` that is
   applied or explicitly declined with Arbiter grounds, never left as a
   session aside. Its lifecycle authority is ADR 0012, which this document
   cites rather than restates. See the source document for the full
   must-apply rule, design/build-time reuse steps, and applied-evidence
   table.

This ADR supersedes nothing in ADR 0012-0015 or ADR 0016-0018. Their subject
matter does not overlap this one's: ADR 0012 governs the review-finding
*lifecycle* (`proposed -> accepted -> in_progress -> resolved -> closed`),
which the findings-must-apply ledger above cites as its lifecycle authority
rather than restating; ADR 0013-0015 govern Preflight validation and review
cost discipline; ADR 0016-0018 govern session topology, portability, and
quality-gate hooks. None of those states the five ledger rules this ADR
formalizes, and this ADR does not reword or narrow any of them.

## Consequences

Positive:

- A later reader or adopter can cite one ADR for "this repository's ledger
  system is an accepted, deliberate decision" instead of inferring it from
  five independently-referenced collaboration documents with no unifying
  record.
- Each ledger's operational detail stays owned by its single source
  document, so this ADR does not go stale when that document's own rules
  change — the same pattern ADR 0016 already uses for
  `docs/collaboration/cross-session-messaging.md`.
- No existing ADR needs rewording: this ADR only names an already-accepted
  set of collaboration documents as one architecture decision.

Negative:

- A reader who wants full operational detail for any one ledger still has
  to follow the pointer to that ledger's own document; this ADR is a
  pointer layer, not a self-contained reference.
- Adding a sixth ledger later requires either amending this ADR or writing
  a new one and stating the relationship explicitly — this ADR does not
  itself define how the set grows.

## Enforcement

Code review should reject:

- a change to this ADR that restates a ledger's operational content
  (numbering schemes, status vocabularies, section field lists) instead of
  pointing at the source document, creating a second copy that can drift.
- a claim that this ADR supersedes or reworks any rule in ADR 0012-0015 or
  ADR 0016-0018.
- treating this ADR's `Accepted` status as authorizing a change to any of
  the five source documents' own content — that requires its own design
  agreement and, for `CLAUDE.md`-adjacent contract files, the separate
  process in `docs/collaboration/prompt-instruction-change-control.md`.
