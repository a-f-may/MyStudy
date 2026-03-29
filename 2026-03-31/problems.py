# 2026-03-31 応用問題 - 実行して確認してみよう

# 問題1: バグのあるコードを修正してみよう
def check_user_age_buggy(age):
    """バグあり版"""
    if age is 18:       # ← バグ！
        return "ちょうど18歳"
    elif age > 18:
        return "18歳以上"
    else:
        return "18歳未満"

def check_user_age_fixed(age):
    """修正済み版"""
    if age == 18:       # ← 修正
        return "ちょうど18歳"
    elif age > 18:
        return "18歳以上"
    else:
        return "18歳未満"

print("問題1 - 年齢チェック")
for a in [17, 18, 19, 300]:
    print(f"  {a}歳(buggy): {check_user_age_buggy(a)}")
    print(f"  {a}歳(fixed): {check_user_age_fixed(a)}")
print()

# 問題2: id()を使って確認
print("問題2 - id() での確認")
test_values = [-6, -5, 0, 100, 256, 257, 1000]
for val in test_values:
    a = val
    b = val
    same_id = id(a) == id(b)
    print(f"  {val:5d}: a is b={a is b}, id同一={same_id}")
print()

# 問題4: 総合確認
print("問題4 - 総合確認")
for i in [0, 100, 256, 257, 500, -5, -6]:
    a = i
    b = i
    print(f"  {i:4d}: is={a is b}, =={a == b}")
