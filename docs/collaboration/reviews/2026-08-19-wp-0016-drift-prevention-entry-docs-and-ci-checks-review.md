# Review Record: WP-0016 — Drift-Prevention Entry Documents and CI Checks

Use this when the Reviewer persona issues a decision inside the execution loop.

A review that does not satisfy all three constraints below does not count as an
approval, whatever this record says.

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in a fresh session with no
      prior memory of this work plan's chat history. Nothing was read from a
      chat transcript or trusted from any agent's summary. Every claim below
      was independently re-derived from repository artifacts: the backlog
      item, ADR 0020, LISS-0044, DA-2026-08-19-08 (including its Settled
      Ambiguities/Reopening Log recording the mid-work-plan correction),
      WP-0016, LISS-0048 (including its self-review and correction
      addendum), the AI work trace, and the actual landed files, read
      directly from the git tree at commit `b5609cf` (checked out in this
      worktree). The Implementer's own reasoning in the trace/self-review was
      read only to identify what to independently re-verify, never accepted
      as the grounds for approval.
- [x] **Deterministic precondition.** `python3 scripts/check-contract-consistency.py`
      was re-run independently in this reviewing session (not copied from
      WP-0016's own pasted Preflight output) — see Deterministic Verification
      Output below. In addition, every synthetic-case claim in LISS-0048's
      Work Notes and the AI work trace was independently reconstructed from
      scratch, with fresh command output, rather than trusted from the
      pasted transcripts.
- [x] **Falsification burden.** 18 scenarios searched, each with grounds and
      an actual result (not "no problems found") — see Falsification Search
      below. Two genuine, reproducible gaps were found that the design
      agreement did not anticipate.

## Review Target

- Artifact: WP-0016 (`docs/work-plans/WP-0016-drift-prevention-entry-docs-and-ci-checks.md`)
  / LISS-0048 (`docs/issues/LISS-0048-drift-prevention-entry-docs-and-ci-checks.md`)
  — `docs/collaboration/terminology-migration.md` (new),
  `scripts/check-contract-consistency.py` (four edit points),
  `docs/architecture/agent-quickstart.md` (new section),
  `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md` (closed).
- Covering design agreement: `DA-2026-08-19-08`
  (`docs/collaboration/agreements/2026-08-19-drift-prevention-entry-docs-and-ci-checks.md`),
  as amended by its own Reopening Log entry (2026-08-19, the
  `check_no_archive_reference_from_entry` false-positive correction).
- Specification: none (documentation/process-governance change plus
  deterministic tooling; DA-2026-08-19-08's own "Specifications" section
  states this explicitly).
- Current phase: Architecture Path, Work-Plan Review (post-Preflight,
  pre-Director-close).
- Producing persona: Implementer (LISS-0048), with a mid-work-plan
  correction cycle involving the Design & Review group (Planner) in a
  separate context, per the DA's own Reopening Log.
- Reviewing persona / model / tool: Reviewer, Claude Sonnet 5 via Claude
  Code, separate context/session from both the Planner/Specifier session
  that wrote DA-2026-08-19-08 and the Implementer session that executed it.
- Approval type: specification-conformance, phase-correctness,
  boundary-conformance, evidence-sufficiency (all four assessed; see
  Checklist).
- Preflight Validation record: WP-0016's own Preflight Validation section
  (`docs/work-plans/WP-0016-drift-prevention-entry-docs-and-ci-checks.md`),
  recorded at commit `b5609cf`.
- Preflight result: pass (independently re-run below, not merely trusted).

## Deterministic Verification Output

Re-run independently in this reviewing session, against the actual repo tree
at commit `b5609cf` (this worktree's HEAD), without reading WP-0016's own
pasted Preflight output first.

```text
$ git rev-parse HEAD
b5609cf... (docs: record Preflight pass for WP-0016)

$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
$ echo $?
0

$ find docs/archive
bfs: error: docs/archive: No such file or directory.
```

Clean pass, exit 0. `docs/archive/` confirmed absent from the tree — the
synthetic verification case left no trace. This matches WP-0016's own
Preflight claim, independently reproduced rather than trusted.

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | `check_retired_terminology`'s term-extraction regex (`^\| `([^`]+)` \| `[^`]+` \|`) matches the placeholder row `| _(no entries yet)_ | | | |` and treats it as a retired term | Independently ran the regex against the real, unmodified `docs/collaboration/terminology-migration.md`; `retired_terms == []`. The placeholder row has no backticks, so the pattern (which requires a literal backtick immediately after `\| `) cannot match it. | not reproduced |
| 2 | `check_retired_terminology` scans its own table file (`docs/collaboration/terminology-migration.md`) and flags its own listed retired terms inside the table | Read the function: `if rel.startswith(RECORD_DIRS) or rel == TERMINOLOGY_MIGRATION_TABLE: continue` explicitly skips the table file by exact path match. | not reproduced |
| 3 | A short/common retired term causes `check_retired_terminology` to false-positive as a substring match inside unrelated words across the whole repo (e.g., retiring "AI" flags "AI-assisted", "AIDE", `update-ai-collaboration-files.sh`, etc.) | The check's own matching is `if term in line:` — a plain substring test, no word-boundary regex, no case sensitivity control, no minimum-length guard. Independently added `| \`AI\` | \`LLM\` | test | 2026-08-20 |` to a scratch copy of the table plus a scratch file containing "AI-assisted... AI-powered... AIDE integration", then ran the real checker. | **reproduced** — 389 failures across the repo (`.cursor/rules/*.mdc`, `scripts/update-ai-collaboration-files.sh`, and many more), all from the substring "AI" appearing inside legitimate unrelated words, not just the constructed scratch case. Synthetic artifacts fully removed afterward; `git status --porcelain` confirmed clean. This is a real, currently-latent design gap: nothing in the DA, the check's own docstring, or `terminology-migration.md`'s own guidance to future term-retirers warns against choosing a short/common term. See Reasons below. |
| 4 | `ENTRY_ARCHIVE_REFERENCE` (`docs/archive/[\w./-]*\.\w+`) flags a bare mention of the `docs/archive/` directory with no file-shaped path after it (should NOT be flagged, per the check's own docstring) | Confirmed by the real-tree clean run above: `agent-quickstart.md`'s own File-3-mandated abstract sentence ("Once ADR 0020's archive mechanism has moved a document under `docs/archive/`, treat it the same way...") produces zero failures. Also confirmed by direct regex reasoning: the pattern requires a literal `.` plus `\w+` after the `[\w./-]*` run; a bare `docs/archive/` with nothing file-shaped after it cannot satisfy that. | not reproduced |
| 5 | `ENTRY_ARCHIVE_REFERENCE` treats a Markdown-link-style reference (`[text](docs/archive/foo.md)`) differently from a bare backticked one, letting one form evade detection | Independently tested both forms against the compiled regex in isolation. Both match identically — the regex does a plain substring search regardless of surrounding Markdown syntax; trailing `)` correctly stops the match at the right point (`)` is not in `[\w./-]`). | not reproduced |
| 6 | A genuine, file-shaped `docs/archive/...` reference is silently missed by `check_no_archive_reference_from_entry` when it is split across a hard line-wrap — this repository's own dominant prose convention (every document read for this review, including `agent-quickstart.md` itself and this very design agreement, hard-wraps prose well under 80 columns) | The check scans line-by-line (`for lineno, line in enumerate(text.splitlines(), 1)`), with no cross-line joining or normalization. Independently constructed the exact realistic case: `` "  point at `docs/archive/" `` on one line, `` "issues/LISS-0005-foo.md` for the historical record." `` on the next — ran the compiled regex against each line individually. | **reproduced** — neither line matches; the reference is completely invisible to the check. This is a false negative in exactly the scenario the check exists to catch (ADR 0020 Rule 1: "no Entry-layer document may reference a specific `docs/archive/` file directly"), and it is not a contrived edge case — it is a direct consequence of this repository's own established Markdown wrapping convention colliding with a per-line-only scan. See Reasons below. |
| 7 | `ENTRY_ARCHIVE_REFERENCE` fails to match a file-shaped archive path containing parentheses (e.g. `docs/archive/issues/LISS-0005-foo(1).md`) | `(` and `)` are not in the character class `[\w./-]`, so the greedy match backtracks looking for a `.` before the paren, finds none in a parenthesis-free prefix, and the overall match fails at that position. Independently verified against the compiled regex. | reproduced, but low real-world likelihood — this repository's own actual file-naming convention (`NUMBERED_FILE_PATTERNS`, confirmed by reading `scripts/check-contract-consistency.py`'s existing numbered-file regexes) never uses parentheses in filenames; noted for completeness, not treated as a blocking gap. |
| 8 | `ENTRY_ARCHIVE_REFERENCE` fails to match a backslash-style (Windows) path `docs\archive\foo.md` | The pattern literally requires forward slashes (`docs/archive/`). Independently tested; no match. | reproduced, but not a realistic risk for this repository — every document sampled uses forward-slash paths exclusively; noted for completeness only. |
| 9 | Adding `"docs/archive/",` to `RECORD_DIRS` has an unconsidered effect on `check_id_range_collisions`, `check_issue_status_sync`, or `check_open_findings_gate` | Independently greped the whole script for `RECORD_DIRS` usage (not trusting the claim in WP-0016's own reasoning): it appears at its own definition, in `check_references` (existing usage), and in the new `check_retired_terminology` (this work plan's own addition, using it by design). Read `check_id_range_collisions` (uses `NUMBERED_FILE_PATTERNS`/`os.listdir` on `docs/issues`, `docs/work-plans`, `docs/backlog`, `docs/architecture/adr`, plus full `git log --all` history — never touches `RECORD_DIRS` or `docs/archive/`), `check_issue_status_sync` (uses `glob.glob("docs/issues/LISS-*.md")` and `glob.glob("docs/work-plans/WP-*.md")` directly), and `check_open_findings_gate` (same glob pattern, plus `loop-settings.toml`) — none references `RECORD_DIRS` or `docs/archive/` anywhere. Also confirmed via `git show 3ae03d6:...` that at the DA's own baseline commit, `RECORD_DIRS` had exactly one usage site (`check_references`), so the claim was accurate for the *pre-existing* checks at the time it was made. | not reproduced |
| 10 | LISS-0044's claimed fix (outbound link from an archived file is exempt) does not actually hold on the real, final, corrected tree | Independently constructed a fresh synthetic case (not copying the Implementer's own removed artifacts): created `docs/archive/issues/LISS-9998-reviewer-synthetic-test.md` with an outbound backticked reference to a real existing ADR file, ran the checker. | not reproduced — clean pass (`contract consistency: all checks passed`), confirming the `RECORD_DIRS` exemption independently. Synthetic file and directory fully removed afterward; `find docs/archive` confirmed absent again. |
| 11 | LISS-0044's claimed fix over-broadly also stops checking *inbound* references to files under `docs/archive/`, so a genuinely dangling inbound reference would be silently missed | Independently added a scratch file (outside any `RECORD_DIRS` path) referencing the same freshly-created archived file by its real, existing path, ran the checker, then reverted; then independently tested the negative case — a scratch file referencing a *non-existent* `docs/archive/...` path. | not reproduced for the positive case (existing target resolves cleanly, no failure) — **and correctly reproduced a real failure** for the negative case: `references: reviewer-dangling-scratch.md:1 names 'docs/archive/issues/LISS-0000-does-not-exist.md', which does not exist`, exit 1. Confirms `check_references` genuinely still performs existence checking on inbound archive references rather than blanket-exempting the target side. |
| 12 | The corrected `check_no_archive_reference_from_entry` (post-`b8cc099`) over-corrected into no longer catching any genuine file-shaped reference | Independently re-read the corrected regex and re-derived (scenario 6 above already exercises it against a genuine two-line case); also confirmed via the real-tree clean run that the check is still registered and active in `main()`, not silently disabled. | not reproduced — the check still fires correctly on a genuine same-line file-shaped reference (confirmed by direct regex testing) and is still called in `main()`. |
| 13 | The scoping decision (deferring single-canonical-per-theme and canonical-source-link checks) is presented as if facet 5 is fully "done," overstating completeness the way an earlier finding this session flagged for facet 4 | Read DA-2026-08-19-08's Direction and Deferred Questions sections, WP-0016's own Goal ("Close item-0012 facet 5's **two most tractable** deterministic checks... explicitly deferred"), and LISS-0048's title ("item-0012 facet 5, scoped"). Also grepped the whole repository for every other mention of "facet 5" outside this work plan's own files, to check for an overclaiming reference elsewhere (in ADR 0020, WP-0014's review, WP-0015's review, item-0014's backlog note, the spike case file). | not reproduced — every reference sampled, in this work plan's own records and in every other document that mentions facet 5, consistently describes it as a scoped, partial subset (two of five proposed checks), with the two deferred checks explicitly named and a settling condition stated. No document found claims facet 5 is complete. |
| 14 | LISS-0044's own "Verification" section, written before the `b8cc099`/`d9fe2a2` correction, is now factually stale/inaccurate — it characterizes the `agent-quickstart.md:57` failure as "a genuine design-agreement content defect... not a `RECORD_DIRS`/`check_references` problem," but the actual resolution later established the opposite: the check's own regex was too broad, and File 3's content was never at fault | Diffed `b8cc099` and `d9fe2a2` directly (`git show <sha> --stat`): both touch `scripts/check-contract-consistency.py`, the DA, the trace, and LISS-0048's Work Notes — **neither touches `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`**. LISS-0044's Verification section was written at the initial close (`2862129`) and never revisited after the correction landed. | **reproduced** — this is a real, if minor and non-functional, documentation-accuracy gap in a closed record. It does not affect the actual fix LISS-0044 exists to verify (the `RECORD_DIRS` entry itself, independently reconfirmed at #10/#11 above), but a future reader of LISS-0044 alone, without also reading LISS-0048's later Work Notes addendum, would be misled about the root cause of the one failure it discusses. See Reasons below. |
| 15 | `docs/collaboration/terminology-migration.md` does not match DA-2026-08-19-08's File 1 verbatim, or contains a real data row | Read-through diff of the file's actual content against File 1's exact text in the DA. | not reproduced — character-for-character match, including the single placeholder row `| _(no entries yet)_ | | | |` and zero real data rows. |
| 16 | `scripts/check-contract-consistency.py`'s four edit points do not match the DA's *corrected* File 2 (i.e., the original, pre-correction bare-substring-match version was left in place instead of the fix) | `git diff 3ae03d6..HEAD -- scripts/check-contract-consistency.py`, read in full, checked against the DA's Settled Ambiguities correction row verbatim. | not reproduced — the landed code uses `ENTRY_ARCHIVE_REFERENCE = re.compile(r"docs/archive/[\w./-]*\.\w+")` and the corrected docstring item-11 wording ("a bare mention of the directory, with no file-shaped path after it, is not flagged"), matching the corrected DA text exactly, not the original bare-substring version. |
| 17 | `docs/architecture/agent-quickstart.md` does not match File 3 verbatim, is inserted at the wrong point, or other parts of the file were touched | `git diff 3ae03d6..HEAD -- docs/architecture/agent-quickstart.md`, read in full; confirmed insertion point (immediately after Session Entry's item 6, before the next section) by reading surrounding context. | not reproduced — exact verbatim match, single clean insertion, nothing else in the file changed. |
| 18 | LISS-0044 was left open, or its Status/original entries were edited/deleted rather than appended to (Invariant 2) | `git diff 3ae03d6..HEAD -- docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`, read in full. | not reproduced for status/append-only structure — `Status: proposed` → `closed`; a new, dated Work Notes entry appended (original entries byte-for-byte unchanged); the placeholder `Verification` section (`Not yet run...`) replaced with real content, which is the expected placeholder-fill behavior at closure, not an edit to a substantive original entry. (The content-accuracy problem in that same Verification section is tracked separately as scenario #14 above.) |

## Scenarios Not Searched

- Whether `check_retired_terminology` or `check_no_archive_reference_from_entry`
  behaves correctly on non-UTF-8 or unusual line-ending (CRLF) content — not
  tested; `read()`/`read_optional()` use `errors="replace"`, which likely
  degrades gracefully, but this was not independently exercised.
- Performance/runtime cost of the new checks at repository scale — not
  assessed; both are straightforward linear scans consistent with the
  script's existing checks, and no scale concern was raised anywhere in the
  DA or trace.
- The two explicitly deferred facet-5 checks (single-canonical-per-theme,
  canonical-source-link) — out of scope for this work plan by design; not
  reviewed as if they should exist yet.
- Whether `ENTRY_DOCUMENT_GLOBS` (`.grok/rules/*.md`, `.cursor/rules/*.mdc`)
  correctly enumerates every intended Entry-adjacent file in every possible
  adopting-project layout — only verified against this template's own actual
  tree.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked
      in. (Architecture Path throughout; content/code fully pre-specified by
      the DA, Implementer transcribed rather than independently designed,
      confirmed by the trace's own "Avoided LLM work" note.)
- [x] Every `Then`-equivalent acceptance criterion in DA-2026-08-19-08's Plan
      table is asserted by the work (Tasks 1-9 all have corresponding
      evidence in the trace, LISS-0048, and WP-0016; Task 10 is this review).
- [x] The dependency rule and port boundaries hold. (Not applicable in the
      Clean Architecture sense — this is documentation/process tooling, no
      application layers touched; confirmed no Domain/UseCase/Adapter code
      exists in this change.)
- [x] No boundary named in the design agreement was crossed. (No
      `docs/archive/` content persists; `CLAUDE.md`/mirrors untouched;
      confirmed independently above.)
- [x] Specifications and accepted tests were not modified to make work pass.
      (N/A — no specs; the one modification to the DA itself, at `b8cc099`,
      is a documented, dated Reopening Log correction to the DA's own
      internal contradiction, not a weakening of an acceptance criterion —
      the corrected check is *narrower*, not disabled, and still
      independently verified to catch a genuine case at scenario #12 above.)
- [x] Every claim in the artifact states its grounds. (One exception found:
      scenario #14 — LISS-0044's Verification section states a claim whose
      grounds became outdated after a later correction it was never updated
      to reflect. Non-blocking; see Reasons.)
- [x] The record would let a third party re-run this same search. (Every
      scenario above states the exact construction and command; none relies
      on this session's own internal state.)

## Decision

- [x] Approved

## Reasons

- **Mechanical conformance is complete and independently verified.** All
  three "Exact Content to Produce" files match their DA text verbatim at
  every specified insertion point (scenarios 15-17); the corrected (not
  original) version of File 2 landed (scenario 16); `docs/archive/` leaves
  no trace in the final tree; the real-tree run is independently clean
  (Deterministic Verification Output above, reproduced without trusting
  WP-0016's own pasted Preflight output); LISS-0044 is closed with its
  original entries preserved and a new entry appended (scenario 18).

- **LISS-0044's own resolution is genuinely verified, not merely asserted.**
  Scenarios 10-11 independently reconstruct the exact case LISS-0044's
  Acceptance Notes demanded — outbound link from an archived file exempt,
  inbound link to an existing archived file still resolves, inbound link to
  a *non-existent* archived file still correctly flagged as dangling — using
  fresh synthetic artifacts this review created and removed itself, not the
  Implementer's own (already-deleted) ones.

- **The mid-work-plan correction (DA Reopening Log, commit `b8cc099`) is
  sound.** The Implementer's Task 4 run correctly surfaced a genuine
  self-contradiction in the DA's own original text (a bare substring check
  flagging the DA's own mandated File 3 prose); the Design & Review group's
  fix narrows the check to a file-shaped-path regex without disabling it
  (scenario 12), and the correction was applied to the right layer (the
  check's logic, not a reword of File 3, preserving Rule 1's actual intent
  that Entry documents may describe the archive mechanism in the abstract).
  This is the process working as ADR 0014/0016 intend: a contradiction found
  during execution routed back through a design-agreement amendment, not
  silently patched around.

- **Two real, reproducible gaps exist in the shipped check logic that the
  design agreement did not anticipate (scenarios 3 and 6), but neither
  currently breaks anything and both are the same class of gap this
  repository's own precedent (LISS-0044 itself, found by WP-0014's Reviewer
  and shipped as Approved-with-tracked-finding, resolved two work plans
  later by this very WP-0016) already establishes as non-blocking:**
  - `check_retired_terminology`'s plain substring match (`if term in line`)
    has no word-boundary safeguard. Retiring a short or common term as a
    substring of other legitimate words or identifiers would produce a
    large, indiscriminate false-positive blast radius on every future CI
    run — independently demonstrated at 389 failures for a single
    constructed example. The table is empty today, so this is a no-op
    currently, exactly like `RECORD_DIRS` was a no-op before `docs/archive/`
    existed.
  - `check_no_archive_reference_from_entry` scans line-by-line with no
    cross-line joining, so a genuine specific-file archive reference split
    across a hard line-wrap — this repository's own dominant prose
    convention, observed in every document read for this review — would be
    silently invisible to the check, a false negative in precisely the
    scenario ADR 0020 Rule 1 and this check exist to catch.

  Both gaps are latent (they require a specific future edit to manifest,
  not present in the tree today), both are independently reproducible with
  actual command output (not asserted), and both are the kind of design gap
  this repository's own process routes through a tracked `Type:
  review-finding` issue and a follow-up work plan rather than blocking the
  work plan that shipped the otherwise-correct, otherwise-verified check —
  the same disposition WP-0014's Reviewer gave the structurally identical
  `RECORD_DIRS` gap that became LISS-0044.

  **Required as a condition of this Approval, per
  `docs/collaboration/findings-reuse.md`'s "must change the system or be
  explicitly declined" rule:** the Design & Review group must open two new
  `Type: review-finding` issues in `docs/issues/`, citing this review record,
  before treating facet 5's two shipped checks as durably complete:
  1. `check_retired_terminology`'s substring-match false-positive risk —
     recommend either a word-boundary-aware match (e.g. `\b`-anchored regex
     per term) or, at minimum, an explicit warning in
     `docs/collaboration/terminology-migration.md`'s own guidance telling a
     future term-retirer not to choose a term that is a substring of other
     legitimate current usage, with the check enforcing a minimum term
     length or flagging short/common terms for extra scrutiny at retirement
     time.
  2. `check_no_archive_reference_from_entry`'s per-line-only scan missing a
     reference split across a hard line-wrap — recommend scanning a
     whitespace-normalized join of the document text (or a bounded sliding
     window across adjacent lines) in addition to, or instead of, the
     current per-line scan.

  Also worth a low-priority mention in the same or a separate finding: the
  regex additionally cannot match a filename containing parentheses
  (scenario 7) or a backslash-style path (scenario 8) — both low real-world
  likelihood given this repository's own actual naming and path
  conventions, noted for completeness rather than requiring independent
  tracking.

- **One minor, non-blocking documentation-accuracy gap (scenario 14):**
  LISS-0044's own "Verification" section, written before the `b8cc099`
  correction, still characterizes the one failure it discusses as "a
  genuine design-agreement content defect... not a `RECORD_DIRS`/
  `check_references` problem" — which the later correction shows was
  actually the reverse (the check's own regex was too broad; File 3's
  content was correct all along). LISS-0044's own actual fix (the
  `RECORD_DIRS` entry) is unaffected and independently reconfirmed correct
  (scenarios 10-11); this is a stale characterization of an unrelated
  failure that happened to co-occur in the same command output, not a
  defect in LISS-0044's own resolution. Recommend a follow-up one-line
  correction to LISS-0044's Verification section (or a dated addendum, per
  Invariant 2 — never edit the original entry) noting the later correction,
  the next time any issue touches that file; not required to gate this
  Approval, since it is a closed record's prose accuracy, not a functional
  defect, and this review's own explicit instructions were not to touch
  LISS-0044 further.

- **The deferred-scope framing is honest.** Facet 5's two hardest checks
  (single-canonical-per-theme, canonical-source-link) are consistently
  described across every document that mentions them — the DA, WP-0016,
  LISS-0048's own title, and every other repository document that
  cross-references facet 5 — as explicitly deferred pending a "theme
  registry" concept this repository does not yet have, with a stated
  condition for when to revisit. No document found overstates facet 5 as
  fully complete (scenario 13); this does not repeat the facet-4-style
  overstatement pattern this session's earlier review flagged.

This work plan's mechanical execution, its LISS-0044 resolution, and its
mid-flight self-correction are all independently sound. The two functional
gaps found are real but latent, non-blocking under this repository's own
established precedent for exactly this class of finding, and are made a
binding condition of this Approval via mandatory tracked follow-up issues
rather than left as unrecorded observations.
