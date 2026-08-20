# Review Record: LISS-0049 / LISS-0050 — Word-Boundary and Line-Wrap Fix Review

Minor Fix Path separate-context Reviewer confirmation, per `CLAUDE.md`'s
"Minor Fix Path" section. Each fix is judged independently.

## Constraints (all three must hold)

- [x] **Context separation.** Fresh session, no prior chat memory of this
      work plan or its correction cycle. Nothing read from a chat transcript
      or trusted from any agent's summary. Read directly from the repository
      tree at commit `19b9580` (checked out detached in this worktree,
      confirmed matching `origin/process/item-0012-remaining-facets`): the
      originating review record, LISS-0049, LISS-0050, the current
      `scripts/check-contract-consistency.py`, `terminology-migration.md`,
      and WP-0016's Work-Plan Review section. Every command in this record
      was run independently by this session, not copied from either issue
      file's pasted output.
- [x] **Deterministic precondition.** `python3 scripts/check-contract-consistency.py`
      re-run independently against the real tree (clean, exit 0 — see
      below). All synthetic test cases below were independently constructed
      by this session (different terms and wording than either issue file
      uses), run against the real checker, and fully removed afterward.
- [x] **Falsification burden.** Both fixes' claimed positive/negative cases
      were independently reconstructed with different constructions than
      the issue files' own pasted evidence, *and* actively probed for gaps
      the issue files did not test (regex-special-character terms,
      punctuation-only terms, coincidental cross-line concatenation, and
      the de-duplication logic's own correctness). Two of these probes
      surfaced genuine, reproducible defects — not "no problems found."

## Review Target

- LISS-0049 (`docs/issues/LISS-0049-retired-terminology-substring-false-positive.md`):
  `check_retired_terminology`'s word-boundary regex fix.
- LISS-0050 (`docs/issues/LISS-0050-entry-archive-reference-line-wrap-gap.md`):
  `check_no_archive_reference_from_entry`'s cross-line-pair scan fix.
- Originating review:
  `docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md`
  (Falsification Search #3 and #6).
- Pre-fix baseline: commit `b5609cf`. Fix commit: `19b9580`.
- Reviewing persona / model / tool: Reviewer, Claude Sonnet 5 via Claude
  Code, separate context/session from the Design & Review group session
  that made the fix.

## Scope Conformance (both fixes)

```text
$ git diff b5609cf..HEAD --name-status
A   docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md
M   docs/collaboration/terminology-migration.md
A   docs/issues/LISS-0049-retired-terminology-substring-false-positive.md
A   docs/issues/LISS-0050-entry-archive-reference-line-wrap-gap.md
M   docs/work-plans/WP-0016-drift-prevention-entry-docs-and-ci-checks.md
M   scripts/check-contract-consistency.py
```

Exactly the files LISS-0049/LISS-0050 name, plus the review record and
WP-0016's own findings-table update. No specification, ADR, port, data
model, or architecture boundary is touched — confirmed by reading the full
`git diff b5609cf..HEAD -- scripts/check-contract-consistency.py`: both
changes are additive logic inside the two named functions
(`check_no_archive_reference_from_entry` gains a second, cross-line-pair
scanning loop; `check_retired_terminology` gains a compiled
`\bterm\b`-anchored pattern list replacing `if term in line`), plus
docstring/guidance-text updates. WP-0016's Work-Plan Review section
(`docs/work-plans/WP-0016-drift-prevention-entry-docs-and-ci-checks.md:119-124`)
correctly lists both `LISS-0049` and `LISS-0050` as `in_progress`, not
`resolved`/`closed` — confirmed by direct read, not premature closure.

## Deterministic Verification — Real Tree

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
$ echo $?
0

$ python3 -c "import ast; ast.parse(open('scripts/check-contract-consistency.py').read())"
(no output — parses cleanly)

$ git status --porcelain
(empty both before and after all synthetic testing below)
```

## LISS-0049: `check_retired_terminology` word-boundary fix

### Independently reproduced positive/negative case (own term, real tree — not "AI")

Retired the word `log` (not `AI`) in a scratch copy of
`docs/collaboration/terminology-migration.md`, restored to case-matching
lowercase after an initial uppercase `LOG` attempt produced zero matches
(regex is case-sensitive; noted as a real property of the fix, not a
defect — the table's own term casing controls what matches). Ran the real
checker against the entire real repository tree, which already contains
132 files using "backlog" outside `docs/backlog/` — a much larger,
real-world adversarial surface than a constructed scratch file.

```text
$ sed -i 's/| _(no entries yet)_ | | | |/| `log` | `audit record` | reviewer-test | 2026-08-20 |/' docs/collaboration/terminology-migration.md
$ python3 scripts/check-contract-consistency.py
retired terminology:
  .github/workflows/ci.yml:70 uses retired term 'log' -- ...
  README.md:299 uses retired term 'log' -- ...
  docs/architecture/adr/0011-external-resource-adoption-contract.md:85 uses retired term 'log' -- ...
  docs/architecture/adr/0020-document-and-log-lifecycle-model.md:6 uses retired term 'log' -- ...
  [... 29 total matches, all genuine standalone/hyphen-token uses of "log" ...]
contract consistency: 1 failure(s)
$ echo $?
1

$ grep "retired term" <output> | grep -iE "backlog|catalog|logic|dialog"
(no output — zero false positives from any of the 132 files containing "backlog", or from "catalog"/"logic"/"dialog")
```

Restored `terminology-migration.md` to its exact original content
(`diff` confirmed identical); `git status --porcelain` confirmed clean.

**Conclusion: the fix genuinely resolves the documented finding.** The
word-boundary regex correctly flags every standalone use of an adversarial,
realistically common term while producing zero false positives against a
real, large-scale fused-substring surface (132 files) — a stronger
adversarial test than the issue's own constructed scratch case.

### Independent gap search beyond the issue's own testing

The task asked me to inspect the regex construction itself
(`\b` + `re.escape(term)` + `\b`) for gaps the issue's testing (which only
used the alphanumeric term "AI") did not cover: regex-special-character
terms, and terms that are themselves entirely non-word characters.

```text
>>> import re
>>> def make_pattern(term): return re.compile(r"\b" + re.escape(term) + r"\b")
>>> p = make_pattern("C++")
>>> p.pattern
'\\bC\\+\\+\\b'
>>> bool(p.search("the C++ language"))
False
>>> p2 = make_pattern("->")
>>> p2.pattern
'\\b\\-\\>\\b'
>>> bool(p2.search("a -> b"))
False
>>> bool(p2.search("use -> here"))
False
>>> bool(p2.search("x->y"))
True
```

**A real, reproducible gap the issue's own testing did not cover:** `\b`
only fires at a transition between a `\w` character and a `\W`/boundary
character. For a retired term that ends or begins with a non-word
character (e.g. `C++`, `->`, or any term containing punctuation at its
edges), `\b` frequently fails to match in the term's *natural* usage —
`re.escape` correctly makes the special characters literal, but does not
fix the boundary-adjacency problem. Two distinct failure shapes were
reproduced:
- `C++` retired and written in ordinary prose (`"the C++ language"`, the
  overwhelmingly common way it would actually appear) is **never flagged**
  — a silent, total no-op for a real, plausible term choice, not merely a
  narrowed-but-still-functional check.
- `->` retired shows the *inverse* of the intended semantics: it is
  **not** flagged in its natural spaced usage (`"a -> b"`) but **is**
  flagged when fused directly to word characters on both sides
  (`"x->y"`) — the opposite of what the fix exists to distinguish
  (standalone-use-should-flag vs. fused-into-identifier-should-not).

This is real and independently reproduced, but its practical exposure is
narrower than the original finding: it only manifests for a retired term
that itself starts/ends in punctuation, which is a less typical choice
than a plain word or multi-word phrase, and `terminology-migration.md`'s
own updated guidance already steers future retirements toward multi-word
phrases (though that guidance does not explicitly warn against a
punctuation-edged term, so it does not fully close this gap).

### LISS-0049 Decision: **Approved**

The fix resolves the specific documented finding (Falsification Search
#3's substring-match blast-radius risk), verified with an independently
constructed, more adversarial real-tree test than the issue's own pasted
evidence, with zero false positives and correct positive detection.

**Required as a condition of this Approval**, per the same
`findings-reuse.md` "must change the system or be explicitly declined"
rule the originating review itself invoked: open a new `Type:
review-finding` issue documenting that a retired term beginning or ending
in a non-word (punctuation) character can silently fail to match its own
natural standalone usage, or match only in the fused case — the reverse of
the check's intent — and recommend `terminology-migration.md`'s guidance
explicitly warn against choosing such a term, or that the check gain a
minimum-alnum-boundary-character guard.

## LISS-0050: `check_no_archive_reference_from_entry` line-wrap fix

### Independently reproduced positive case (own wording, real file)

```text
$ printf 'See the retired snapshot under `docs/archive/adr/\n0007-old-decision.md` for the superseded rationale.\n' >> docs/architecture/agent-quickstart.md
$ python3 scripts/check-contract-consistency.py
entry archive reference:
  docs/architecture/agent-quickstart.md:228-229 references a specific docs/archive/ file ('docs/archive/adr/0007-old-decision.md'), split across a line wrap -- ...
contract consistency: 1 failure(s)
```

File restored via `cp` from a pre-test backup; `diff` confirmed identical;
`git status --porcelain` clean afterward. The cross-line scan correctly
catches a genuine split reference with wording distinct from the issue's
own tested case.

### Independent false-positive probe: coincidental cross-line concatenation

The task asked whether two adjacent, unrelated lines could coincidentally
concatenate into a false match. Constructed a case where line 1 makes a
*bare* mention of `docs/archive/` — explicitly permitted by the check's
own docstring ("may describe the archive mechanism in the abstract") — and
line 2 is a wholly unrelated sentence that happens to start with a
filename-shaped token:

```text
$ printf 'This document explains the archive mechanism in the abstract; see docs/archive/\nconfig.py contains unrelated local script settings, not an archive pointer.\n' >> docs/architecture/agent-quickstart.md
$ python3 scripts/check-contract-consistency.py
entry archive reference:
  docs/architecture/agent-quickstart.md:228-229 references a specific docs/archive/ file ('docs/archive/config.py'), split across a line wrap -- ...
contract consistency: 1 failure(s)
```

**Reproduced — a genuine false positive.** Line 1's bare `docs/archive/`
mention is, on its own, exactly the case the check's own docstring says
must *not* be flagged. Line 2 has nothing to do with the archive. The
no-separator concatenation `lines[i] + lines[i+1]` manufactures a
file-shaped match purely from adjacency, not from any actual reference.
This is not a contrived pathological input — a bare abstract mention of
the directory followed, on the very next line, by unrelated prose that
happens to start with a dotted filename-shaped token (a version string, a
different filename, an abbreviation) is a plausible occurrence in ordinary
technical prose. File restored and confirmed identical via `diff`.

### Independent probe: de-duplication logic correctness

The task asked whether the "skip a pair where either individual line
already matched on its own" de-duplication could under- or over-suppress a
real cross-line finding. Constructed a case where line *i* has its own
genuine, unrelated standalone match, *and* also ends with a second, bare
`docs/archive/` continuing onto line *i+1* as a genuinely different split
reference:

```text
$ printf 'First see `docs/archive/known.md` for background, and also `docs/archive/\nnewer.md` for the follow-up update.\n' >> docs/architecture/agent-quickstart.md
$ python3 scripts/check-contract-consistency.py
references:
  docs/architecture/agent-quickstart.md:228 names 'docs/archive/known.md', which does not exist
entry archive reference:
  docs/architecture/agent-quickstart.md:228 references a specific docs/archive/ file ('docs/archive/known.md') -- ...
contract consistency: 2 failure(s)
```

**Reproduced — a genuine under-suppression bug.** Only the standalone
`docs/archive/known.md` on line 228 is reported. The second, genuinely
split reference `docs/archive/newer.md` (line 228's trailing bare
`docs/archive/` continuing onto line 229's `newer.md`) is never checked at
all, because the pair-skip condition fires whenever *either* line has
*any* standalone match — not only when that match is the same one the pair
would otherwise re-detect. This silently misses a real violation of
exactly the rule LISS-0050 was opened to make the check catch (ADR 0020
Rule 1), whenever it co-occurs on a line that already has an unrelated
archive reference. File restored and confirmed identical via `diff`.

### Cleanup confirmation

```text
$ diff docs/architecture/agent-quickstart.md <backup>
(no output — identical)
$ git status --porcelain
(empty)
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
```

### LISS-0050 Decision: **Rejected**

The fix does catch its own stated positive case (confirmed independently,
different wording than the issue's own test). However, two independently
reproduced defects mean it does not reliably resolve the finding it was
built for, and introduces a new failure mode the pre-fix code did not
have:

1. **A genuine functional regression (new false positive).** The pre-fix
   code never flagged a bare, explicitly-permitted abstract mention of
   `docs/archive/`. The fix's naive no-separator line-concatenation can
   now flag exactly that, whenever the next line happens to start with any
   filename-shaped token unrelated to archiving — directly contradicting
   the check's own docstring carve-out. This is not a pre-existing latent
   gap being narrowed (LISS-0049's disposition); it is a new way for the
   check to fail on legitimate content that did not fail before.
2. **A silent under-suppression bug in the fix's own de-duplication
   logic.** When a line with its own unrelated standalone archive
   reference also carries a second, genuinely split reference onto the
   next line, the pair-skip condition discards the pair entirely and the
   second, genuine violation is never reported — the exact class of
   silent miss ADR 0020 Rule 1 and this check exist to prevent, and the
   exact failure mode LISS-0050 itself was opened to close.

Recommend returning this to the Design & Review group for a corrected
approach — e.g., joining adjacent lines only when the first line's
trailing content is itself a continuation-shaped fragment (no sentence-
ending punctuation before the wrap, or the accumulated match only counted
when the file-shaped continuation begins immediately with no intervening
word/space), and checking each pair independently of whether either line
also has its own separate standalone match, rather than skipping the pair
outright.

## Summary

| Fix | Decision |
| --- | --- |
| LISS-0049 (word-boundary regex) | **Approved** — resolves its documented finding; one new, narrower latent gap found (punctuation-edged terms) and made a required tracked follow-up condition of this Approval. |
| LISS-0050 (cross-line-pair scan) | **Rejected** — introduces a reproducible false positive against the check's own stated abstract-mention exemption, and has a reproducible under-suppression bug in its own de-duplication logic that can silently miss a genuine second cross-line violation. |
