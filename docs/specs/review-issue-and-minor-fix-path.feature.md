# Feature: Review issues and minor fixes

## Scenario: Record an actionable review finding

Given a Reviewer records a concrete failure scenario against an artifact
When the finding is written as a `review-finding` ISSUE
Then the ISSUE contains the review record, affected artifact, failure scenario,
  status `proposed`, and deterministic verification needed for closure

## Scenario: Accept and resolve a review finding

Given a `review-finding` ISSUE has status `proposed`
When the finding is accepted and the Implementer applies a correction
Then the ISSUE records status `accepted`, the changed files, verification output,
  and status `resolved` before a separate Reviewer verifies it as `closed`

## Scenario: Reject a review finding with grounds

Given an Implementer disputes a `review-finding`
When an Arbiter determines that the finding is not actionable under the agreement
Then the ISSUE records status `wont_do`, the Arbiter decision, the grounds, and
  the rejected alternatives

## Scenario: Use the Minor Fix Path

Given a correction is planning size `S`, limited to existing accepted behavior,
  changes no architecture boundary, and is expected to complete in one attempt
When the task is routed through Minor Fix Path
Then it records a compact design note, applies the minimum correction, runs
  deterministic verification, and receives separate Reviewer confirmation

## Scenario: Escalate a correction out of the Minor Fix Path

Given a correction changes a specification, ADR, port, data model, dependency,
  or requires a second attempt
When the correction is classified
Then it is routed to Feature Path or Architecture Path and is not treated as a
  Minor Fix Path task

## Scenario: Route by capability class

Given a task is classified by its operation and risk
When the task is dispatched
Then it uses the smallest capable route from the model capability matrix and
  records any escalation reason and compatibility state
