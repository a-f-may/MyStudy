# 整数キャッシュ範囲 理解度確認問題（1回目：2026-03-31）

## ポイント

- Pythonは `-5` 〜 `256` の整数をキャッシュしている
- `==` は**値**の比較、`is` は**同一オブジェクト**かの比較
- 整数の値比較には必ず `==` を使うこと

---

## Q1

次のコードの出力を答えてください。

```python
a = 100
b = 100
print(a is b)
print(a == b)
```

<details>
<summary>解答を見る</summary>

```
True
True
```

`100` はキャッシュ範囲内なので `a` と `b` は同じオブジェクト。どちらも `True`。

</details>

---

## Q2

次のコードの出力を答えてください。

```python
a = 257
b = 257
print(a is b)
print(a == b)
```

<details>
<summary>解答を見る</summary>

```
False
True
```

`257` はキャッシュ範囲外。値は等しいが別オブジェクトなので `is` は `False`、`==` は `True`。

</details>

---

## Q3

次のコードの出力を答えてください。

```python
print(-5 is -5)
print(-6 is -6)
print(256 is 256)
print(257 is 257)
```

<details>
<summary>解答を見る</summary>

```
True
False
True
False
```

`-5` と `256` はキャッシュ範囲の境界値。`-6` と `257` は範囲外。

</details>

---

## Q4

次のコードの出力を答えてください。

```python
def double(n):
    return n * 2

a = double(100)
b = double(100)
print(a is b)   # 200

x = double(150)
y = double(150)
print(x is y)   # 300
```

<details>
<summary>解答を見る</summary>

```
True
False
```

`200` はキャッシュ範囲内 → `True`。`300` はキャッシュ範囲外 → `False`。

</details>

---

## Q5

次のコードにはバグがあります。何が問題で、どう直しますか？

```python
def is_adult(age):
    if age is 18:
        return "ちょうど18歳"
    return "18歳ではない"

print(is_adult(18))
```

<details>
<summary>解答を見る</summary>

**問題：** `is` で整数の値を比較している。

**修正：**
```python
def is_adult(age):
    if age == 18:
        return "ちょうど18歳"
    return "18歳ではない"
```

</details>

---

## Q6（総合）

空欄を埋めてください。

- Pythonの整数キャッシュ範囲は `___` 〜 `___`
- `a is b` は `id(a) ___ id(b)` と等価
- 整数の値を比較するときは `___` 演算子を使うべき

<details>
<summary>解答を見る</summary>

- `-5` 〜 `256`
- `id(a) == id(b)` と等価
- `==` 演算子を使うべき

</details>
