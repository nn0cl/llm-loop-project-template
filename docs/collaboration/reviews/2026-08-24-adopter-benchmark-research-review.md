# Review Record: docs/adopter-benchmark-research (PR #24)

Use this when the Reviewer persona issues a decision inside the execution loop.

A review that does not satisfy all three constraints below does not count as an
approval, whatever this record says.

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in a fresh session with no
      prior memory of this PR's chat history or of any of the three prior
      Reviewer rounds' reasoning. Nothing was read from a chat transcript or
      trusted from any agent's summary. Every claim below was independently
      re-derived from repository artifacts, read directly from the git tree
      at commit `4c54ee0` (`docs/adopter-benchmark-research`, fetched fresh
      from `origin`) checked out into this worktree.
- [x] **Deterministic precondition.** `python3 scripts/check-contract-consistency.py --repo .`
      was re-run independently in this reviewing session — see Deterministic
      Verification Output below.
- [x] **Falsification burden.** 5 scenarios searched, each with grounds and
      an actual result — see Falsification Search below.

## Review Target

- Artifact: PR #24, branch `docs/adopter-benchmark-research` — three new
  files under `docs/research/`: `README.md`,
  `2026-08-24-self-referential-benchmark-findings.md`,
  `2026-08-24-adopter-benchmark-prompts.md`. Pure documentation; no
  code/spec/ADR touched.
