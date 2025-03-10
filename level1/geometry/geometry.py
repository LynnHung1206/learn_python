# 自行定義模組
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)
