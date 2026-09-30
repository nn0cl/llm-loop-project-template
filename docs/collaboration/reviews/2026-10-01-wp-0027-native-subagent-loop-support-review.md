# WP-0027 independent review

## Design intake and target
[DESIGN CHECK]
- Active persona: Reviewer only, fresh child context with no inherited parent conversation.
- Covering design agreement: DA-2026-10-01-01.
- Scope: whole documentation support package and bounded active-parent native primitive probe, snapshot 8f2b808b7d246941d66f73f7c8de1a329ff4ac65 against main 4587e05.
- Inspected: WP Review Summary Packet/integrated preflight; agreement; item-0023; LISS-0074/0075; AGENTS, quickstart/settings, change-control/review template, definition of done; changed guide/template/adoption, source records and probe artifacts.
- Boundaries: no runtime/adapters/ports changed; no paid calls, cloud, upgrades, schedules or Director authority change.
- Included context: authoritative artifacts, target diff and raw outputs. Omitted: producer transcript/hidden reasoning; producer trace is audit metadata, not justification.
- Routing: independent deterministic CLI reruns and primary-source web retrieval.
- Verification: contract/structural/link checks, independent temporary copy inclusion/exclusion, typed snapshot replay and hashes, primary-source falsification.

## Constraints
- [x] Context separation: fresh artifact-only Reviewer; producer reasoning not used.
- [x] Deterministic precondition: outputs below; all structural signals passed.
- [x] Falsification burden: named searches below, including a reproduced source-grounding defect.
- Preflight: pass, integrated-preflight.txt; permits review only.

## Deterministic verification output
Independent commands:
`python3 scripts/check-contract-consistency.py --repo .`
`python3 docs/spike/case-0005-native-subagent-loop-support/evidence/implementation-document-check.py`
`git diff --check`

```text
contract consistency: all checks passed
PASS six tool sections, eight stage cells, evidence/failure fields, touched relative links
LIMIT: structural checks do not certify native behavior, source correctness or account entitlement
```
Each exit 0; whitespace command emitted no output.

Independent Python temporary-directory smoke invoked `bash scripts/copy-ai-collaboration-files.sh --target <temporary directory> --non-interactive`, compared source/target bytes, asserted history absence, then SHA-256 checked each native manifest entry and compared both decisions with required_output (including boolean type):

```text
copy exit=0
PASS copied bytes docs/collaboration/native-subagent-loop-compatibility.md
PASS copied bytes docs/templates/agent-tool-conformance.md
PASS copied bytes docs/collaboration/adoption-guide.md
PASS history excluded docs/spike/case-0005-native-subagent-loop-support
PASS history excluded docs/work-plans/WP-0027-native-subagent-loop-support.md
PASS sha256 acceptance.json
PASS sha256 attempt-1-decision.json
PASS sha256 decision.json
PASS sha256 review-1.md
PASS sha256 review-2.md
attempt-1-decision.json: FAIL (expected rejection)
decision.json: PASS
```
Exit 0. Reproduce with tempfile.TemporaryDirectory, subprocess.run above, bytes equality for the three paths, pathlib.exists false for two history paths, hashlib.sha256 against sha256.json, and JSON required_output vs each decision. The original raw probe commands/reviews remain under case-0005/evidence/native-probe.

## Falsification search
| Failure scenario | Grounds/result |
| --- | --- |
| Full eight-stage or six-tool live certification asserted | Not reproduced: guide labels all live cells Unknown; probe-scope explicitly limits active-parent primitives; no idle/exit/restart/duplicate claim. |
| Shared workspace called isolated / fork accepted as independent | Not reproduced: explicit worktree checks and separate context/allowlist; Cursor default sharing and Claude default-branch warning match current primary docs. Copilot `/new worktree` vs `/fork worktree` distinction and Antigravity branch/share distinction corroborated. |
| Hook event guarantees continuation | Not reproduced: Cursor five default cap and Copilot eight-block cap match hooks docs; Grok primary Hooks states only PreToolUse blocks and passive stdout ignored; idle/closed-client guarantee withheld. |
| Historical/version/surface facts unsupported by stated source | Reproduced: LISS-0076, CLI release facts cite unified changelog that currently omits them; versioned official releases corroborate the facts but are absent from submitted grounds. |
| Copy excludes shipped support package or ships plan history | Not reproduced: byte comparisons/history-absence assertions above. |
| Paid adoption implied or new orchestration shipped | Not reproduced: entitlement Unknown/deferred; source candidates are Inferred; documentation only. |
| Seeded rejection/fix fabricated by snapshot content | Not reproduced at artifact level: hashes match, first decision fails, corrected decision typed-match passes, two independent fixture records are scope-limited. Native event delivery itself cannot be replayed from JSON. |
| Producer self-approves contract or closes plan/backlog | Not reproduced: independent approval pending, backlog promoted, Director close pending; fixture approval explicitly separate. |
| Missing work-plan closure/finding lifecycle | No false completion asserted; this review introduces LISS-0076 and blocks Done until addressed. |

Primary sources independently retrieved 2026-10-01: code.claude.com/docs/en/sub-agents; cursor.com/docs/subagents and /hooks; docs.x.ai/build/features/subagents, /worktrees, /hooks, /sessions (initial direct web errors resolved by following official internal links); docs.github.com/en/copilot/reference/hooks-reference and copilot-cli-reference/cli-command-reference; www.antigravity.google/docs/subagents/ and /hooks/; learn.chatgpt.com/docs/environments/git-worktrees and /changelog; official openai/codex GitHub release tags 0.156.0, 0.159.0, 0.159.1. These source inspections validate documentation candidates, not installed native behavior or billing entitlements.

## Scenarios not searched / verification gaps
No new native agent execution, idle/ended-parent/client-exit/crash/duplicate recovery test, authenticated six-tool fixture, account billing validation, or real Director close. Source pages can change; release citations need versioned grounding. Raw probe logs establish configured fresh context/input limits, not an independent inspection of hidden system state. No producer transcript was supplied or read.

## Typed decision
- Specification conformance: withheld pending LISS-0076 source correction; other documentation acceptance and bounded-probe representation pass.
- Phase correctness: approved, docs-only phase expressly authorized by agreement; no application Red/Green promise or production leakage.
- Boundary conformance: approved within documentation support-package/partial probe scope; no authority, spend, runtime or dependency boundary change.
- Evidence sufficiency: rejected pending LISS-0076; deterministic output passes but the release source attribution is not reconstructible as submitted.

Overall **Rejected** for one bounded actionable finding: LISS-0076. Correct source grounding and obtain independent contract confirmation; no producer document fix performed by Reviewer. This is not eight-stage adoption approval or Director work-plan close.
