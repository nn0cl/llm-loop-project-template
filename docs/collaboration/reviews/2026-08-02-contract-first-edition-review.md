# Review Record: Contract First Edition (v1.0.0)

Reviewing persona: Reviewer.
Model / tool: Claude Sonnet 5, via a fresh Claude Code agent session with no
memory of the producing session. This session was given only the repository
working tree at `main` (tag `v1.0.0`, commit `eea2f6e26f8d34be25fa1d18608b1459cf2c3fe5`),
the design agreement, the trace as an artifact under review, `personas.md`,
and `docs/templates/review-record.md`. The producing session's reasoning was
not supplied and was not consulted.

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in a fresh agent session that
      was never party to the work that produced this edition. The trace at
      `docs/collaboration/traces/2026-08-02-contract-first-edition.md` was
      read only as an artifact under review (to know what was claimed), never
      as justification — every claim in it that mattered to the decision below
      was independently re-run rather than trusted. Several claims in it turned
      out to be incomplete (see Falsification Search rows 1, 4, 5).
- [x] **Deterministic precondition.** Deterministic verification was run in
      this session and its actual output is recorded below.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below, each with the grounds on which it does or does not occur. Four
      reproduced.

## Review Target

- Artifact: the agent operating contract at `main` / tag `v1.0.0` — the nine
  contract files, `docs/` (architecture, collaboration, at-tdd, templates),
  `.github/workflows/ci.yml`, `scripts/`.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-contract-first-edition.md`
  (DA-2026-08-02-03).
- Specification: none (documentation/contract change); the design agreement's
  Plan table and Falsification Criteria stand in for a spec.
- Current phase: Architecture Path, all four plan rows claimed complete.
- Producing persona: Specifier (per the trace).
- Reviewing persona / model / tool: Reviewer / Claude Sonnet 5 / Claude Code.
- Approval type: specification-conformance (against the design agreement's
  Plan and Falsification Criteria), boundary-conformance, evidence-sufficiency.
  Phase-correctness is not separately meaningful here — there is no Red/Green/
  Refactor artifact, only Architecture Path documentation.

## Deterministic Verification Output

ADR filename/title agreement (11 ADRs, `0001`–`0011`):

```text
$ for f in docs/architecture/adr/*.md; do head -3 "$f" | head -1; done
# ADR 0001: Director-Centered Planning and an AI-Closed Execution Loop
# ADR 0002: Design-First AI Request Routing
# ADR 0003: Input, Output, and Reasoning Contracts
# ADR 0004: Human-Readable Source Code Quality
# ADR 0005: Local Issue Planning
# ADR 0006: Prompt and Instruction Change Control
# ADR 0007: Trunk-Oriented Branching for AI-TDD Collaboration
# ADR 0008: Pull-Based Template Update Propagation
# ADR 0009: Bug Planning and AI Usage Records
# ADR 0010: AI Failure Recovery and Slow-Job Runner CLI Contract
# ADR 0011: Optional External Resource Adoption Contract
```
All 11 match `docs/architecture/README.md`'s "Accepted Decisions" index and
the `.github/workflows/ci.yml` ADR-existence loop (`0001`..`0011`), which was
also run directly and passed (all 11 `OK`).

Stale-reference grep (repo-wide, excluding `.git`):

```text
$ grep -rn "ADR 001[23]\|adr/001[23]\|0001-0013" --include='*.md' ...
docs/collaboration/traces/2026-08-02-contract-first-edition.md:105-106  (meta: describes the check itself)
# 0 stale hits in normative content.

$ grep -rn "LISS-" ... | grep -v 'LISS-0000\|LISS-NNNN'
# all hits are the documented ID-glob pattern (docs/issues/LISS-*.md) in
# local-issue-planning.md, session-start-and-resume.md, branch-commit-pr-
# discipline.md, definition-of-done.md, ci.yml, and the sync scripts. 0 stale.

$ grep -rln "Adjudicator" ... ; grep -rln "Referee" ...
docs/collaboration/agreements/2026-08-02-contract-first-edition.md  (meta: names the retired role as the subject of the removal check)
docs/collaboration/traces/2026-08-02-contract-first-edition.md      (meta: same)
# 0 hits in any normative contract or architecture document.
```

CI repository-sanity steps, reproduced locally:

```text
$ (63-entry required_files array from ci.yml, existence-checked in Python)
count: 63
missing: []

$ for n in 0001..0011; do ls docs/architecture/adr/${n}-*.md; done
0001 OK ... 0011 OK

$ bash -n scripts/copy-ai-collaboration-files.sh scripts/update-ai-collaboration-files.sh \
    scripts/init-llm-context.sh scripts/lib/collaboration-template-paths.sh
syntax OK

$ git grep -n -E '^(<<<<<<<|=======|>>>>>>>)' -- . ':!.git'
none found
```

Copy smoke test, reproduced locally (own temp target, own `git init`):

```text
$ scripts/copy-ai-collaboration-files.sh --target "$tmp/target" \
    --project-name "Smoke App" --domain-summary "template smoke test" --stack "test stack"
... Done. Existing files were left unchanged. Recorded sync point ...
(exit 0)

$ grep -RIn 'PROJECT_NAME|FILL IN' AGENTS.md CLAUDE.md .github/copilot-instructions.md .grok/rules .cursor/rules
(no hits — the CI regex, run verbatim, also reports no hits, exit 0)

$ ls docs/collaboration/agreements docs/collaboration/reviews docs/collaboration/traces  # in target
(all empty — excluded paths correctly absent)

$ grep -n "Fill in:" CLAUDE.md   # in target, AFTER the copy script ran with --stack "test stack"
326:`<Fill in: desktop/web/mobile runtime, backend language, frontend framework,
# unfilled placeholder shipped to the target; see Finding 3.
```

Link/backtick-path resolution check (custom script, 71 `.md`/`.mdc` files,
`docs/templates/examples/` excluded per the design agreement's declared
out-of-scope):

```text
Checked 71 files
Found 0 problems
```

CI traceability-check reproduction (exact case pattern copied from
`.github/workflows/ci.yml` lines 172–181, fed one changed file):

```text
$ changed_files="docs/collaboration/reviews/2026-08-02-contract-first-edition-review.md"
$ # ... exact case/esac block from ci.yml ...
contract_changed=true trace_added=false
WOULD FAIL CI: contract files changed without an accompanying trace
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | A rule stated in one contract file is absent from another (design agreement Task 3; Falsification Criterion 1) | Reproduced: `docs/architecture/external-resource-adoption-contract.md`, `docs/collaboration/ai-failure-recovery.md`, and `docs/collaboration/runner-cli-contract.md` are named in CLAUDE.md's Reading Sequence (lines 123, 138–139) and are real, cross-referenced files (each cited by ADR 0010, `model-tool-capability-matrix.md`, `process-gap-register.md`, and each other) — but `grep` for all three filenames across `AGENTS.md`, `.github/copilot-instructions.md`, and all six `.grok`/`.cursor` files returns 0 hits. An agent that only reads AGENTS.md (which Codex, Cursor, and Grok all also load) is never directed to these two collaboration documents or this architecture document. `docs/architecture/README.md`'s own "Detailed Rules" list also names `external-resource-adoption-contract.md`, which AGENTS.md's parallel list omits, so AGENTS.md lags even the document it is supposed to summarize. | reproduced |
| 2 | Same class, second instance: the "Reopening the Design Agreement" trigger list | Reproduced: `AGENTS.md`, `CLAUDE.md`, `.grok/rules/03-collaboration-and-completion.md`, and `.cursor/rules/03-collaboration-and-completion.mdc` all state five specific reopening triggers (unsettled decision required, named boundary crossed, accepted spec would change, deterministic verification contradicts an assumption, Arbiter finds neither side grounded / falsification criterion met). `.github/copilot-instructions.md` has no such section — `grep -i reopen` finds only two narrow mentions (missing design-intake fields at session entry; general "when uncertain") and never states boundary-crossing, spec-change, verification-contradiction, or Arbiter-deadlock as reopening triggers. The trace's own parity matrix (line 120–123) says it checked AGENTS.md for "no reopening section" and fixed it, but did not check copilot-instructions.md for the same gap. | reproduced |
| 3 | The copy-script/CI placeholder-fill guarantee (design agreement Task 3: "copy smoke test asserting placeholder fill in the target") does not actually catch every unfilled placeholder | Reproduced: `CLAUDE.md` carries a section, `## Selected Stack` (line 324), with no counterpart heading in any other contract file. Its placeholder text is `<Fill in: desktop/web/mobile runtime, backend language, frontend framework, package manager, migration tool, etc.>` — worded differently from the `<FILL IN: e.g. backend language, frontend framework, package manager>` pattern that `scripts/copy-ai-collaboration-files.sh` substitutes (lines 166–168) and that CI's smoke test greps for (`<FILL IN: e\.g\. backend`, case-sensitive). Running the real copy script with `--stack "test stack"` into a fresh target, then running CI's own placeholder grep against that target, passes (exit 0) — while `CLAUDE.md` in that same target still reads the literal, unfilled `<Fill in: ...>` line. The smoke test's green result does not mean what Task 3 says it means. | reproduced |
| 4 | CI's agent-operating-contract traceability check (`.github/workflows/ci.yml` "Check agent operating contract change traceability") matches a broader file set than the Reviewer/Planner personas can satisfy | Reproduced: the check's `case` pattern includes `docs/collaboration/*.md`. In bash `case`, `*` matches `/`, so this pattern also matches nested paths — verified directly (`case "docs/collaboration/traces/foo.md" in docs/collaboration/*.md) ... esac` prints "MATCHED"). The first `case` arm intercepts `docs/collaboration/traces/*.md` before that, so trace files are unaffected — but `docs/collaboration/agreements/*.md` and `docs/collaboration/reviews/*.md` are not given a first-arm exception and fall through to the "contract changed" arm. Feeding the workflow's exact snippet a changed-file list containing only this review record (`docs/collaboration/reviews/2026-08-02-contract-first-edition-review.md`) yields `contract_changed=true`, `trace_added=false`, and the failure message. `docs/collaboration/prompt-instruction-change-control.md` (the document CI is implementing) defines the contract file set as `docs/collaboration/*.md` "(except files under `docs/collaboration/traces/`)" — an exception stated only for `traces/`, which reads as confirming agreements/ and reviews/ were meant to be swept in, not excluded by oversight. Either reading is a defect: if inclusion is intended, it conflicts with `personas.md`, which gives the Reviewer exactly one output (a review record) and the Planner/Specifier exactly one relevant output (a design agreement or plan) with no stated trace obligation — so a Reviewer or Planner following their own persona definition to the letter produces a PR that CI rejects. If inclusion is not intended, the CI implementation is a bug against its own source document. Either way, a real PR carrying only this review record would fail CI today. | reproduced |
| 5 | `CHANGELOG.md`, called out by name in the design agreement's Task 4 scope as a required deliverable of this edition, is not verified by CI | Reproduced: `.github/workflows/ci.yml`'s `required_files` array (63 entries, all independently verified to exist) does not include `CHANGELOG.md`. The file exists and its content is accurate (checked against README banners and the version marker; see row 6), but nothing in CI would catch its removal. | reproduced |
| 6 | The edition declaration is unverifiable or inconsistent (Falsification Criterion 3: "An adopting project cannot tell which edition it installed") | Not reproduced. `README.md` and `README.ja.md` both banner `**Contract edition: v1.0.0.**` and link `CHANGELOG.md`; `CHANGELOG.md`'s `v1.0.0` entry matches the ADR renumbering and record-reset claims; the annotated tag `v1.0.0` (`git cat-file -p v1.0.0`) points at `eea2f6e`, which is `HEAD` of `main`; the copy script's `write_version_marker` writes `source`, `ref`, and `edition` (via `git describe --tags`) into the target's `.collaboration-template-version`, and the reproduced smoke-test target actually got `edition: v1.0.0`. | not reproduced |
| 7 | A retired decision (the superseded governance ADR, the role-rename ADR) is still readable as if in force (Falsification Criterion 4) | Not reproduced. Both retired ADRs are absent from `docs/architecture/adr/`; `Adjudicator`/`Referee` do not appear in any normative document (only in the agreement/trace, describing the removal check itself, which is expected); the old ADR numbers `0012`/`0013` do not appear anywhere except the trace's description of the grep it ran. | not reproduced |
| 8 | Links or backtick-quoted repository paths in the changed documentation resolve to nothing (dangling reference) | Not reproduced. A custom resolver checked every Markdown link and every backtick-quoted `docs/…`/`scripts/…`/`.github/…`/`.grok/…`/`.cursor/…` path across 71 `.md`/`.mdc` files (excluding `docs/templates/examples/`, out of scope per the agreement) and found 0 unresolvable targets. | not reproduced |
| 9 | The nine-file "63 required files" and "0001–0011 ADR" CI checks are inaccurate as claimed in the trace | Not reproduced for these two specific checks — both were re-run independently in this session with the exact figures the trace claims (63/63, 11/11). | not reproduced |

## Scenarios Not Searched

- GitHub Actions itself (network-dependent; only the steps' shell logic was
  reproduced locally, as the design agreement's own Verification section
  anticipates).
- Full byte-level diff of every one of the ~30 "Updated" files listed in the
  trace's Changed Files section against their pre-change content; this review
  read full contents of the nine contract files, `ci.yml`,
  `docs/architecture/README.md`, `docs/architecture/adr/0006`,
  `prompt-instruction-change-control.md`, `personas.md`, the two record
  templates, `CHANGELOG.md`, both READMEs, and the copy script's substitution
  logic, but did not line-by-line diff every architecture document listed as
  touched (e.g. ADRs 0004, 0005, 0008, 0010, 0011 individually).
- Whether the `.grok`/`.cursor` files agree with each other and with
  `AGENTS.md` on every clause (only structural/heading-level and targeted
  cross-reference comparisons were run, plus the two gaps found above; a full
  clause-by-clause parity matrix across all nine files was not built).
- Line-width/formatting conventions: the trace's "80-column" claim was spot
  checked and found to include non-ASCII (Japanese PR-summary lines) and YAML
  frontmatter in a naive column count, which are not meaningful hits; a
  properly scoped re-check (ASCII prose lines only, excluding code fences and
  frontmatter) was not built, so this claim is neither confirmed nor
  falsified here.

## Checklist

- [x] The artifact belongs to the phase that was run (Architecture Path
      documentation); no later phase leaked in — there is no production code
      or test change in scope.
- [ ] Every `Then` clause in the specification is asserted by the work — not
      applicable; no Gherkin specification covers this change (design
      agreement states "Specifications: None").
- [x] The dependency rule and port boundaries hold — not applicable to a
      documentation-only change; nothing in scope touches Domain/UseCase/
      Adapter code.
- [ ] No boundary named in the design agreement was crossed — **partially
      fails**: Task 3's boundary ("no contract file states a rule another one
      lacks") is crossed by Findings 1–2 below.
- [x] Specifications and accepted tests were not modified to make work pass —
      not applicable, none exist for this change.
- [ ] Every claim in the artifact states its grounds — the trace's Verification
      section states grounds for its claims, but two of those claims (parity
      matrix completeness, "copy smoke test: passed") are shown by this review
      to have missed real gaps; see Findings 1–3.
- [x] The record would let a third party re-run this same search — every
      command above is a literal shell one-liner or a short Python snippet
      runnable against the same commit.

## Decision

- [ ] Approved
- [x] **Rejected** — reasons and the specific artifact changes required below
- [ ] Deadlocked — escalate to Arbiter
- [ ] Reopening request

### Approval type outcomes

- **Specification-conformance**: **Rejected.** The design agreement's Task 3
  acceptance criterion ("No contract file states a rule another one lacks;
  every file names the product and stack") is not met — Findings 1 and 2 are
  direct instances of a rule (required reading, reopening triggers) stated in
  some contract files and absent from others. Task 3's stated verification
  method ("copy smoke test asserting placeholder fill in the target") is
  itself shown to have a blind spot by Finding 3: it passes while a real
  placeholder ships unfilled.
- **Phase-correctness**: **Approved.** The change is documentation/contract
  work; no phase artifact was produced ahead of or behind the phase it claims.
- **Boundary-conformance**: **Rejected.** Finding 4 shows the CI mechanism
  this edition ships crosses a boundary the contract itself draws (Reviewer's
  and Planner's defined outputs in `personas.md`) — a Reviewer or Planner
  acting exactly as their persona instructs produces a PR that this edition's
  own CI rejects, on the reviewing/planning artifact alone. That is a boundary
  the design agreement did not intend to create and did not name as accepted
  risk.
- **Evidence-sufficiency**: **Rejected.** Deterministic checks were run and
  their output recorded in the trace, satisfying the letter of the invariant,
  but three of the trace's specific pass/fail conclusions (parity matrix
  complete; copy smoke test proves placeholder fill; "0 defects" from the link
  audit implicitly extended to the reading-sequence lists) do not hold up
  under independent re-execution in this session, which is exactly the
  scenario context separation and a Reviewer role exist to catch.

## Reasons

1. **(Blocking, spec-conformance)** Fill the gap named in Falsification Search
   row 1: add reading-sequence references to
   `docs/architecture/external-resource-adoption-contract.md`,
   `docs/collaboration/ai-failure-recovery.md`, and
   `docs/collaboration/runner-cli-contract.md` to `AGENTS.md` (and by mirror
   obligation, `.github/copilot-instructions.md` and `.grok/rules/01-quickstart.md`;
   Cursor inherits from `AGENTS.md` per ADR 0006 and needs no separate edit).
2. **(Blocking, spec-conformance)** Fill the gap named in row 2: give
   `.github/copilot-instructions.md` the same "Reopening the Design Agreement"
   trigger list that `AGENTS.md`, `CLAUDE.md`, `.grok/rules/03-…`, and
   `.cursor/rules/03-…` already state, or an equivalent full-coverage
   restatement per ADR 0006.
3. **(Blocking, spec-conformance)** Fix the placeholder in row 3: either give
   `CLAUDE.md`'s `## Selected Stack` section the exact
   `<FILL IN: e.g. backend language, frontend framework, package manager>`
   text the copy script already substitutes (dropping the unique, unfilled
   wording), or extend `replace_placeholders()` in
   `scripts/copy-ai-collaboration-files.sh` and CI's smoke-test grep to also
   match it. As shipped, an adopting project's `CLAUDE.md` contains a visibly
   unfilled placeholder that CI reports as clean.
4. **(Blocking, boundary-conformance)** Resolve row 4 before this edition
   governs real PRs: either (a) scope
   `docs/collaboration/prompt-instruction-change-control.md`'s file list and
   `ci.yml`'s case pattern to explicitly exclude
   `docs/collaboration/agreements/` and `docs/collaboration/reviews/` (mirroring
   the existing `traces/` exception, since those are also records produced by
   following the contract rather than the contract itself), or (b) add a
   trace-writing obligation to the Reviewer and Planner/Specifier entries in
   `personas.md` and to `docs/templates/review-record.md` /
   `docs/templates/design-agreement.md`, so the persona contract and the CI
   gate agree. Right now neither document tells a Reviewer to write a trace,
   and CI, as actually evaluated by bash, requires one anyway.
5. **(Non-blocking, evidence-sufficiency)** Add `CHANGELOG.md` to `ci.yml`'s
   `required_files` array, since the design agreement names it as a Task 4
   deliverable and nothing currently verifies its presence.

This is a rejection of the artifact as it stands, not of the overall
direction: rows 6–9 (edition declaration, retired-ADR archaeology, link
resolution, the numeric CI claims) all held up under independent
re-verification, and the renumbering/retirement work is sound. The five
items above are narrow, named, and reproducible from the commands in this
record.
