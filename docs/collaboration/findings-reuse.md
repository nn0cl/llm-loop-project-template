# Findings Reuse

Actionable review findings must change the system or be explicitly declined.
"Acknowledged" without a durable issue and outcome is a process failure.

Governed settings: `docs/collaboration/loop-settings.toml` → `[findings]`.
Lifecycle authority: `docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md`.

## Must-apply rule

When `[findings].must_apply` is true (default):

1. Every actionable Reviewer finding becomes a `docs/issues/LISS-*.md` entry
   with `Type: review-finding` and a link to the originating review record.
2. Lifecycle is `proposed -> accepted -> in_progress -> resolved -> closed`.
3. `wont_do` requires an Arbiter decision record with grounds and rejected
   alternatives.
4. `resolved` requires changed files and deterministic verification output.
5. Only a separate-context Reviewer moves the finding to `closed`.
6. Session prose, sticky notes, or chat agreement do not count as application.

## Reuse at design and build time

When `[findings].reuse_at_design_intake` is true (default), Planner and
Implementer design intake must:

1. Search `docs/issues/` for `Type: review-finding` affecting the same area,
   ports, specs, or contract files.
2. Search recent `docs/collaboration/reviews/` for findings still open.
3. Record in the design note (or design agreement settled/deferred table):

   | Finding ID | Status | How this work honors it |
   | --- | --- | --- |
   | LISS-00xx | closed | already applied in commit … |
   | LISS-00yy | open | this work plan includes fix … |
   | LISS-00zz | n/a | different subsystem; reason … |

4. Not re-introduce a defect a closed finding already eliminated, without an
   explicit ADR or agreement change that supersedes that fix.

## Work-plan gate

When `[findings].block_work_plan_done_on_open_findings` is true (default):

- Work-plan Done requires every finding from that plan's Reviewer pass to be
  `closed` or `wont_do` (with Arbiter).
- Preflight should fail if open findings from the current review cycle remain
  untracked as issues.

## Applied evidence (what "活かす" means)

A finding is applied only when at least one of the following is true and
recorded:

| Outcome | Required evidence |
| --- | --- |
| Code/docs fix | Changed paths + verification output + finding → `closed` |
| Spec/ADR change | Updated artifact + agreement or review path that authorizes it |
| Process change | Contract/ADR update under prompt-instruction change control |
| Decline | Arbiter record + `wont_do` |

Link the finding ID from the implementing issue, spike, or agreement so a
later audit can follow the chain without chat history.
