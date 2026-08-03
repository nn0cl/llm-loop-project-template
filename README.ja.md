# LLM Loop Project Template 日本語ガイド

[English README](README.md) · [Quickstart: 導入とアンインストール](QUICKSTART.ja.md)
 · [Changelog](CHANGELOG.md)

**契約バージョン: v2.2.0。** このリポジトリの運用契約はバージョン管理されて
おり、導入先プロジェクトはバージョンを指定して導入・参照できます。各版が
何を含むかは [CHANGELOG.md](CHANGELOG.md) を参照してください。

## プロジェクトの方向性

このプロジェクトは、**人間介入モデルに対する反証プロジェクト**です。

従来のモデルでは、人間は開発ループの二箇所に立ちます。最初の *BigDecide*
——何を、どの制約のもとで作るのかという枠組みの決定——と、agent が出す成果物
一つ一つへのフィードバックです。このモデルは、生成された成果物を正しく保つ
ものは常駐する人間の判断である、という前提に立っています。

このプロジェクトが人間を取り除くのは、開発**ループ**からです。プロジェクト
全体からではありません。

**人間がいる場所。** Director が1つのワークプランの方向性を示し、Planner
ペルソナとの対話によって詳細な計画を組み立て、設計フェーズを閉じる設計合意
（design agreement）に至ります。計画は完成した成果物のレビューではなく対話
であり、合意は相互的です——Director は「この計画が自分の作りたいものを表し
ている」ことに合意し、AI は「これ以上の解釈なしに実行可能である」ことに合意
します。Director はもう一度、ワークプラン完了時に登場します——AI が承認した
成果物を読み、同じ行為の中で次の方向性を述べます。

**人間がいない場所。** その2点の間のすべてです。phase transition の承認も、
issue 単位の test レビューも、成果物単位の sign-off もありません。issue 内の
phase transition は Implementer が自己コンテキストでレビューし、ワークプラン
内のすべての issue が完了したら、別コンテキストの Reviewer が1回だけワーク
プラン全体を審査します。ループは、この完了時点まで人間のために止まりません。
それより前に止まるのは、何が未決着かを名指しして設計合意を再開するときだけ
です。

検証したい主張はこうです。AI 支援開発における正しさは、ループに立つ人間では
なく、書かれた契約とその検証から来る。閉じたループが耐えうる成果物を出すの
であれば、人間介入モデルは前提とされてきたような必要条件ではない。出さない
のであれば、その失敗の仕方こそが発見であり、それは人間がその場で埋め合わせて
しまうのではなく、artifact 上に見える形で残らなければならない。

### AI の自己承認を形骸化させない仕組み

AI が自分の成果物を承認することは、制約がなければ無価値です。self-review
（issue 内の phase transition）と Reviewer の承認（ワークプラン単位、1回）の
どちらにも次の3つの制約がかかりますが、コンテキスト分離だけは self-review
では意図的に免除されます。

1. **コンテキスト分離。** Reviewer は成果物を作ったコンテキストとは別の
   コンテキストで動き、artifact・仕様・契約文書・ツール出力だけを受け取り
   ます。Implementer の推論は正当化根拠として採用されません。ワークプラン
   内の self-review だけがこの制約を免除されます——Reviewer 自身の承認と、
   契約ファイルの変更には適用されません。
2. **決定性の前提条件。** 決定性検証の出力が記録されていない承認は出せません。
   AI の判断は test・linter・境界検査への上乗せであって、代替ではありません。
3. **反証負荷。** 「探した失敗シナリオ」と「それが起きない根拠」を名指しする
   ことで承認します。「問題は見つからなかった」は、どちらの層でも承認では
   ありません。

self-review はコンテキスト分離をレビュー頻度と引き換えにしています——
Implementer が毎回の phase transition で自分の作業を見直す代わりに、別
コンテキストがワークプラン完了時にまとめて1回見直します。このトレードオフ
の根拠は
[ADR 0014](docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md)
を参照してください。

### 変わらないもの

`llm-project-template` から 3 つの不変条件をそのまま引き継ぎます。人間の承認を
外したことで、これらを破るコストは下がるどころか上がります——欠けた根拠を
後から補ってくれる人間は下流にいないからです。

1. **あらゆる決定はドキュメントを生む。**
2. **実行した事実は証拠を残す。**
3. **あらゆる主張は根拠を述べる。**

決定記録は
[ADR 0001](docs/architecture/adr/0001-director-centered-planning-and-closed-loop.md)
（設計フェーズとペルソナ）と
[ADR 0014](docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md)
（実行ループの粒度）にあります。運用モデルの定義は
[ai-human-scheme.md](docs/collaboration/ai-human-scheme.md)、
[personas.md](docs/collaboration/personas.md)、
[design-agreement.md](docs/collaboration/design-agreement.md) にあります。

---