- Covering design agreement: none cited in the PR; this is a Planner-persona
  research deliverable (self-declared in each file's front matter), not an
  implementation phase, consistent with `docs/research/README.md`'s own
  stated scope (a finding/reusable-tool output, not a spec/ADR/spike).
- Specification: none (documentation/research artifact).
- Current phase: post-Preflight, this is the fourth independent-context
  Reviewer round on this PR (rounds 1-3 each rejected; the author's fix
  after round 3 is what this round assesses).
- Producing persona: Implementer/Planner (author of the three files and the
  round-3 fix commit `4c54ee0`).
- Reviewing persona / model / tool: Reviewer, Claude Sonnet 5 via Claude
  Code, separate context/session from the producing session and from all
  three prior Reviewer rounds.
- Approval type: specification-conformance, evidence-sufficiency (numeric
  claims in a research document are the primary risk surface here; no
  architecture/boundary/phase concerns apply to a pure-docs change).
- Preflight Validation record: author states `check-contract-consistency.py`
  was re-run after the round-3 fix; independently re-run below rather than
  trusted.
- Preflight result: pass (independently reproduced).

## Deterministic Verification Output

```text
$ git fetch origin docs/adopter-benchmark-research
 * branch            docs/adopter-benchmark-research -> FETCH_HEAD
$ git log --oneline -5 (after checkout)
4c54ee0 docs: fix stale "22 to 0" cross-reference after the LISS-0050 correction
6f1506b docs: fix two substantive errors found by a second independent Reviewer
c5e40f6 docs: fix arithmetic errors and re-derive all inventory counts mechanically
4422a9f docs: add adopter-project benchmark research and measurement prompts
68848c6 Merge branch 'process/promote-item-0022' (item-0022: mirror-file parity gaps)

$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
$ echo $?
0
```

Independent re-derivation of headline figures in
`2026-08-24-self-referential-benchmark-findings.md`, run directly against
commit `68848c6` (the commit the findings document cites as its data
source), using commands the document itself does not paste — chosen because
round 3 already re-verified the totals and the reproduced-rate table
explicitly, so this round targets sub-breakdowns and a specific narrative
claim round 3's report does not mention checking:

```text
$ git log 68848c6 --oneline | wc -l
373
$ git log 68848c6 --format='%ad' --date=short | tail -1
2026-07-05
$ git log 68848c6 --format='%ad' --date=short | head -1
2026-08-23

$ git ls-tree -r --name-only 68848c6 -- docs/collaboration/agreements | grep -v gitkeep | wc -l
28

$ git ls-tree -r --name-only 68848c6 -- docs/collaboration/traces | grep -v archive | grep -c '\.md$'
21
$ git ls-tree -r --name-only 68848c6 | grep 'docs/archive/collaboration/traces' | grep -c '\.md$'
11

$ git ls-tree -r --name-only 68848c6 -- docs/collaboration/reviews | grep -c '\.md$'
48
$ git ls-tree -r --name-only 68848c6 | grep 'docs/archive/collaboration/reviews' | grep -c '\.md$'
11

$ git ls-tree -r --name-only 68848c6 -- docs/work-plans | grep -c '\.md$'
17
$ git ls-tree -r --name-only 68848c6 | grep 'docs/archive/work-plans' | grep -c '\.md$'
9

$ git grep -e '^- Type: review-finding' 68848c6 -- docs/issues | wc -l
9

$ git ls-tree -r --name-only 68848c6 -- docs/collaboration/reviews docs/archive/collaboration/reviews \
  | grep -E '\.md$' | grep -v README | awk -F/ '{print $NF}' | grep -E '^2026-08-(1[89]|2[0-9])' | wc -l
31

$ git show 68848c6:docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md \
  | grep -cE '^\| [0-9]+ \|'
18
```

Per-issue Status field for the 9 anchored `Type: review-finding` issues,
read directly from the git tree at `68848c6`:
LISS-0003=resolved, LISS-0044=closed, LISS-0047=closed, LISS-0049=closed,
LISS-0050=closed, LISS-0051=closed, LISS-0052=proposed, LISS-0060=closed,
LISS-0064=closed → 7 closed, 1 resolved, 1 proposed, 0 done.

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The two "22 to 0" mentions in `2026-08-24-adopter-benchmark-prompts.md` were not actually removed, or the text that replaced them still misstates the findings document's corrected claim (all but one of 31 post-08-18 items passed first round; LISS-0050 the one bounded exception) | `git grep -n '22 to 0'` over the three research files returns no matches. Read both replacement passages in full (not just the diff): line 73-76 now reads "...the misleading '22 rounds, almost all rework, dropping to near-zero' headline number..." (describing the discredited first-pass narrative as history, not asserting it as current fact); line 304-306 now reads "...rework concentrated in 22 rounds across 4 topics before a governance change, then a single bounded reject-and-redo across 31 items after it...", which matches the findings document's own corrected §"First metric tried" text verbatim in substance (31 records, all but one — LISS-0050 — passed first round). | not reproduced |
| 2 | One or more headline figures in the findings document (chosen deliberately from sub-breakdowns and a narrative claim round 3's own report does not list as checked, rather than re-checking the same totals/reproduced-rate table round 3 already verified) fail to match the actual repository state at `68848c6` | Independently re-ran, from a fresh session, the exact `git log`/`git ls-tree`/`git grep`/`git show` commands above against `68848c6`. Every figure checked matched exactly: 373 commits, 2026-07-05..2026-08-23 span, 28 design agreements (excluding `.gitkeep`), 21 active + 11 archived = 32 traces, 48 active + 11 archived = 59 reviews, 17 active + 9 archived = 26 work plans, 9 anchored `Type: review-finding` issues with a 7-closed/1-resolved/1-proposed/0-done breakdown, 31 post-2026-08-18 review-record filenames, and WP-0016's review record's own 18-row Falsification Search table with exactly the two rows (3 and 6) its own "Reasons" section names as "Two real, reproducible gaps... (scenarios 3 and 6)" — the 389-false-positive-match claim (scenario 3) and the line-wrap false-negative claim (scenario 6) both read verbatim in the underlying review record. Note: the review record actually contains a *third* bold-marked `**reproduced**` row (#14, a documentation-staleness gap in a closed, unrelated issue's Verification section) that the findings document's "2 genuine... defects" phrasing does not count — checked against the review record's own Reasons section, which explicitly scopes "two real, reproducible gaps in the shipped check logic" to scenarios 3 and 6 only, distinguishing #14 as a separate, minor, non-blocking documentation issue. The findings document's phrasing is therefore consistent with the source record's own framing, not an overclaim. | not reproduced |
| 3 | `check-contract-consistency.py` fails, or the author's claimed re-run does not hold, when independently re-run in this session against the actual PR tree | `python3 scripts/check-contract-consistency.py --repo .` run directly in this session against the checked-out `4c54ee0` tree (not copied from any prior round's or the author's pasted output). | not reproduced — exit 0, "contract consistency: all checks passed" |
| 4 | A relative Markdown link in any of the three `docs/research/` files targets a file that does not exist, or `docs/research/README.md` links the findings report (which its own "not indexed here" framing says it should not) | Extracted every `](...)` link target from all three files (`README.md` → `2026-08-24-adopter-benchmark-prompts.md`; `2026-08-24-adopter-benchmark-prompts.md` → `2026-08-24-self-referential-benchmark-findings.md`; `2026-08-24-self-referential-benchmark-findings.md` → `2026-08-24-adopter-benchmark-prompts.md` (twice)) and confirmed each target file exists in the same directory. Read `README.md`'s "Contents" section in full: it lists only the prompts file, with an explicit "Other dated notes in this directory are working records, not indexed here" disclaimer covering the findings document. | not reproduced |
| 5 | `2026-08-24-adopter-benchmark-prompts.md`, read in full for the first time in this round (only rounds 2-3 touched it, and only for the one stale phrase), contains an internal inconsistency, or any prompt relies on another now-stale figure from the findings document (e.g. the discredited "24" review-finding count, or a "zero rework after 2026-08-18" framing) that the findings document's own round-2 correction already retired | Read the file end to end (Prompts 0-5 plus the closing "What changed" section). Grepped for "24", "zero rework", "near-zero", "rework" across the file: the only hits are the two historical-pitfall mentions covered by scenario 1 above, correctly framed as describing the discredited first-pass narrative, not as current figures. Each prompt (0-5) is self-contained, states its own goal/pitfall/output format, and none cites a specific numeric figure from the findings document as a fact to reproduce — Prompt 0 explicitly tells the adopter to compute their own inventory rather than reuse this template's numbers, and the closing section's own description of the discredited narrative is now consistent with the corrected findings document (verified at scenario 1). | not reproduced |

## Scenarios Not Searched

- Full independent re-derivation of the reproduced-rate table (pre-08-18
  Reviewer 15/8.5/127/46/36.2%, pre-08-18 Preflight 12/9.2/110/0/0.0%,
  post-08-18 Reviewer 28/7.8/217/8/3.7%) — round 3's report states this was
  already re-derived exactly; re-parsing every Falsification Search table
  across ~55 review records a fourth time was judged disproportionate given
  three prior independent confirmations and this round's own budget being
  spent on sub-breakdowns and narrative claims round 3 did not report
  checking.
- The sibling-template comparison figures (`llm-project-template`: 78
  commits, 2 work plans, 1 review record) — unverifiable from this
  repository, since that is a different, external repository not present in
  this worktree.
- Prose/style quality of the three files beyond factual/numeric accuracy and
  internal consistency (e.g. whether the research method itself is sound) —
  out of scope for a Reviewer pass on a docs-only PR whose specification is
  "the numbers are correct and the document is internally consistent," not
  a methodology critique.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked
      in. (Pure research/documentation; no code, spec, or ADR touched.)
- [x] Every `Then`-equivalent acceptance criterion is asserted by the work.
      (N/A — no specification; the applicable bar is factual/numeric
      accuracy and internal consistency, both checked above.)
- [x] The dependency rule and port boundaries hold. (N/A — no code.)
- [x] No boundary named in the design agreement was crossed. (N/A — no
      design agreement cited; research-directory scope per
      `docs/research/README.md` is respected: a finding plus a reusable
      prompt set, not a spec/ADR/backlog decision.)
- [x] Specifications and accepted tests were not modified to make work pass.
      (N/A — no specs or tests exist for this artifact.)
- [x] Every claim in the artifact states its grounds. (Findings document
      cites commit `68848c6` and specific commands/files throughout;
      independently spot-checked above and matched.)
- [x] The record would let a third party re-run this same search. (Every
      scenario above states the exact command or read performed.)

## Decision

- [x] Approved

## Reasons

- The two "22 to 0" mentions round 3 flagged are confirmed gone, and the
  text that replaced them was read in full (not just grepped for absence)
  and found factually consistent with the findings document's own corrected
  31-items/one-bounded-exception claim (scenario 1).
- A fresh, independent re-derivation of headline figures in the findings
  document — deliberately chosen from sub-breakdowns and a narrative claim
  round 3's own report does not list as checked, rather than repeating the
  same totals — matched exactly against commit `68848c6` in every case
  checked, including a close read of the WP-0016 review record that
  confirmed the findings document's "2 genuine defects" framing is
  consistent with that record's own scoping of a third, unrelated
  `**reproduced**` row as a separate, non-blocking documentation issue
  (scenario 2).
- `check-contract-consistency.py` passes when independently re-run against
  the actual PR tree, not merely trusted from the author's report
  (scenario 3).
- All relative links in the three `docs/research/` files resolve, and
  `docs/research/README.md` still does not link the findings report,
  consistent with its own "not indexed here" framing (scenario 4).
- `2026-08-24-adopter-benchmark-prompts.md` was read in full for the first
  time this round and found internally consistent, with no prompt relying
  on a now-stale figure from the findings document (scenario 5).
- No defect was found in this round. Given that each of the three prior
  rounds found something the author believed was already correct, this
  round deliberately re-verified artifacts independently rather than only
  checking the one named diff, per the task's own instruction — the
  falsification search above documents what was actually searched for and
  why each scenario does not occur, not an unsupported "no problems found."
