# Review Record: LISS-0047 Facet-4 Split-Wording Fix (Minor Fix Path)

Lighter structure than `docs/templates/review-record.md`, per `CLAUDE.md`'s
Minor Fix Path — this is a review-finding correction confirmation, not a
work-plan-level review.

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in a context with no prior
      memory of this fix or of WP-0015. No chat transcript from the session
      that made the correction was read or trusted. The reviewing worktree
      was moved to commit `6b37de9` on `origin/process/item-0012-remaining-facets`
      (`git fetch origin`, `git checkout 6b37de9`, confirmed via `git log
      --oneline -1`) before any of the four touched files, or the finding
      they answer, was read. Everything below was independently re-derived:
      item-0012's own facet 4 paragraph, ADR 0008's actual Tiered Sync
      Policy text, `contract-file-sync-prompt.md`'s actual Steps 2-4, the
      originating review record's scenario 10, LISS-0047's Acceptance
      Notes, and `git diff`/`git show` on the actual commit — not the
      fix's own framing of any of these, taken as claims to verify rather
      than facts.
- [x] **Deterministic precondition.** `scripts/check-contract-consistency.py`
      re-run independently in this session against the actual current tree
      at `6b37de9`. Output recorded below.
- [x] **Falsification burden.** Named failure scenarios below, each with
      grounds and a result.

## Review Target

- Artifact: the four-file wording correction at commit `6b37de9` —
  `docs/collaboration/agreements/2026-08-19-contract-sync-diff-records.md`,
  `docs/issues/LISS-0046-contract-sync-diff-records-and-agent-registry.md`,
  `docs/issues/LISS-0047-facet-4-template-target-split-granularity.md`,
  `docs/work-plans/WP-0015-contract-sync-diff-records.md`
- Finding answered: `docs/issues/LISS-0047-facet-4-template-target-split-granularity.md`
  (originating in `docs/collaboration/reviews/2026-08-19-wp-0015-contract-sync-diff-records-review.md`,
  scenario 10)
- Path: Minor Fix Path — planning size `S`, no specification/ADR/port/
  data-model/architecture-boundary change, single attempt
- Producing persona: Design & Review group (Planner), per LISS-0047's own
  Work Notes entry
- Reviewing persona / model / tool: Reviewer, Claude Sonnet 5 via Claude
  Code, separate context/worktree from the session that made the fix

## Deterministic Verification Output

