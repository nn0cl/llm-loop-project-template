# Feature: Preflight Validation before independent review

## Scenario: Pass a clean change to the independent Reviewer

Given the Implementer has completed a change
When deterministic checks and the Preflight checklist pass
Then a Preflight record contains the commands, outputs, scope check, and
  `pass`, and the change is submitted to an independent Reviewer

## Scenario: Return an incomplete change before independent review

Given a required file, evidence field, reference, or scope condition is missing
When Preflight Validation runs
Then it records `fail`, names the failed check, and returns the change to the
  Implementer without issuing Reviewer approval

## Scenario: Use a lightweight model only for checklist assistance

Given deterministic checks have run
When document consistency remains to be checked
Then a lightweight reasoning model may identify omissions or inconsistent terms
  but may not approve specification conformance, set `wont_do`, or close an ISSUE

## Scenario: Preserve independent review

Given Preflight Validation has passed
When the change enters review
Then a separate Reviewer context still performs falsification and records the
  typed approval decisions
