# Review Record: Contract Consistency Checker, Round 2 (PR #8, `d479308`)

Reviewing persona: Reviewer.
Model / tool: Claude Sonnet 5, via a fresh Claude Code agent session with no
memory of the producing session's reasoning. Read the redesigned
`scripts/check-contract-consistency.py`, the round-2 Preflight record, and my
own prior rejection (`docs/collaboration/reviews/2026-08-02-contract-consistency-review.md`)
only as a statement of what was claimed fixed — every claim was independently
re-tested rather than trusted. Per the coordinator's instruction, this round
attacks the **redesigned** rules rather than repeating the three original
attacks (those were re-run only briefly, to confirm the specific fixes claimed
for them, not as the basis for a decision).

Branch note: confirmed `2183b8e` (the commit I reviewed last round) is still
an ancestor of the current branch tip (`git merge-base --is-ancestor 2183b8e
origin/process/contract-consistency-check` → true), so the force-push the
coordinator mentioned did not invalidate anything this record relies on.

## Constraints (all three must hold)

- [x] **Context separation.** Did not produce the fix; producing context's
      reasoning not supplied or relied on.
- [x] **Deterministic precondition.** All checks below re-run in this session,
      against the real branch and against a disposable scratch copy for
      destructive defect injection.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below. Five reproduced as real gaps in the new code; two of those are
      severe (a smuggle-through-escape-hatch and a regression that removes
      protection the previous round had).

## Method

Copied the full tree (`git archive HEAD` + `.git`) into a fresh scratch
directory, confirmed a clean baseline (`contract consistency: all checks
passed`), then injected defects targeted at each of the five items in the
coordinator's list, one at a time, reverting between tests via `git checkout`.

## Review Target

- Artifact: branch `process/contract-consistency-check` / commit `d479308`,
  pull request #8.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-contract-consistency-check.md`
  (DA-2026-08-02-07).
- Producing persona: Implementer, responding to my prior rejection.
- Reviewing persona / model / tool: Reviewer / Claude Sonnet 5 / Claude Code.
- Approval type: specification-conformance, boundary-conformance,
  evidence-sufficiency.
- Preflight (round 2):
  `docs/collaboration/reviews/2026-08-02-contract-consistency-preflight-2.md`
  — pass, independently re-verified below (its own negative test reproduces
  in spirit; its coverage claim does not survive new attacks).

## Deterministic Verification Output

**Baseline and CI:**

```text
$ python3 scripts/check-contract-consistency.py --repo .   # real branch
contract consistency: all checks passed

$ gh pr checks 8
Repository sanity   pass   11s   .../actions/runs/30743089367/job/91483870930
$ gh pr view 8 --json headRefOid
{"headRefOid":"d4793080e6d31b745c4cea7ef4a2200a302e8ad0"}

$ required_files: 65, missing: []
$ python3 -m py_compile scripts/check-contract-consistency.py: OK
$ (copy script into a fresh git-init'd target, then inside it)
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```

**Sanity re-check of the three originally-reported holes** (brief, not the
basis for this decision):

```text
$ # "0001 to 0011" (wrong separator, round-1 attack) -> caught:
ADR range:
  README.md:235 states the range 0001-0011; the repository has 0001-0013
exit: 1                                                          # fixed

$ # reworded false banner, no escape words -> caught:
version claims:
  README.md:6 names v1.1.0, which has no git tag. ...
exit: 1                                                          # fixed

$ # totally nonexistent bare filename -> caught:
references:
  docs/collaboration/personas.md:99 names 'does-not-exist-review-record.md', ...
exit: 1                                                          # fixed

$ # NOTE: the adopter-start-number sub-case ("starting from 0012", the OTHER
$ #   half of the original ADR-range finding) still evades detection:
$ python3 scripts/check-contract-consistency.py --repo .   # QUICKSTART.md edited
contract consistency: all checks passed                          # NOT fixed
```
This last one is not a new finding — it is explicitly named in the new
docstring's "What this cannot check" section ("the sentence telling an
adopting project where to start their own numbering is matched by phrase, so
an unusual wording can evade it"), so it is disclosed rather than hidden. I
note it here only to record that the disclosure is accurate for this specific
point, not to re-litigate it as undisclosed.

### Item 1 — bare-filename leniency masking a wrong-but-existing-elsewhere reference

