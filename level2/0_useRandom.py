import random

data = [1, 3, 5, 6]
# 隨機取數
print(random.choice(data))  # 取1
print(random.sample(data, 2))  # 取2

# 隨機調換順序 修改本身
random.shuffle(data)
print(data)

# 隨機亂數 0.0 ~ 1.0 之間的隨機亂數
random.random()
# equals to
random.uniform(0.0, 1.0)

# 常態分配亂數
# 取得 平均數 100 標準差 10 的常態分配亂數
# 得到的資料多數在 90~110 之間
print(random.normalvariate(100, 10))
