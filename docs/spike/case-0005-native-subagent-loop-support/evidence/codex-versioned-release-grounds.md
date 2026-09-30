# Codex versioned release grounds

Retrieved 2026-10-01 by Implementer after LISS-0076. Replaces sole reliance on the unified changelog; it is not a live feature test. Dates are page date labels, not a claim about Japan-local rollout time.

| Source | Page date label | Tag / commit | Supporting section (paraphrased) |
| --- | --- | --- | --- |
| https://github.com/openai/codex/releases/tag/rust-v0.156.0 | 22 Sep | rust-v0.156.0 / fe74a77 | New Features: agent-command-center worktree sessions and default worktree availability. Bug Fixes: streamed plans preserved on failure/interruption/child completion; Plan mode restored on resume. |
| https://github.com/openai/codex/releases/tag/rust-v0.159.0 | 29 Sep | rust-v0.159.0 / 687a119 | New Features: opt-in instant_interrupt steers model responses and long Code Mode calls. |
| https://github.com/openai/codex/releases/tag/rust-v0.159.1 | 29 Sep | rust-v0.159.1 / 8e68a98 | New Features: Sol 6.1 default catalog entry, including Bedrock catalogs. |

Reviewer reproduced a current missing 0.156.0 entry in the unified changelog. These directly retrieved primary release pages support the same facts without that index. Installed CLI remains 0.153.4; desktop/API parity and full-loop support remain unverified.
