# while
print("while 的用法")
a = 2
while a < 10:
    print(a)
    a += 1
else:
    print("before end") # before loop end will run this else area

print("---- end... ----")

print("for 的用法")
for x in [1, 2, 3]:
    print(x)

for x in "Hello":
    print(x)
print("---- end... ----")

# range 用法 可參考4
print("range的用法：")

for x in [0, 1, 2]: print(x)
print("equals to")
for x in range(3): print(x)  # 一樣的東西

for x in range(3, 6): print(x)
print("equals to")
for x in [3, 4, 5]: print(x)

# ---
print("-----")
for x in range(6):
    if x == 3:
        print("hello")
        continue
    print(x)
else:
    print("it will say goodbye")# before loop end will run this else area

for x in range(6):
    if x == 3:
        break # use break to broke loop will not run else area
else:
    print("nothing happened")

