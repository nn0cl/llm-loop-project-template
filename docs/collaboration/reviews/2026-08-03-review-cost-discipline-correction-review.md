# Review Record: Review Cost Discipline — Correction (PR #12)

Reviewing persona: Reviewer.

Model / tool: Claude Sonnet 5, via a fresh Claude Code agent invocation with
no memory of any prior session, dialogue, or reasoning about this repository.
Nothing from the Implementer's producing session was supplied as context.
Every claim below was independently re-derived from the checked-out branch
`process/review-cost-discipline-fixes` (commits `daf62e6`, `8188a52`, on top
of `main` at `a11c2df`, tag `v2.1.0`), `git show`/`git diff`, directly re-run
commands, and scratch copies of the repository used for negative testing.
This is a fresh-context review, not a resumed session — per the covering
design agreement's own required condition for this task (DA-2026-08-03-03,
Plan #9).

## Constraints (all three must hold)

- [x] **Context separation.** Did not produce any artifact on this branch —
      `self-review.md`, the two `EXTRA_MIRRORED_RULES` entries, the five
      Preflight-carrying files' scope marker, the rewritten design agreement
      and trace, `prompt-instruction-change-control.md`, or ADR 0015's
      rewrite. No reasoning from the producing session was supplied or relied
      on. Every finding below was re-derived from the checked-out tree, `git
      show`, and commands I ran myself in this session, including scratch
      copies under `/tmp` independent of the working tree.
- [x] **Deterministic precondition.** All checks below were run in this
      session against the real branch and against scratch copies. Output is
      pasted, not summarized.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below, each with the grounds on which it does or does not occur,
      including two scenarios outside the seven named findings.

## Review Target