Re-run independently in this reviewing worktree, at commit `6b37de9`:

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
```

Exit code: 0.

Scope re-verification:

```text
$ git diff 4286567..HEAD --name-status
M	docs/collaboration/agreements/2026-08-19-contract-sync-diff-records.md
M	docs/issues/LISS-0046-contract-sync-diff-records-and-agent-registry.md
M	docs/issues/LISS-0047-facet-4-template-target-split-granularity.md
M	docs/work-plans/WP-0015-contract-sync-diff-records.md
```

Exactly the four files the finding names as needing correction. No artifact
under `docs/templates/`, no `sync-diff-record.md`, no
`prompt-instruction-change-control.md`, no ADR 0008, and no code/script file
was touched — this is a pure wording correction, not a re-run of any
implementation work.

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The correction misrepresents ADR 0008's actual mechanism (e.g., claims it is content-level, or claims something ADR 0008 doesn't say) | Read ADR 0008's "Tiered Sync Policy" section independently. Tier 1/Tier 2 is decided once per file via `is_contract_persona_file`; Tier 1 wins outright with no merge, Tier 2 is flagged for reconciliation. Nothing in ADR 0008 classifies content within a file. The corrected DA/LISS-0046/WP-0015 text says exactly this ("addresses... at the whole-file level... not, by itself, at the content level within one file") — accurate. | not reproduced |
| 2 | The correction misrepresents `contract-file-sync-prompt.md`'s Steps 2-4 (e.g., claims it produces a standing document, or overstates what it does) | Read Steps 2-4 independently: Step 2 diffs target-current vs. template-old to find adopter facts; Step 3 diffs template-old vs. template-new to find template's own changes; Step 4 merges, flagging conflicts as open questions. The corrected text calls this "the existing per-sync-event reconciliation process," never claims it is a standing document, and explicitly contrasts it against a hypothetical ahead-of-time registry (Resolution 2, not built). Accurate, no overstatement in either direction. | not reproduced |
| 3 | The correction silently edits away the original overstated claim instead of leaving evidence per Invariant 2 | `git diff 4286567..HEAD -- docs/issues/LISS-0046-...` shows the original Work Notes entry ("Research confirmed ADR 0008's Tiered Sync Policy already satisfies...") is untouched; a new, separately dated Work Notes entry is appended below it, explicitly naming itself a correction. Same pattern in LISS-0047's own Work Notes (original Reviewer-opened entry kept, Planner's resolution entry appended). The Design Agreement's Direction section is edited in place (not a chronological log), but the change and its reason are recorded in the agreement's own Reopening Log row — the correct mechanism for that document type. | not reproduced |
| 4 | LISS-0047's own `Status` field was advanced further than this fix is entitled to (e.g., to `resolved`) | `git diff 4286567..HEAD -- docs/issues/LISS-0047-...` shows `Status: proposed` -> `Status: in_progress` only. Not `resolved`. Matches the fix's own stated posture ("pending separate-context Reviewer confirmation"). | not reproduced |
| 5 | WP-0015's Work-Plan Review findings table claims a status for LISS-0047 other than `in_progress` | Table row reads `\| LISS-0047 \| in_progress \| ... \|`. Matches. | not reproduced |
| 6 | Some file outside the four named in the finding was also changed (scope creep, artifact rebuild) | `git diff 4286567..HEAD --name-status` — see Deterministic Verification Output above — exactly four files, all named by the finding. | not reproduced |
| 7 | `check-contract-consistency.py` fails against the corrected tree | Re-run independently at `6b37de9`: `contract consistency: all checks passed`, exit 0. | not reproduced |

## Independent Judgment on the Resolution-1 Substantive Question

This is the part that matters, and I read item-0012's facet 4 paragraph
myself, independently of how the finding or the fix each frame it:

> Split rules explicitly into Template-owned (shared path/phase/review/
> sync/logging conventions) versus Target-owned (adopter-specific
> language/domain/architecture/ADRs). Syncing should not mean "make every
> mirror file textually identical" — it should produce a diff record
> naming: the template's own change, the target's own change, any
> conflict, and the adopt/reject/defer decision for each. Where
> per-agent-tool differences are intentional..., record which rule
> applies to which agent in a canonical document rather than treating the
> difference as an error.

Two readings are both available in this text, and I want to state both
honestly rather than pick the convenient one:

- **The stricter reading** (closer to what the original finding leans
  toward): sentence 1 is its own independent directive — "split rules...
  into Template-owned versus Target-owned" reads as an artifact to
  produce (a classification that exists and can be consulted), separate
  from sentence 2's diff-record ask. Under this reading, a reader who
  wants to know, for a rule that has never yet been touched by a sync,
  whether it is template- or target-owned, has nothing to consult —
  Resolution 1 never produces that answer ahead of an actual sync event,
  only after one occurs on that specific file.
- **The reading the fix adopts (Resolution 1)**: the paragraph is one
  flowing description of a single mechanism, not three independent
  asks. "Split rules explicitly" is satisfied by *how* the sync is done
  (explicitly separating template's-own-change from target's-own-change,
  per Steps 2-3 of `contract-file-sync-prompt.md`, rather than a blind
  merge), and the diff record is exactly where that explicit split gets
  written down. Facet 4's own two example category lists ("shared path/
  phase/review/sync/logging conventions" vs. "adopter-specific language/
  domain/architecture/ADRs") read naturally as guidance an agent applies
  *during* that per-event diffing step, not necessarily as entries in a
  pre-built lookup table.

Weighing these against each other: the stricter reading has real force —
sentence 1 is grammatically its own sentence, and "split rules explicitly"
most naturally suggests an artifact a reader can inspect, which a
per-event process genuinely does not provide for an as-yet-unsynced rule.
That gap is real, and the fix does not pretend otherwise — it is exactly
what the original finding (scenario 10) identified, and this fix does not
claim to have built anything new that closes it; it only reclassifies
whether the existing mechanism already counts as an adequate answer.

But the fix's reading is not a stretch to the point of being
indefensible. Facet 4's own second sentence is explicitly about *syncing*
("syncing should not mean... it should produce a diff record"), and the
whole paragraph is titled "Single-source multi-agent contract sync" — its
subject throughout is the sync mechanism, not a general documentation
requirement. Read that way, "split rules explicitly" as a lead-in to "so
that syncing produces a diff record" is a legitimate architectural
choice: making the split durable and explicit *at the point where it is
actually consequential* (a real sync, where getting it wrong would
silently destroy an adopter's fact or bury a template improvement) rather
than maintaining a standing document that could drift out of date between
syncs with no sync ever having caught the drift. A standing document
(Resolution 2) is not obviously more correct — it would need its own
upkeep discipline the paragraph doesn't specify, and nothing in facet 4's
wording rules out an at-sync-time delivery of the split.

My own conclusion: **Resolution 1 is a genuinely defensible reading**, not
a rubber-stamped convenience. It is not the only reading, and I would not
call it the stronger of the two on the text alone — if I were deciding
this from scratch with no prior reasoning to weigh, I could plausibly land
on Resolution 2 instead. But the fix does not hide this: LISS-0047's own
Work Notes state the reasoning explicitly, quote the paragraph's own
structure to support it, and explicitly disclaim that Resolution 1 is not
a permanent foreclosure — "if a future session finds the dynamic-process
answer insufficient in practice, that is a new finding against this same
question, not a reopening of this one." That is the right posture for a
genuinely close call: a reasoned, disclosed judgment, with an explicit
escape hatch for a future session that weighs the same tradeoff
differently once there is real per-sync-event evidence to look at (i.e.,
after the Sync Diff Record mechanism has actually run a few times against
Tier 2 files and someone can judge whether the split it produces is
functioning as an adequate substitute for a standing document).

Per this task's own framing, a Minor Fix Path confirmation is not the
venue to relitigate an already-reasoned Planner judgment call from
scratch — my job is to confirm the reasoning is sound and disclosed, not
to independently redesign the mechanism. The reasoning is sound (it
engages honestly with the paragraph's actual structure, not just its
surface wording) and it is disclosed (in LISS-0047's Work Notes, the
Design Agreement's Reopening Log, and cross-referenced from LISS-0046 and
WP-0015). I confirm it on that basis, while recording for any future
reader that this is a closer call than the corrected wording alone
conveys, and that the stricter reading remains available as grounds for a
future finding if the dynamic process proves insufficient in practice.

## Checklist

- [x] The corrected wording in all three files (agreement, LISS-0046,
      WP-0015) accurately distinguishes ADR 0008's whole-file split from
      facet 4's content-level split, without introducing a new inaccuracy
      (scenarios 1-2).
- [x] `git diff 4286567..HEAD` shows only the wording correction — no
      artifact rebuilt, no scope change, no file outside the four named by
      the finding (scenario 6, Deterministic Verification Output).
- [x] The correction is transparent about being a correction: LISS-0046's
      original Work Notes entry is left in place, a new dated entry is
      appended (scenario 3).
- [x] LISS-0047's own `Status` field is `in_progress`, not `resolved`
      (scenario 4) — this review's confirmation is what would allow that
      next step, not something the fix claimed for itself.
- [x] WP-0015's Work-Plan Review findings table lists LISS-0047 as
      `in_progress` (scenario 5).
- [x] `scripts/check-contract-consistency.py` passes, re-run independently
      against the actual current tree (scenario 7).
- [x] The Resolution-1 substantive judgment call is independently examined
      against item-0012's own facet 4 wording, not merely accepted on the
      finding's or the fix's framing (see Independent Judgment section
      above).

## Decision

- [x] Approved
- [ ] Rejected — reasons and the specific artifact changes required
- [ ] Deadlocked — escalate to Arbiter, with both positions stated
- [ ] Reopening request — the design agreement does not settle this; state
      what is unsettled and what the loop needs in order to continue

## Reasons

- Mechanical accuracy holds: the corrected text in all three files matches
  an independent reading of both ADR 0008 and `contract-file-sync-prompt.md`,
  and introduces no new inaccuracy (scenarios 1-2).
- Scope is exactly the four files the finding names; nothing else in the
  repository changed (scenario 6).
- The correction is transparent per Invariant 2 — original claims are
  preserved, corrections are appended/logged, not silently rewritten
  (scenario 3).
- Status fields are exactly where they should be at this point in the
  lifecycle: LISS-0047 `in_progress` (not `resolved`), WP-0015's findings
  table `in_progress` (scenarios 4-5) — this review's own Approved
  decision is what the Design & Review group needs to advance either
  field further, which this review does not do itself.
- `scripts/check-contract-consistency.py` passes, independently re-run
  (scenario 7).
- On the substantive question: Resolution 1 is a genuinely defensible,
  reasoned, and disclosed reading of facet 4's own wording — not the only
  possible reading, and not obviously the stronger one on the text alone,
  but sound enough, and honest enough about its own limits (the explicit
  disclaimer that a future finding remains available), to confirm under
  Minor Fix Path's actual charge: verify the reasoning is sound and
  disclosed, not redesign the mechanism from scratch.

## Non-Blocking Observations

- The stricter reading of facet 4's sentence 1 (a standing, ahead-of-time
  artifact, separate from the diff-record mechanism) remains available.
  If, after the Sync Diff Record mechanism has actually run against real
  Tier 2 syncs, a future reader judges the per-event process is not in
  practice producing an adequately explicit split, that is grounds for a
  new finding against this same question — not a defect in this fix, and
  not something this fix should have pre-empted, since LISS-0047's own
  Work Notes already say so explicitly.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
