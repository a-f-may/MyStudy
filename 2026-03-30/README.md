# 2026-03-30：中級問題 — 関数・リスト・条件分岐でのキャッシュ挙動

## 学習目標

- 関数の引数・戻り値でのキャッシュ挙動を理解する
- リスト内の整数とキャッシュの関係を把握する
- 演算結果に対するキャッシュの適用を理解する

---

## 問題 1：関数の戻り値

次のコードを実行すると何が表示されますか？

```python
def get_number(n):
    return n

a = get_number(200)
b = get_number(200)
print(a is b)

x = get_number(300)
y = get_number(300)
print(x is y)
```

<details>
<summary>解答を見る</summary>

```
True
False
```

**解説：** 関数を経由しても整数キャッシュの挙動は変わりません。`200` はキャッシュ範囲内なので `True`、`300` は範囲外なので `False` です。

</details>

---

## 問題 2：演算結果のキャッシュ

次のコードを実行すると何が表示されますか？

```python
a = 128 + 128
b = 256
print(a is b)

x = 128 + 129
y = 257
print(x is y)
```

<details>
<summary>解答を見る</summary>

```
True
False
```

**解説：** `128 + 128 = 256` はキャッシュ範囲内なので既存のキャッシュオブジェクトが返されます。`128 + 129 = 257` はキャッシュ範囲外なので新しいオブジェクトが生成されます。

</details>

---

## 問題 3：リスト内の整数

次のコードを実行すると何が表示されますか？

```python
list1 = [1, 2, 3, 256, 257]
list2 = [1, 2, 3, 256, 257]

print(list1[0] is list2[0])    # 1
print(list1[3] is list2[3])    # 256
print(list1[4] is list2[4])    # 257
```

<details>
<summary>解答を見る</summary>

```
True
True
False
```

**解説：** リストの要素として格納された整数も、キャッシュ機構は同様に働きます。`1` と `256` はキャッシュ範囲内、`257` は範囲外です。

</details>

---

## 問題 4：`sys.intern` との比較

次のコードを実行すると何が表示されますか？（文字列との比較）

```python
import sys

# 文字列のインターン
s1 = sys.intern("hello world")
s2 = sys.intern("hello world")
print(s1 is s2)   # ?

# 整数キャッシュ（自動）
n1 = 100
n2 = 100
print(n1 is n2)   # ?
```

<details>
<summary>解答を見る</summary>

```
True
True
```

**解説：** `sys.intern()` は文字列を明示的にインターンします。整数の `-5〜256` は自動的にインターンされます。どちらも同じオブジェクトを指すため `is` は `True` です。

</details>

---

## 問題 5：条件分岐でのよくある間違い

次のコードはバグがあります。何が問題で、どう修正すればよいですか？

```python
def process(value):
    result = value * 2
    if result is 300:        # ← ここに問題がある！
        print("300です")
    else:
        print(f"{result}です")

process(150)
```

<details>
<summary>解答を見る</summary>

**問題：** `is` は同一オブジェクトの比較であり、値の比較ではありません。`300` はキャッシュ範囲外なので、`result` と `300` は別オブジェクトとなり、条件は `False` になります。

**修正：**
```python
def process(value):
    result = value * 2
    if result == 300:        # == で値を比較する
        print("300です")
    else:
        print(f"{result}です")

process(150)  # "300です" と表示される
```

**教訓：** 整数の値比較には必ず `==` を使いましょう。`is` はオブジェクトの同一性チェック専用です。

</details>

---

## チェックリスト

- [ ] 関数経由でも整数キャッシュは機能することを理解した
- [ ] 演算結果もキャッシュの対象になることを理解した
- [ ] `is` ではなく `==` で値比較すべき理由を説明できる
- [ ] リスト要素でもキャッシュが機能することを確認した
