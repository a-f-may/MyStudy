# 2026-03-29 基礎問題 - 実行して確認してみよう

# 問題1: キャッシュ範囲内
a = 100
b = 100
print("問題1")
print(f"a is b: {a is b}")    # ? 
print(f"a == b: {a == b}")   # ?
print(f"id(a): {id(a)}, id(b): {id(b)}")
print()

# 問題2: キャッシュ範囲外
a = 257
b = 257
print("問題2")
print(f"a is b: {a is b}")    # ?
print(f"a == b: {a == b}")   # ?
print(f"id(a): {id(a)}, id(b): {id(b)}")
print()

# 問題3: 下限の境界値
print("問題3")
a, b = -5, -5
x, y = -6, -6
print(f"-5 is -5: {a is b}")   # ?
print(f"-6 is -6: {x is y}")   # ?
print()

# 問題4: 上限の境界値
print("問題4")
a, b = 256, 256
c, d = 257, 257
print(f"256 is 256: {a is b}")   # ?
print(f"257 is 257: {c is d}")   # ?
print(f"256 is not 256: {a is not b}")  # ?
print(f"257 is not 257: {c is not d}")  # ?
