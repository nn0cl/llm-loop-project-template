# Design Agreement: Preflight Validation Before Independent Review

## Identity

- Agreement ID: DA-2026-08-02-05
- Date: 2026-08-02
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Codex / GPT-5
- Supersedes agreement (if any): none

## Direction

重い独立 Reviewer の前に、決定的検査と軽量モデルによる Preflight Validation を置き、形式不備・証拠不足・スコープ不一致を安価に検出する。Preflight は承認ではなく、独立 Reviewer の判断を置き換えない。

## Scope

- In scope:
  - Preflight Validation の適用条件、検査項目、出力、失敗時の遷移を定義する。
  - deterministic tool と lightweight reasoning model の routing を追加する。
  - Reviewer が再利用できる Preflight 証拠欄を追加する。
- Explicitly out of scope:
  - 独立 Reviewer の廃止または承認権限の移譲。
  - Preflight による仕様適合、`wont_do`、`closed` の確定。
  - 特定ベンダー、商用モデル、実行ランナーの選定。

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Preflight の契約と失敗遷移を定義 | Specifier | Architecture Path | pass/fail、検査項目、失敗時の修正経路、Reviewer 非代替が明記される | 仕様・ADR・契約語彙の整合性検査 |
| 2 | 文書テンプレートと routing を同期 | Implementer | Phase 2 Green | trace、review record、routing 表、agent contract に同じ規則がある | `git diff --check`、参照・語彙検索 |
| 3 | 決定的検証結果を記録し Reviewer に引き渡す | Implementer | Phase 2 Green | Preflight のコマンドと出力が記録され、Reviewer の独立判断を要求する | deterministic checks、レビュー記録 |

Sequencing and dependencies:

- Task 1 が Task 2 に先行する。
- Task 3 の成果は独立 Reviewer の入力になるが、承認の根拠を Preflight だけにしない。

## Specifications

- `docs/specs/preflight-validation.feature.md`

## Boundaries

- Preflight は提出可否の事前検査であり、AI approval ではない。
- Preflight を実行した Implementer は Reviewer として同じ変更を承認できない。
- `fail` は Implementer に戻す。修正後は Preflight を再実行する。
- `pass` でも独立 Reviewer を必ず実行する。
- Preflight の lightweight model は、欠落・不整合の指摘だけを行い、意味的な最終判定をしない。

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Preflight の目的 | 明白な形式・証拠・スコープ不備を独立レビュー前に除去する | Director-approved planning |
| pass の意味 | Reviewer に提出可能。承認済みを意味しない | Existing approval model |
| fail の意味 | Implementer に修正を戻し、Reviewer へ送らない | Process design |
| routing | deterministic tool を先行し、文書整合性の補助に lightweight reasoning model を使う | Existing routing policy |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Preflight の自動 runner 化 | 手動検査による再発または記録漏れが観測された時点 |

## Verification

- `git diff --check`
- 必須ファイル存在検査
- Preflight 語彙と Reviewer 非代替規則のリポジトリ検索
- ADR index とトレース記録の整合性検査

The Preflight contract coverage count means these eight named synchronization
surfaces, not every file in the repository that happens to contain the word
`Preflight`: `AGENTS.md`, `CLAUDE.md`, `docs/architecture/implementation-
readiness.md`, `docs/collaboration/ai-human-scheme.md`,
`docs/collaboration/definition-of-done.md`,
`docs/collaboration/model-tool-capability-matrix.md`,
`docs/templates/review-record.md`, and `docs/templates/ai-work-trace.md`.

Recorded deterministic result is preserved verbatim in the trace. Artifact
dates use the executing environment's `date` output; another context's
displayed date alone does not establish a date inconsistency.

## Falsification Criteria

- Preflight pass が独立 Reviewer の省略を許す。
- Preflight fail が修正と再検査を要求しない。
- 軽量モデルが最終仕様適合や `wont_do` を確定できる。
- Preflight の実行結果が Reviewer に渡る記録欄がない。

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation.

Recorded basis: Director request `追加して` following the agreed Preflight
Validation design direction.
