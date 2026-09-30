# AI Work Trace: Native subagent compatibility guide

## Request
- Date: 2026-10-01
- Active persona: Implementer
- Covering design agreement: DA-2026-10-01-01
- Current phase: docs-only Architecture Path; no Red/Green/Refactor claim
- Canonical issue/work plan: LISS-0075 / WP-0027
- AI planning record: AIP-WP0027-001
- Request: ship copied guide, conformance template and adoption entry link after closed case-0005.

## Design Check and Readiness
[DESIGN CHECK]
- Active persona: Implementer.
- Covering design agreement: docs/collaboration/agreements/2026-10-01-native-subagent-loop-support.md.
- Scope and expected behavior: six-tool, eight-stage compatibility guidance and disposable evidence fixture; no orchestrator implementation.
- Specifications and files inspected: agreement, WP-0027, LISS-0075, closed case-0005 and research/local inventory, adoption guide, quickstart, readiness, Architecture Path policy documents, AGENTS.md and ADR 0016/0017.
- Component boundaries, ports/adapters, VO/DTO candidates: documentation only; no runtime DTO, port, dependency or production boundary introduced.
- Applicable constraints: existing billing; artifact-only Reviewer; opt-in workspace isolation; Director close; prompt-instruction-change-control independent review.
- Decisions, assumptions, unresolved ambiguities: documentation-derived capabilities remain Inferred; missing live surface/account entitlement remains Unknown/deferred. Agreement explicitly settles documentation-only execution.
- Included and omitted AI context: relevant public contracts and source evidence included; private accounts, secrets, producer transcript for Reviewer and unrelated product code omitted.
- Task routing: dedicated Implementer worktree /private/tmp/llm-loop-wp0027, branch codex/native-subagent-guide, base 4b2acaaa6236be858e182f0b8d95576f77fc8412; shell/Python verification, separate Reviewer later.
- Input/output evidence contract: authoritative artifacts in; guide/template plus command output out; reject invented configuration, unsupported continuation or live certification.
- Verification plan: contract checker, whitespace check, disposable copy smoke with byte comparisons and document/link checks.
- Readiness result: docs-only agreement and phase/persona recorded; case dependency closed. Coding-phase readiness checks are N/A. No new architecture decision needed.
- Findings reuse: LISS-0064 status synchronization honored by updating issue and plan together; LISS-0070 closed mirror finding honored by leaving reading order/mirror contracts untouched; LISS-0044/LISS-0059 copy exclusions honored by testing shipping paths while leaving historical records excluded. No new disposition of unrelated open findings.

## Context Ledger
- Included: documents named above and current official six-tool documentation retrieved 2026-10-01.
- Omitted: private account exports, credentials, cloud runs and transcripts as review justification.
- Assumptions: native events are transport only; existing governance still applies.
- Open decisions: exact live configuration/entitlement per tool; deferred, not implementation premises.

## Routing
- Model/assistant/tool: inherited Codex child; displayed model/reasoning unavailable in authoritative output.
- Compatibility state: Inferred for official capabilities; Unknown for full live loop.
- Privacy: public repository documents only.

## AI Execution Records
### Attempt 1
- Agent: guide_implementer, Implementer only.
- Environment: Codex desktop native child, isolated Git worktree.
- Model as displayed: N/A; not surfaced.
- Reasoning setting as displayed: N/A; not surfaced.
- Estimated token range/midpoint: N/A; no reliable attribution measurement.
- Actual tokens / metric / source / attribution boundary: N/A.
- Actual token unavailable reason: native tool does not return per-child usage.
- Estimate variance / variance reason: N/A.
- Scope: documentation and recorded deterministic preflight only.
- Attempt boundary: initial source recovery through preflight; historical research trace preserved.
- Result: documentation delivered and deterministic preflight pass; independent approval pending.

## Cost / Reasoning Control
- Operating path: Architecture Path, required for contract companion guidance.
- Deterministic checks: contract consistency, copy smoke, byte comparison, links, whitespace.
- Escalation reason: none; unavailable live features explicitly deferred.
- Avoided LLM work: no source-code generation or paid tooling.
- Rework caused by AI output: checker interpreted the concrete Cursor sample definition as an existing reference. Changed it to generic definition wording; initial failure preserved in implementation-contract-initial.txt.

## Decisions Carried
- Director: bounded scope and existing billing from agreement.
- Reviewer: pending independent review; producer issues no contract approval.
- Arbiter: none.

## Verification and Preflight
- Required: yes. Result: pass for documentation scope; independent Reviewer required.
- Raw output directory: docs/spike/case-0005-native-subagent-loop-support/evidence/.
- Command: `python3 scripts/check-contract-consistency.py --repo .`
  Output in implementation-contract-check.txt: `contract consistency: all checks passed`.
- Initial checker defect and exact output retained in implementation-contract-initial.txt; sample filename corrected before successful rerun.
- Command: `python3 docs/spike/case-0005-native-subagent-loop-support/evidence/implementation-document-check.py`
  Output in implementation-document-check.txt:
  ```text
  PASS six tool sections, eight stage cells, evidence/failure fields, touched relative links
  LIMIT: structural checks do not certify native behavior, source correctness or account entitlement
  ```
- Copy smoke command: Python creates a temporary target, invokes `bash scripts/copy-ai-collaboration-files.sh --target <temporary-target> --non-interactive`, compares shipped bytes and hashes. Raw command/script output and target path in implementation-copy-smoke.txt; exit 0 and three byte-identical PASS lines, concluding `PASS isolated copy delivers guide, template, adoption entry`.
- Command: `git diff --check`; raw output in implementation-diff-check.txt, exit 0 with no diagnostics.
- Scope result: docs-only guide/template/adoption link and status/evidence records; no production code, dependencies, mirrors or mandatory reading order changed.
- Failure scenarios exposed for independent review: copied files absent (byte comparisons); missing stage/tool/relative links (structural check); unsupported native guarantee or wrong source (not certified by checker, Reviewer must inspect); producer self-approval (none issued); status drift (checker); Director close bypass (explicit pending).
- Verification gaps: native commands and billing not exercised by this implementation; closed-client wake/full fixture unknown. Source correctness still needs independent review.
- Next action: fresh artifact-only Reviewer, then Director checkpoint.

## Changed Files
- docs/collaboration/native-subagent-loop-compatibility.md
- docs/templates/agent-tool-conformance.md
- docs/collaboration/adoption-guide.md
- this trace
- docs/issues/LISS-0075-native-subagent-adoption-guide.md
- docs/work-plans/WP-0027-native-subagent-loop-support.md
- case-0005/evidence implementation verification outputs

## Next Safe Action
Run deterministic preflight, then hand only artifacts to a fresh independent Reviewer. Director close remains pending after approval.
