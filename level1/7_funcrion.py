# declare function

def function_one(s):
    print("hi")
    ss = set(s)
    if "i" in ss:
        return "fail"
    print(s)


print(function_one("hi"))  # 順序會影響ㄛ 所以要先定義涵式


# 可以給他預設資料
def function_two(s="hi hi"):
    print(s)


function_two("xxxxxxxx")


# 用參數名稱來對應資料 噁心！ ->Python 允許關鍵字參數（Keyword Arguments）
def function_three(x, y):
    print(x + y)


function_three(y=1, x=2)
function_three(1, 2)


# function_three(2, y=1)  # ✅ 正確
# function_three(y=1, 2)  # ❌ 錯誤，位置參數不能在關鍵字參數之後

# 無限參數 +* it will be a tuple just like java's ...
def function_four(*msgs):
    print(msgs)
    for msg in msgs:
        print(msg)
    print("end")

function_four(1, 2, 3, 66, 77, 55)
