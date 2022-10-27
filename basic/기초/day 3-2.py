# 4교시 함수 계산기 출력
# def add(a,b):
#     return a+b

# def mi(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a//b

# number01, opStr, number02 = map(str, input("계산식을 입력하세요 예) 3 + 4 : ").split(" "))

# # print(number01, opStr, number02)
# # print(type(number01), type(number02))
# number01 = int(number01)
# number02 = int(number02)

# # print(type(number01), type(number02))

# ans = ""

# if opStr == "+":
#     ans = add(number01, number02)
# elif opStr == "-":
#     ans = mi(number01, number02)
# elif opStr == "/":
#     ans = div(number01, number02)
# elif opStr == "*":
#     ans = mul(number01, number02)
# else:
#     print(f"'{opStr}' is a not operator.")


# if ans:
#     print(f"{number01} {opStr} {number02} = {ans} 입니다.")

# 5교시 피보나치수열 앞뒤더한값 1,1,2,3,5,8,13,,,
a=1
b=1
c=0 #계산이니까 ""말고 0으로
for i in range(5): #반복
    a=b
    b=c
    c=a+b
    print(c)
print()
#함수로 만들어서 쓰자
def fivonacci(n):
    a,b=1,1
    c=0
    for i in range(n):
        a=b
        b=c
        c=a+b

    return c
# print(fivonacci(10)) #다른 페이지에서 from day3-2 import fivonacci 하고 print하면 값나옴

import camelcase
c=camelcase.CamelCase()
txt= "hello world"
print(c.hump(txt))

#6교시 class 개체 함수넣을수있 (dictionary 랑 비슷하지만 다름 함수넣을수없)
class myClass:
    name="james"
    age=20
    gender="Female"

print(myClass.name)

# object

# class myClass:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1=myClass("john",30)
# p2=myClass("Park",20)

# 1~45 정수랜덤

from random import *

lottoNumber=[]
cnt=6
while cnt>0:
    x=randint(1,45)
    if x in lottoNumber:
        print(f"{x}값이 {lottoNumber}에 있습니다. 다시 돌릴게요")
        continue
    else:
        lottoNumber.append(x)
        cnt -=1

print(lottoNumber)