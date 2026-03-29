# 整数キャッシュ範囲 確認問題（2回目）
# 実行して答えを確認しよう

print("=== Q1 ===")
a = 100
b = 100
print(a is b)   # ?
print(a == b)   # ?
print()

print("=== Q2 ===")
a = 257
b = 257
print(a is b)   # ?
print(a == b)   # ?
print()

print("=== Q3 ===")
print(-5 is -5)    # ?
print(-6 is -6)    # ?
print(256 is 256)  # ?
print(257 is 257)  # ?
print()

print("=== Q4 ===")
def double(n):
    return n * 2

a = double(100)  # 200
b = double(100)
print(a is b)    # ?

x = double(150)  # 300
y = double(150)
print(x is y)    # ?
print()

print("=== Q5 バグ確認 ===")
def is_adult_buggy(age):
    if age is 18:    # バグ
        return "ちょうど18歳"
    return "18歳ではない"

def is_adult_fixed(age):
    if age == 18:    # 修正
        return "ちょうど18歳"
    return "18歳ではない"

for a in [18, 1800]:
    print(f"  {a}歳 buggy: {is_adult_buggy(a)}")
    print(f"  {a}歳 fixed: {is_adult_fixed(a)}")
