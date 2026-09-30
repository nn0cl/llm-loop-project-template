# WP-0027 source correction confirmation

## Review target and separation
- Active persona: Reviewer only; this context produced the original rejection and never produced the correction.
- Agreement: DA-2026-10-01-01; Architecture Path, docs-only review.
- Target: immutable producer snapshot ed507e6d6e01b0f312ab810bcfbfb0b430d05ef9; LISS-0076 acceptance and whole WP-0027 within the original review scope.
- Inputs: target diff, LISS-0076, corrected backlog/guide/research, versioned-release grounds, deterministic outputs and canonical contract artifacts. Producer rationale/trace/chat is not justification.
- Original rejection preserved: 2026-10-01-wp-0027-native-subagent-loop-support-review.md.
- Preflight: original pass plus source-correction-check.txt; independently rerun below.

## Constraints
- [x] Context separate from correction producer; artifact-only input.
- [x] Recorded deterministic output.
- [x] Named falsification searches and grounds.

## Independent verification
Commands: `python3 scripts/check-contract-consistency.py --repo .`; `python3 docs/spike/case-0005-native-subagent-loop-support/evidence/implementation-document-check.py`; `git diff --check`. Each exit 0; last command silent.

```text
contract consistency: all checks passed
PASS six tool sections, eight stage cells, evidence/failure fields, touched relative links
LIMIT: structural checks do not certify native behavior, source correctness or account entitlement
```

Exact independent copy/source check:

```python
import tempfile, subprocess, pathlib
r=pathlib.Path.cwd()
for f in ['docs/backlog/item-0023-native-subagent-closed-loop-support.md','docs/collaboration/native-subagent-loop-compatibility.md','docs/spike/case-0005-native-subagent-loop-support/evidence/research.md']:
 for v in ['0.156.0','0.159.0','0.159.1']:
  assert 'https://github.com/openai/codex/releases/tag/rust-v'+v in (r/f).read_text()
 print('PASS versioned grounds '+f)
with tempfile.TemporaryDirectory(prefix='wp0027-confirm-') as d:
 p=subprocess.run(['bash','scripts/copy-ai-collaboration-files.sh','--target',d,'--non-interactive'],capture_output=True,text=True)
 assert p.returncode==0,p.stderr
 print('copy exit=0')
 for f in ['docs/collaboration/native-subagent-loop-compatibility.md','docs/templates/agent-tool-conformance.md','docs/collaboration/adoption-guide.md']:
  assert (r/f).read_bytes()==(pathlib.Path(d)/f).read_bytes()
  print('PASS copied bytes '+f)
```

Output, exit 0:

```text
PASS versioned grounds docs/backlog/item-0023-native-subagent-closed-loop-support.md
PASS versioned grounds docs/collaboration/native-subagent-loop-compatibility.md
PASS versioned grounds docs/spike/case-0005-native-subagent-loop-support/evidence/research.md
copy exit=0
PASS copied bytes docs/collaboration/native-subagent-loop-compatibility.md
PASS copied bytes docs/templates/agent-tool-conformance.md
PASS copied bytes docs/collaboration/adoption-guide.md
```

## Primary-source/date confirmation
Independent official-page retrieval in this Reviewer context on 2026-10-01 corroborates:
- [0.156.0](https://github.com/openai/codex/releases/tag/rust-v0.156.0): page label 22 Sep 19:51, commit fe74a77; worktree creation/default availability under New Features, completion/interruption preservation and Plan-mode restore under Bug Fixes.
- [0.159.0](https://github.com/openai/codex/releases/tag/rust-v0.159.0): 29 Sep 08:05, commit 687a119; opt-in instant_interrupt under New Features.
- [0.159.1](https://github.com/openai/codex/releases/tag/rust-v0.159.1): independently re-fetched for confirmation, 29 Sep 20:32, commit 8e68a98; bundled and Bedrock default catalog update under New Features.

These are source facts and page labels, not Japan-local rollout or installed feature verification. Corrected grounds match the independently retrieved pages. The generic changelog is now navigation only.

## Falsification
| Scenario | Grounds | Result |
| --- | --- | --- |
| Correction merely adds links without supporting facts | Release sections above support each corrected row; tags/commits/date labels match grounds record. | not reproduced |
| Generic changelog remains sole release authority | All three affected files now include exact versioned URLs and navigation-only qualification. | not reproduced |
| Copy path loses corrected guide | Independent byte equality above. | not reproduced |
| Correction broadens certification, billing or authority | Diff changes source grounds only; installed CLI 0.153.4 vs desktop distinction remains; no full eight-stage certification, live matrix Unknown, API/cloud deferrals and Director close intact. | not reproduced |
| Source correction bypasses independent contract review | This record independently confirms the guide change; producer did not approve it. | not reproduced |
| Rejection erased or finding closes before confirmation | Original rejection remains committed; Reviewer closes LISS-0076 only with this confirmation. | not reproduced |

## Whole-plan typed decision
- **Specification conformance: approved** for six-tool documentation assessment, copied support guide/template, and accurately bounded active-parent probe; LISS-0076 acceptance is satisfied.
- **Phase correctness: approved** for agreement-authorized docs-only work and disposable primitive evidence; no production Red/Green implementation promised or leaked.
- **Boundary conformance: approved** within documentation/partial-probe scope; original review's checks remain valid, source-only correction creates no new runtime, spend or authority boundary.
- **Evidence sufficiency: approved** for the support package and partial probe: original independent checks/replay/hashes plus corrected retrievable primary-source grounds and reruns above.

Overall **Approved**, narrowly scoped to WP-0027's documentation support package and partial active-parent native primitive fixture. LISS-0076 is independently confirmed and closed. No new findings.

## Remaining gaps / next action
Original review's unsearched scenarios remain unverified: full eight-stage six-tool adoption, idle/ended-parent/client-exit/restart/crash/duplicate handling, authenticated entitlement/billing, and real Director close. No new native calls were made for this correction. Director close remains pending; Reviewer approval does not mark the plan Done or close the promoted backlog. Present this bounded approved result at that existing checkpoint.

## Lifecycle synchronization disposition
The approved outcome permits these mechanical status-only updates: LISS-0075 `review -> done` with this confirmation link; its WP row `done`; Current Next Issue `none; Director close pending`; Work-Plan Review links this confirmation. These changes record the approval already issued and do not broaden it. Work-Plan Close must remain pending, backlog remains promoted, and no guide/acceptance/scope content changes are covered by this disposition. Parent must run contract consistency and whitespace checks after applying those exact updates; any other substantive change needs review.

Post-record validation: `python3 scripts/check-contract-consistency.py --repo .` output `contract consistency: all checks passed`, exit 0; `git diff --check` emitted nothing, exit 0.
