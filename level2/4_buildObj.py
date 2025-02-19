import math


class Point:
    def __init__(self, x, y):  # 初始化 self 固定
        self.x = x
        self.y = y

    def distance(self, targetX, targetY):
        return math.sqrt((self.x - targetX) ** 2 + (self.y - targetY) ** 2)


# ------------------
p1 = Point(1, 2)
print(p1.x)
print(p1.y)

p2 = Point(4, 6)


# print(p2) # 記憶體位置
# ------------------
class FullName:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = self.firstName + " " + self.lastName

    def sayhi(self):  # 透過self操作物件
        print("hi hi", self.fullName)


# ------------------

n = FullName("Hung", "Lynn")
n.sayhi()


# print(n.fullName)
# ------------------
import enums.FileMode as mode

class File:
    def __init__(self, fileName, mode):
        self.filePath = fileName
        self.file = None  # null
        self.mode = mode

    def read(self):
        with open(self.filePath, mode=self.mode, encoding="utf-8") as file:
            self.file = file.read()
            return self.file

f1 = File("test.txt", mode.FileMode.r)
print("file=",f1.read())
