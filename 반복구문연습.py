# 반복구문연습.py

value = 5
while value > 0:
    print(value)
    value -= 1


print("=== for in 루프 ===")

lst = [1, 2, 3]

for item in lst:
    print(item**100)


print("=== range function ===")

print(list(range(10)))
print(list(range(1,11)))
print(list(range(2000,2026)))
print(list(range(1,32)))


print(" --- list inner --- ")

lst = list(range(1,11))
print(lst)
print([i*2 for i in lst if i>5])
tp = ("apple", "kiwi")
print([len(i) for i in tp])