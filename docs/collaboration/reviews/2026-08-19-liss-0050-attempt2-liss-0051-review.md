# Review Record: LISS-0050 (Attempt 2) / LISS-0051 — Round 2 Confirmation

Minor Fix Path separate-context Reviewer confirmation, per `CLAUDE.md`'s
"Minor Fix Path" section. Each fix is judged independently. This is round 2
for LISS-0050 — Attempt 1 was Rejected by a prior separate-context Reviewer
(`docs/collaboration/reviews/2026-08-19-liss-0049-liss-0050-word-boundary-and-line-wrap-fix-review.md`).

## Constraints (all three must hold)

- [x] **Context separation.** Fresh session, no prior chat memory of this
      work plan or its correction cycle. Nothing read from a chat transcript
      or trusted from any agent's summary. Read directly from the repository
      tree at commit `415a78f` (detached-checked-out in this worktree,
      confirmed descended from `origin/process/item-0012-remaining-facets`):
      the prior Rejection review record, LISS-0050 (current state, both
      attempts preserved), LISS-0051, the current
      `scripts/check-contract-consistency.py`, `terminology-migration.md`,
      and WP-0016's Work-Plan Review section. Every command below was run
      independently by this session against the real tree, not copied from
      either issue file's pasted output.
- [x] **Deterministic precondition.** `python3 scripts/check-contract-consistency.py`
      re-run independently against the real tree (clean, exit 0). AST parse
      re-confirmed. All synthetic test cases below were independently
      constructed by this session (different wording/constructions than
      either issue file or the prior Reviewer round used), run against the
      real checker, and fully removed afterward (`diff` + `git status
      --porcelain` confirmed clean after every probe).
