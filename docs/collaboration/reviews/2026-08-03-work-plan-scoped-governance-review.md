# Review Record: Work-Plan-Scoped Self-Review and Combined Checkpoint (ADR 0014)

Reviewing persona: Reviewer.
Model / tool: Claude Sonnet 5, via a fresh Claude Code agent session with no
memory of the producing session's reasoning or dialogue with the Director.
Only the checked-out branch, its documents, and directly re-run commands were
used as evidence. This review runs under the **pre-change** contract (ADR
0001's per-artifact separate-context requirement), per the design agreement's
own bootstrapping discipline: this change cannot validate itself under the
model it introduces.

## Constraints (all three must hold)

- [x] **Context separation.** Did not produce ADR 0014, the design agreement,
      the trace, or the propagation diff. No reasoning from the producing
      session was supplied or relied on; every claim below was independently
      re-derived from the checked-out branch and re-run commands.
- [x] **Deterministic precondition.** All checks below were run in this
      session against the real branch, and additional adversarial checks were
      run against a disposable scratch copy for defect injection. Output is
      pasted, not summarized.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below, each with the grounds on which it does or does not occur.

## Review Target

- Artifact: branch `process/work-plan-scoped-governance`, commit `2c6f219`,
  pull request #10 against `main`.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-03-work-plan-scoped-governance.md`
  (DA-2026-08-03-01).
- Specification: none — governance/process change, no application
  specification, as stated in the design agreement.
- Current phase: Architecture Path, documentation/ADR only. No Red/Green/
  Refactor artifact; "phase-correctness" does not apply.
- Producing persona: Specifier, then Implementer (per the trace).
- Reviewing persona / model / tool: Reviewer / Claude Sonnet 5 / Claude Code.
- Approval type: specification-conformance, boundary-conformance,
  evidence-sufficiency.
- Preflight Validation record: **none exists for this submission.** No file
  matching `docs/collaboration/reviews/2026-08-03-*preflight*` or similar was
  found, and the design agreement's own Verification section does not list a
  Preflight step. ADR 0013 (unchanged, still in force per the design
  agreement's Boundaries section) frames Preflight as a step "between
  Implementer completion and independent review" for any submission, not only
  work-plan-scoped ones — and the repository's own prior practice bears this
  out: the contract-consistency-checker change went through six numbered
  Preflight records (`docs/collaboration/reviews/2026-08-02-contract-
  consistency-preflight-*.md`), one per review round. This submission has
  none. See Finding 2 below.
- Preflight result: N/A — not produced. In its place, this review
  independently re-ran the full deterministic check suite the trace claims,
  from a fresh context, before relying on any of it (see Deterministic
  Verification Output).

## Deterministic Verification Output

**Contract consistency checker, on the checked-out branch:**

```text
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
(Exit code 0.)

**ADR file count and range:**

```text
$ ls docs/architecture/adr/*.md | wc -l
      14
$ ls docs/architecture/adr/
0001-director-centered-planning-and-closed-loop.md
0002-design-first-ai-request-routing.md
0003-input-output-reasoning-contracts.md
0004-human-readable-source-code-quality.md
0005-local-issue-planning.md
0006-prompt-instruction-change-control.md
0007-trunk-oriented-branching.md
0008-template-update-propagation.md
0009-bug-planning-and-ai-usage-records.md
0010-ai-failure-recovery-and-runner-cli-contract.md
0011-external-resource-adoption-contract.md
0012-review-issues-minor-fix-and-model-routing.md
0013-preflight-validation-before-independent-review.md
0014-work-plan-scoped-self-review-and-combined-checkpoint.md
```

**Stale ADR-count sweep (expect zero hits outside historical record dirs):**

```text
$ grep -rn "thirteen\|13 件\|0001-0013\|0001–0013\|0013 以降\|0014 以降\|0014 and up" \
    --include="*.md" --include="*.mdc" . | grep -v \
    "docs/collaboration/traces/\|docs/collaboration/reviews/\|docs/collaboration/agreements/\|docs/issues/\|docs/work-plans/\|CHANGELOG.md"
(no output — 0 hits)
```

**Current ADR-count statements, confirmed correct in every entry document:**

```text
QUICKSTART.ja.md:157-158: 14 件... 0015 以降
QUICKSTART.md:153-154: fourteen... 0015 and up
QUICKSTART.md:180: ADRs 0001–0014
README.md:247: fourteen ADRs included here (0001-0014)
README.md:300: adr/ (0001-0014 = process ADRs)
docs/architecture/README.md:86: fourteen process ADRs
README.ja.md: ADR 0014 links present, no stale range statement
```

**CI status (via `gh pr view 10`):** `Repository sanity` check — `SUCCESS`,
confirming the CI-run copy of the same `check-contract-consistency.py` and ADR
existence loop also passed on this exact commit.

**Copy-script propagation smoke test, run independently in this review (not
reused from the trace):**

```text
$ git init -q /tmp/.../adopt-smoke-test
$ bash scripts/copy-ai-collaboration-files.sh --target /tmp/.../adopt-smoke-test \
    --project-name "Smoke Test" --domain-summary "smoke test domain" --stack "python"
Done.
$ python3 scripts/check-contract-consistency.py --repo /tmp/.../adopt-smoke-test
contract consistency: all checks passed
```

**Nine contract files, read in full and cross-checked directly (not only via
the checker) for `self-review`, `Reviewer`, `work-plan`, `context separation`:**
`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
`.grok/rules/01-quickstart.md`, `.grok/rules/02-architecture-boundaries.md`,
`.grok/rules/03-collaboration-and-completion.md`,
`.cursor/rules/01-quickstart.mdc`, `.cursor/rules/02-architecture-boundaries.mdc`,
`.cursor/rules/03-collaboration-and-completion.mdc`. All nine state: (a) issue-
level phase transitions are self-reviewed by the Implementer, in the same
context, requiring deterministic output and named failure scenarios but not
context separation; (b) the Reviewer runs once per work plan, in a separate
context, after every issue is self-reviewed and Preflight passes; (c)
"Contract-file changes are never self-reviewed, regardless of work-plan
scope" / equivalent, tying back to ADR 0006. No file contradicts another.

**`docs/architecture/adr/0006-prompt-instruction-change-control.md`: confirmed
untouched** (`git diff main...HEAD` for this file is empty) and still states
an unconditional separate-context Reviewer requirement for contract-file
changes.

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | ADR 0014 waives more than context separation (e.g., quietly drops the deterministic precondition or falsification burden for self-review) | Read ADR 0014 Decision §2 in full: "Only context separation is waived at this layer... An Implementer that records neither of the other two has not self-reviewed; it has skipped the phase gate." Cross-checked against all nine contract files, `ai-human-scheme.md`, `personas.md`, `at-tdd/process.md`, `definition-of-done.md` — every occurrence of "self-review" in this diff is paired with "deterministic" and "failure scenarios" in the same sentence or the immediately following one. No instance found where self-review is described without both. | not reproduced |
| 2 | Contract-file changes are described, somewhere in the propagation, as eligible for self-review (which would make this very PR's own model self-undermining) | ADR 0014 Decision §7 states the exclusion explicitly. Verified the same exclusion sentence (or a clear equivalent) is present in `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, both `.grok`/`.cursor` rule sets' collaboration file, `ai-human-scheme.md`, and that `docs/architecture/adr/0006-*.md` is unmodified and still unconditional. `grep -rn "Reviewer persona"` across the whole tree (excluding record dirs) found no sentence asserting a per-issue or per-phase Reviewer as current. | not reproduced |
| 3 | A stale per-phase / per-issue separate-context Reviewer statement survives somewhere the checker's mirror-parity check would not catch, since parity only checks presence of new phrases, never absence of old ones | Ran three independent greps: `"before Phase 2 starts"` / `"before Phase 3 starts"` (1 hit, in `at-tdd/process.md`, immediately followed by "self-reviews" — correct); `"each phase"` / `"every phase"` near Reviewer (all hits are either invariant statements unrelated to approval cadence, or explicitly describe self-review, not Reviewer); `"per-issue"` / `"per issue"` combined with "review" (all hits explicitly deny a per-issue gate, consistent with the new model). No survivor of the old per-phase claim found. | not reproduced |
| 4 | One of the nine contract files did not actually get the new rules mirrored in, despite the checker reporting pass (the checker's own disclosed "meaning" blind spot: presence of a phrase, not correctness of the sentence around it) | Read all nine files directly, in full, not just via the checker's regex. Every file independently confirmed to state self-review, the work-plan-level Reviewer, and the combined close consistently (see Deterministic Verification Output above). No divergence found in the actual repository content. | not reproduced |
| 5 | The ADR-count/range bump (13→14, adopter-start 14→15) missed an instance, or bumped one incorrectly | Grepped for both the stale forms (`thirteen`, `0001-0013`, `13 件`, `0014 以降`, `0014 and up`) — zero hits outside record/CHANGELOG dirs — and the current forms (`fourteen`, `0001-0014`, `14 件`, `0015 以降`, `0015 and up`) — found in `QUICKSTART.md`, `QUICKSTART.ja.md`, `README.md`, `docs/architecture/README.md`, all internally consistent with the actual ADR directory listing (14 files, `0001`–`0014`). `.github/workflows/ci.yml`'s existence loop confirmed to include `0014`. | not reproduced |
| 6 | The new `EXTRA_MIRRORED_RULES` regex patterns have a false-negative gap — a mirror could pass parity while the actual rule content is missing, the exact defect shape this script's own docstring says caused four of six prior rejection rounds | **Reproduced.** See Finding 1. The `"Work-plan-level Reviewer (ADR 0014)"` pattern is `r"work.plan.level Reviewer\|whole (?:completed )?work plan"` — an OR of two branches, and the second branch requires no mention of "Reviewer" at all. In a scratch copy, I deleted every line in `CLAUDE.md` that ties "Reviewer" to "work plan" (removing the actual work-plan-level-Reviewer rule), left one unrelated sentence containing "the whole work plan" (about Preflight, nothing to do with the Reviewer), and reran the checker: `contract consistency: all checks passed`. A mirror that had silently dropped the Reviewer's work-plan scope would still pass this specific check. | **reproduced** |
| 7 | The new patterns are also brittle in the other direction — correct content written with ordinary stylistic variation (e.g., no hyphen) incorrectly fails parity | Reproduced as a secondary observation, not a soundness defect: replacing `"self-review"` with `"self review"` (no hyphen) throughout a scratch copy of `CLAUDE.md` made the checker correctly report failure (`CLAUDE.md does not state 'Self-review (ADR 0014)'`). This fails *closed* (a true positive risk of false rejection on stylistic variance), which is the safe direction of error, unlike Finding 1's false-*negative* gap. Noted for completeness, not treated as a defect requiring correction. | reproduced (non-blocking, fails safe) |
| 8 | The content-meaning blind spot the script's docstring already discloses ("a mirror that keeps the phrase `context separation` while inverting the rule underneath it passes here") actually holds for the new self-review rules specifically | Reproduced as an independent confirmation, not a new defect — the script's own docstring already names this class. In a scratch copy of `CLAUDE.md`, inverted "but not context separation, which is waived only at this layer" to "and also context separation, which is required even at this layer" while keeping every required phrase intact. Checker still reported `all checks passed`. This is the pre-disclosed limitation operating exactly as documented, not an undisclosed one. | reproduced (pre-disclosed, not a new finding) |
| 9 | The tradeoff (slower defect discovery for fewer review invocations) is glossed over or missing from a document a future reader would plausibly check | Read ADR 0014 Context/Consequences, the design agreement's Direction and Deferred Questions, and the trace's Notes section in full. All three name the six-round contract-checker history explicitly, state plainly that self-review "cannot catch what the producing context cannot see about itself," and that the risk scales with work-plan size (named as an open Deferred Question, not silently assumed away). `README.md`'s new "What keeps AI self-approval honest" section states it too, with a direct link to ADR 0014. No document asserts the tradeoff was mitigated or solved — all treat it as accepted risk. | not reproduced |
| 10 | The Director's "combined checkpoint" is documented, somewhere in the propagation, as satisfiable by reading alone, or as two separate acts | Checked `design-agreement.md` ("Closing is one combined action, not two... in the same turn. It is not satisfied by reading alone with no stated next step"), `ai-human-scheme.md`, `definition-of-done.md` ("A work plan is not Done on Reviewer approval alone"), `work-plan.md` template (single "Work-Plan Close" section combining "Result read" and "Next direction" fields), and ADR 0014 Decision §5. All consistent; no split-gate or reading-only framing found. | not reproduced |
| 11 | `CHANGELOG.md` should have gained an entry for this change but did not, understating what shipped | `git diff main...HEAD -- CHANGELOG.md` is empty — confirmed no entry was added. Checked repository history: `v1.1.0`'s changelog entry was added in a dedicated release commit (`5e21958 process: release v1.1.0`) *after* independent-review approval, separate from the commits that did the actual propagation work (`2d83262`, `9b0d435`, `21a6c17`, `2183b8e`). This PR is at the equivalent pre-approval stage. Consistent with established practice, not a gap. | not reproduced |
| 12 | The design agreement's own Verification section omits a step it should have named (Preflight) | See Finding 2 — reproduced as a genuine gap, distinct from #11. | reproduced — see Finding 2 |

## Scenarios Not Searched

- Whether the Arbiter persona definition needs adjustment under work-plan-
  scoped review — explicitly named as a Deferred Question in the covering
  agreement, not something this change claims to settle, so not falsified
  here.
- Whether work-plan size should be bounded — same: an explicit Deferred
  Question, not evaluated for a "right" answer here.
- Full read-through of every file the trace's Context Ledger says was
  *omitted* as unaffected (`preflight-validation.feature.md`,
  `review-issue-and-minor-fix-path.feature.md`, historical trace/review/
  agreement records dated 2026-08-02 and earlier). Spot-checked
  `docs/collaboration/evaluation-and-golden-examples.md` and
  `docs/collaboration/source-code-quality.md` instead (not in the trace's
  list at all) and found no contradiction, but did not exhaustively re-derive
  the omission list's completeness against every file in the repository.
- Whether the `.cursor/rules/*` complement-only design (per ADR 0006, which
  this change does not touch) is itself sound — treated as settled by ADR
  0006, out of this review's scope.
- Runtime/behavioral testing of an actual multi-agent session operating under
  the new model (e.g., simulating an Implementer that self-reviews dishonestly)
  — out of scope for a documentation/ADR-only Architecture Path change with no
  code to execute.

## Checklist

- [x] The artifact belongs to the phase that was run (Architecture Path,
      documentation/ADR only); no Red/Green/Refactor artifact leaked in.
- [x] Every `Then` clause in the specification is asserted by the work — N/A,
      no application specification exists for this change, confirmed against
      the design agreement's own Specifications section ("None.").
- [x] The dependency rule and port boundaries hold — N/A, no code changed;
      confirmed no `docs/specs/`, port, or data-model file appears in the diff.
- [x] No boundary named in the design agreement was crossed — checked
      specifically: ADR 0006 untouched (diff empty), Preflight/Minor-Fix-Path
      mechanisms reused not redesigned (their templates/specs unmodified
      except for scope wording), no spec/ADR-other-than-0014/port/data-model
      changed.
- [x] Specifications and accepted tests were not modified to make work pass —
      N/A, no tests exist for this change.
- [x] Every claim in the artifact states its grounds — ADR 0014's Context
      section cites the six-round contract-checker history by name; the
      design agreement's Settled Ambiguities table names who decided each
      point.
- [x] The record would let a third party re-run this same search — every
      command above is reproducible verbatim from the branch; the two
      reproduced findings include the exact scratch-copy steps used.

## Decision

- [x] **Approved** — specification-conformance, boundary-conformance, and
      evidence-sufficiency, with two findings tracked as required follow-up
      (non-blocking, Minor-Fix-Path-eligible, per this repository's own
      established pattern of approving with recorded findings — see round 6's
      approval of the contract-consistency checker, which produced LISS-0003).

## Reasons

**Why approved.** ADR 0014's Decision precisely states what is waived
(context separation only) and what is not (the deterministic precondition and
the falsification burden), and every one of the nine contract files, plus
`ai-human-scheme.md`, `personas.md`, `design-agreement.md`,
`definition-of-done.md`, `at-tdd/process.md`, and the templates, restate this
without contradiction — verified by reading each directly, not only through
the checker. The contract-file exclusion (ADR 0006 still governs, unconditionally,
including for this very PR) is stated everywhere the design agreement's scope
requires it and holds in the one place it matters most: ADR 0006 itself is
unmodified. The ADR-count bump (13→14, adopter start 14→15) is complete and
correct everywhere I could find a statement of it. The copy-script propagation
smoke test reproduces cleanly into a fresh target. The tradeoff being accepted
is named plainly, with its own empirical grounds (the six-round
contract-checker history), in ADR 0014, the design agreement, the trace, and
now `README.md` — a future reader would not mistake this for an oversight.

**Why not rejected outright, despite two reproduced findings.** Neither
finding shows the *content* of what shipped is wrong, incomplete, or
dishonest about the tradeoff — both are about the supporting deterministic
tooling and this submission's own process compliance, not about whether
self-review as designed is unsafe. Finding 1 is a latent soundness gap in a
regex that, as verified, does not currently produce a false pass on the real
repository content — every mirror genuinely does state the work-plan-level
Reviewer rule correctly right now. It is a risk to *future* drift-detection,
exactly the class of risk ADR 0014 accepts more of at the self-review layer,
which makes it worth fixing but not a reason to reject content that is
independently confirmed correct today. Finding 2 (missing Preflight record)
is a process gap in submitting this PR, not a verification gap — every check
Preflight exists to cheaply front-load was independently re-run by this
Reviewer directly, from a fresh context, before this approval was issued, so
the substance Preflight protects is not actually missing, only its formal
record.

## Findings (tracked, non-blocking)

**Finding 1 — `EXTRA_MIRRORED_RULES["Work-plan-level Reviewer (ADR 0014)"]`
has a false-negative branch.**

- File: `scripts/check-contract-consistency.py`, lines 151-152.
- Current pattern: `r"work.plan.level Reviewer|whole (?:completed )?work
  plan"`.
- Defect: the second alternative requires no mention of "Reviewer" at all. A
  future mirror could lose the actual work-plan-level-Reviewer rule while
  keeping an unrelated sentence containing "the whole work plan" (e.g., about
  Preflight scope, or work-plan sizing), and mirror parity would still report
  pass. Reproduced in a scratch copy (see Falsification Search #6).
- Suggested correction (Minor Fix Path eligible — a regex change only, no
  spec/ADR/port/data-model/boundary change): require "Reviewer" to co-occur
  with "work plan" in the matched span, e.g. `r"work.plan.level Reviewer|
  Reviewer[^.]{0,80}whole (?:completed )?work plan|whole (?:completed )?work
  plan[^.]{0,80}Reviewer"`, or split into two separately-tracked rules ("work
  plan is reviewed once" and "reviewed by the Reviewer specifically") so each
  half is independently falsifiable the way `MIRRORED_SECTIONS` entries are.

**Finding 2 — No Preflight Validation record for this submission.**

- Expected location: `docs/collaboration/reviews/2026-08-03-*preflight*.md`
  (by analogy with the six `2026-08-02-contract-consistency-preflight-*.md`
  records this repository produced for the comparable-scope prior change).
- Defect: ADR 0013 (unmodified, still in force, explicitly not superseded by
  ADR 0014 per the design agreement's Boundaries section) frames Preflight as
  a step "between Implementer completion and independent review," not scoped
  only to multi-issue work plans. This submission went directly from the
  trace to a PR seeking independent review with no Preflight record, and
  neither the design agreement's Verification section nor the PR itself names
  one as produced or intentionally skipped.
- Note: `.github/pull_request_template.md` itself has no checklist item
  naming Preflight explicitly — this is a pre-existing template gap, not
  introduced by this PR, but it means nothing currently prompts a submitter
  to produce one. Worth a separate, smaller fix to the template.
- Suggested correction: add a Preflight Validation record for this
  submission (retroactively, citing this review's independently-reproduced
  deterministic checks as its evidence, since they are equivalent to what
  Preflight would have produced), and separately, add an explicit Preflight
  checklist line to `.github/pull_request_template.md` so future submissions
  are prompted.

## Falsification Criteria Check (from the covering design agreement)

- "Any of the nine contract files describes the superseded per-phase
  separate-context requirement as still current." — Not found. See
  Falsification Search #3, #4.
- "The self-review layer is used to approve a contract-file change." — Not
  found; ADR 0006 exclusion holds everywhere checked, including for this PR
  itself. See Falsification Search #2.
- "The combined human checkpoint is documented as two separate gates rather
  than one." — Not found. See Falsification Search #10.
- "The tradeoff being accepted... is not stated anywhere a future reader
  would find it." — Not found; stated in ADR 0014, the design agreement, the
  trace, and README.md. See Falsification Search #9.

None of the design agreement's own falsification criteria were met.
