# Design Agreement: Review Issues and Minor Fix Path

## Identity

- Agreement ID: DA-2026-08-02-04
- Date: 2026-08-02
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Codex / GPT-5
- Supersedes agreement (if any): none

## Direction

レビュー結果の指摘事項を追跡可能な ISSUE として記録し、採択された指摘を修正・検証できるようにする。レビュー結果に異議がある場合は、根拠付きで否定できるようにする。また、軽微な修正には独立した短い経路を設け、作業内容に応じて最小の安全なモデル能力クラスを選択する。

## Scope

- In scope:
  - `LISS-*` ISSUE に `review-finding` 型とレビュー指摘の状態遷移を追加する。
  - 指摘の採択、修正、検証、否定を記録するテンプレートと契約を追加する。
  - Minor Fix Path と適用条件を定義する。
  - 処理単位ごとのモデル能力クラスの標準ルーティングを定義する。
- Explicitly out of scope:
  - 特定ベンダー、商用モデル名、API、価格、プロバイダーの選定。
  - アプリケーション固有の ISSUE 永続化スキーマ。
  - 既存の Director ゲート、Reviewer の独立コンテキスト、決定的検証の要件の変更。

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | レビュー指摘 ISSUE の状態・証拠・否定規則を定義 | Specifier | Architecture Path | 指摘が提起から終了まで追跡でき、否定には Arbiter の根拠が必要 | 文書整合性検索、リンク検査 |
| 2 | Minor Fix Path を定義 | Specifier | Architecture Path | 適用条件、除外条件、検証、Reviewer 要件が明記される | 契約文書検索、シナリオ照合 |
| 3 | 処理別のモデル能力クラスを定義 | Specifier | Architecture Path | 全処理に最小の推奨能力クラスとエスカレーション条件がある | ルーティング表の網羅性検査 |
| 4 | ISSUE・レビュー記録・作業計画テンプレートを同期 | Implementer | Phase 2 Green | 新しい状態と証拠欄が各テンプレートで一貫する | YAML/Markdown構文、参照検索 |

Sequencing and dependencies:

- Tasks 1–3 が先行し、Task 4 はその決定を反映する。
- Task 4 の後に、別コンテキストの Reviewer が文書と決定的検証結果を確認する。

## Specifications

- `docs/specs/review-issue-and-minor-fix-path.feature.md`

## Boundaries

- ISSUE はレビュー結果の証拠台帳であり、自由記述だけで状態を確定しない。
- Implementer は自分の修正を Reviewer として承認しない。
- 指摘の否定は `wont_do` とし、Reviewer の単独判断ではなく Arbiter の根拠付き記録を必要とする。
- Minor Fix Path は既存仕様・既存境界の範囲内に限る。仕様、ADR、ポート、データモデル、依存関係を変える場合は通常の Architecture/Feature Path に戻る。
- モデルの具体名は選ばず、能力クラスと互換性状態を記録する。

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| 指摘はどの台帳で管理するか | 既存の `docs/issues/LISS-*.md`。`Type: review-finding` を追加する | Director-approved planning |
| 指摘への異議を誰が確定するか | Arbiter。根拠がなければ設計合意を再開する | Existing closed-loop contract |
| 軽微修正で省略できるもの | 別 ISSUE/計画の新設のみ。決定的検証と Reviewer 確認は省略しない | Existing phase discipline |
| モデル指定の粒度 | ベンダー名ではなく能力クラス。実行時の表示名と互換性状態を記録する | Existing ADR 0002/ADR 0010 |
| 記録の日付 | 実行環境の `date` 出力を根拠として記録し、別コンテキストの表示日付との差だけでは不整合としない | Planner; shell evidence |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| 特定モデル名の標準値 | 採用プロバイダーと実行環境が ADR で決定された時点 |
| ISSUE を自動生成・遷移する CI/CLI | 実運用で手作業の状態ドリフトが観測された時点 |

## Verification

- `git diff --check`
- 参照先ファイルの存在検査
- 状態名・能力クラス名のリポジトリ内整合性検索
- 既存 CI のリポジトリ健全性検査

## Falsification Criteria

- 採択された指摘に修正または否定の根拠がない。
- `wont_do` が Arbiter の記録なしに設定できる。
- Minor Fix Path が仕様・境界変更を覆い隠す。
- 単純な作業が常に強い推論エージェントへ送られる、または複雑な判断が軽量モデルだけで完結する。

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation.

Recorded basis: Director message `承認` following the reopening request and the
settled decisions recorded above.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
| 2026-08-02 | Review issues, Minor Fix Path, and model routing were outside the previous agreement | This agreement records the new scope and boundaries |