```text
$ # docs/collaboration/personas.md, Reviewer persona's Outputs line:
$ #   "Written with `docs/templates/review-record.md` and stored under..."
$ #   -> "Written with `design-agreement.md` and stored under..."
$ #   (WRONG document for a Reviewer's output — a Reviewer never writes a
$ #    design agreement — but `design-agreement.md` genuinely exists, twice:
$ #    docs/collaboration/design-agreement.md and docs/templates/design-agreement.md)
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Reproduced, blocking.** The bare-name resolution rule ("accept it if any
file in the repository has that name") cannot distinguish "this bare name
refers to the file the surrounding sentence describes" from "this bare name
happens to match some unrelated file elsewhere in the tree." A content error —
citing the wrong template entirely — passes silently as long as the wrong
name coincides with a real filename anywhere in the repository, which is
common here precisely because this repository's naming conventions repeat
(`design-agreement.md`, `README.md`, and the `2026-08-02-*.md` record-slug
family all exist in multiple directories).

### Item 2 — "two distinct tokens on one line are a range," both directions

**2a. False positive — a line legitimately citing two unrelated, individually
valid ADRs:**

```text
$ # README.md, inserted: "See ADR 0006 for the mirror-parity contract and
$ #   ADR 0013 for Preflight Validation, both discussed above."
$ #   (0006 and 0013 both exist; nothing here is wrong)
$ python3 scripts/check-contract-consistency.py --repo .
ADR range:
  README.md:234 states the range 0006-0013; the repository has 0001-0013
exit: 1
```
**Reproduced, as the coordinator predicted.** A correct sentence that happens
to cite two real ADRs is misread as a stale range statement and fails CI.

**2b. False negative — a genuinely wrong range split across two lines:**

```text
$ # QUICKSTART.md, rewritten across two lines:
$ #   "`0001-*.md` is where the process ADRs this template ships with begin."
$ #   "The last one it ships is `0011-*.md`; remove only those, ..."
$ #   (WRONG — the template ships through 0013, not 0011 — but each line has
$ #    only one ADR-shaped token, and 0011 is itself a real, existing ADR
$ #    number, so it passes the per-token existence check too)
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Reproduced, blocking, and the more dangerous direction.** This is a false
*negative* on the exact defect class (a stale ADR-range endpoint) the check
exists to catch, achieved with nothing more than natural sentence-splitting —
no adversarial phrasing tricks needed, just writing the same claim across two
sentences instead of one, which is a completely ordinary edit a human
copyeditor or a future agent could make without any intent to evade anything.

### Item 3 — `EXAMPLE_DOCUMENT_NAMES` and `TEMPLATE_ONLY_FILES`

**`EXAMPLE_DOCUMENT_NAMES`** — its own comment says it exists "so that a
genuine dangling reference on such a line is still caught" (as opposed to a
rule about "e.g." lines). But the suppression is by filename alone, with no
check that the reference actually sits in an illustrative context:

```text
$ # Inserted into docs/collaboration/definition-of-done.md, a normative file,
$ #   in no "e.g." context at all:
$ #   "Before merging, confirm `persistence.md` documents the current
$ #    storage schema."
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Reproduced, non-blocking but real.** Today, none of the four names in
`EXAMPLE_DOCUMENT_NAMES` are used outside their illustrative "e.g." lists, so
this is not currently masking anything — but the suppression mechanism itself
does not enforce that, so "genuinely unresolvable-by-design" is true of the
current tree's actual usage, not of the rule as written.

**`TEMPLATE_ONLY_FILES`, second use (masking references, not just skipping
absent-file checks)** — tested exactly what the coordinator asked: whether it
can mask a real dangling reference in the template repository itself.

```text
$ mv README.md /tmp/...
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed          # README.md is GONE
$ mv /tmp/... README.md   # restored

$ # repeated for the other four TEMPLATE_ONLY_FILES entries:
$ for f in QUICKSTART.md CHANGELOG.md QUICKSTART.ja.md README.ja.md; do
    mv "$f" /tmp/del_$f
    python3 scripts/check-contract-consistency.py --repo .
    mv /tmp/del_$f "$f"
  done
