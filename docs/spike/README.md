# Spike Cases

Spikes reduce uncertainty through investigation. They are not feature
implementation and do not replace acceptance specifications or ADRs.

Most development decisions can be closed by research and comparison. Use a
spike when planning size would otherwise stay `TBD`, when several options
exist, or when a specification cannot yet be written without guessing.

## Location and naming

```text
docs/spike/
├── README.md                 # this file
├── .gitkeep
└── case-NNNN-short-slug/     # one directory per spike
    ├── case.md               # required record (copy from templates)
    └── evidence/             # optional notes, command output, links dump
```

Numbering:

- Use four digits: `case-0001`, `case-0002`, …
- Do not reuse numbers.
- Create the directory by copying
  `docs/templates/spike-case/` → `docs/spike/case-NNNN-short-slug/`.

Link a related local issue when the spike is on a work plan
(`Type: spike` on a `LISS-*` file is optional; the case directory is the
canonical spike record).

## Allowed work

- Web and documentation research (internet search is expected).
- Comparison tables and discard reasons.
- Throwaway proofs of concept on a throwaway branch only.
- Measurements and recorded command output under `evidence/`.

## Forbidden work

- Merging production implementation from a spike.
- Treating a spike recommendation as an Accepted ADR.
- Changing an accepted specification to match a preferred option.
- Guessing past a question the spike did not close — escalate instead.

## Selection policy: free by default, quality required

Investigate on the public internet and in primary sources (official docs,
standards, maintained project sites, advisory databases).

Default preference:

1. **No paid license or paid API required** for the selected option, when a
   free or open option meets the quality bar.
2. **Quality over cheapest-looking.** Prefer maintained projects, clear
   docs, security posture, and fit to Clean Architecture boundaries over
   novelty or marketing.
3. **Record cost explicitly.** If a paid option is still recommended, state
   the fee model, why free options fail the quality or fit bar, and what
   the Director must approve before adoption.
4. **Do not invent vendor claims.** Cite sources in `case.md`. Prefer
   primary documentation over secondary blog summaries when they conflict.

"Free" means no mandatory spend to adopt for this project's intended use
(self-hosted open source, free tiers that cover the stated load, or tools
already licensed to the Director). It does not mean "abandon quality."

## Done when

`case.md` records all of the following:

1. The question in one sentence.
2. Candidates and evaluation criteria.
3. Selected option (or "none / need human decision / abandon") with
   discard reasons for the rest.
4. Evidence (links, measurements, PoC results) with sources.
5. **Next action** is exactly one of:
   - write or refine a Spec and open an implementation issue
   - open or update an ADR (`Proposed` until a design agreement accepts it)
   - open a human decision issue (`Type: decision`) when research cannot close it
   - return the item to backlog or drop it

## Loop rules

- Do not start Green implementation that depends on an open spike.
- Model the dependency with `depends_on` on the implementation issue, or
  state the case ID in the issue's blocked reason.
- A closed spike that recommends an architecture policy still needs an ADR
  path before that policy is treated as settled.
- Preflight for a work plan should fail if a planned implementation issue
  still depends on an open spike case.

## Status values (in `case.md`)

- `open` — investigation not finished
- `closed` — next action recorded; do not keep editing selection without a
  new case or a revision section
- `superseded` — replaced by a later case ID