- Artifact: branch `process/review-cost-discipline-fixes` (GitHub PR #12),
  commits `daf62e6` and `8188a52`, based on `main` at `a11c2df` (tag
  `v2.1.0`). 15 files changed, +1259/-105.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-03-review-cost-discipline-correction.md`
  (DA-2026-08-03-03).
- Specification: none — process/governance change. The record this work is
  judged against is
  `docs/collaboration/reviews/2026-08-03-review-cost-discipline-review.md`'s
  "Required artifact changes" (items 1-6), per DA-2026-08-03-03's own
  Specifications section, plus a Director-instructed self-review
  search-scope refinement (item 7) folded into the same plan.
- Current phase: Architecture Path, documentation/ADR/template/CI only. No
  Red/Green/Refactor artifact; phase-correctness does not apply beyond
  confirming no application code was touched (confirmed — none was).
- Producing persona: Implementer, per both trace files
  (`docs/collaboration/traces/2026-08-03-review-cost-discipline-correction.md`
  and the rewritten `docs/collaboration/traces/2026-08-03-review-cost-discipline.md`),
  both of which now state this explicitly (Finding 5's own remediation,
  confirmed present).
- Reviewing persona / model / tool: Reviewer / Claude Sonnet 5 / Claude Code.
- Approval type: specification-conformance, boundary-conformance,
  evidence-sufficiency.
- Preflight Validation record:
  `docs/collaboration/reviews/2026-08-03-review-cost-discipline-correction-preflight.md`,
  produced by the Implementer (states so explicitly, and states it is not an
  approval).
- Preflight result: **pass**, as recorded — independently re-run below rather
  than trusted.

## Deterministic Verification Output

**Contract consistency checker, on the checked-out branch:**

```text
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```

**Negative test 1 — delete the short-form-default sentence (sentence A) from
`CLAUDE.md` in a scratch copy, confirm the new rule fails (not just the old
`"Self-review (ADR 0014)"` rule, which the rejection record showed could not
detect this):**

```text
$ cp -R <repo> /tmp/negtest/repo && cd /tmp/negtest/repo
$ python3 - <<'PY'
path = 'CLAUDE.md'
txt = open(path).read()
sentence_a = '''Use `docs/templates/self-review.md`'s short form by default (size `S`);
escalate to the full form only at size `M` or larger, per
`docs/architecture/adr/0015-review-cost-discipline.md`.
'''
assert sentence_a in txt
open(path, 'w').write(txt.replace(sentence_a, ''))
PY
$ python3 scripts/check-contract-consistency.py --repo .

mirror parity:
  CLAUDE.md does not state 'Self-review short-form default (ADR 0015)' (no match for /self-review\.md.{0,20}short form/)

contract consistency: 1 failure(s)
```
Exit code 1. Confirmed.

**Negative test 2 — delete the finding-response scope-marker paragraph
(sentence B) from `CLAUDE.md` in a fresh scratch copy, confirm the second new
rule fails:**

```text
$ python3 scripts/check-contract-consistency.py --repo /tmp/negtest2/repo

mirror parity:
  CLAUDE.md does not state 'Finding-response delta guidance (ADR 0015)' (no match for /review finding on a\b/)

contract consistency: 1 failure(s)
```
Exit code 1. Confirmed.

**Negative test 3 — same as test 1, but on the "grok" mirror, which
concatenates three physically separate files
(`.grok/rules/{01,02,03}...md`) rather than one. Sentence A lives in
`02-architecture-boundaries.md` for this mirror, not `03` — confirming the
rule still has teeth on the split-file layout, not just the monolithic one:**

```text
$ python3 scripts/check-contract-consistency.py --repo /tmp/negtest3/repo

mirror parity:
  grok does not state 'Self-review short-form default (ADR 0015)' (no match for /self-review\.md.{0,20}short form/)

contract consistency: 1 failure(s)
```
Exit code 1. Confirmed.

**Negative test 4 — same as test 2, on `.github/copilot-instructions.md`
(the "copilot" mirror):**

```text
$ python3 scripts/check-contract-consistency.py --repo /tmp/negtest4/repo

mirror parity:
  copilot does not state 'Finding-response delta guidance (ADR 0015)' (no match for /review finding on a\b/)

contract consistency: 1 failure(s)
```
Exit code 1. Confirmed. All three `FULL_MIRRORS` targets (`CLAUDE.md`,
`copilot`, `grok`) independently confirmed to fail closed when either
sentence is removed from any of their constituent files.

**Old-loophole check — did either new sentence already exist, in any form,
in any of the eight full-mirror-constituent files before ADR 0015 (the exact
shape of the pre-existing-content loophole the rejection record found in the
old `"Self-review (ADR 0014)"` rule)?**

```text
$ for f in CLAUDE.md .github/copilot-instructions.md \
    .grok/rules/01-quickstart.md .grok/rules/02-architecture-boundaries.md \
    .grok/rules/03-collaboration-and-completion.md; do
    git show 53c339e^:"$f" | grep -c "self-review.md\|short form\|review finding on a"
  done
0
0
0
0
0
```
None of the eight full-mirror files (five shown; `AGENTS.md` and the two
`.cursor` files, not checked by `check_mirror_parity`, were also confirmed at
0) contained either phrase before ADR 0015 introduced them. The new rules are
anchored on genuinely new text, not text every mirror already had.

**`required_files` count and existence, read directly from
`.github/workflows/ci.yml`, checked against the working tree:**

```text
$ (70-entry required_files array extracted from ci.yml and checked with
   os.path.isfile)
70 entries, missing: []
```

**ADR loop range and file count:**

```text
$ grep -n "for n in 0001" .github/workflows/ci.yml
108:          for n in 0001 0002 0003 0004 0005 0006 0007 0008 0009 0010 0011 0012 0013 0014 0015; do
$ ls docs/architecture/adr/*.md | wc -l
      15
```

**Stale ADR-count sweep across entry documents:**

```text
$ grep -n "0001.*0014\|fourteen ADRs\|14 件" README.md README.ja.md \
    QUICKSTART.md QUICKSTART.ja.md docs/architecture/README.md
(no output)
```

**`bash -n` on touched/exercised shell scripts:**

```text
$ bash -n scripts/copy-ai-collaboration-files.sh scripts/update-ai-collaboration-files.sh \
    scripts/init-llm-context.sh scripts/lib/collaboration-template-paths.sh
(no output — syntax OK)
```

**Conflict-marker sweep:**

```text
$ grep -rn "^<<<<<<<\|^=======$\|^>>>>>>>" --include="*.md" --include="*.py" \
    --include="*.sh" --include="*.yml" --include="*.mdc" .
(no output)
```

**Fresh copy-script target, `check-contract-consistency.py` re-run against
the adopter copy (the exact check that caught the dangling-reference defect
fixed in commit `8188a52`):**

```text
$ mkdir -p /tmp/copytest/target
$ bash scripts/copy-ai-collaboration-files.sh --target /tmp/copytest/target
...
Done.
$ python3 scripts/check-contract-consistency.py --repo /tmp/copytest/target
contract consistency: all checks passed
```

**GitHub CI status on PR #12:**

```text
$ gh pr checks 12
Repository sanity	pass	10s	https://github.com/nn0cl/llm-loop-project-template/actions/runs/30796047209/job/91629749776
$ gh pr view 12 --json mergeable -q '.mergeable'
MERGEABLE
```
Confirmed via the run log that the same job also ran and passed "Check
template copy smoke test" and "Check agent operating contract change
traceability" as sub-steps of the single "Repository sanity" job, not just
the headline name.

**Commit `8188a52`'s own fix, independently confirmed as a real, necessary
correction rather than cosmetic:** `git show 8188a52` removes two references
to `docs/collaboration/reviews/2026-08-03-review-cost-discipline-review.md`
from `ADR 0015` and `prompt-instruction-change-control.md` (both files that
ship to every adopter via the copy script, which always skips
`docs/collaboration/{agreements,traces,reviews}/*` as this repository's own
history). Confirmed the copy-script smoke test above passes only because of
this fix — the reference would otherwise be dangling in any adopter copy.

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur / does occur | Result |
|---|---|---|---|
| 1 | `self-review.md`'s short form still permits a one-line summary instead of pasted output, anywhere, including the full-form escalation path (Finding 2). | Read the full current template. The short form now reads `Result: <the actual output, pasted>` with an explicit paragraph: "`Result` is the actual output, always. Not a summary... If the output is too long to paste whole, paste the last 20–30 lines and the exact command a reader can re-run to see the rest; do not replace the output with a hand-written description." The full form defers to `review-record.md`'s own "Deterministic Verification Output" section, which states "Paste the actual output. A summary of it is not evidence." Checked `review-record.md` directly (not just trusted the pointer) — no escape hatch there either. No loophole found in either path. | not reproduced |
| 2 | The new `EXTRA_MIRRORED_RULES` entries are satisfiable by unrelated pre-existing text, the way the old `"Self-review (ADR 0014)"` rule was satisfied by ADR 0014's own prior content (rejection record Finding 3). | Checked all eight full-mirror-constituent files (`CLAUDE.md`, `copilot-instructions.md`, three `.grok/rules/*.md`) at `53c339e^` (immediately before ADR 0015) for either phrase: zero occurrences anywhere. The anchors are genuinely new text, not text every mirror already had. Also ran four independent negative tests (deleting sentence A or B from `CLAUDE.md`, `.grok/rules/02-architecture-boundaries.md`, and `.github/copilot-instructions.md`) — all four correctly produce a failure naming the specific missing rule. See Deterministic Verification Output above. | not reproduced |
| 3 | The regex proximity window (`.{0,20}` / `\b` anchors) could be satisfied by two unrelated mentions sitting near each other by coincidence, the way the script's own docstring warns `EXTRA_MIRRORED_RULES` proximity rules can be (a documented, structural limitation of this checker, not specific to this PR). | The two new patterns are tight (20-char window on one; a fixed 15-character literal phrase plus word boundary on the other) and, per test 2 above, anchor on genuinely novel phrasing. I found one real fragility: `self-review\.md.{0,20}short form` does not match across a markdown line-wrap (Python `.` does not match `\n` without `re.DOTALL`), so in `CLAUDE.md` the pattern currently matches only sentence A, not sentence B (sentence B's "self-review.md`'s" and "short form" are split across a line break). This is not a false-negative today — negative test 1 confirms deleting sentence A alone is still caught — but it means the rule's specificity is partly an accident of the current line-wrap, not a designed property; a future reflow of sentence B onto one line would make the rule satisfiable by either sentence, weakening (not breaking) its power to catch sentence A's specific deletion in the case where sentence B still exists. Worth noting for future maintenance, not blocking. | reproduced (minor, non-blocking fragility) |
| 4 | The scope-marker fix (Finding 6) is unambiguous in all five Preflight-carrying files, not just moved. | Read the exact paragraph in `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.cursor/rules/03-collaboration-and-completion.mdc`, `.grok/rules/03-collaboration-and-completion.md` directly (not via grep alone). All five now read, verbatim: "...always requires a separate-context Reviewer — including a fix that answers a Reviewer finding on a contract-file change; the short form below documents that fix, it does not exempt it from separate-context approval." followed by a paragraph break and "For a review finding on a **non-contract-file** change: ...". The explicit "non-contract-file" marker removes the ambiguity the rejection record named — a reader can no longer reach the misreading that a contract-file finding-response is exempted from separate-context review. | not reproduced |
| 5 | The rewritten design agreement (DA-2026-08-03-02) still omits a `design-agreement.md`-required field. | Compared section-by-section against `docs/templates/design-agreement.md`. Present and filled: Identity, Direction, Scope, Plan, Specifications, Boundaries, Settled Ambiguities, Deferred Questions, Verification, Falsification Criteria, Agreement, Reopening Log. Every field the template requires is present with substantive (not placeholder) content. | not reproduced |
| 6 | The rewritten trace(s) do not conform to `ai-work-trace.md` or fail to name a persona. | Compared both `docs/collaboration/traces/2026-08-03-review-cost-discipline.md` and `docs/collaboration/traces/2026-08-03-review-cost-discipline-correction.md` section-by-section against the template. Both use all eleven top-level sections, both state `Active persona: Implementer` explicitly in the Request section. | not reproduced |
| 7 | The "no Director-override exception to ADR 0006" language, added to `prompt-instruction-change-control.md` and ADR 0015, contradicts something elsewhere in the contract (Minor Fix Path, Arbiter provisions, `ai-human-scheme.md`). | Read `ai-human-scheme.md` in full (all "Director" mentions), `personas.md`'s Arbiter section, the Minor Fix Path text in `CLAUDE.md`/`AGENTS.md`, and ADR 0006 itself. Nothing anywhere grants the Director authority to waive a separate-context Reviewer requirement; the Minor Fix Path explicitly still requires "separate Reviewer confirmation"; the Arbiter settles Implementer/Reviewer disagreements, not Director overrides of the review gate itself; ADR 0006's own Decision section states the requirement with no override clause. The new language closes a gap rather than opening a contradiction. | not reproduced |
| 8 | This branch's own diff introduces a regression the seven named findings did not cover (open-ended sweep beyond the brief). | Diffed every one of the 15 changed files against `a11c2df` directly, not only the files the rejection record named. Found: (a) `CHANGELOG.md`'s `v2.1.0` entry still reads "**Unreviewed.** Per explicit Director instruction, independent review was skipped for this release," with no pointer to the fact that this was later found to be an unauthorized boundary violation and corrected — this entry was written at the original (defective) release and this branch does not touch `CHANGELOG.md` at all. This is a real, first-time-observed gap: a reader of the changelog alone — the one required, adopter-shipped file most likely to be read in isolation — gets a materially stale picture. (b) The rejection review document itself, `docs/collaboration/reviews/2026-08-03-review-cost-discipline-review.md`, does not exist anywhere in this repository's git history before commit `daf62e6` — the same commit that also fixes every finding it names. `git log --all --oneline -- <that path>` returns exactly one commit. There is no independently-committed, independently-timestamped record that the rejection review predated the fix as a genuinely separate act; both were authored by the same account in the same commit. This does not, by itself, mean the review was not genuinely produced in a separate context (Claude Code sessions can differ even when committed together), but it is unverifiable from repository history, which is the same category of evidentiary gap ADR 0001 and this contract's own invariants exist to prevent ("a command that was run has its output recorded... a claim is not evidence" applies equally to "a review that was independently produced"). I re-derived every one of the seven findings' substance myself in this session rather than relying on that document's authority, so this gap does not undermine my own approval of the content — but it is a real, first-time-observed process gap worth recording. | reproduced (both, non-blocking) |
| 9 | `check_parity_completeness` (every `AGENTS.md` section classified) or `check_references` regressed because of this branch's edits. | Diffed `AGENTS.md`'s `## ` headings before and after this branch: identical set, no new or removed headings. Full consistency-checker run (which includes both checks) passes with zero failures on both the working tree and the fresh copy-script target. | not reproduced |
| 10 | DA-2026-08-03-03's own Falsification Criteria are vague restatements rather than checkable conditions. | Read the four listed criteria. Each names a specific, checkable observable: a false positive against copy-script output (checked directly above — none found), a design-agreement/trace field still missing (checked directly — none missing), a contradiction in the no-override language (checked directly — none found), and merging without recorded Reviewer approval (directly checkable — as of this review, not yet merged; PR #12 is open). All four are genuine negative cases, not restatements of the plan. | not reproduced |

## Scenarios Not Searched

- Whether GitHub branch-protection settings on this repository actually
  require a review before merge (a server-side control this contract's own
  documents note "repository documents alone cannot enforce") was not
  checked via the GitHub API. This review rests on the contract's own stated
  rule and this record's approval, not on whether the hosting platform
  additionally permits a bypass.
- I did not attempt to independently re-verify ADR 0015's underlying
  diagnosis (the specific line-count/round-count figures in its Context
  section) a second time — the prior rejection review already flagged this
  as unsearched and it is unchanged by this correction; it is not one of the
  seven findings this branch answers.
- I did not have another model or tool available to cross-check this
  review's own regex/negative-test work; all verification in this record was
  produced by the same model (Claude Sonnet 5) that will also be credited as
  Reviewer here. The design agreement's own text notes "different model...
  is recommended, not required" for this reason.

## Checklist

- [x] The artifact belongs to the phase that was run (Architecture Path,
      documentation/template/CI/checker only); no later phase leaked in —
      confirmed no application code exists in this diff.
- [ ] N/A — no Gherkin specification covers a process/governance change.
- [x] The dependency rule and port boundaries hold (no application code
      touched).
- [x] No boundary named in the design agreement was crossed. DA-2026-08-03-03's
      Boundaries section (must not weaken ADR 0006, must not merge without
      genuine independent review, must not present `v2.1.0` as reverted) all
      hold: the branch is still open pending this review, ADR 0006's
      requirement is stated as strengthened not weakened, and `v2.1.0` is
      described as merged-but-corrected, never reverted.
- [x] Specifications and accepted tests were not modified to make work pass
      (none exist for this change).
- [x] Every claim in the artifact states its grounds, with the two exceptions
      named in Falsification Search row 8 (the stale `CHANGELOG.md` entry,
      and the unverifiable-from-history provenance of the antecedent
      rejection review) — both tracked as findings below, neither blocking.
- [x] This record would let a third party re-run the same search: every
      command above is exact and was run against the real checked-out tree
      or a reproducible scratch copy.

## Decision

- [x] **Approved** — specification-conformance, boundary-conformance, and
      evidence-sufficiency, with two findings tracked as required follow-up
      (non-blocking, Minor-Fix-Path-eligible), following this repository's
      own established pattern for approving with recorded findings (see
      `docs/collaboration/reviews/2026-08-03-work-plan-scoped-governance-review.md`'s
      Decision).
- [ ] Rejected
- [ ] Deadlocked — escalate to Arbiter
- [ ] Reopening request

**Per approval type:**

- **Specification-conformance: Approved.** Every one of the seven findings
  named in `docs/collaboration/reviews/2026-08-03-review-cost-discipline-review.md`'s
  "Required artifact changes" is fixed, verified directly against the actual
  file contents and by running the negative tests myself rather than trusting
  the branch's own claims — see Falsification Search rows 1-7 and the
  Deterministic Verification Output's four independent negative tests.
- **Boundary-conformance: Approved.** No boundary in DA-2026-08-03-03 was
  crossed (checklist above). The "no Director-override" language added to
  `prompt-instruction-change-control.md` and ADR 0015 is unconditional and
  consistent with the rest of the contract (Falsification Search row 7) — it
  closes Finding 1's gap rather than relocating it.
- **Evidence-sufficiency: Approved, with two tracked findings.** The design
  agreement and trace both meet their templates in full (rows 5-6). The
  extended checker rules have real, independently-confirmed detection power
  across all three `FULL_MIRRORS` targets, including the split-file grok
  layout (Deterministic Verification Output, negative tests 1-4). Two
  first-time-observed, non-blocking gaps are tracked below rather than
  silently accepted: a stale `CHANGELOG.md` entry, and an unverifiable
  provenance detail about the antecedent review's own context separation.

## Reasons

**Why approved, not rejected.** Every one of the seven required fixes is
real, substantive, and independently verified in this session — not merely
asserted by the branch's own commit messages or design agreement, which this
review was specifically asked not to trust at face value. I ran my own
negative tests (four of them, across all three `FULL_MIRRORS` targets, one
on the split-file grok layout specifically) rather than accepting the
Preflight record's single reported negative test, and confirmed each of the
five artifact-content findings (2, 3, 4, 5, 6) by direct section-by-section
comparison against the relevant templates, and Finding 1's remediation by
reading the surrounding contract documents in full for a contradiction that
was not there. None of the checklist's boundary items failed. The two new
observations (Falsification Search row 8) are real but bounded: neither
changes what shipped in a way that misrepresents current behavior to an
agent following this contract today, and both are the kind of paperwork-level
gap this repository's own precedent
(`2026-08-03-work-plan-scoped-governance-review.md`) treats as
Approved-with-tracked-findings rather than blocking, because they are
consistency/completeness gaps, not boundary violations or evidence that the
core content is wrong.

**What this approval does and does not cover.** This approval covers the
branch as it stands (commits `daf62e6`, `8188a52`) against the seven named
findings plus my own open-ended sweep. It does not retroactively bless the
original `v2.1.0` merge's process (which remains, correctly, described in
this branch as an unauthorized boundary violation, not a legitimate
exception) — it approves the correction. It does not certify that the
antecedent rejection review was itself produced in a genuinely separate
context from this fix; that specific claim is unverifiable from git history
alone (Falsification Search row 8b), and I flag it rather than either
vouching for it or treating its unverifiability as disqualifying, since I
independently re-derived every finding's substance rather than relying on
that document's authority.

**Required follow-up (tracked, non-blocking, Minor-Fix-Path-eligible):**

1. `CHANGELOG.md`'s `v2.1.0` entry ("**Unreviewed.** Per explicit Director
   instruction, independent review was skipped for this release.") should be
   annotated or the next changelog entry (for this correction) should state
   plainly that the original framing was superseded — that the skip was
   later found to be an unauthorized boundary violation, not a disclosed,
   accepted exception, per ADR 0015's now-corrected Status section. Until
   then, a reader of `CHANGELOG.md` alone sees a materially incomplete
   picture. This can be folded into whatever changelog entry this branch's
   own eventual release produces (per the trace's "deferred to merge time"
   note on the version bump), rather than requiring a separate commit first.
2. Going forward, when a review record documents a rejection that a
   following commit then fixes, consider committing the review record on its
   own (or otherwise establishing an independently-timestamped point) before
   the fix, so a future auditor does not have to take "this was produced in
   a separate context" on faith the way this review currently must for the
   original rejection record. Not required to retroactively fix — named as a
   process recommendation, not an artifact defect in this branch.

## Findings (tracked, non-blocking)

**Finding A — `CHANGELOG.md`'s `v2.1.0` entry is stale relative to the
corrected narrative.** See Falsification Search row 8a. Severity: low,
consistency/completeness only — no deterministic check catches this (the
checker's own docstring discloses it only checks presence, never whether
content "still says the same thing"), and it does not misstate what code or
process exists today, only what was true about the original release's
justification.

**Finding B — The antecedent rejection review's context-separation is
unverifiable from repository history.** See Falsification Search row 8b.
Severity: low as applied to this specific review (I independently re-derived
every finding rather than relying on the antecedent document's authority),
but worth naming as a process gap for future contract-file corrections.

## Falsification Criteria Check

DA-2026-08-03-03's Falsification Criteria (four items) were each checked
directly in this review:

1. "The extended checker rules produce a false positive against the
   copy-script's distributed output" — checked; the fresh copy-script target
   passes with zero failures. Not observed.
2. "The rewritten design agreement or trace still omits a field its template
   requires unconditionally" — checked section-by-section against both
   templates; none omitted. Not observed.
3. "The independent Reviewer's fresh review finds that the 'no override
   exception' language... contradicts existing text elsewhere in the
   contract" — checked against `ai-human-scheme.md`, `personas.md`, the
   Minor Fix Path text, and ADR 0006 itself. Not observed.
4. "This branch merges without a recorded, separate-context Reviewer
   approval" — as of this review, PR #12 is open and unmerged; this record
   is that approval, satisfying rather than triggering this criterion,
   provided it is recorded before merge (which it now is).

None of the four falsification criteria were met. This does not, by itself,
prove the design was right — it confirms the design's own stated negative
cases did not occur, which is what the template asks for.