contract consistency: all checks passed   (x4, one per file)
```
**Reproduced, blocking, and the most severe finding in this round.** This is
also a direct answer to item 5 ("anything the redesign broke that the
previous version caught"): in my prior review of round 1 of this checker, I
tested this exact scenario and it **was** caught — deleting `README.md`
produced four `references` failures, because other tracked documents
(`QUICKSTART.md`, `QUICKSTART.ja.md`, `README.ja.md`) cross-link to it and
`check_references` had no reason to exempt that target. The redesign's
`TEMPLATE_ONLY_FILES` list unconditionally exempts these five exact filenames
from ever being reported as dangling, anywhere, including inside this
repository where four of the five are real, always-present, currently-existing
files with no other guard: none of `README.md`, `QUICKSTART.md`,
`QUICKSTART.ja.md`, or `README.ja.md` is in CI's `required_files` (confirmed:
`grep -n '"README.md"' .github/workflows/ci.yml` — no hits, unchanged by this
PR). `CHANGELOG.md` is the one exception with a backstop (`required_files`
still lists it), so its deletion would still be caught by a different CI
step — but purely by coincidence of a separate list, not because this checker
protects it. The stated justification — "an adopting project owns its own
README and receives no CHANGELOG from us" — is true and adequate for the
*first* use (`read_optional`, skipping checks over content that is absent
because it was never distributed). It does not extend to the second use,
which silences a signal about a file that is present in this repository and
is supposed to stay that way.

### Item 4 — the version rule's `unreleased`/`CHANGELOG` skip as an escape hatch

```text
$ # README.md banner line rewritten:
$ #   "**Contract edition: v1.0.0.**" ->
$ #   "**v1.1.0 is now released** (see CHANGELOG.md for details)."
$ #   (an explicit, false "v1.1.0 is now released" claim, backed by no tag)
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
**Reproduced, blocking, and severe.** The per-line skip
(`re.search(r"unreleased|未リリース|CHANGELOG", line, re.IGNORECASE)`) fires on
the mere presence of the substring "CHANGELOG" anywhere on the line — it does
not check that the line is actually *saying* the version is unreleased. A
line can say the opposite and cite the changelog as a footnote and still be
skipped.

