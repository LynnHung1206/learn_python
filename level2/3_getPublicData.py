import urllib.request as req
import json

# step 1
# ck data format Json/csv/other
# data.taipei 有資料可供參閱
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with req.urlopen(src) as resp:
    # data = resp.read().decode("utf-8")
    # loads input is str / load input is obj
    data = json.load(resp)
# print(data)
dataList = data['result']['results']
print(dataList)
with open("company.txt", "w", encoding="utf-8") as file:
    for company in dataList:
        file.write(company['公司名稱'] + "\n")
