# if
from unittest import case

Str = "hihihihihi"
ss = set(Str)
if "hi" in ss:
    print("hi hi")  # 我最討厭的tab很重要 為啥不用大括號＃＃
elif "h" in ss:
    print("hi h")
else:
    print("popopo")

# an example
x = input("please input a number: ")
x = int(x)
if x > 100:
    print("over 100 lol")
elif 50 < x < 100:  # 吐槽：果然很數學 我的邏輯大概是從 java的 && -> x < 100 and x > 50 -> now
    print("over 50 lol")
else:
    print("no lol")

# switch in python 3.9 以下不支援
t = int(input("please input a number2: "))
match t:
    case 1:
        print("1st case")
    case 2:
        print("2nd case")
    case 33:
        print("3rd case")
