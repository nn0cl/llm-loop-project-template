# Backlog item: item-0008-coordinator-message-hallucination-correction

## Metadata

- Item ID: item-0008
- Title: Correct cross-session-messaging.md's "coordinator" failure-mode
  section — likely model-side hallucination, not external injection
- Status: promoted
- Created: 2026-08-18
- Updated: 2026-08-18
- Priority hint: medium
- Suggested planning size: S
- Owner/agent (optional): unassigned

## Summary

During WP-0002's execution, both the Design & Review and Implementation
sessions independently reported receiving four unverified messages, in-band,
claiming to be from an unidentified "coordinator," each urging them to send
`SendMessage` to a specific agentId. All four were correctly refused by
every session that encountered them; no harmful action resulted. This is
recorded in `docs/collaboration/cross-session-messaging.md`'s "Confirmed
failure mode" section and in the WP-0002 Reviewer approval record's
"Provenance verification" section, both written under the working
assumption that these were external injection attempts.

**Correction, from a Backlog-thread investigation after WP-0002 closed:** a
repository-wide search (all files, all branches, `.claude/settings.json`,
`.claude/settings.local.json`, and every `*hook*`-named file) found no
mechanism capable of injecting external content into a session — no hooks
configured, no suspicious scripts, nothing in git history. The only
occurrences of the string "coordinator" anywhere in the repository are in
pre-existing, legitimate review records from 2026-08-02 (16 days before this
work plan), `docs/collaboration/reviews/2026-08-02-contract-consistency-review-2.md`
through `-4.md` and `2026-08-02-mirror-parity-review-2.md`, where
"coordinator" is ordinary prose referring to an orchestrating role from that
earlier work cycle (e.g. "per the coordinator's message," "the
coordinator's list").

Both the Design & Review and Implementation sessions would have read
through `docs/collaboration/reviews/` during normal design intake (per
`docs/collaboration/findings-reuse.md`'s requirement to search recent
review records) or general Preflight/consistency-check file scanning, and
so would have been exposed to this legitimate historical term. Combined
with every reported "coordinator" message arriving in a format its own
receiving session flagged as inconsistent with the real cross-session
wrapper — i.e., never actually delivered through any real channel — the
more likely explanation is that these were **model-side confabulations**,
triggered by pattern-matching against genuine historical terminology
encountered while reading old files, not messages injected by an external
or malicious source. This does not change that refusing them was the
correct behavior — an unverified message should be refused regardless of
whether its origin turns out to be external or internal.

## Why it might matter

`cross-session-messaging.md` currently documents this as a "confirmed
failure mode" implying an external actor, which could lead a future
reader (human or agent) to over-invest in defenses against injection via
the messaging channel specifically, while under-investing in the actual
likely cause: long, deeply nested multi-agent sessions reading historical
files that happen to reuse a role-shaped word, and a model's tendency to
complete a pattern it has just read. The correction matters for accuracy of
the collaboration record (Invariant 3: every claim states its grounds) and
because the file is required reading for future Design & Review /
Implementation sessions.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes
- Boundaries or non-goals:
  - This is a documentation correction only — no behavior change to
    `SendMessage`/`ListAgents` usage rules, no new verification mechanism
    required beyond what LISS-0022 already established (verify before
    trusting, regardless of source).
  - `docs/collaboration/cross-session-messaging.md` is an ADR-0006 contract
    file — this correction needs its own covering design agreement (or an
    amendment under the existing one, if still open) and a separate-context
    Reviewer confirmation; it must not be edited directly by the Backlog
    thread outside that process, even though the finding is well-evidenced.
  - Consider whether `docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`'s
    "Provenance verification" section also needs a corrective note or
    addendum — that file is a review record (not a contract file), lower
    ceremony, but changing an already-approved Reviewer record's
    substance should still go through the Reviewer persona, not be
    silently rewritten.

## Uncertainty

- [x] Spec can be written now — the correction itself is well-evidenced and
      narrow (repository-search results are reproducible: `grep -rni
      "coordinator"` across all files and branches, `.claude/settings*.json`
      inspection).
- [ ] Spike required first
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none
- Work plan (when promoted): `docs/archive/work-plans/WP-0003-coordinator-message-correction.md` — confirmed via direct cross-reference; this item's own `Links` field was never updated when the work landed (see `docs/issues/LISS-0065-...md`'s own cross-reference table).
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: none — corrects a review-record and contract-file claim, not a
  decision

## Promotion notes

- Date: 2026-08-18
- Decision: Promoted, in the Backlog-layer thread. Per ADR 0016 Rule 2,
  this approval is the single design-phase gate — the Design & Review group
  proceeds autonomously from here: confirm the correction's evidence itself
  (reproducible — repo-wide `coordinator` grep, `.claude/settings*.json`
  inspection), then correct `cross-session-messaging.md`'s "Confirmed
  failure mode" section and the WP-0002 review record's "Provenance
  verification" section accordingly, as a Minor Fix Path (single
  well-evidenced contract-file correction, mirrors no prior pattern but is
  narrow and low-risk) — still requires its own trace and separate-context
  Reviewer confirmation per ADR 0006, without a further live dialogue turn
  with the Director for this item.
- Reason: Well-evidenced, narrow correction; ready to run.
