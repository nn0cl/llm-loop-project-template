# Adopter-Project Benchmark: Measurement Prompts

- Date: 2026-08-24
- Persona: Planner (research deliverable, not an implementation phase)
- Depends on: [2026-08-24-self-referential-benchmark-findings.md](2026-08-24-self-referential-benchmark-findings.md)
  — read that first. Every prompt below exists to avoid a specific pitfall
  found while trying to benchmark this template against its own history.

## Purpose and scope

This is a set of ready-to-paste prompts for measuring whether adopting this
template's Director-centered, closed-loop, Reviewer-gated process
(ADR 0001, ADR 0014) produces measurably better outcomes, run against a
**project that has actually adopted the template** — not against this
template repository itself. Run them from a coding-agent session (this tool
or another) whose working directory is the adopter project's repository.

Each prompt is self-contained: paste it as-is into a fresh agent session.
Run Prompt 0 first — it decides whether the rest are worth running at all.

### What "adopted the template" is assumed to mean

The prompts assume the adopter project keeps the same artifact shapes this
template defines: `docs/collaboration/agreements/`,
`docs/collaboration/reviews/`, `docs/collaboration/traces/`,
`docs/architecture/adr/`, `docs/issues/LISS-*.md`, `docs/work-plans/WP-*.md`,
and review records that include a Falsification Search table (see
`docs/templates/review-record.md`). If the adopter customized paths or
dropped a template file, adjust the paths in each prompt accordingly — the
method matters more than the exact glob.

---

## Prompt 0 — Feasibility and inventory check

**Goal:** decide whether this adopter project has enough data to benchmark
before spending effort on the rest, and surface the single biggest risk
found in the template's own self-referential attempt: a process or contract
change partway through the history being measured.

