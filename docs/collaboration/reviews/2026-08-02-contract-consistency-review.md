# Review Record: Contract Consistency Checker (PR #8, `2183b8e`)

Reviewing persona: Reviewer.
Model / tool: Claude Sonnet 5, via a fresh Claude Code agent session with no
memory of the producing session's reasoning. This session read the design
agreement (DA-2026-08-02-07), the Preflight record
(`docs/collaboration/reviews/2026-08-02-contract-consistency-preflight.md`),
the trace, and `scripts/check-contract-consistency.py` itself — all treated
as claims to verify, not as justification. Every claim that mattered to the
decision below was independently re-executed, including building adversarial
test trees of my own rather than reusing the Preflight's negative test.

## Constraints (all three must hold)

- [x] **Context separation.** This session did not produce the checker or its
      fixes, and was not given the producing context's reasoning.
- [x] **Deterministic precondition.** All checks below were run in this
      session — against the real branch, against a full working copy of the
      tree in scratch space for destructive testing, and against `main` at
      `c15dcf3` for the separate `v1.0.1` question.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below, each with the grounds on which it does or does not occur. Three
      reproduced as blocking; two reproduced as non-blocking / disclosed.

---

# Part 1: `main` at `c15dcf3` — does it close the `v1.0.1` gap?

**Yes, confirmed independently.** This is a factual check, not a re-review of
already-decided work.

```text
$ git rev-parse origin/main
c15dcf372542e4241dc2905131112c321f3b7338

$ for f in AGENTS.md CLAUDE.md .github/copilot-instructions.md .grok/rules/01-quickstart.md; do
    ext=$(git show c15dcf3:"$f" | grep -c external-resource-adoption-contract)
    fail=$(git show c15dcf3:"$f" | grep -c ai-failure-recovery)
    runner=$(git show c15dcf3:"$f" | grep -c runner-cli-contract)
    echo "$f  ext-res:$ext failrec:$fail runner:$runner"
  done
AGENTS.md                          ext-res:1 failrec:1 runner:1
CLAUDE.md                          ext-res:1 failrec:1 runner:1
.github/copilot-instructions.md    ext-res:1 failrec:1 runner:1
.grok/rules/01-quickstart.md       ext-res:1 failrec:1 runner:1

$ git show c15dcf3:CHANGELOG.md | sed -n '11,16p'
## v1.1.0 — Independent review, and the rules it produced (unreleased)
**Unreleased.** No `v1.1.0` tag exists yet; the released edition is still
`v1.0.0`, which is what both READMEs banner. ...

$ git show c15dcf3:README.md | grep -n "Contract edition"
6:**Contract edition: v1.0.0.**
```
All four full-mirror files carry the three reading-sequence references on
`main` itself (not just on a branch), and `CHANGELOG.md`/`README.md` on `main`
remain mutually consistent (unreleased `v1.1.0`, banner still `v1.0.0`, no
tag). The gap I held rejected against `main` in my prior record is closed on
`main` as it actually stands today.

---

# Part 2: PR #8, `process/contract-consistency-check` at `2183b8e`

## Review Target

- Artifact: branch `process/contract-consistency-check` / commit `2183b8e`,
  open as pull request #8 against `main` (`c15dcf3`).
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-contract-consistency-check.md`
  (DA-2026-08-02-07).
- Specification: none new; the agreement's Plan, Boundaries, and
  Falsification Criteria stand in for a spec.
- Current phase: Architecture Path.
- Producing persona: Implementer.
- Reviewing persona / model / tool: Reviewer / Claude Sonnet 5 / Claude Code.
- Approval type: specification-conformance, boundary-conformance,
  evidence-sufficiency.
- Preflight Validation record:
  `docs/collaboration/reviews/2026-08-02-contract-consistency-preflight.md`.
- Preflight result: pass — independently re-verified below; several of its
  affirmative coverage claims do not survive adversarial testing (see
  Falsification Search).

## Method

I copied the full tree (`git archive HEAD` plus `.git`) into a scratch
directory so I could inject defects destructively without touching the real
working tree, confirmed the copy reproduces a clean baseline
(`contract consistency: all checks passed`), then constructed defects of my
own — not the Preflight's negative-test defects — for each of the five check
categories plus the specific attack surfaces named for this review: reworded
(not deleted) mirror content, a reference form the resolver might mishandle,
an ADR-range statement in unmatched prose, and a version banner in an
unanticipated form. Each injected defect was reverted before the next test.

## Deterministic Verification Output

**Baseline — checker on the real branch and inside a fresh copy-script
target:**

```text
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed

$ (copy script into a fresh git-init'd target, then inside it)
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```

**Real CI, queried live:**

```text
$ gh pr checks 8
Repository sanity   pass   7s   .../actions/runs/30742491426/job/91482270710
$ gh pr view 8 --json headRefOid,mergeable,state
{"headRefOid":"2183b8ee...","mergeable":"MERGEABLE","state":"OPEN"}
```

**CI-equivalent checks, reproduced locally:**

```text
required_files: 65, missing: []
python3 -m py_compile scripts/check-contract-consistency.py: OK
bash -n <four shell scripts>: OK
conflict markers: none
traceability case-block against this PR's actual changed-file list:
  contract_changed=true trace_added=true -> WOULD PASS CI
```

**Sanity check — my own simple positive/negative tests, before the targeted
attacks:**

```text
$ (inserted an unclassified '## A Brand New Rule' heading into AGENTS.md)
parity completeness:
  AGENTS.md section 'A Brand New Rule' is not classified. ...
exit: 1
$ (reverted) -> clean
```
Check 2 works as claimed for the simple case.

### Attack 1 — a rule reworded, not deleted, in a mirror

```text
$ # in .github/copilot-instructions.md, kept the Prime Directive's matched
$ # phrase intact but changed a neighboring line's meaning:
$ #   "No approval by the context that produced the work."
$ #   -> "Approval by the context that produced the work is permitted for
$ #       Fast Path changes."
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Reproduced.** The checker only tests for the presence of a matching
substring per rule (`re.search(pattern, text)`), not equivalence of the full
rule. A mirror that silently grants self-approval — the exact thing
`personas.md` and the Reviewer's constraints exist to prevent — passes clean
as long as the unrelated trigger phrase for a different sentence in the same
section survives. **This is explicitly disclosed**, however: the agreement's
Deferred Questions table names precisely this ("Whether the checker should
also verify that each mirror's wording still carries the same meaning") and
defers it pending "evidence that a present-but-reworded rule has actually
caused a failure." I found no such historical instance — my test is
synthetic. Judged **non-blocking**: a real, demonstrated gap, but not a false
claim, since nothing in the agreement or PR body claims wording-equivalence
checking.

### Attack 2 — references that resolve from one anchor but not another; and a class the resolver skips entirely

```text
$ # bare filename in a backtick path, no directory component, in a NORMATIVE
$ # contract file (not a record):
$ #   docs/collaboration/personas.md:
$ #   "with `docs/templates/review-record.md`" -> "with `does-not-exist-review-record.md`"
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Reproduced, blocking.** `check_references`' `CODE_PATH` branch contains
`if "/" not in target ...: continue` — any backtick-quoted bare filename
(no `/`) is skipped before existence is even checked, regardless of whether
it resolves. `does-not-exist-review-record.md` does not exist anywhere in the
tree, in a file that is not under any `RECORD_DIRS` exclusion, and the
checker reports full success. This directly contradicts check 3's own
docstring claim, "every relative path a current document names resolves" — a
bare filename is a relative path, and the checker was never told to exclude
it. (The `MD_LINK` branch, by contrast, has no such filter — a broken
`[text](missing.md)` markdown link *would* be caught. The gap is specific to
the backtick-path convention, which is the dominant citation style throughout
this contract's own prose.)

I also tested the root-vs-sibling dual resolution directly (constructing a
reference that would only resolve via the sibling path, and one that would
only resolve via the root path) — both resolved correctly, and I did not find
a case where dual resolution masked a genuinely wrong path with an
accidentally-existing same-named file elsewhere in the tree. That specific
sub-attack did not reproduce.

### Attack 3 — an ADR range stated in prose the regex does not match

```text
$ # README.md: "The thirteen ADRs included here (0001-0013) describe..."
$ #          -> "The eleven ADRs included here (numbered 0001 to 0011) describe..."
$ #   (deliberately WRONG count and range, phrased with "to" instead of "-")
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Reproduced, blocking.** The regex
`r"(\d{4})\s*(?:-|–|〜|through|から)\s*\*?\.?m?d?\*?`?\s*(\d{4})"` only
recognizes five specific separators. "0001 to 0011" — an ordinary, plausible
English phrasing — matches none of them, so the statement is never even
examined, let alone flagged as stale.

```text
$ # QUICKSTART.md: "project numbered afterward (0014 and up)."
$ #              -> "project numbered afterward, starting from 0012."
$ #   (reintroducing the exact collision defect round 2's mirror-parity PR
$ #    was written to fix, just reworded)
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Reproduced, blocking, and materially worse than a hypothetical:** the
"and up" / "以降" pattern is the only recognized form for the
adopter-starting-number statement. "starting from 0012" — a natural way to
say the same thing — evades it completely. This is not a contrived edge
case; it is the literal defect class (adopters told to number into the
template's own range) that caused a rejection in round 2 of my review of the
branch this one stacks on, restated in different words.

### Attack 4 — a version banner in a form not anticipated

```text
$ # README.md: "**Contract edition: v1.0.0.**"
$ #          -> "**This repository currently ships template edition v1.1.0.**"
$ #   (a FALSE claim - v1.1.0 has no tag - in different words)
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Reproduced, blocking.** `check_version_claims`' banner regex only matches
the literal prefixes `Contract edition:` / `契約バージョン:`. Any other
phrasing of the same claim — including one asserting exactly the false
"v1.1.0 shipped" claim that caused two of my prior rejections — passes
silently. The banner text is free prose, not a fixed template macro; nothing
stops a future edit from rewording it in the course of normal copyediting.

### Checking `REFERENCE_ALLOWLIST`

```text
$ grep -n "\.\./docs/architecture" docs/templates/examples/rust-agent-instructions.md
../docs/architecture/rust-clean-architecture.md
../docs/architecture/persistence.md
../docs/architecture/testing-strategy.md
$ ls docs/architecture/rust-clean-architecture.md docs/architecture/persistence.md
(both: No such file or directory)
$ python3 -c "import os; print(os.path.exists('docs/templates/examples/../docs/architecture/testing-strategy.md'))"
False
```
Both allowlisted files' paths are written relative to a deployment location
(`<backend-dir>/`, one level below a target project's root) that does not
match where the example currently sits in this repository
(`docs/templates/examples/`), so they cannot resolve here even for the one
document (`testing-strategy.md`) that does exist in this repo — confirmed by
computing the actual normalized path, which lands on a directory that does
not exist. The allowlist's justification holds; nothing real is hidden by it.

### Checking `AGENTS_ONLY_SECTIONS`

```text
$ grep -n "Project Boundaries\|Current Non-Decisions" .github/copilot-instructions.md .grok/rules/*.md
(no hits in any of the four files)
$ grep -n -i "non-decision\|deferred to an ADR\|ADR topic" .github/copilot-instructions.md .grok/rules/*.md
(no hits)
$ grep -n "If a dependency is unknown, add an interface boundary or an ADR question" \
    .github/copilot-instructions.md .grok/rules/02-architecture-boundaries.md
(both present, in "Anti-Hallucination Rules")
```
**Reproduced, non-blocking, but real.** The comment above
`AGENTS_ONLY_SECTIONS` states both entries are exempt because "each tool file
carries its own." For `Project Boundaries`, that is false for every full
mirror except `CLAUDE.md` — `.github/copilot-instructions.md` and every
`.grok/rules/*.md` file have no placeholder for it at all, in any form, so an
adopting project's filled-in runtime/trust boundaries (written once, in
`AGENTS.md`/`CLAUDE.md`) are invisible to an agent reading only Copilot's or
Grok's own files. For `Current Non-Decisions`, the specific labeled concept
and its rule ("Treat these as ADR topics, not assumptions") do not appear
verbatim anywhere in Copilot or Grok, though a generic, narrower cousin
survives in their shared "Anti-Hallucination Rules" line about unknown
dependencies. I judge this non-blocking because the exemption's *underlying
design choice* — not forcing identical fill-in scaffolding into every
tool file — is defensible on its own terms, and it does not cause the
checker to miss an inconsistency that exists in the *current* tree (there is
no unfilled promise here, since this is template scaffolding, not an
already-stated rule going missing). But the comment's stated justification,
read literally, is inaccurate, and it is exactly the kind of claim this
whole review chain exists to stop taking on faith.

### Checking the `.cursor/rules/*` exemption in `FULL_MIRRORS`

```text
$ grep -n "alwaysApply" .cursor/rules/*.mdc
01: alwaysApply: true / 02: alwaysApply: true / 03: alwaysApply: true
$ grep -n "Before writing implementation\|Reading Sequence" .cursor/rules/*.mdc
(no hits — no competing, possibly-incomplete list exists on the Cursor side)
```
Consistent with what I verified in my prior two rounds against ADR 0006's own
recorded finding (Cursor auto-loads root `AGENTS.md` natively, independent of
`.mdc`). Not re-litigated here beyond confirming the document-side
precondition still holds after this PR's edits — it does.

### Checking the target-skip logic (`read_optional`) cannot silently disable a check in the template repo itself

```text
$ mv README.md /tmp/... ; python3 scripts/check-contract-consistency.py --repo .
references:
  QUICKSTART.ja.md:101 names 'README.md', which does not exist
  QUICKSTART.md:7,100 names 'README.md', which does not exist
  README.ja.md:3 names 'README.md', which does not exist
exit: 1                                          # caught -- restored after
$ mv QUICKSTART.md /tmp/... ; python3 scripts/check-contract-consistency.py --repo .
references: 2 failures (README.md, QUICKSTART.ja.md name it)
exit: 1                                          # caught -- restored after
$ mv CHANGELOG.md /tmp/... ; python3 scripts/check-contract-consistency.py --repo .
references: 4 failures (README.md, README.ja.md name it twice each)
exit: 1                                          # caught -- restored after
```
**Did not reproduce, but the protection is incidental, not designed.** All
three template-only files I tried deleting are heavily cross-referenced by
other tracked, non-record documents, so `check_references` catches the
deletion as a dangling link even though `read_optional` itself would stay
silent about it. `CHANGELOG.md` is additionally covered directly by CI's
`required_files`; `README.md`, `QUICKSTART.md`, and `QUICKSTART.ja.md` are
**not** in `required_files` (confirmed: `grep -n '"README.md"'
.github/workflows/ci.yml` → no hits) and rely entirely on this incidental
cross-referencing. If a future edit deleted one of these files *and* its
last remaining cross-reference in the same change, both this checker and
`required_files` would go silent about the deletion. Non-blocking today,
because it does not reproduce against the current tree, but worth hardening
explicitly (add the three files to `required_files`) rather than relying on
cross-linking as a safety net.

### Checking the boundary: does the checker assert a rule the contract does not state?

Spot-checked `EXTRA_MIRRORED_RULES` and a sample of `MIRRORED_SECTIONS`
patterns against `AGENTS.md`'s actual text (e.g. `"docs/collaboration/agreements/"`
and `"docs/collaboration/reviews/"` both appear verbatim in `AGENTS.md` at the
lines the checker's patterns would match). Every rule name I checked traces to
real, pre-existing `AGENTS.md` content; I found no instance of the checker
inventing an obligation. Falsification Criterion 4 ("The checker asserts a
rule the contract does not state") did not reproduce.

## Falsification Search

| # | Failure scenario searched for | Grounds it does or does not occur | Result |
|---|---|---|---|
| 1 | A rule reworded (not deleted) in a mirror evades mirror-parity | Confirmed: substring-presence matching does not detect a changed neighboring sentence. Explicitly named as deferred in the agreement, with a stated non-reproduction condition. | reproduced, non-blocking (disclosed) |
| 2 | A genuinely broken reference is skipped by the resolver | Confirmed: bare-filename backtick paths are excluded from checking entirely (`"/" not in target` filter), contradicting check 3's own "every relative path... resolves" claim. Not disclosed anywhere. | **reproduced, blocking** |
| 3 | An ADR range/adopter-start statement in ordinary prose evades check 4 | Confirmed twice: "0001 to 0011" (wrong separator) and "starting from 0012" (wrong next-number phrasing, and the literal historical defect class) both pass silently. | **reproduced, blocking** |
| 4 | A version banner reworded in ordinary prose evades check 5 | Confirmed: a differently-phrased but equally false "v1.1.0 shipped" banner passes silently. | **reproduced, blocking** |
| 5 | `REFERENCE_ALLOWLIST` hides a real, currently-broken reference | Not reproduced: both entries' paths are computed to be unresolvable from their current location under any interpretation, in this repo, regardless of the allowlist. | not reproduced |
| 6 | `AGENTS_ONLY_SECTIONS`'s stated justification is false | Reproduced for `Project Boundaries` (no equivalent anywhere in Copilot/Grok) and partially for `Current Non-Decisions` (only a generic, unlabeled cousin exists). Judged non-blocking: no currently-stated rule is going missing as a result, only project-fill scaffolding. | reproduced, non-blocking |
| 7 | The `.cursor/rules/*` exemption leaves Cursor agents unable to reach mirrored content | Not reproduced: `alwaysApply: true` on all three `.mdc` files, no competing incomplete list, consistent with ADR 0006's recorded finding, re-checked after this PR's edits. | not reproduced |
| 8 | The target-skip logic (`read_optional`) silently disables a check when a template-only file is deleted or renamed in the template repo itself | Not reproduced against the current tree — deletion of `README.md`, `QUICKSTART.md`, or `CHANGELOG.md` is each caught via incidental cross-reference breakage — but the protection is not a deliberate guard, and three of the four files are absent from `required_files`. | not reproduced (fragile) |
| 9 | The checker asserts a rule the contract does not already state | Not reproduced in the entries checked; every traced `EXTRA_MIRRORED_RULES`/`MIRRORED_SECTIONS` pattern matches real, pre-existing `AGENTS.md` text. | not reproduced |
| 10 | The three defects the checker found on its first run were not real, or their fixes were cosmetic | Not reproduced: independently confirmed the review-record-location gap (now present in AGENTS.md/CLAUDE.md/copilot/grok-03/cursor-03, byte-matched) and the missing Prime Directive in `.github/copilot-instructions.md` (now byte-identical to `AGENTS.md`'s five-line directive). Both are genuine content fixes, not suppressions. | not reproduced (fixes are real) |
| 11 | The reported "checker bug" (trailing-period capture) was actually a suppressed real finding | Not reproduced: the regex's `[\d.]+` character class is greedy on literal periods, so without `.rstrip(".")` a banner like `v1.0.0.` (with the sentence-ending period, since `.` is in the character class) would never string-equal a clean changelog heading `v1.0.0` — a false *positive* (spurious failure), not a hidden true defect. The `.rstrip(".")` fix is present and correct in the shipped script. | not reproduced |

## Scenarios Not Searched

- Whether other AI coding tools' actual rule-loading behavior (beyond Cursor,
  already checked against ADR 0006's recorded test) matches the `FULL_MIRRORS`
  model — e.g., whether GitHub Copilot genuinely treats
  `.github/copilot-instructions.md` as the entirety of its context the way
  the checker assumes. Taken from prior rounds' review of ADR 0006, not
  re-tested live here.
- A full enumeration of every prose form the ADR-range and version-banner
  regexes might miss; I found two and three concrete counter-examples
  respectively and stopped once the pattern was established, rather than
  exhaustively cataloging the regex's blind spots.
- GitHub Actions execution beyond the one observed job.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked
      in.
- [ ] Every `Then` clause in the specification is asserted — not applicable,
      no Gherkin spec; the agreement's Falsification Criteria stand in, and
      three of four are shown to reproduce.
- [x] The dependency rule and port boundaries hold — not applicable,
      documentation/tooling only.
- [x] No boundary named in the design agreement was crossed — no ADR added or
      revised; the checker does not appear to legislate an unstated rule.
- [x] Specifications and accepted tests were not modified to make work pass.
- [ ] Every claim in the artifact states its grounds — **fails**: the PR body
      and Preflight record claim the checker covers five defect classes
      without qualification; three of those five have concrete, reproducible
      counter-examples that were not disclosed (unlike the reworded-rule gap,
      which is disclosed).
- [x] The record would let a third party re-run this same search — every
      injected defect above is a literal two-line Python or shell
      reproduction against the same commit.

## Decision

- [ ] Approved
- [x] **Rejected** — reasons and the specific artifact changes required below
- [ ] Deadlocked — escalate to Arbiter
- [ ] Reopening request

### Approval type outcomes

- **Specification-conformance**: **Rejected.** Task 1's acceptance criterion
  ("Every defect class found in review rounds 1-3 is detected by a command")
  and the agreement's Falsification Criterion 1 ("The checker passes on a
  tree containing a defect of a class it claims to cover") are both directly
  contradicted: I constructed real trees with real defects in the reference,
  ADR-range, and version-claim classes — three of the five the checker
  explicitly claims to cover — and the checker reported
  `all checks passed` on each. Two of the three (the ADR-range "starting
  from 0012" case and the version-banner reworded-false-claim case) are not
  hypothetical corner cases; they are the literal historical defect classes
  from rounds 2 and 3 of this review chain, reproduced through nothing more
  than ordinary rewording.
- **Boundary-conformance**: **Approved.** No ADR added or revised; the
  checker's rules trace to real, pre-existing contract text everywhere I
  checked; the `.cursor` and `REFERENCE_ALLOWLIST` exemptions hold up under
  direct testing.
- **Evidence-sufficiency**: **Rejected.** The Preflight record's own checks
  are real and its negative test is genuine (independently reproduced in
  spirit with my own defects), but its central claim — that the checker
  "detects every defect class it claims to cover" — does not survive
  adversarial testing with defects the Preflight's own negative test did not
  think to try. A checklist that passes is not evidence the tree is correct;
  this PR's own commit message makes that exact point about round 1 of the
  branch beneath it, and the same point now applies to this checker.

## Reasons

1. **(Blocking, specification-conformance)** Fix the reference resolver's
   bare-filename gap in `check_references`: either check bare filenames
   against the file's own directory and the repo root the same as
   slash-containing targets, or explicitly document why they are excluded
   (I found no stated reason — the `"/" not in target"` filter appears to be
   an oversight, not a design choice, since it silently narrows "every
   relative path" to "every relative path with an explicit directory
   component").
2. **(Blocking, specification-conformance)** Broaden `check_adr_range`'s
   regexes to cover ordinary English/Japanese phrasing beyond the five
   hard-coded separators and two hard-coded next-number phrases — or,
   more robustly, restructure the check to look for *any* four-digit-number
   pair near ADR-related words rather than matching a fixed set of
   connectives. As shipped, this check's real coverage is much narrower than
   its docstring claims, and it would not have caught round 2's actual
   defect if that defect had been phrased one word differently.
3. **(Blocking, specification-conformance)** Broaden `check_version_claims`'s
   banner regex beyond the literal `Contract edition:` / `契約バージョン:`
   prefixes, or restructure it to search for any `v[\d.]+`-shaped token in
   the README files' opening lines and flag ones that don't match a
   released tag, rather than requiring an exact label.
4. **(Non-blocking, evidence-sufficiency)** Correct or narrow the
   `AGENTS_ONLY_SECTIONS` comment's justification — "each tool file carries
   its own" is not true for `Project Boundaries` in three of four full
   mirrors, and only loosely true for `Current Non-Decisions`. State the
   actual reason (these are project-fill scaffolding sections, not
   general contract rules, so exact per-tool duplication is not required)
   rather than a claim that does not hold under inspection.
5. **(Non-blocking, evidence-sufficiency)** Add `README.md`, `QUICKSTART.md`,
   and `QUICKSTART.ja.md` to CI's `required_files` (as `CHANGELOG.md`
   already is), so their existence in the template repository is guarded
   directly rather than incidentally through other documents' cross-links.

This is not a rejection of the direction: the checker is a real improvement,
it found three genuine, previously-undetected defects on its first run, and
two of the five check categories (parity, parity-completeness) held up
against everything I tried, including the specific attacks requested. The
three blocking findings are narrow, each has a concrete fix path, and none
requires revisiting the checker's overall design — only widening three
regexes and closing one filter that appears to be an oversight rather than
an intended exclusion.

---

## Cross-Review Observations

- This is the fourth round across three PRs in which independent review
  found a real gap between what a change claims to do and what it actually
  does under adversarial testing, and the third time the gap was in the
  "silent, no broken link, green CI" category the checker itself was built
  to close. That the checker has exactly this kind of gap in its own
  coverage is not an indictment of the idea — it is the expected outcome of
  subjecting a new deterministic tool to the same falsification burden
  applied to everything upstream of it, rather than trusting its self-report.
- None of the three blocking findings requires wording-equivalence checking
  (the one gap the agreement already, correctly, defers) — all three are
  about the checker's regexes covering less of "ordinary prose" than their
  docstrings claim. That is a narrower, more mechanical fix than the deferred
  question, and does not reopen the agreement's boundaries.

## Verification Environment

- Real branch inspected directly (`process/contract-consistency-check`,
  `2183b8e`); destructive defect injection was done in a separate scratch
  copy (`git archive HEAD` plus `.git`, in the scratchpad directory) so the
  working tree used for other checks was never mutated by the attacks.
- `gh pr checks 8`, `gh pr view 8`, and `git show c15dcf3:...` queried live
  repository/GitHub state at review time (2026-08-02, this session).
- Model: Claude Sonnet 5. Tool: Claude Code, fresh session, no access to any
  producing session's reasoning.
