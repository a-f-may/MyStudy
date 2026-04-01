# 問題作成ルール

新しい問題を作成する際は必ず以下すべてを行うこと。

---

## 1. フォルダ構成

- 日付フォルダがなければ作成する。日付は「今日から 2日後、4日後、6日後」の3つ。
- 問題はQuestionフォルダに作成
- 対象の日付のチェックリストに、Questionフォルダに作成した問題のリンクを記載する。

```
{YYYY-MM-DD}/
  checklist.md        ← 問題リスト
Question/
  {QuestionName}.html

```

---

## 2. 問題ファイル（HTML）

- **必ずHTML形式**で作成する（.md不可）。
- ファイル名はトピックを表す名前（例：`integer_cache_problems.html`）。
- 解答は `<details>` タグで折りたたみにする。
- Questionフォルダに入れる
- かっこよく作る

---

## 3. checklist.md

- 日付フォルダに対して１つ
- **1問題ファイルにつき1行**。
- Questionフォルダの問題を
- リンクは**GitHub PagesのURL**を使用する。

```markdown
# 問題リスト（N回目：YYYY-MM-DD）

- [ ] [トピック名](https://a-f-may.github.io/MyStudy/{YYYY-MM-DD}/{topic_name}.html)
```

---

## 4. index.html（ルート）

- リポジトリルートに `index.html` を置き、全日付フォルダへのリンクを記載する。
- GitHub Pagesのトップページ： `https://a-f-may.github.io/MyStudy/`

---

## 5. Googleカレンダー

- 問題リストという名前の予定（なければ作成）に、そこにその日のチェックリストのURLを入れる
- チェックリストの問題数を更新する
- 説明欄のカレンダー上の情報としては、問題数＋チェックリストのURLとなる

```
タイトル： {topic}
説明：問題フォルダ:
https://a-f-may.github.io/MyStudy/Question/{topic_name}.html
```
---

## 6. GitHub

- ブランチに push する。
- GitHub Pages は `https://a-f-may.github.io/MyStudy/` で公開される。

## 7.問題をチェックリストに追加依頼
チェックリストに追加してといったら　２、４、６日後のチェックリストに追加して~ん
問題は作らなくていいから、こっちが指定した文字列のままチェックリストだけ更新して～ん
Googleカレンダーにもチェックリストのリンクを無ければ追加して～ん