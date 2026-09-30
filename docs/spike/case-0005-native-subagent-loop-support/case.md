# Spike Case: Native subagent loop support

## Metadata
- Case ID: case-0005
- Status: closed
- Created: 2026-10-01
- Closed: 2026-10-01
- Owner/agent: Planner, root with read-only research children
- Related work plan: WP-0027
- Related local issue: LISS-0074
- Related backlog item: item-0023

## Question
Which current native capabilities can reliably support the existing approved-backlog-to-Director-close loop without a different billing arrangement?

## Why a spike
Six-tool end-to-end support, fresh Reviewer inputs, completion delivery, recovery and billing coverage cannot be inferred from parallelism alone.

## Constraints
No paid calls, installation, upgrades, schedules or real automatic closure. Existing gates and artifact-only continuity apply.

## Candidates
A: existing native parent-child primitives with explicit artifact handoffs and isolation.
B: optional hook/scheduler transport configured in existing licensed local environment.
C: separate API/cloud orchestrator, deferred due to billing uncertainty.

## Evaluation criteria
Eight-stage fixture from item-0023; document/native/auxiliary/unconfirmed coverage by stage; fresh context; isolated checkout; completion delivery; recoverability; current entitlement.

## Research log
See evidence/research.md for retrieved primary sources for all six tools and evidence/local-inventory.txt for installed versions.

## Comparison
The reusable guide will expose per-stage native/auxiliary/unconfirmed coverage. All six require repository-level authorization, evidence/finding lifecycle and Director close. Cursor/Copilot/Antigravity have documented bounded continuation primitives; Grok passive hooks do not provide it; closed-client continuation remains unconfirmed.

## Cost and quality judgment
No paid service invoked. Installed binary versions alone are not proof of entitlement or successful agent behavior.

## Selection
- Selected: A, existing native parent-child capabilities with explicit artifact handoffs and isolation.
- Rationale: supports the existing portable baseline without new spend or a new orchestration authority. Current source evidence supports a reusable compatibility guide and a conformance evidence template.
- Discard B as a mandatory dependency: hook semantics and limits differ, runtime entitlement is unverified; retain as optional configured mechanisms.
- Discard C for this plan: separately billed/API/cloud operation is deferred.
- No product is certified for the complete eight-stage loop by this selection.

## Evidence
Local inventory and subsequent commands recorded under evidence/.

## Next action (exactly one)
- [x] Spec + implementation issue: refine LISS-0075 acceptance into a copied compatibility guide and conformance-evidence template; implementation remains docs-only. The disposable native probe records partial evidence separately, not full adoption certification.

## Open risks after close
Full unattended behavior and unavailable account surfaces require later live validation; no Verified claim yet.
