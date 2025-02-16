# declare function

def function_one(s):
    print("hi")
    ss = set(s)
    if "i" in ss:
        return "fail"
    print(s)

print(function_one("hi")) # 順序會影響ㄛ 所以要先定義涵式


