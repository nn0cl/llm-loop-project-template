# Native probe scope

Active persona: Planner recording tool observations, not approving product compatibility.
Authority: DA-2026-10-01-01 / WP-0027. Disposable fixture; no real backlog execution.

Actual primitives exercised in the current Codex desktop chat tool environment:
- spawn_agent with fork_turns=none started a worker from task instructions; isolated Git worktree fixture-worker at acceptance commit b2a2806.
- Worker completed attempt 1; parent received native completion notification.
- Separate Reviewer with fork_turns=none received only acceptance.json and decision.json, independently ran deterministic comparison and rejected the seeded execute:true artifact (required execute:false).
- followup_task resumed the completed worker, same branch/worktree/base, for correction. Worker independently compared corrected output, PASS exit 0.
- Fresh Reviewer with fork_turns=none independently compared corrected decision and issued fixture-only APPROVE; no producer logs or chat history supplied.

This is not proof of installed CLI 0.153.4 behavior, idle-parent wake, closed-client delivery, automatic authorization, eight-stage full-loop certification, all-tool availability, restart/duplicate/crash handling, or removal of Director close. Parent remained active throughout. Raw reviews state exact allowed inputs; clean dispatch is configured, not inferred from separate worktrees.

Deliberate rejection is a fixture failure, not a production review finding. Its correction does not close a real review-finding issue or this work plan. Fixture disposition remains separate from repository approval.
