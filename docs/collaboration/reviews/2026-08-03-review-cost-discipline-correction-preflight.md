# Preflight Validation Record

Per ADR 0013. **Not an approval.**

## Target

- Change: fixes for all 7 findings in
  `docs/collaboration/reviews/2026-08-03-review-cost-discipline-review.md`
  (rejection of ADR 0015 / PR #11's content), plus the Director's
  forward-looking self-review search-scope refinement.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-03-review-cost-discipline-correction.md`
  (DA-2026-08-03-03).
- Branch: `process/review-cost-discipline-fixes`, off `main` at `a11c2df`
  (tag `v2.1.0`). Not yet committed at the time of this record; committed
  immediately after.
- Producer of this Preflight: Implementer, Claude Sonnet 5 via Claude Code.
  Per ADR 0013 this producer cannot review the same change — the fresh,
  independent Reviewer round (design agreement task 9) still applies in
  full and is not replaced by this record.

## Result

**pass** — ready for submission to a fresh-context independent Reviewer.

## Findings Addressed

| # | Reviewer finding | Fix |
|---|---|---|
| 1 | Merged without the separate-context Reviewer approval ADR 0006 requires unconditionally, with no contractual override provision | `docs/collaboration/prompt-instruction-change-control.md` now states explicitly that no Director instruction waives the separate-context requirement, names this incident, and states it is not precedent; `docs/architecture/adr/0015-review-cost-discipline.md`'s Status and Consequences sections rewritten to stop presenting the skip as a disclosed-but-valid exception and instead name it as the boundary violation it was; this branch will not merge without a genuine fresh-context Reviewer approval (design agreement task 9) |
| 2 | `self-review.md`'s short form permitted a one-line summary in place of recorded output | `docs/templates/self-review.md`'s `Result` field now reads "the actual output, pasted" with an explicit paragraph forbidding a hand-written summary as a substitute, tying it directly to the Prime Directive's "'Tests pass' without output is a claim, not evidence" |
| 3 | Consistency checker was not extended to verify ADR 0015's own new content, so the pre-existing `"Self-review (ADR 0014)"` rule could not detect deletion of the new sentences | Added two new `EXTRA_MIRRORED_RULES` entries anchored on text unique to ADR 0015's additions (`Self-review short-form default (ADR 0015)`, `Finding-response delta guidance (ADR 0015)`); negative-tested below |
| 4 | Covering design agreement omitted Plan, Specifications, Boundaries, Settled Ambiguities, Deferred Questions, dedicated Verification, and Falsification Criteria | `docs/collaboration/agreements/2026-08-03-review-cost-discipline.md` rewritten in place with every `design-agreement.md` section filled, including a corrected Boundaries section naming the original omission directly |
| 5 | Trace did not use `ai-work-trace.md`'s template and never named its own persona | `docs/collaboration/traces/2026-08-03-review-cost-discipline.md` rewritten in place using the full template, `Active persona: Implementer` stated explicitly, Preflight/Routing/Context-Ledger sections added |
| 6 | Ambiguous placement of finding-response guidance relative to the contract-file rule | All 5 Preflight-carrying files (`CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.cursor/rules/03-collaboration-and-completion.mdc`, `.grok/rules/03-collaboration-and-completion.md`) now have an explicit scope marker: the contract-file sentence states it applies "including a fix that answers a Reviewer finding on a contract-file change," and the finding-response sentence is scoped to "a review finding on a **non-contract-file** change" |
| 7 | Bounded evidentiary thinning in the finding-response path | Addressed jointly by the Finding-2 fix (no summary substitution permitted at any point in the self-review path, including finding-responses, since finding-responses use the same template) and by the Director's separate instruction that self-review's *search* must be as broad as an independent Reviewer's even though the *record* stays short — now stated in both `self-review.md` and ADR 0015 rule 1 |
| recommendation | No provision exists for a Director-override exception to ADR 0006 | Stated explicitly, conservative default: no such provision is adopted; see `prompt-instruction-change-control.md`'s new paragraph and Enforcement bullet |

## Checks

| # | Check | Result |
|---|---|---|
| 1 | Contract consistency checker, working tree | pass |
| 2 | Negative test: ADR 0015 short-form-default sentence removed from a scratch copy of `CLAUDE.md` | fails as expected, naming the new rule |
| 3 | `required_files` existence | pass — 70, 0 missing |
| 4 | ADR existence `0001`-`0015` | pass |
| 5 | `bash -n` (no shell scripts touched by this change; `copy-ai-collaboration-files.sh` re-checked as a smoke test since it is exercised below) | pass |
| 6 | Conflict-marker sweep | pass — none found |
| 7 | Fresh copy-script target, `self-review.md` distributes | pass |

## Command Output

```text
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```

Negative test (proves Finding 3's fix has real detection power — the
pre-existing `"Self-review (ADR 0014)"` rule could not do this, per the
rejection record's Falsification Search row 3):

```text
$ grep -n "self-review.md.*short form" CLAUDE.md
229:Use `docs/templates/self-review.md`'s short form by default (size `S`);
$ <remove that line from a scratch copy of CLAUDE.md, then>
$ python3 scripts/check-contract-consistency.py --repo <scratch>
mirror parity:
  CLAUDE.md does not state 'Self-review short-form default (ADR 0015)'
  (no match for /self-review\.md.{0,20}short form/)

contract consistency: 1 failure(s)
```

```text
$ python3 -c "
import re
m = re.search(r'required_files=\((.*?)\)', open('.github/workflows/ci.yml').read(), re.S)
files = re.findall(r'\"([^\"]+)\"', m.group(1))
import os
print(len(files), 'entries, missing:', [f for f in files if not os.path.isfile(f)])
"
70 entries, missing: []
```

```text
$ grep -n "for n in 0001" .github/workflows/ci.yml
108:          for n in 0001 0002 0003 0004 0005 0006 0007 0008 0009 0010 0011 0012 0013 0014 0015; do
$ ls docs/architecture/adr/*.md | wc -l
      15
```

```text
$ grep -rl "^<<<<<<<\|^=======$\|^>>>>>>>" --include="*.md" .
(no output)
```

```text
$ tmpdest=$(mktemp -d); bash scripts/copy-ai-collaboration-files.sh --target "$tmpdest"
...
Done.
$ find "$tmpdest" -name "self-review.md"
$tmpdest/docs/templates/self-review.md
```

## Scope Result

Within the covering design agreement's scope. Every change is one of the 6
required artifact changes named in the rejection record, or the Director's
separately-requested self-review search-scope refinement, or this Preflight
record and its covering agreement/trace. No specification, port, data model,
dependency, or architecture boundary changed beyond what the rejection
record and the Director's instruction already named. `v2.1.0`'s merge is not
reverted; this branch corrects defects in what shipped.

## Routing and Compatibility

- Capability class: strong reasoning agent for template/ADR rewrites and
  regex work; deterministic tooling for verification.
- Displayed model / reasoning setting: Claude Sonnet 5, default.
- Compatibility state: default routing, same session that received the
  rejection.
- Escalation reason: contract-file and ADR content changed; Architecture
  Path already in force from the original change.

## Next Action

Commit, push `process/review-cost-discipline-fixes`, open a PR, wait for CI,
then submit the full branch diff to a **fresh** independent Reviewer — a new
`Agent` spawn with no memory of this producing session, per ADR 0015 rule 3
and per the exact gap this whole correction cycle exists to close. Do not
merge without that Reviewer's recorded approval.
