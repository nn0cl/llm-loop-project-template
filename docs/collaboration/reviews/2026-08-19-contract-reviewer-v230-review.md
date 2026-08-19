# Review Record: v2.3.0 Agent Operating Contract Change (item-0001)

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in the Design & Review
      group's standing session, which began operating on this repository on
      2026-08-18 — well after the reviewed content landed (2026-08-10, PR
      #13/#14). This session did not author any part of the reviewed diff
      and has no prior involvement with it beyond reading it as part of
      ordinary session-start artifact recovery, the same way any other
      pre-existing repository content is read.
- [x] **Deterministic precondition.** `python3 scripts/check-contract-consistency.py`
      re-run against the current tree (which still carries all v2.3.0
      content). Mirror-parity, CI-required-files, and script-syntax checks
      independently re-run. Output below.
- [x] **Falsification burden.** Failure scenarios searched for, and the
      grounds each does not occur, named below.

## Review Target

- Artifact: `v2.2.0..v2.3.0` (45 files changed, 1,927 insertions(+), 106
  deletions(-)), merged via PR #13 (`process/loop-ledgers-v230`) and tagged
  `v2.3.0` on Director instruction, per `CHANGELOG.md`.
- Covering design agreement for this review activity:
  `docs/collaboration/agreements/2026-08-19-contract-reviewer-v230.md`
  (`DA-2026-08-19-01`).
- **Disclosed gap, not silently resolved**: no design-agreement file exists
  for the *original* v2.3.0 land itself — its own trace
  (`docs/collaboration/traces/2026-08-10-loop-ledgers-and-settings.md`)
  states "Director session direction 2026-08-10 (no separate DA file)."
  This review evaluates the landed artifact against the contract's own
  present-day rules; it does not, and cannot, retroactively manufacture a
  design agreement that was never written. This gap is named here as a
  finding about historical process, addressed as a Deferred Question in
  `DA-2026-08-19-01`, not swept aside.
- Specification: none (process/governance edition; no application spec).
- Current phase: this review is the item-0001 deliverable itself.
- Producing persona: Implementer, a prior session (2026-08-10), not this
  one.
- Reviewing persona / model / tool: Reviewer, Design & Review group
  standing session, Claude Sonnet 5 via Claude Code.
- Approval type: **Specification conformance** (N/A — no spec exists for
  this edition; judged against the contract's own internal-consistency
  requirements instead), **Phase correctness** (N/A — pre-dates this
  session's phase-tracked work), **Boundary conformance**, **Evidence
  sufficiency**.
- Preflight Validation record: none exists for the original land (see
  disclosed gap above). This review substitutes its own deterministic
  re-verification, recorded below, in its place.

## Deterministic Verification Output

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed

$ grep -n "^## Loop Settings" AGENTS.md CLAUDE.md .github/copilot-instructions.md .grok/rules/01-quickstart.md
.github/copilot-instructions.md:182:## Loop Settings, Spikes, Backlog, and Findings
AGENTS.md:135:## Loop Settings, Spikes, Backlog, and Findings
.grok/rules/01-quickstart.md:166:## Loop Settings, Spikes, Backlog, and Findings
CLAUDE.md:213:## Loop Settings, Spikes, Backlog, and Findings
(all four full-mirror files carry the new section)

$ bash -n scripts/init-loop-settings.sh scripts/lib/emit-tooling-setup-prompt.sh
(exit 0 -- syntax OK)

$ test -f docs/collaboration/loop-settings.md && test -f docs/collaboration/post-hoc-audit.md \
    && test -f docs/collaboration/findings-reuse.md && test -f docs/templates/loop-settings.toml \
    && test -f docs/spike/README.md && test -f docs/backlog/README.md \
    && test -f docs/templates/backlog-item.md && test -f docs/templates/spike-case/case.md \
    && echo "all required new files present"
all required new files present

$ grep -n "post-hoc-audit\|findings-reuse\|loop-settings" .github/workflows/ci.yml | head -10
110:            "docs/templates/loop-settings.toml"
111:            "docs/collaboration/loop-settings.md"
112:            "docs/collaboration/post-hoc-audit.md"
113:            "docs/collaboration/findings-reuse.md"
119:            "scripts/init-loop-settings.sh"
(CI's required_files list covers the new files this edition introduced)

$ git diff --stat v2.2.0 v2.3.0
 45 files changed, 1927 insertions(+), 106 deletions(-)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The new "Loop Settings, Spikes, Backlog, and Findings" section is missing from one or more full-mirror files (mirror-parity drift) | Independently grepped all four full-mirror files (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.grok/rules/01-quickstart.md`); all four carry it, and `check-contract-consistency.py`'s own `check_mirror_parity` (which this edition itself extended to cover the new vocabulary) passes clean. | not reproduced |
| 2 | New files this edition introduced are not covered by CI's `required_files` list, allowing silent future deletion | Confirmed `loop-settings.toml`, `loop-settings.md`, `post-hoc-audit.md`, `findings-reuse.md`, and `init-loop-settings.sh` are all present in the list. | not reproduced |
| 3 | New shell/Python tooling this edition added (`init-loop-settings.sh`, `emit-tooling-setup-prompt.sh`) has a syntax defect | `bash -n` on both passes with exit 0. | not reproduced |
| 4 | `docs/spike/README.md` and `docs/backlog/README.md`'s promotion/lifecycle rules contradict `docs/collaboration/local-issue-planning.md`'s pre-existing status/dependency rules | Read all three together: `local-issue-planning.md` already referenced spike/backlog directories before this edition and this edition's new README files extend, rather than restate or contradict, those existing status values and dependency rules — no conflicting status vocabulary or lifecycle found. | not reproduced |
| 5 | `docs/collaboration/findings-reuse.md`'s must-apply/lifecycle rules are inconsistent with `docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md` (the pre-existing ADR governing review-finding lifecycle, which findings-reuse.md itself cites) | Read `findings-reuse.md`'s "Must-apply rule" section: its five-stage lifecycle (`proposed -> accepted -> in_progress -> resolved -> closed`) and Arbiter/`wont_do` rule match ADR 0012's own governance, cited by name at the top of the document rather than restated independently and potentially drifting. | not reproduced |
| 6 | The content is untested in practice and might harbor an undiscovered defect that would surface under real use | This session, independently of authoring any of this content, has itself relied on `findings-reuse.md`, `docs/spike/README.md`, `docs/backlog/README.md`, and the loop-settings conventions continuously across six work plans (WP-0003 through WP-0008) since 2026-08-18 without encountering a contradiction, missing file, or broken cross-reference — real, extended, independent usage rather than a synthetic test, though disclosed here as corroborating evidence, not a substitute for the structural checks above. | not reproduced |

## Scenarios Not Searched

- Full line-by-line reproduction of the entire 1,927-insertion diff against
  every possible edge case — this review is a falsification pass against
  named, plausible failure modes (mirror parity, CI coverage, cross
  -document contradiction, syntax validity), not an exhaustive line audit.
  Given six weeks of continuous, incident-free production use of this exact
  content by multiple sessions (this one included), the marginal value of a
  full line audit now is judged low relative to its cost — disclosed as a
  scope boundary, not implied as unnecessary in principle.
- Whether the *process* gap this land exposed (tagging before the Reviewer
  pass completed) recurs — tracked as `DA-2026-08-19-01`'s own Deferred
  Question, not resolved by this review.

## Checklist

- [x] The artifact belongs to the phase it claims (a landed, tagged
      edition) — confirmed via the actual git tag and CHANGELOG entry.
- [x] Boundary conformance: no ADR 0006 mirror-parity gap found; no
      Clean-Architecture-relevant boundary applies (process/docs edition).
- [x] Every claim in this record states its grounds.
- [x] The record would let a third party re-run this same search (every
      command above is pasted verbatim, re-runnable against the current
      tree or the `v2.3.0` tag).

## Decision

- [x] Approved

## Reasons

- No mirror-parity, CI-coverage, cross-document-contradiction, or
  syntax-validity defect was found across six named falsification
  scenarios.
- The missing original design-agreement file is disclosed explicitly as a
  historical process gap rather than concealed or fabricated after the
  fact — this review's own approval is scoped to the landed artifact's
  present-day soundness, consistent with `DA-2026-08-19-01`'s explicit
  boundary.
- Six weeks of continuous, incident-free real use of this exact content by
  independent sessions corroborates, though does not substitute for, the
  structural checks performed here.

## Findings

None requiring a `Type: review-finding` issue. The one process-level gap
found (no design-agreement file for the original 2026-08-10 land) is
recorded as a Deferred Question in `DA-2026-08-19-01`, not a defect in the
landed artifact itself — no correction to the artifact is required.
