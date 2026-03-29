# 問題作成ルール

新しい問題を作成する際は必ず以下すべてを行うこと。

---

## 1. フォルダ構成

- 日付フォルダを作成する。日付は「今日から 2日後、4日後、6日後」の3つ。
- 同じ問題を反復して解く間隔学習のため、**3つのフォルダ内容は全て同じ**にする。

```
{YYYY-MM-DD}/
  {topic_name}.html   ← 問題ファイル（HTML）
  problems.py         ← 実行して確認できるPythonファイル
  checklist.md        ← 問題リスト
```

---

## 2. 問題ファイル（HTML）

- **必ずHTML形式**で作成する（.md不可）。
- ファイル名はトピックを表す名前（例：`integer_cache_problems.html`）。
- 解答は `<details>` タグで折りたたみにする。
- タイトルに回数（1回目・2回目・3回目）と日付を記載する。

---

## 3. checklist.md

- **1問題ファイルにつき1行**。
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

- 3日分の終日イベントを作成する。
- イベントの説明欄に GitHub Pages の問題URLを記載する。

```
タイトル： {topic} 確認問題（N回目）
説明：問題フォルダ:
https://a-f-may.github.io/MyStudy/{YYYY-MM-DD}/{topic_name}.html
```

---

## 6. GitHub

- ブランチに push する。
- GitHub Pages は `https://a-f-may.github.io/MyStudy/` で公開される。
