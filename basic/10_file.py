# 檔案物件 = open(檔案路徑,mode=開啟模式)
# 開啟模式:
#          1. 讀取模式  r
#          2. 寫入模式  w
#          3. 讀寫模式  r+
# autoClosable 一樣的東西
# with open(檔案路徑,mode=開啟模式) as 檔案物件:
#   讀取或寫入......
# ------------------------
# basic
# file = open("testData.txt", mode="w", encoding="utf-8")  # open
# file.write("hi hi\nbello\n妳好")  # operation
# file.close()  # close


# best
with open("testData.txt", mode="w", encoding="utf-8") as file:
    file.write("1\n2\n98")# 寫入檔案(儲存) 換行用\n
# ------------------------
# 讀取全部文字 file.read()
# basic
# file = open("testData.txt", mode="r", encoding="utf-8")  # open
# v = file.read()
# print(v)
# ------------------------
# 一次讀取一行 for var in file:
#              x 依序讀取到v
# basic
# sum0 = 0
# file = open("testData.txt", mode="r", encoding="utf-8")
# for line in file:
#     sum0+=int(line)
# print(sum0)

# best
sum0 = 0
with open("testData.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        sum0 += int(line)
print(sum0)

# ------------------------
import json

# 讀 Json
# v = json.load(file)
with open("ttt.json", mode="r", encoding="utf-8") as file:
    data = json.load(file) # dictionary type
print(data["name"])
# 寫入 Json
# json.dump(要寫入的資料,file)
data["name"]="WWW"
with open("ttt.json", mode="w", encoding="utf-8") as file:
    json.dump(data, file)

