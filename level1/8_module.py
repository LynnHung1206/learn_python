import sys
import geometry.geometry as geom

print(sys.path)  # s.path 印出模組的搜尋路徑 載入模組時按照順序查找
# sys.path.append("geometry") # 增加模組搜尋路徑
# print(sys.path)
# print(sys.platform)  # s.platform
# print(sys.maxsize)  # s.maxsize

print(geom.distance(1, 1, 5, 5))
print(geom.slope(1, 2, 5, 6))
