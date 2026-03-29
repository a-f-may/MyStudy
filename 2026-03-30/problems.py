# 2026-03-30 中級問題 - 実行して確認してみよう

# 問題1: 関数の戻り値
def get_number(n):
    return n

print("問題1")
a = get_number(200)
b = get_number(200)
print(f"get_number(200) is get_number(200): {a is b}")   # ?

x = get_number(300)
y = get_number(300)
print(f"get_number(300) is get_number(300): {x is y}")   # ?
print()

# 問題2: 演算結果
print("問題2")
a = 128 + 128   # = 256
b = 256
print(f"128+128 is 256: {a is b}")   # ?

x = 128 + 129   # = 257
y = 257
print(f"128+129 is 257: {x is y}")   # ?
print()

# 問題3: リスト内の整数
print("問題3")
list1 = [1, 2, 3, 256, 257]
list2 = [1, 2, 3, 256, 257]
print(f"list[0](1) is: {list1[0] is list2[0]}")     # ?
print(f"list[3](256) is: {list1[3] is list2[3]}")   # ?
print(f"list[4](257) is: {list1[4] is list2[4]}")   # ?
print()

# 問題5: バグのあるコード（修正してみよう）
print("問題5")
def process_buggy(value):
    result = value * 2
    if result is 300:   # ← バグ！
        return "300です"
    else:
        return f"{result}です"

def process_fixed(value):
    result = value * 2
    if result == 300:   # ← 修正
        return "300です"
    else:
        return f"{result}です"

print(f"バグあり: {process_buggy(150)}")   # 意図通り動かない
print(f"修正済み: {process_fixed(150)}")   # 正しく動く