- [x] **Falsification burden.** Both of the prior round's reproduced defects
      were re-tested with my own independently worded constructions (not the
      issue file's pasted cases). Beyond that, I searched specifically for a
      *third* adversarial construction the prior round did not try: fenced
      code blocks, double/triple-backtick spans, opening-backtick-alone
      lines, and chained multi-line matches. One genuine, reproducible gap
      was found (not a regression, but an undisclosed scope limit) — see
      below. "No problems found" is not the outcome here.

## Review Target

- LISS-0050 (`docs/issues/LISS-0050-entry-archive-reference-line-wrap-gap.md`):
  `check_no_archive_reference_from_entry`'s corrected (Attempt 2)
  backtick-delimited cross-line-pair scan.
- LISS-0051 (`docs/issues/LISS-0051-retired-terminology-punctuation-edged-term-gap.md`):
  `terminology-migration.md`'s guidance-text mitigation for punctuation-edged
  retired terms.
- Prior Rejection: `docs/collaboration/reviews/2026-08-19-liss-0049-liss-0050-word-boundary-and-line-wrap-fix-review.md`
  (LISS-0050 section — Attempt 1 Rejected for a new false positive and a
  silent under-suppression bug).
- Pre-Attempt-2 baseline: commit `19b9580` (Attempt 1's state). Attempt 2
  commit: `415a78f`.
- Reviewing persona / model / tool: Reviewer, Claude Sonnet 5 via Claude
  Code, separate context/session from the Design & Review group session
  that made the Attempt 2 correction.

## Scope Conformance

```text
$ git diff 19b9580..HEAD --name-status
A   docs/collaboration/reviews/2026-08-19-liss-0049-liss-0050-word-boundary-and-line-wrap-fix-review.md
M   docs/collaboration/terminology-migration.md
M   docs/issues/LISS-0049-retired-terminology-substring-false-positive.md
M   docs/issues/LISS-0050-entry-archive-reference-line-wrap-gap.md
A   docs/issues/LISS-0051-retired-terminology-punctuation-edged-term-gap.md
M   docs/work-plans/WP-0016-drift-prevention-entry-docs-and-ci-checks.md
M   scripts/check-contract-consistency.py
```

Exactly the files LISS-0050/LISS-0051 name (the script, the terminology
guidance, both issue files, WP-0016's own table update, plus the prior
review record that this correction cycle produced). No specification, ADR,
port, data model, or architecture boundary touched.

```text
$ grep -n "^- Status:" docs/issues/LISS-0050-entry-archive-reference-line-wrap-gap.md docs/issues/LISS-0051-retired-terminology-punctuation-edged-term-gap.md
docs/issues/LISS-0050-entry-archive-reference-line-wrap-gap.md:7:- Status: in_progress
docs/issues/LISS-0051-retired-terminology-punctuation-edged-term-gap.md:7:- Status: in_progress
```

Both correctly `in_progress`, not prematurely `resolved`/`closed`, pending
this decision. WP-0016's Work-Plan Review section (lines ~119-124) lists
both the same way.

## Deterministic Verification — Real Tree

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
$ echo $?
0

$ python3 -c "import ast; ast.parse(open('scripts/check-contract-consistency.py').read())"
(no output — parses cleanly)

$ git status --porcelain
(empty, both before and after every synthetic probe below)
```

## LISS-0050 (Attempt 2): `check_no_archive_reference_from_entry` corrected cross-line scan

### Design read

`ENTRY_ARCHIVE_REFERENCE` (no backtick requirement) still runs unconditionally
per-line, first, exactly as before Attempt 1 ever existed. The backtick
requirement (`ENTRY_ARCHIVE_BACKTICKED_SPAN`) is only added as a *second*,
additional pass for cross-line matches. This directly answers one of the
questions this round was asked to check: **requiring backticks for the
cross-line case does not narrow the pre-existing same-line case**, because
that check is untouched and still backtick-agnostic.

### Re-confirmed with my own wording (not the issue's pasted cases)

```text
$ printf '\nThe archive holds retired documents; browse it at docs/archive/\nsettings.py is unrelated and lives under scripts/, not archive.\n' >> docs/architecture/agent-quickstart.md
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
(no false positive on my own bare-abstract-mention wording; file restored, diff identical)

$ printf '\nCross-reference `docs/archive/example-one.md` here, and also `docs/archive/\nexample-two.md` there for more.\n' >> docs/architecture/agent-quickstart.md
$ python3 scripts/check-contract-consistency.py
entry archive reference:
  docs/architecture/agent-quickstart.md:229 references a specific docs/archive/ file ('docs/archive/example-one.md') -- ...
  docs/architecture/agent-quickstart.md:229-230 references a specific docs/archive/ file ('docs/archive/example-two.md'), split across a line wrap -- ...
contract consistency: 3 failure(s)
(both violations reported on my own wording, no under-suppression; file restored, diff identical)
```

Both of Attempt 1's reproduced defects are genuinely fixed, not merely fixed
for the exact wording the prior Reviewer happened to construct. This is the
same conclusion the issue file's own Attempt 2 verification reaches, now
independently reconfirmed with different constructions.

### Same-line detection unaffected by the backtick requirement

```text
$ printf '\ntest: docs/archive/some-test-path-no-backtick.md end\n' >> docs/architecture/agent-quickstart.md
$ python3 scripts/check-contract-consistency.py
entry archive reference:
  docs/architecture/agent-quickstart.md:229 references a specific docs/archive/ file ('docs/archive/some-test-path-no-backtick.md') -- ...
contract consistency: 1 failure(s)
(caught with no backticks anywhere on the line -- confirms ENTRY_ARCHIVE_REFERENCE
still runs independently of the new backtick-bounded cross-line pass; restored)
```

### Chained cross-line matches (own adversarial construction)

Two separate backtick-bounded references, each independently spanning a line
wrap, sharing a middle line:

```text
$ printf '\nSee `docs/archive/adr/\n0007.md` and also `docs/archive/adr/\n0008.md` for details.\n' >> docs/architecture/agent-quickstart.md
$ python3 scripts/check-contract-consistency.py
entry archive reference:
  docs/architecture/agent-quickstart.md:229-230 references a specific docs/archive/ file ('docs/archive/adr/0007.md'), split across a line wrap -- ...
  docs/architecture/agent-quickstart.md:230-231 references a specific docs/archive/ file ('docs/archive/adr/0008.md'), split across a line wrap -- ...
contract consistency: 2 failure(s)
(both reported separately, no double-count, no drop; restored)
```

The per-adjacent-pair scan (`for i in range(len(lines) - 1)`) processes each
`i` independently, and because the backtick character is excluded from the
content character class `[\w./\n-]`, `finditer` naturally treats a backtick
as a hard delimiter within one joined pair — this rules out the greedy
`*` accidentally swallowing past an intervening backtick into a second,
unrelated span on the same joined string.

### Double-backtick (markdown escape convention) — accidental but correct

```text
$ printf '\nSee ``docs/archive/adr/\n0009.md`` for details.\n' >> docs/architecture/agent-quickstart.md
$ python3 scripts/check-contract-consistency.py
entry archive reference:
  docs/architecture/agent-quickstart.md:229-230 references a specific docs/archive/ file ('docs/archive/adr/0009.md'), split across a line wrap -- ...
contract consistency: 1 failure(s)
(caught -- restored)
```

Markdown's own double-backtick escape convention (used when the enclosed
text itself contains a literal backtick) still matches, because the regex's
single-backtick delimiters land on the *inner* pair of the doubled
delimiters. Not a designed feature of this fix, but not a defect either —
verified directly rather than assumed.

### New gap found: a reference split inside a fenced code block is invisible to both checks

I was asked to specifically try a code fence (```` ``` ````) instead of
inline backticks. This is a genuine, reproducible miss:

```text
$ printf '\n```\ndocs/archive/adr/\n0007-old-decision.md\n```\n' >> docs/architecture/agent-quickstart.md
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
(the split reference goes completely undetected -- restored)
```

Neither check catches this: the per-line check needs `docs/archive/` and a
file extension on the *same* line, and this split defeats it exactly as the
original (pre-LISS-0050) per-line-only scan was defeated; the new cross-line
pass requires an opening and closing single backtick immediately around the
span, and a fenced code block's triple-backtick delimiters sit on their own
lines, never adjacent to the path text itself, so `ENTRY_ARCHIVE_BACKTICKED_SPAN`
never matches.

**Disposition:** this is not a regression introduced by Attempt 2 — no prior
version of this check (pre-LISS-0050, or Attempt 1) ever caught this case
either, and the code's own comments and LISS-0050's Acceptance Notes
explicitly scope the fix to "a reference still bounded by an opening and
closing backtick," never claiming fenced-code-block coverage. It is,
however, a real, undisclosed scope limit — distinct from the already-named
"3+ line split" Deferred Question in the issue file. Given this repository's
Entry documents can plausibly contain a fenced example (a directory listing,
a sample command) referencing an archived file, I judge this the same class
of narrow, disclosed-after-the-fact gap as LISS-0049's punctuation-edged-term
finding, not grounds for a third Rejection on the backtick-bounded case this
fix actually claims to solve.

**Required as a condition of this Approval**, consistent with the LISS-0049
precedent in the prior review round: open a new `Type: review-finding` issue
documenting that a `docs/archive/` specific-file reference split across a
hard line-wrap inside a fenced code block (```` ``` ````, not inline single
backticks) is invisible to both the per-line and cross-line passes, and
record it as a Deferred Question or a scope note in LISS-0050 alongside the
existing 3+-line-split item.

### Docstring/comment accuracy

Re-read `ENTRY_ARCHIVE_BACKTICKED_SPAN`'s comment block and
`check_no_archive_reference_from_entry`'s docstring/inline comments
(`scripts/check-contract-consistency.py:1080-1163`) against the behavior
exercised above: the claims ("requiring backticks... avoids flagging a bare
legitimate abstract mention," "a match fully contained within one line...
already reported... skip it," "independent of whether either line also
carries its own separate standalone match") all match what was actually
observed. The one place the comment overreaches slightly is calling
backtick-bounding "this repository's own established convention for every
specific-file reference" — checked against the real tree
(174 `docs/archive/` mentions, 131 immediately backtick-prefixed; the
remaining ~43 are bare abstract mentions with no file extension, or are
themselves inside quoted command-output blocks in trace/review files, not
genuine un-backticked Entry-document prose references). The claim holds in
practice; "established convention," not an absolute guarantee, is a
reasonable characterization given real usage.

### LISS-0050 (Attempt 2) Decision: **Approved**

Both of Attempt 1's reproduced defects (new false positive on a bare
abstract mention; silent under-suppression when a line carries both a
standalone and a separate cross-line match) are genuinely fixed — reconfirmed
with my own independently worded constructions, not just the issue's pasted
evidence. The backtick requirement does not regress the pre-existing
same-line detection. No overlapping-match double-count or drop was found
across a 3-line chained construction. Docstrings/comments are accurate.

**Required as a condition of this Approval**: open a `Type: review-finding`
issue for the fenced-code-block gap found above (a `docs/archive/` reference
split across a line wrap inside a ```` ``` ```` code fence is invisible to
both checks) — narrow, undisclosed-until-now, not a regression, same
disposition class as LISS-0049's own required follow-up.

## LISS-0051: `terminology-migration.md` guidance mitigation

### Guidance text re-verified against real `re` behavior

```text
>>> import re
>>> def make_pattern(term): return re.compile(r"\b" + re.escape(term) + r"\b")
>>> bool(make_pattern("C++").search("the C++ language"))
False
>>> bool(make_pattern("->").search("a -> b"))
False
>>> bool(make_pattern("->").search("x->y"))
True
```

Matches the guidance's exact claim: a punctuation-edged term either silently
fails to match its own natural usage (`C++`), or is flagged only in the
fused case, never the natural spaced case (`->`) — the reverse of intent.

### Additional own check: the guidance's positive claim

The guidance also asserts "a term made only of letters, digits, and internal
hyphens/spaces does not have this problem" — verified directly rather than
taken on faith:

```text
>>> bool(make_pattern("audit-record").search("the audit-record system"))
True
>>> bool(make_pattern("audit-record").search("preaudit-recordx"))
False
>>> bool(make_pattern("legacy log system").search("the legacy log system was retired"))
True
```

Both hold: a hyphenated or multi-word term with alphanumeric start/end
characters is correctly flagged in standalone use and correctly excluded
when fused into a longer identifier — `\b` only needs a word/non-word
transition at the term's own edges, and an internal hyphen or space never
touches that. The guidance neither overstates the risk (it names the exact
two reproduced failure shapes, not a vaguer "may misbehave") nor understates
it (it explains the mechanism, not just the symptom, so a future
term-retirer can judge other punctuation-edged terms by the same reasoning).

### Verification re-run

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
$ echo $?
0
```

Documentation-only change; no check logic touched, consistent with the
issue's own Acceptance Notes.

### LISS-0051 Decision: **Approved**

The guidance text accurately describes the real `\b`-boundary failure mode,
correctly names both reproduced failure shapes, and correctly characterizes
what kind of term avoids the problem — verified independently against actual
`re` behavior, not merely read for plausibility. Proportionate response given
the narrow practical exposure (a future retirement would have to deliberately
choose a punctuation-edged term against this warning).

## Cleanup Confirmation

```text
$ diff /tmp/aq-backup.md docs/architecture/agent-quickstart.md
(no output — identical, after every probe above)
$ git status --porcelain
(empty)
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
```

## Summary

| Fix | Decision |
| --- | --- |
| LISS-0050 (Attempt 2 — backtick-delimited cross-line scan) | **Approved** — both Attempt 1 defects genuinely fixed, reconfirmed with independently worded constructions; no regression to same-line detection; no double-count/drop across a 3-line chain. **Condition:** open a new `Type: review-finding` issue for the fenced-code-block gap (a split reference inside ```` ``` ```` is invisible to both checks) — narrow, pre-existing, disclosed now, not a regression. |
| LISS-0051 (terminology guidance mitigation) | **Approved** — guidance text verified accurate against real `re.search` behavior for both the negative claim (punctuation-edged terms misbehave, in the two documented shapes) and the positive claim (internal-hyphen/space, alnum-edged terms do not). Proportionate documentation-only response. |