これは `README.md` の逐語訳ではありません。日本語話者がこのテンプレートを
導入・運用するときに、判断を迷いやすい点を短く確認するための入口です。
正式な運用契約は `AGENTS.md`、`CLAUDE.md`、`.github/copilot-instructions.md`、
`.grok/rules/`、`.cursor/rules/` と `docs/` 配下の各文書を参照してください。
Codex は `AGENTS.md` を直接読むため専用ファイルは不要です。Cursor と Grok
Build は `AGENTS.md`（Grok Build は `CLAUDE.md` も）をフォールバックとして
ネイティブに読みますが、各ツール固有のルール面の方が強く効くため、専用
ファイルは引き続き維持しています。

## これは何か

このリポジトリは、Clean Architecture と AT-TDD を前提に、人間の Director と
複数の AI coding agent が協調するためのテンプレートです。人間は方向性の提示、
対話による計画立案、設計合意までを担い、その後の実行ループは AI ペルソナだけで
閉じます。

このリポジトリでの **AT-TDD** は、独立した標準手法名ではなく、
**ATDD + TDD のハイブリッド運用**を指す repo 内の呼び名です。受け入れ仕様から
失敗する test を作り、review 済み test に基づいて最小実装し、Green 確認後に
Refactor します。

このテンプレート配布物は、アプリケーションの仕様、技術スタック、DB、外部 API、
LLM provider、ドメインモデルを事前には決めません。それらは導入後に、導入先
リポジトリの仕様・ADR・設計合意・アーキテクチャ文書に基づいて決めます。

## 大事な考え方

- 仕様なしで実装しない。
- Phase を飛ばさない。
- 実行なしの前に設計合意を必ず記録する。
- issue 内の phase transition は Implementer が自己コンテキストで
  self-review する。ワークプラン単位の承認は Reviewer ペルソナが別
  コンテキストで1回だけ行う。
- 決定性検証の出力なしに承認しない。self-review でも決定性検証と反証負荷は
  免除されない。
- 人間 Director が関わるのはワークプランごとに2回——最初の方向性と、完了
  後のレビュー＋次の方向性（1つの行為に統合）。それ以外の細かい承認はしない。
- 記録は 3 か所に残す。設計合意は `docs/collaboration/agreements/`、
  Reviewer の判断は `docs/collaboration/reviews/`、作業の trace は
  `docs/collaboration/traces/`。
- AI に渡す context は最小限にする。
- 高度な reasoning が本当に必要だったかを trace に軽く残す。
- AI output は信頼済みデータとして扱わず、構造・根拠・review status を確認する。
- 導入先の README、仕様、アーキテクチャをテンプレートで上書きしない。

## これを使うと何が良いか

このテンプレートの価値は、AI との開発を場当たり的な chat ではなく、
review 可能な engineering workflow に寄せることです。

期待できる効果:

- 仕様が曖昧なまま AI が実装を推測することを減らす。
- Red / Green / Refactor の phase 飛ばしを減らす。
- adapter、UI、provider client、persistence に business logic が隠れるのを防ぐ。
- Fast Path / Feature Path / Architecture Path で、強い reasoning の使いすぎを抑える。
- AI に渡す context を小さくし、privacy と cost を管理しやすくする。
- dependency 採用時に、脆弱性、対象 version の実装例、troubleshooting、実ファイルでの
  最小 test、POC 可否を確認しやすくする。
- handoff や再開時に、仕様・ADR・trace から状況を追いやすくする。

詳しくは `docs/collaboration/template-benefits.md` を参照してください。

## 作業 path の使い分け

このテンプレートは、毎回 AI に重い reasoning をさせないために 3 つの path を
使い分けます。

大きめの作業では `docs/collaboration/llm-cost-reduction.md` に沿って、
選んだ path、読んだファイル、あえて省いた context、deterministic check、
強い reasoning へ escalation した理由を短く trace に残します。

### Fast Path

機械的で局所的な作業に使います。

例:

- typo 修正。
- README の短い補足。
- shell script の構文確認。
- ファイルコピーの dry-run。
- formatter、linter、search、test など deterministic tool で確認できる作業。

Fast Path では full `[DESIGN CHECK]` は不要です。compact design note で、scope、
読んだ context、省いた context、実行する deterministic check を示します。

### Feature Path

AT-TDD の Phase 1/2/3 に使います。

- Phase 1: Red。失敗する test だけを書く。
- Phase 2: Green。review 済み test を通す最小実装だけを書く。
- Phase 3: Refactor。挙動を変えずに読みやすさと境界を整える。

Feature Path では target spec、phase rule、関連 architecture document を読み、
full `[DESIGN CHECK]` を出します。

### Architecture Path

ADR、prompt/instruction 変更、privacy-sensitive routing、境界判断、process 変更に
使います。プロジェクト方針を変える場合は Director への reopening request が
必要です。

## 新規リポジトリへ導入する