```text
In this repository, inventory the artifacts a process benchmark would need:

1. `git log --oneline | wc -l` and the first/last commit dates
   (`git log --format='%ad' --date=short | tail -1` /
   `... | head -1`) — total commits and calendar span.
2. Count files in `docs/collaboration/agreements/`,
   `docs/collaboration/reviews/`, `docs/collaboration/traces/`,
   `docs/architecture/adr/`, `docs/issues/`, `docs/work-plans/`
   (and `docs/archive/` equivalents of each, if present).
3. List every commit that touches a file under `docs/architecture/adr/`,
   `docs/collaboration/*.md` (contract/policy files, not per-work-plan
   records), or the root agent-instructions file (e.g. `CLAUDE.md`),
   with dates. These are candidate governance/process changepoints.
4. Report: total counts per artifact type, calendar span, and the dated
   list of governance-file changes from step 3.

Do not compute any rate or trend yet. Just report the inventory and flag,
in plain language, whether there appear to be enough review records
(rule of thumb: at least ~15-20 on each side of any governance change you
want to compare) to support a before/after comparison at all.
```

**Output format expected:** a short inventory table plus a bulleted list of
governance-change dates. If review records number fewer than ~20 total, or
if every governance-file change lands within the last few days of history,
say so plainly rather than proceeding — the template's own attempt hit
exactly this wall (contract-file-only samples on one side of its own
changepoint numbered a single record).

**Pitfall this avoids:** starting metric computation before knowing whether
a governance change happened mid-history. In this template's own repository,
skipping this step is exactly what produced the misleading "22 rounds → 0
rounds" headline number in the first pass of this investigation.

---

## Prompt 1 — Active work time, excluding human decision and off-hours gaps

**Goal:** compute how much time the agent(s) actually spent working per
work plan, excluding waiting on a human Director gate and excluding
overnight/off-hours interruptions — per this project's own request that
human decision time and sleep-driven interruptions be excluded from the
benchmark.

```text
For each work plan under docs/work-plans/ (and its archived equivalents
under docs/archive/work-plans/ if present), find the commits associated
with it (match by branch name, by an explicit "WP-NNNN" mention in commit
messages, or by the files the work plan's own Issue Graph names).

For each work plan's commit timestamps, sorted:
1. Compute the gap in minutes between each consecutive pair of commits.
2. Cluster commits into "sessions": start a new session whenever the gap
   exceeds a threshold (start with 3 hours; report results at 2h and 4h too
   so the threshold's sensitivity is visible).
3. Sum only the intra-session gaps as "active duration" for that work plan.
   Gaps between sessions (including anything spanning a night) are excluded
   entirely, not counted as either active or idle time charged to the plan.
4. Separately, identify and report the elapsed time between:
   a. the work plan's design agreement file's own date/commit and the
      first commit that begins execution (design-phase human decision
      latency), and
   b. the last Reviewer-approval commit and the work-plan close /
      Director-close commit (close-phase human decision latency).
   Report these two separately from active duration — do not fold them in.

Report a table: work plan | active duration (2h/3h/4h threshold) | design
handoff latency | close handoff latency | number of sessions.
```

**Output format expected:** one row per work plan, three active-duration
columns (one per threshold) so the reader can see how threshold-sensitive
the result is, plus the two excluded human-gate latencies reported
separately rather than netted out silently.

**Pitfall this avoids:** a single arbitrary gap threshold silently changing
the answer. Reporting three thresholds side by side surfaces that
sensitivity instead of hiding it in a single chosen number.

---

## Prompt 2 — Rework rounds per review topic (with the disposition caveat)

**Goal:** count how many times each reviewed change was rejected and
resubmitted — but only as one input, never as a standalone verdict on
process quality. Prompt 3 must be run alongside this one; see below for why.

```text
In docs/collaboration/reviews/ (and docs/archive/collaboration/reviews/ if
present), group review record filenames by topic: strip the leading date
and the trailing round-number suffix, and separate "preflight" (self-review)
filings from "review" (Reviewer) filings as different tracks within the same
topic.

For each topic, report: number of preflight rounds, number of review
rounds, and the calendar date range the topic's rounds span.

Then, for every topic that reached exactly 1 review round, open that single
review record and check its Decision/Reasons section (or equivalent) for
any mention of a finding being filed as a separate issue or follow-up work
plan rather than blocking this one (search for phrasing like "review-finding
issue", "follow-up work plan", "tracked separately", or similar). Report,
per topic, whether this disposition-splitting language appears.

Do not conclude from round count alone that a topic "passed cleanly" — a
topic reaching round 1 with a disposition-split defect found is a different
outcome from a topic reaching round 1 with nothing found. Report both.
```

**Output format expected:** a table with columns: topic | preflight rounds |
review rounds | date range | disposition-split language present (Y/N).

**Pitfall this avoids:** exactly the one this investigation fell into on the
template's own repository — reading "1 round" as "reviewer found nothing."
Under this template's own governance model (ADR 0014/0015), a work plan can
pass in one round while a real defect was found and routed elsewhere. Round
count alone conflates "no defect found" with "defect found but not blocking
this plan."

---

## Prompt 3 — Reproduced-defect rate from Falsification Search tables

**Goal:** the metric that actually measures review rigor and defect-finding
outcome, independent of the disposition-routing question in Prompt 2 —
**and split by task category**, which is the confound that stopped this
investigation on the template's own repository.

```text
For every review record under docs/collaboration/reviews/ (and its archived
equivalent), find its Falsification Search table — rows shaped like
"| # | scenario | grounds | result |". For each row, classify the Result
cell as "reproduced" (a genuine defect was found) or "not reproduced",
using this rule: if the cell contains "not reproduced", classify as
not-reproduced; otherwise, if it contains "reproduced" in any form
(including "**reproduced**" or "reproduced — ..."), classify as reproduced.

Separately, classify each review record's SUBJECT MATTER (not the review
record itself) into one of two categories by inspecting which files the
reviewed change actually touched (from its design agreement, work plan, or
the review record's own "Review Target" section):
  - "contract/governance change": touches docs/architecture/adr/,
    docs/collaboration/*.md policy files, the root agent-instructions file,
    or scripts that enforce those contracts.
  - "ordinary change": everything else (features, bugfixes, application
    code, most documentation).

Report a table broken out by BOTH time period (before/after any governance
changepoint found in Prompt 0) AND subject-matter category (contract vs
ordinary): n, avg scenarios per review, total scenarios, total reproduced,
reproduced rate. If any of the four resulting cells has fewer than ~10
review records, say so explicitly next to that cell's numbers rather than
letting the percentage stand alone — a rate computed from a handful of
records is not a trend.
```

**Output format expected:** a 2x2 (or more, if there are multiple
changepoints) table: rows = before/after each changepoint, columns =
contract-change / ordinary-change, cells = n / avg scenarios / reproduced
rate, with a low-n flag inline wherever n < 10.

**Pitfall this avoids:** the confound that ended this investigation on the
template's own repository — comparing a before-period sample that was
almost entirely contract/governance changes against an after-period sample
that was almost entirely ordinary changes, and mistaking a subject-matter
shift for a process effect. Splitting by category before comparing across
time is the fix; if one of the four cells is too small to populate, that is
itself the finding to report, not a gap to paper over with the other three
cells' numbers.

---

## Prompt 4 — Review-finding lifecycle: is routed work actually closed?

**Goal:** check whether findings that get split out from a passing review
(per Prompt 2) are actually tracked to resolution, or quietly dropped — the
check that partly (not fully) rules out a rubber-stamping explanation.

```text
Find every issue file under docs/issues/ (and docs/archive/issues/ if
present) whose type field marks it as a review finding (e.g.
"Type: review-finding"). For each, extract its Status field and, if present,
a creation date and a closing/resolution date (from its own Work Notes /
history section, or from git log on the file: first commit that added it
vs. the commit where its Status field last changed to a closed/done/resolved
value).

Report:
1. Status distribution (counts per status value).
2. Closed rate: (closed + done + resolved) / total.
3. For closed items with both a start and end date recoverable, the
   distribution of days-to-resolution (min/median/max), separately for
   items opened before vs. after any governance changepoint found in
   Prompt 0.
4. List any item open (not closed/done/resolved) for longer than the
   project's own median resolution time, by name — these are the candidates
   worth reading by hand for a rubber-stamping check, not the aggregate
   rate alone.
```

**Output format expected:** status distribution table, closed-rate
percentage, days-to-resolution summary, and a short named list of
long-open outliers.

**Pitfall this avoids:** treating a high closed-rate as proof of rigor by
itself. A finding can be closed by being marked `wont_do` without a grounded
Arbiter decision, or closed quickly without real follow-through. The
closed-rate number is necessary but not sufficient; the named-outlier list
gives a human something concrete to spot-check.

---

## Prompt 5 — Report assembly

**Goal:** combine Prompts 0-4 into one report without smoothing over the
confounds each one was designed to surface.

```text
Using the outputs already collected from prompts 0-4 in this session,
assemble a single benchmark report for this project's adoption of the
llm-loop-project-template process. Structure it as:

1. Inventory and calendar span (from Prompt 0), with governance changepoints
   listed explicitly.
2. Active work time per work plan, all three thresholds shown, human-gate
   latency reported separately (Prompt 1).
3. Rework rounds AND disposition-split flags together, never rounds alone
   (Prompt 2).
4. Reproduced-defect rate broken out by period x category, with low-n cells
   flagged (Prompt 3).
5. Review-finding closure rate, days-to-resolution, and named long-open
   outliers (Prompt 4).
6. A conclusion section that states, explicitly, for each of sections 3-5:
   whether the sample size and category balance were sufficient to draw a
   before/after conclusion, and if not, what additional data (more work
   plans of a specific category, more time elapsed) would be needed. Do not
   state a process-quality conclusion for any comparison where one side of
   the split has fewer than ~10 records — say the comparison is
   inconclusive at current sample size instead.

Write this report in [PROJECT'S OWN docs.language SETTING, if the project
has a loop-settings.toml — otherwise match the language this repository's
own documents are written in].
```

**Output format expected:** a single Markdown report following the
structure above, suitable for placing under this adopter project's own
`docs/research/` (or equivalent) directory.

**Pitfall this avoids:** synthesis steps are where confounds most often get
silently dropped, because a clean narrative is more satisfying to write than
a caveated one. Section 6 exists specifically to force the same discipline
this template's own review records require of a Reviewer: name what was not
established, not just what was.

---

## What changed from the template's own self-referential attempt

This prompt set exists because running an equivalent of Prompts 2-3 directly
against `llm-loop-project-template`'s own history produced a misleadingly
clean-looking result (rework rounds dropping from 22 to 0) that fell apart
under two follow-up checks: reading review record bodies instead of trusting
pass/fail verdicts (Prompt 2's disposition-split check), and splitting the
reproduced-rate by subject-matter category instead of by time period alone
(Prompt 3's category split). Both checks are now built into the prompts
themselves rather than left as something a benchmark author has to discover
independently, the way this investigation had to.
