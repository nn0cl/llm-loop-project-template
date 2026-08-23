# Self-Referential Benchmark Findings

- Date: 2026-08-24
- Persona: Planner (research/investigation, not an implementation phase)
- Status: closed — superseded by the adopter-project plan in
  [2026-08-24-adopter-benchmark-prompts.md](2026-08-24-adopter-benchmark-prompts.md)

## Question

Can this repository's own git history and collaboration records (design
agreements, ADRs, review records, AI work traces, issues, work plans) be used
directly as a benchmark of whether the Director-centered, closed-loop,
Reviewer-gated process (ADR 0001, ADR 0014) produces measurably better
outcomes than not using it?

## What data exists

At commit `68848c6` (this template's `main` tip throughout this
investigation): 373 commits over 2026-07-05..2026-08-23, 28 design
agreements, 20 ADRs, 32 AI work traces (21 active, 11 archived), 59 review
records (48 active, 11 archived, including Preflight self-review filings),
38 local issues (9 of them carrying `- Type: review-finding` as their own
Metadata field), 26 work plans (17 active, 9 archived under
`docs/archive/work-plans/`). This is a substantial artifact set — the
question was never whether there was enough data, but whether the data
measures what a benchmark needs it to measure.

*Note on verification:* this section went through three revisions before
its numbers held up under independent re-derivation. A first pass summarized
long directory listings by eye rather than counting them (understating
commits, agreements, traces, reviews, issues, and work plans — it missed
`WP-0026` entirely). A first separate-context Reviewer pass caught two
arithmetic slips in the fixed version. A second separate-context Reviewer
pass, re-deriving every figure independently rather than trusting the
document's claim that it had already done so, then caught two further
defects that were not slips: a review-finding count (24) inflated by an
unanchored substring search that matched *mentions* of the term as well as
the field itself (true count, from `git grep -e '^- Type: review-finding'`:
9), and a "zero rework after 2026-08-18" claim that a review record's own
text (`2026-08-19-liss-0050-attempt2-liss-0051-review.md`, which names
itself "Round 2") directly contradicted. Both are corrected below. This
history is left in rather than cleaned up because it is itself evidence for
this document's own thesis: even a document *about* rigorous
self-measurement needed two rounds of independent, adversarial
re-verification — not self-checking — to stop asserting numbers its own
author had not actually confirmed.

A sibling template, `llm-project-template` (this template's predecessor
lineage, forked 2026-07-05), was considered as a comparison point and
rejected: it uses a structurally different governance vocabulary
(per-phase Adjudicator approvals — Scope/Architecture/Technology/Phase/
Implementation — rather than this template's two Director gates plus
in-work-plan self-review plus one separate-context Reviewer pass per work
plan), and has far sparser artifacts over the same calendar window (78
commits, 2 work plans, 1 review record). The independent-context Reviewer
pass this template uses is itself a relatively recent addition
(formalized by ADR 0014, 2026-08-03); no equivalent exists in the sibling
template to compare against. Cross-template numeric comparison was judged
not meaningful and dropped in favor of a single-repository longitudinal
study.

## First metric tried: rework rounds per review topic

Review records were grouped by topic (stripping the date prefix and the
trailing round number) and counted. This produced a striking split:

- 2026-08-02..03 (four topics — `contract-consistency`, `mirror-parity`,
  `work-plan-scoped-governance`, `review-cost-discipline`): 22 total rounds
  across 4 topics, including a Preflight/Reviewer round on
  `contract-consistency` reaching round 6, and one Arbiter escalation on the
  archived `WP-0001` (`review-issues-minor-fix-path`).
- 2026-08-18 onward: 31 review records (every filename dated 2026-08-18 or
  later under `docs/collaboration/reviews/` and its archived equivalent —
  spanning the numbered work plans WP-0010..WP-0026, the archived WP-0002..
  WP-0008 batch, the WP-0009 `contract-reviewer-v230` review, the
  minor-fix-path LISS reviews, and the most recent
  contract-consistency-checker fix): all but one passed on the first round.
  The one exception is itself informative, not a counterexample to what
  follows: LISS-0050 was rejected in
  `2026-08-19-liss-0049-liss-0050-word-boundary-and-line-wrap-fix-review.md`
  (bundled with LISS-0049) and approved on a second attempt in
  `2026-08-19-liss-0050-attempt2-liss-0051-review.md` (bundled with
  LISS-0051) — a single, bounded reject-and-redo cycle through the Minor
  Fix Path, not the same topic bouncing through six rounds the way
  `contract-consistency` did before 2026-08-18.

Read naively, this near-clean split still looks like strong evidence that
ADR 0014/0015 (adopted 2026-08-03, operational from 2026-08-18) fixed the
process. It is not strong evidence of that, for the reason found next.

## Why the naive reading is wrong

Reading the review record bodies (not just their pass/fail verdicts) showed
two things:

1. **Falsification effort did not drop.** Post-2026-08-18 review records
   still perform independent re-execution of scripts, injected synthetic
   defects, and destructive mutation testing — e.g. WP-0016's review
   (`docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md`)
   names 18 failure scenarios and reproduces 2 genuine, previously-unknown
   defects (one of them a real design gap: a short retired term causes
   389 false-positive matches by plain substring search). This is not
   rubber-stamping by volume or by rigor of individual scenarios.