テンプレート側で実行します。

```bash
scripts/copy-ai-collaboration-files.sh --target /path/to/target-repo
```

placeholder を少し埋める場合:

```bash
scripts/copy-ai-collaboration-files.sh \
  --target /path/to/target-repo \
  --project-name "Example Product" \
  --domain-summary "one-line target project summary" \
  --stack "backend language, frontend framework, package manager"
```

導入後、target repo で初回 LLM session 用 prompt を作ります。

```bash
cd /path/to/target-repo
scripts/init-llm-context.sh .
```

出力された prompt を、そのリポジトリの最初の AI session に貼ります。

### 記録の状態

このリポジトリの記録ディレクトリは空です。2026-08-02 に Director がリセット
しました。テンプレートを作る過程で溜まった local issue、work plan、trace、
review record、設計合意、sample rollout spec を作業ツリーから削除し、導入先
プロジェクトが始めるのと同じ初期状態にしてあります。git 履歴は意図的に残して
あり、削除された記録はすべてそこから辿れます。削除した commit 自体が、その
決定の記録です。

いずれにせよ copy/update script はこれらのパスを導入先には配りません。導入先
には空の `.gitkeep` 付きディレクトリだけを配り、導入先自身の agreement、
review、trace、issue、spec を作ります。

## 既存リポジトリへ途中導入する

まず dry-run します。

```bash
scripts/copy-ai-collaboration-files.sh --target /path/to/existing-repo --dry-run
```

問題なければ `--force` なしで実行します。デフォルトでは既存ファイルを
上書きしません。既存の product README や architecture document は導入先が
所有する文書として保持します。

導入先でのオンボーディングは `docs/collaboration/adoption-guide.md` を見ます。

## 導入後に最初に埋めるもの

1. `AGENTS.md`、`CLAUDE.md`、`.github/copilot-instructions.md`、
   `.grok/rules/*.md`、`.cursor/rules/*.mdc` の target 固有 placeholder。
   copy script は `--project-name`、`--domain-summary`、`--stack` で
   project 名・概要・stack placeholder を埋められますが、runtime boundary、
   datastore、migration tool、external resource、stack-specific
   architecture document は設計合意で確定した導入先の事実に基づいて
   埋めます。
2. `docs/architecture/README.md` の project-specific な説明。
3. `docs/specs/` 配下の最初の EARS/Gherkin specification。
4. 必要になった architecture document。必要になるまで作りすぎない。
5. 外部 resource 一覧。DB、settings、secret storage、外部 API、LLM provider など。

## プロジェクトを始める・進める

詳しい手順は `docs/collaboration/project-start-guide.md` にあります。

最初の流れ:

1. テンプレートを導入する。
2. project 名、stack、境界、未決定事項を placeholder に記入する。
3. 最初の仕様を `docs/specs/` に EARS/Gherkin で書く。
4. 外部 resource を ports にする候補として列挙する。
5. Feature Path の Phase 0 design intake で、必要な domain model 候補を整理する。
6. 最初のタスク群を含む設計合意を Director と結んでから test を書く。

開発中の流れ:

1. issue または no-issue reason を確認する。
2. `docs/architecture/agent-quickstart.md` を読んで path を選ぶ。
3. Feature Path では target spec と関連 architecture document を読む。
4. path に合った design note を出す。
5. 計画された phase だけを実行する。
6. deterministic verification を走らせる。
7. phase transition ごとに self-review を記録する（決定性検証の出力と
   反証シナリオ、コンテキスト分離は不要）。
8. 必要なら trace と cost/reasoning control を残す。
9. ワークプラン内のすべての issue が self-review 完了したら Preflight を
   走らせ、Reviewer ペルソナの承認を別コンテキストで1回受け、その判断を
   `docs/collaboration/reviews/` に review record として残す。
10. Reviewer 承認後、Director が結果を読み、次の方向性を同じ行為の中で
    述べる（ワークプラン close）。

ドメインモデルは、この流れの中で決めて構いません。むしろ導入後のプロジェクト
では、仕様と review 済み test に基づいて domain model を育てることが想定されて
います。

## やってはいけないこと

- テンプレート配布物や導入スクリプトに、導入先固有の domain model を含める。
- 仕様・ADR・設計合意なしに、AI が domain model を推測で決める。
- placeholder 例を、そのまま技術選定として扱う。
- Feature Path で review 前に Phase 2 へ進む。
- Fast Path で仕様変更、architecture 変更、agent instruction 変更をする。
- `--force` で既存文書をまとめて上書きする。
- private data、secret、`.env` 全文を AI prompt に入れる。

## 迷ったら

- ただの局所作業なら Fast Path。
- accepted spec に対する実装作業なら Feature Path。
- 方針や境界を変えるなら Architecture Path。
- path が曖昧なら Architecture Path に寄せて、Director に reopening request を
  出します。
