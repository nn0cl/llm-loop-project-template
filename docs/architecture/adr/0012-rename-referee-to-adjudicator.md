# 12. Referee から Adjudicator への役割名称変更

Date: 2026-07-16
Status: Accepted; 役割定義は ADR 0013
(Director-Centered Planning and an AI-Closed Execution Loop) により
2026-08-02 に superseded

この ADR はもはや規範ではない。人間の役割名は `Director` に変更され、
名称だけでなく責務そのものが変わった。現行の規則は
`docs/architecture/adr/0013-director-centered-planning-and-closed-loop.md`
を参照すること。本文は、その変更前に何が決まっていたかの記録として残す。

## Context

本テンプレートでは、AIとの協働において最終的な意思決定を下し、フェーズゲートを管理する人間の役割を「Referee（裁定者・審判）」と呼んできた。この名称は、「ルールの番人としてプロセスをコントロールする存在」というアジャイル寄りのニュアンスを持っていた。

しかし、この役割は単なるルールの進行役にとどまらず、アーキテクチャの意思決定（ADRの採否）、仕様と実装の境界の確定、およびプロジェクトの責任の最終的な引き受けという、極めて重い「裁定（Adjudication）」を伴うものである。

AIエージェントの自律性が高まるにつれ、人間の役割が「単なるファシリテーターやレビューアー」ではなく、「公式な意思決定と責任の所有者」であることをより明確に示す必要があるという議論が提起された。

## Decision

本テンプレートおよび関連ドキュメント全般において、人間の意思決定者・裁定者を指す用語を **「Referee」から「Adjudicator」に変更する**。

これに伴い、以下の関連用語も変更する：
- Referee -> Adjudicator
- Referee-centered collaboration -> Adjudicator-centered collaboration

## Consequences

- **ポジティブ:** 
  - 人間の役割が「公式な裁定者・意思決定者」であることが名称からも明確になり、AIと人間の責任分界点がより強調される。
  - ADRのような「法（Law）」を扱うアーキテクチャにおいて、法的な決定権を持つ「Adjudicator」という用語はドメインの比喩と強固に整合する。
- **ネガティブ:** 
  - 馴染みのある「Referee」という言葉に比べ、「Adjudicator」はフォーマルでやや重い単語であるため、初学者の認知的ハードルが一時的に上がる可能性がある。
  - この変更はリポジトリ内の広範なファイルに影響を与えるため、既存の下流プロジェクトで同期時にマージコンフリクトが発生する可能性がある。

## References

- 関連: ADR 0003: AI-Human Collaboration Governance（同じく ADR 0013 により
  supersede 済み）
- 関連: ADR 0013: Director-Centered Planning and an AI-Closed Execution Loop
- この ADR はかつて rationale essay 集への参照を持っていたが、当該ディレクトリ
  は Director の指示により 2026-08-02 に削除された。参照先が存在しないため
  リンクは復元せず削除した。経緯は
  `docs/collaboration/traces/2026-08-02-director-model-contract-rewrite.md`
  に記録されている。
