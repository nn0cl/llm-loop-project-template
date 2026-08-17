# LISS-0023: Add the standing two-group pair as a session type

## Metadata

- Local issue ID: LISS-0023
- GitHub issue: none
- Status: review
- Phase: process-only
- Type: architecture
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: n/a
- Owner/agent: unassigned (persona: Implementer)
- Related branch: process/session-start-standing-pair

## Summary

- Contract file: `docs/collaboration/session-start-and-resume.md` (governed
  by ADR 0006).
- Add a fourth session type, "Standing Two-Group Pair", describing:
  - the Director starts the Design & Review group session and the
    Implementation group session once each (not per work plan);
  - each session's first message states its group and persona set, per the
    existing Session Entry Checklist;
  - both sessions read `docs/collaboration/loop-settings.toml` and the
    normal recovery-order documents at their own start, same as any other
    session;
  - ongoing operation follows the handoff protocol in
    `docs/collaboration/cross-session-messaging.md` (LISS-0022) rather than
    the Director restating a task message per work plan;
  - when either session ends (process restart, crash, manual stop), the
    Director or the other group re-establishes it using the same repository
    artifacts (backlog, agreements, work plans) as any resumed session —
    the standing pair does not introduce a new continuity mechanism, it
    reuses the existing artifact-only continuity rule.

## Acceptance Notes

- The new session type is listed alongside the existing three, with its own
  short heading.
- It cross-references LISS-0022's protocol document instead of duplicating
  its content.
- It restates that artifact-only continuity (no chat memory) still applies
  to a standing session after a restart.

## Dependencies

- Parent: WP-0002
- Depends on: LISS-0019
- Blocks: none
- Related: LISS-0022

## Decisions Not Settled by the Design Agreement

- None known.

## Context

- Included: `docs/collaboration/session-start-and-resume.md`, ADR 0016
- Omitted: n/a
- Assumptions: none

## References

- `docs/collaboration/session-start-and-resume.md`

## Work Notes

- 2026-08-18 (Implementer, Implementation group, first standing session):
  renamed "Three Session Types" to "Four Session Types" and added
  "4. Standing Two-Group Pair" to
  `docs/collaboration/session-start-and-resume.md`, covering: one-time
  Director start per group; each session's first message stating its group
  and persona set per the Session Entry Checklist; both sessions reading
  loop-settings and the normal recovery-order documents at their own start;
  ongoing operation via `docs/collaboration/cross-session-messaging.md`
  instead of a restated per-work-plan task message; and re-establishment
  after a restart following the existing artifact-only continuity rule
  (cross-referenced, not restated as a new mechanism).
- Trace: `docs/collaboration/traces/2026-08-18-liss-0023-session-start-standing-pair.md`.

### Self-Review (Implementer, design note -> drafted change)

Per `docs/templates/self-review.md`, short form.

```text
Phase / finding: Architecture Path design note -> drafted change to
  docs/collaboration/session-start-and-resume.md (new session type 4)

Command run: python3 scripts/check-contract-consistency.py
Result: contract consistency: all checks passed

Risks considered:
  1. The new session type contradicts "Core Idea"'s artifact-only
     continuity rule by implying a standing session's own chat history is
     an acceptable continuity source.
  2. The new section duplicates `cross-session-messaging.md`'s handoff
     content instead of cross-referencing it.
  3. The renumbered "Four Session Types" heading is not matched by an
     actual fourth `###` subsection, leaving the document's own count
     wrong.

Why each does not occur:
  1. The closing paragraph states explicitly: "Re-establishing a standing
     session is not a new continuity mechanism — it follows the same
     artifact-only continuity rule as any resumed session under 'Core Idea'
     above... never from assumed chat memory of the session that ended,"
     directly restating rather than weakening that rule.
  2. The "Ongoing operation" bullet reads "this document does not restate
     that protocol's content; see it for the concrete SendMessage /
     ListAgents contract" — a cross-reference, not a restatement.
  3. Read the full section list after the edit: "### 1. First Session
     After Template Adoption", "### 2. New Session, Same Task (Resume)",
     "### 3. New Session, New Task", "### 4. Standing Two-Group Pair" — four
     `###` subsections under the "## Four Session Types" heading.
```
