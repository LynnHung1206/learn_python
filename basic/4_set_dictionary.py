# set 操作
ss = {6, 3, 8, 0, 1}
print(10 in ss)  # 是否在其中
print(10 not in ss)  # 是否不在其中

s1 = {1, 2, 3, 4, 5}
s2 = {5, 6, 7, 8, 9}
s3 = s1 & s2  # 取交集 {5}
print(s3)

s4 = s1 | s2
print(s4)  # 聯集 取全部（重複只放一個）{1, 2, 3, 4, 5, 6, 7, 8, 9}

s5 = s1 - s2  # 差集 {1, 2, 3, 4}
print(s5)

s6 = s1 ^ s2  # 反交集 不重疊的資料 {1, 2, 3, 4, 6, 7, 8, 9}
print(s6)

str = "popopopopu"
spited = set(str)
print(spited)  # {'o', 'p', 'u'} 字串可以拆成set
print('o' in spited)

# dictionary 跟java map差不多Ｒ
dic = {"1": "apple", "2": "banana", "3": "orange"}
print(dic["1"])

dic["1"] = "Apple"
print(dic)

print("999" in dic)
e = dic.pop("1")
print(e)  # 拿出
print(dic)

del dic["3"]  # 刪除
print(dic)

d = {x: x * 2 for x in range(10)}
print(d)
d1 = {x: x * 2 for x in [1, 2, 3]}
print(d1)
