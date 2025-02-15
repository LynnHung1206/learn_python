# 有序列表操作
##List
grades = [60, 79, 95, 20, 776]
print(grades)
print(grades[1])  # 79
grades[1] = 87  # 直接取代
print(grades[1])

print(grades[2:4])  # 包含前面index不包含後面
grades[2:4] = []  # 清空
print(grades)
grades += [1, 2]  # 增加列表
print(grades)

print(len(grades))  # 列表長度

# 巢狀
data = [[1, 2, 2, 2, 5], [3, 4, 4, 4, 5], [5, 6, 4, 6]]
print(data[0])
print(data[0][2:4])
data[0][2:4] = [9, 9, 9, 9, 9]
print(data)
