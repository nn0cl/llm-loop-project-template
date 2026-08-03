# Preflight Validation Record (round 5)

Per ADR 0013. **Not an approval.** Rounds 1-4 of this change each returned
`pass` and each was rejected. Round 4's rejection was narrower in scope than
1-3, but it was in the same family as round 3: a connective-based parsing
approach, evaded by a phrasing not on its whitelist.

## Target

- Change: the round-4 finding that the same-line range rule's separator
  whitelist evades ordinary English ("up to", "up through", comma, slash),
  plus the round-4 disclosure-completeness finding.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-contract-consistency-check.md`
- Review record being answered:
  `docs/collaboration/reviews/2026-08-02-contract-consistency-review-4.md`
- Branch: `process/contract-consistency-check`.
- Producer: Implementer, Claude Opus 5 via Claude Code. Cannot review this.

## Result

**pass** — resubmit.

## What Changed

Four rounds established a pattern: every attempt to detect "this prose states
an ADR range" from a fixed vocabulary of connective words was evaded by an
ordinary phrasing not on the list. Round 1's five separators, round 3's
narrower dash-or-bare-word rule, round 4's finding that even that narrower
rule falls to "up to" — three iterations of the same failure mode.

**The approach is abandoned, not iterated again.** ADR-range detection no
longer parses prose for a range at all. `ENTRY_DOCUMENT_ADR_STATEMENTS`
registers each of the three entry documents' current, actually-existing range
statements as an exact-anchored pattern — the surrounding text is matched
verbatim, with one digit group standing in for the bound that must equal the
newest ADR or the adopter's starting number. There is no connective to evade,
because no connective is read.

This trades unbounded evadability for a bounded, disclosed cost: the pattern
is tied to today's wording. A rewording that changes the anchored text makes
the pattern fail to match — which fails closed (a loud, explicit failure
demanding the pattern be updated), never silently passes a wrong number. An
entirely new range statement added somewhere the check does not know to look
is invisible until registered, which is now named as a fourth structural limit
in the disclosure, are ranked alongside the two round-4 accepted as
irreducible (meaning drift, reference intent).

The disclosure's account of round-4's finding on itself was also corrected:
the round-4 record judged the previous version's coverage claim inaccurate on
inspection; the new disclosure states plainly that four rounds found holes,
names what each hole was in one line, and does not claim broader robustness
than the exact-anchor design provides.

## Defects Found and Fixed While Building This

Running the redesign against its own source and the real entry documents
surfaced three implementation bugs, none reported by any Reviewer round —
caught by re-running the checker after each change, per the practice this
whole exercise established:

1. A pattern in `QUICKSTART.ja.md`'s registry dropped the
   `docs/architecture/adr/` prefix present in the actual sentence, so it never
   matched even the correct text.
2. A capture group written `0(\d{3})` captured three digits instead of four,
   reporting `014` instead of `0014`.
3. The reference checker's own `MD_LINK` pattern matched the script's own
   regex source: `[–-](\d{4})` in a Python raw string parses identically to
   markdown link syntax `[text](target)`, and the checker flagged its own
   source line as a dangling reference to `\d{4}`. Fixed by requiring an
   `MD_LINK` target to look like an actual path — a slash or a recognized
   extension — before treating it as one.

## Checks

| # | Check | Result |
|---|---|---|
| 1 | The "up to" / "up through" evasion is closed | pass |
| 2 | No false positive on two unrelated ADRs cited together | pass |
| 3 | A reworded range statement fails closed rather than silently passing | pass |
| 4 | Negative test across every claimed class, together in one tree | pass — 5 failures, exit 1 |
| 5 | Clean tree | pass |
| 6 | Fresh copy-script target | pass |
| 7 | CI required files | pass — 69, 0 missing |
| 8 | `bash -n` | pass |

## Command Output

The round-4 evasion, now caught by failing closed (the pattern no longer
matches the reworded sentence, which is reported rather than silently passed):

```text
ADR range:
  QUICKSTART.md: expected range statement not found
  (pattern: '`docs/architecture/adr/0001-\\*\\.md` through `(\\d{4})-\\*\\.md`').
  If the sentence was reworded or moved, update ENTRY_DOCUMENT_ADR_STATEMENTS...
```

The round-3 false-positive case, unaffected since no pairing logic remains:

```text
contract consistency: all checks passed
```

Combined negative test, five classes in one tree:

```text
mirror parity:      copilot does not state 'Prime Directive'
parity completeness: AGENTS.md section 'A Brand New Rule' is not classified.
references:          docs/collaboration/personas.md:171 names 'does-not-exist-anywhere.md'
ADR range:           README.md: expected range statement not found (...)
version claims:       README.md:6 names v1.1.0, which has no git tag.

contract consistency: 5 failure(s)
```

Clean tree, target, CI:

```text
contract consistency: all checks passed     (template repo)
contract consistency: all checks passed     (copy-script target)
required_files: 69, missing: []
bash -n OK
```

## Scope Result

Within scope. No specification, ADR, port, data model, dependency, or
architecture boundary changed.

## Routing and Compatibility

- Capability class: deterministic tooling for verification; strong reasoning
  agent for the decision to abandon connective parsing entirely rather than
  narrow the whitelist a fourth time.
- Displayed model / reasoning setting: Claude Opus 5, default.
- Compatibility state: default routing; stdlib-only Python 3.
- Escalation reason: contract tooling changed.

## Next Action

Resubmit. Given four rejections, this record does not ask the Reviewer to
trust that the pattern is finally sound — it asks the Reviewer to register a
fifth range statement of their own choosing (anywhere in the three entry
documents, in any wording) and confirm the check fails closed on it rather
than silently passing.