2. **The disposition policy changed, not just the pass rate.** The same
   review record states explicitly why a reproduced, genuine defect did not
   block the work plan:

   > a `review-finding` issue and a follow-up work plan rather than blocking
   > the work plan that shipped the otherwise-correct, otherwise-verified
   > check

   Under the pre-2026-08-18 convention, a reproduced defect caused a
   reject-and-redo round on the *same* review topic (hence
   `contract-consistency-review` reaching round 6). Under the
   post-ADR-0014/0015 convention, a reproduced defect that does not
   invalidate the work plan's own stated scope is spun out as a separately
   tracked `Type: review-finding` issue and, where needed, its own follow-up
   work plan — and the original work plan is still approved. **"Rounds per
   topic" therefore stopped measuring the same thing partway through the
   history it was computed over.** It went from "how many times did this
   exact change get rejected and resubmitted, with no bound observed in
   practice (up to 6, for `contract-consistency`)" to "how many times did
   this exact change get rejected" (after 2026-08-18: zero for 30 of the 31
   items, one bounded single redo for LISS-0050), while genuine
   defect-finding moved to a different, differently-named artifact (the
   review-finding issue).

   Following that thread: exactly 9 issues in `docs/issues/` carry
   `- Type: review-finding` as their own Metadata field (not merely a
   mention of the term in another issue's body — an earlier, looser
   substring search over-counted this at 24); 8 of 9 (88.9%) have reached
   `closed` or `resolved` status (7 closed, 1 resolved, 1 still
   `proposed`, 0 `done`). Findings routed this way are being tracked to
   closure at a high rate, not silently dropped — this weighs against a
   pure rubber-stamping explanation, though it does not resolve the
   confound below.

## Second metric tried: reproduced-defect rate from Falsification Search tables

Every review record's Falsification Search table (`| # | scenario | grounds
| result |`) was parsed and each row's Result cell classified as
`reproduced` or `not reproduced`. Preflight (self-review) filings were kept
separate from Reviewer filings, since they are a different check performed
by a different party under different constraints (no context separation).

| Bucket | n | avg scenarios/review | total scenarios | reproduced | reproduced rate |
| --- | --- | --- | --- | --- | --- |
| Before 2026-08-18 — Reviewer records only | 15 | 8.5 | 127 | 46 | 36.2% |
| Before 2026-08-18 — Preflight (self-review) records only | 12 | 9.2 | 110 | 0 | 0.0% |
| 2026-08-18 onward — Reviewer records | 28 | 7.8 | 217 | 8 | 3.7% |

Scenario depth per review stayed roughly flat (8.5 → 7.8, about a 10%
decrease — not the sharp drop a "reviewer stopped trying" explanation would
predict). The reproduced rate, however, fell by roughly 9.8x (36.2% →
3.7%). This is the actual open question the naive rounds-per-topic metric
had been hiding: is the process finding fewer real defects because
implementers now produce better work up front (a real governance effect,
consistent with Preflight/self-review having been strengthened by ADR
0013/0014/0015), or because the reviewed material itself became
structurally less defect-prone regardless of process?

## The confound that stopped this line of inquiry

The two time buckets are not comparable on subject matter. The
before-2026-08-18 Reviewer sample is almost entirely governance/contract-file
changes: `contract-consistency`, `contract-first-edition`,
`review-cost-discipline`, `work-plan-scoped-governance` — the highest-risk,
most self-referential category this template defines, which ADR 0006 always
routes to a separate-context Reviewer specifically because it is
error-prone. The 2026-08-18-onward sample is almost entirely ordinary
feature/bugfix work plans; the only contract-file change in that period is
`WP-0009` (`contract-reviewer-v230`), a single review record with 0
reproduced defects out of 6 scenarios — far too small a sample to draw a
conclusion from on its own, and not enough to isolate "same subject matter,
different era" from "different subject matter, different era."

**In other words: the process changed and the mix of work being reviewed
changed at close to the same point in the timeline, and this repository's
own history does not contain enough contract-file-only samples after
2026-08-18 to separate the two effects.** Every candidate metric tried
(rework rounds, reproduced-defect rate, scenario depth) inherits this same
confound, because they are all computed over the same single, non-stationary
history.

## Conclusion

This repository is a single, self-referential sample (N=1) whose governance
process itself changed partway through the window being measured, in a way
that is entangled with a simultaneous change in what kind of work was being
done. No metric computed purely from this repository's own artifacts can
cleanly attribute an outcome change to the process rather than to the
changing subject matter. This is a structural limitation of using a
template's own development history to benchmark itself, not a defect in any
one metric definition — a different metric over the same history would
inherit the same confound.

A meaningful benchmark instead requires **independent adopter projects**:
different codebases, different task mixes, ideally spanning a period where
the governance process itself is stable (or where a specific process change
can be isolated with enough before/after samples *of the same task
category* on both sides). The adopter-facing prompt set in
[2026-08-24-adopter-benchmark-prompts.md](2026-08-24-adopter-benchmark-prompts.md)
carries this finding forward: it collects the same raw artifacts this
investigation used, but explicitly separates them by task category and flags
mid-window process changes, so an adopter project's own benchmark does not
repeat this confound blind.
