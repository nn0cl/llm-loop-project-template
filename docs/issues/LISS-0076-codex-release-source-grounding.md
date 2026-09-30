# LISS-0076: Ground Codex release claims in retrievable release sources

## Metadata
- Local issue ID: LISS-0076
- Status: resolved
- Type: review-finding
- Phase: docs-only Architecture Path correction
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Owner/agent: Implementer
- Active persona at finding: Reviewer
- Parent: WP-0027
- Covering agreement: DA-2026-10-01-01
- Related branch: codex/native-subagent-loop-support

## Finding
The submitted snapshot 8f2b808 attributes CLI 0.156.0/0.159.0/0.159.1 release facts to https://learn.chatgpt.com/docs/changelog. Independent retrieval on 2026-10-01 (including its `?type=codex-cli` filter) returned the unified changelog with no occurrences of `0.156.0`; its September entries cover model/app changes. No retained source extract in case-0005 reconstructs the missing CLI entries. The facts are corroborated by official versioned GitHub releases, so this is a source-grounding defect rather than evidence the capabilities are false.

Affected: item-0023 release table, case-0005/evidence/research.md Codex paragraph, companion guide current-release claim/source C4. The audit contract requires each claim's stated grounds to support it without recovering this chat.

## Reproduction and grounds
Reviewer web open/find on the changelog: `0.156.0` -> No matching text found. Direct official release retrieval:
- https://github.com/openai/codex/releases/tag/rust-v0.156.0 supports September 22 worktree creation/default availability and completion/interruption/Plan-mode fixes.
- https://github.com/openai/codex/releases/tag/rust-v0.159.0 supports September 29 opt-in instant_interrupt.
- https://github.com/openai/codex/releases/tag/rust-v0.159.1 is the version-specific source for catalog changes.

## Required correction / acceptance
Add exact versioned primary-source links alongside the corresponding claims and record independently checkable release/date grounds. Keep the generic changelog as optional navigation, not sole evidence for these CLI facts. Preserve installed CLI vs desktop distinction and all partial/unconfirmed scope limits. Rerun contract/structural/link checks and submit the changed contract guide for separate-context confirmation under ADR 0006. No runtime, new spec, billing, or authority change is requested.

## Exact affected locations in 8f2b808
- docs/backlog/item-0023-native-subagent-closed-loop-support.md:63 and release rows 67–71.
- docs/spike/case-0005-native-subagent-loop-support/evidence/research.md:8.
- docs/collaboration/native-subagent-loop-compatibility.md:24–25 and C4 at 202.

Finding/review record validation after writing: `python3 scripts/check-contract-consistency.py --repo .` emitted `contract consistency: all checks passed`, exit 0; `git diff --check` emitted nothing, exit 0.

## Correction record
- Active persona: Implementer (root), docs-only Architecture Path; no contract self-approval.
- Lifecycle: proposed -> accepted -> in_progress -> resolved on 2026-10-01; separate Reviewer closure pending.
- Minimum correction: versioned links in the three affected files; release/date/tag/commit grounds in case-0005/evidence/codex-versioned-release-grounds.md.
- Verification record: case-0005/evidence/source-correction-check.txt.
- Separate confirmation: pending fresh-context Reviewer; remains a blocking plan finding until confirmation.
