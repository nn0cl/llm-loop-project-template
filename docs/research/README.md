# Research: Benchmarking AI-Agent Development Loop Templates

This directory holds open-ended research that supports a decision or a
methodology, but is not itself a spec, an ADR, or a spike tied to one backlog
item. Spikes (`docs/spike/`) reduce a specific, scoped implementation
uncertainty; this directory holds broader investigations whose output is a
finding or a reusable tool (e.g. a measurement prompt set), not a go/no-go on
one backlog item.

## Contents

- [2026-08-24-adopter-benchmark-prompts.md](2026-08-24-adopter-benchmark-prompts.md)
  — The deliverable: a set of ready-to-run prompts for measuring this template
  (or a fork of it) inside a project that has actually adopted it.

Other dated notes in this directory are working records, not indexed here —
browse the directory listing directly.

## Context

The governing decisions for the template's process itself are
`docs/architecture/adr/0001-director-centered-planning-and-closed-loop.md`
and
`docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`.
This research asks a different question from either: not "is the process
followed correctly" (that is Reviewer/Preflight's job on each work plan) but
"does the process, as a whole, produce measurably better outcomes than not
using it" — a question this repository's own history turned out not to be
able to answer by itself.