```text
$ # second phrasing, same line:
$ #   "**v1.1.0 is not unreleased — it shipped today.**"
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```
The word "unreleased" itself needs no hedging context either — its bare
presence anywhere on the line, even inside an explicit negation ("is not
unreleased"), disarms the check. This is the same defect class that produced
two of my earlier rejections (a version claimed as released with no tag
behind it), now reproduced against the check built specifically to prevent it,
using only ordinary prose.

### Item 5 — regressions

Covered above: the `TEMPLATE_ONLY_FILES` reference-masking behavior is a
genuine regression from round 1 (see Item 3). I looked for others and did not
find any — the straightforward positive-control cases (a plain stale banner
with no escape words, a plain nonexistent bare filename, the original "0001
to 0011" phrasing) are all still caught, and the copy-script target smoke
test still passes cleanly.

### Judging the docstring's "What this cannot check, and who does" disclosure

The two limits it names — meaning drift in mirror parity, and phrase-matching
on the adopter-start-number sentence — are each accurately described and I
independently confirmed both still hold exactly as stated (meaning-drift
re-confirmed via a one-line spot check, not repeated in full since I attacked
new surfaces this round per instruction; the adopter-start-number gap
reproduced directly above). To that extent, the disclosure is honest.

It is not complete, and in one place it reads as broader than it is. The
sentence "the checks that used to depend on a fixed set of separator words or
a literal banner prefix no longer do" is literally true (those specific old
patterns are gone) but invites the reading that checks 3-5 are now
phrase-independent and therefore robust. They are not:

- Check 3 (references) gained a **new** phrase-independent leniency (any
  bare name matching any file anywhere) that creates the wrong-reference risk
  in Item 1, and a **new** filename-based suppression (`TEMPLATE_ONLY_FILES`)
  that reintroduces exactly the kind of silent gap this whole docstring
  section exists to warn about — undisclosed.
- Check 4 (ADR range) traded phrase-dependence for a different structural
  failure mode (same-line token counting), which is neither a phrasing issue
  nor disclosed as a limit — undisclosed.
- Check 5 (version claims) is described as no longer keying off "a literal
  banner prefix," which is true, but it gained a **new** phrase-dependent
  escape hatch (the `unreleased`/`CHANGELOG` line skip) that is exactly the
  kind of thing the docstring's own framing says it wants to warn about, and
  does not — undisclosed, and this is the same "claimed coverage it did not
  have" pattern the commit message uses to describe the *previous* rejection.

Judgment: **the disclosure is honest about what it says, but materially
incomplete, and the overall docstring still overclaims** for checks 3-5 by
omission — the literal claims at the top ("Every relative path... resolves,"
"No document claims a released version that has no tag") remain unqualified
by the "What this cannot check" section, which only qualifies check 1
(parity) and part of check 4.

## Falsification Search

| # | Failure scenario searched for | Grounds it does or does not occur | Result |
|---|---|---|---|
| 1 | Bare-filename resolution accepts a name that exists somewhere but is the wrong file in context | Reproduced: a Reviewer-output reference rewritten to the wrong template name (`design-agreement.md`, which exists twice, in the wrong places) passes clean. | **reproduced, blocking** |
| 2a | Two distinct, individually-valid ADR citations on one legitimate line are misread as a stale range | Reproduced: "ADR 0006 ... and ADR 0013 ..." on one correct sentence fails CI. | **reproduced, blocking (false positive)** |
| 2b | A genuinely wrong range, split across two lines, evades the range check | Reproduced: splitting a wrong "last ADR is 0011" claim onto its own line (each line then has only one, individually-valid, token) passes clean. | **reproduced, blocking (false negative)** |
| 3a | `EXAMPLE_DOCUMENT_NAMES` masks a wrong reference used outside its illustrative context | Reproduced synthetically (not currently present in the real tree): a normative sentence citing `persistence.md` as if real passes clean regardless of context. | reproduced, non-blocking (no live instance today) |
| 3b | `TEMPLATE_ONLY_FILES` masks a real dangling reference to a file that is missing from the template repository itself | Reproduced for all five entries: deleting `README.md`, `QUICKSTART.md`, `QUICKSTART.ja.md`, or `README.ja.md` from the template repo produces zero failures (and none of the four is in CI's `required_files` either); `CHANGELOG.md`'s deletion is still incidentally caught by a separate, unrelated CI check. | **reproduced, blocking** |
| 4 | A false "version X is released" claim is smuggled past the version-claims check by citing "CHANGELOG" or the word "unreleased" on the same line | Reproduced twice: "v1.1.0 is now released (see CHANGELOG.md...)" and "v1.1.0 is not unreleased — it shipped today" both pass clean. | **reproduced, blocking** |
| 5 | The redesign broke a case round 1's checker caught | Reproduced: the `TEMPLATE_ONLY_FILES` regression (row 3b) is exactly this — round 1 caught deleted `README.md` via incidental cross-reference detection; round 2 does not, by design. | **reproduced, blocking (regression)** |
| 6 | The docstring's "What this cannot check" section is inaccurate or incomplete about what remains uncovered | The two limits it names are each accurately described. It omits the five gaps above, three of which (1, 3b, 4) are undisclosed and not obviously implied by the two limits it does name. | reproduced, non-blocking (disclosure gap, judged above) |
| 7 | The three originally-reported holes are not actually fixed | Not reproduced for the core cases: "0001 to 0011," a plain reworded banner, and a wholly nonexistent bare filename are each caught. The adopter-start-number phrasing sub-case is still open but is now explicitly disclosed rather than silently missed. | not reproduced (fixes are real, for what they claim to fix) |
| 8 | The redesign introduced a false positive on the current, actual tree (not a synthetic one) | Not reproduced: the real branch and a fresh copy-script target both report `all checks passed` with no injected defects. | not reproduced |

## Scenarios Not Searched

- Exhaustive enumeration of every filename pair in the repo that could
  reproduce Item 1's masking (I found one concrete pair; there are likely
  others, given how many `2026-08-02-*.md` and `README.md`-family duplicate
  basenames exist).
- Whether `EXAMPLE_DOCUMENT_NAMES`'s risk (Item 3a) could combine with Item
  1's bare-name-anywhere leniency in a single attack — not attempted, since
  Item 3a already demonstrates the underlying mechanism is context-blind on
  its own.
- GitHub Actions execution beyond the one observed job.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked
      in.
- [x] The dependency rule and port boundaries hold — not applicable.
- [x] No boundary named in the design agreement was crossed — no ADR added or
      revised; the newly-mirrored `Project Boundaries`/`Current Non-Decisions`
      content is a completion of an existing mirroring obligation, not a new
      rule.
- [x] Specifications and accepted tests were not modified to make work pass.
- [ ] Every claim in the artifact states its grounds — **fails**: the
      docstring's disclosure section, and the PR/commit message's framing of
      checks 3-5 as no longer phrase-dependent, both read as broader coverage
      claims than the checker actually delivers.
- [x] The record would let a third party re-run this same search — every
      injected defect above is a short, literal reproduction against `d479308`.

## Decision

- [ ] Approved
- [x] **Rejected** — reasons and the specific artifact changes required below
- [ ] Deadlocked — escalate to Arbiter
- [ ] Reopening request

### Approval type outcomes

- **Specification-conformance**: **Rejected.** The design agreement's
  Falsification Criterion 1 ("The checker passes on a tree containing a
  defect of a class it claims to cover") reproduces four separate times
  against the redesigned checks (Items 1, 2a/2b, 3b, 4) — including one, the
  `TEMPLATE_ONLY_FILES` regression, that is strictly worse than the state
  this checker replaced, and another, the version-claims escape hatch, that
  reproduces the checker's own namesake defect class (a false release claim)
  using nothing but ordinary prose.
- **Boundary-conformance**: **Approved.** No ADR touched; the promotion of
  `Project Boundaries`/`Current Non-Decisions` out of `AGENTS_ONLY_SECTIONS`
  completes an existing mirroring obligation rather than inventing a new
  rule; content added to the two mirrors is a faithful paraphrase of
  `CLAUDE.md`'s existing text, not a meaning change.
- **Evidence-sufficiency**: **Rejected.** The three originally-reported holes
  are genuinely closed, and the Preflight's negative test is real — but the
  round's central claim, embodied in the new docstring section, that the
  checker's remaining limits are fully named and structural, does not survive
  testing. A checklist plus a disclosure section, both self-written by the
  same context that could not see its own blind spots, is exactly the
  situation independent review exists to catch.

## Reasons

1. **(Blocking)** `TEMPLATE_ONLY_FILES`'s reference-masking use is too broad.
   Scope it to only suppress a name when it is being read from a document
   that would exist in a copy-script target but the named file would not
   (i.e., preserve the skip for cross-references *originating from* files
   that survive distribution, if that is even the right rule) — or, more
   simply, keep the existence check for these five files unconditional
   within the template repository, and only suppress it for checks that run
   against a copy-script target (which already has a separate, correct
   mechanism: `read_optional` returning `None`). At minimum, add `README.md`,
   `QUICKSTART.md`, and `QUICKSTART.ja.md` to CI's `required_files` (a
   standing recommendation from my prior round, still not done) so their
   deletion is caught by something even if this checker is not fixed.
2. **(Blocking)** Redesign the "two tokens on a line" range heuristic. It
   needs to distinguish "these two numbers are presented as the two ends of
   a range" from "these two numbers are independently cited." A cheap
   improvement: only treat two tokens as a range when a range-shaped
   connective sits between them (even a broad set: hyphen, en dash, wave
   dash, "through," "to," "and," "から," "まで" — broader than round 1's list,
   but still connective-gated) rather than firing on co-occurrence alone;
   and separately, to catch the split-line case, consider the ADR range
   check over a whole paragraph or bullet item rather than per physical
   line, since Markdown soft-wraps a single logical sentence across lines
   routinely (as `README.md` and `QUICKSTART.md` already do throughout this
   repository).
3. **(Blocking)** Narrow the version-claims skip. Do not skip a line merely
   for containing "unreleased" or "CHANGELOG" as a substring; require the
   version token itself to be adjacent to (or the sentence to affirmatively
   state) unreleased status — e.g., only skip when "unreleased" appears
   within some short token distance of the version number, or require an
   explicit marker convention (as `CHANGELOG.md`'s own headings already use:
   `(unreleased)` immediately after the version).
4. **(Non-blocking)** Scope `EXAMPLE_DOCUMENT_NAMES` to the lines that
   actually introduce them as examples (e.g., require the line to also
   contain "e.g." or a similar illustrative marker), rather than suppressing
   the name unconditionally anywhere in the tree — or accept the current risk
   explicitly in the comment, since no live instance exists today.
5. **(Non-blocking)** Extend the docstring's "What this cannot check" section
   to name the reference-masking behavior of `TEMPLATE_ONLY_FILES` and
   `EXAMPLE_DOCUMENT_NAMES`, and the range check's line-scoped, co-occurrence
   heuristic, with the same honesty applied to checks 1 and part of 4 in this
   round. The section's own premise — that the Reviewer's finding was about
   overclaimed coverage, not just missing checks — applies to itself here.

This is not a rejection of the direction or of the genuine progress made:
three real, previously undisclosed holes are now closed for their core cases,
one non-blocking finding was resolved substantively (mirrors completed rather
than justified around), and the other was disclosed rather than silently
carried. The four blocking items above are each narrow and independently
fixable; none requires re-deciding the checker's overall design, and unlike
round 1, none of this round's holes stems from resistance to fixing what was
found — they stem from two redesigns (bare-name resolution, line-scoped range
and version parsing) each solving the reported case while opening an adjacent
one, which is the ordinary shape of security-style hardening work and is
exactly why it needs another adversarial pass rather than a self-report.

---

## Verification Environment

- Real branch inspected directly (`process/contract-consistency-check`,
  `d479308`); destructive defect injection done in a disposable scratch copy
  (`git archive HEAD` + `.git`), reverted between each test via `git
  checkout`, never touching the working tree used for other checks.
- `gh pr checks 8` and `gh pr view 8` queried live GitHub state at review time
  (2026-08-02, this session).
- Model: Claude Sonnet 5. Tool: Claude Code, fresh session, no access to any
  producing session's reasoning.
