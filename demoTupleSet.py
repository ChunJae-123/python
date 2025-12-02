# demoTupleSet.py

# set 형식 연습

a = {1,2,3,4}
b = {3,4,4,5}

print(a)
print(b)
print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# 함수를 정의

def calc(a, b):
    return a+b, a*b

# 호출

result = calc(3,4)
print(result)

print("id;%s, name:%s" % ("sex", "lover"))

args1 = int(input("첫번재 값을 입력해라"))
args2 = int(input("두번재 값을 입력해라"))
print(calc(args1, args2))