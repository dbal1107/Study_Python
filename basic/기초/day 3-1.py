# 1교시 구름) 수열 규칙 2진법 소인수분해 확인 decomposition
# 피보나치수열 자연계법칙
# 2진수-인덱스 / 함수로 만들수있음 좋다.
# list는 0인지 뭔지 순서값 x

# num=int(input("insert"))
# listA=[]
# while num>0: #반복하겠다.
#     listA.append(num%2) #2로 나눈 나머지를 리스트생성
#     num=int(num/2) #num=num//2
# print(listA) #여기까지 2진수 출력 #구름에서는 이 라인 제거 후 출력
#
# for i in range(len(listA)):
#     if listA[i]==1:
#         print([i],end=" ") #값중 1있는거만 출력

# 2교시 Dictionary 분류체계 / key,valuse 데이터 많이씀 / json 파일 많이씀 그냥 텍스트라서 변수로 사용 x 고정값
# user={                   #{}set,user
#     "name":"James",
#     "age":30,
#     "gender":"Female",
#     "job":"student"
# }
#
# user1 = user.copy()
# user2 = dict(user1)
# print("user",user)
# print("user1",user1)
# print("user2",user2)
#
# for key in user:
#     print(user[key])
#
# for i in user.keys():
#     print(i, end=" ")
#
# for i in user.values():
#     print(i, end=" ")
# print()
# print("*"*50)
#
# for 키, 벨류 in user.items():
#     print(f"key:{키}, value:{벨류}")
# print("*"*50)
#
# print(user["name"])
# print(user)
#
# print(user.values())
# print(user.keys())
# print(user.items())
# print(user.get("name"))
# user.popitem()
# print(user)
# user.update({"job":"none"})
# user.update({"hobby":"videogame"})
# user.pop("name")
# del user["job"]
# # user.clear()
# print(user)
# print("*"*50)

# nested {child1 개체 안에 {개체}} 값없이 pass 가능 팀프로젝트에 좋음
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily.keys())
print(myfamily["child1"]["name"])
print(myfamily.get("child1").get("name"))
print("*"*50)
print()

user_name = "james"
user_age = 20
child={
    "name" : user_name,
    "age" : user_age
}
myfamily={
    "child1" : child,
    "child2" : child,
    "child3" : child
}
print(myfamily)
print("*"*50)
print()

# 3교시 math methods

num=10
print(num**10) #10승

import math
import random #import는 . 포함
print(random.random())
print(random.randint(1,7)) #7포함

from math import * #from은 . 미포함
from random import *

listA=[1,3,0,8,7,20,18] # 앞뒤값 비교해서 바꿔두고 결과값 도출
print(random())
print(randint(1,7)) #7포함
print(max(1,2,10))

# abs 절대치 오차율은 절대값 필요
# pow 제곱
listB=[-1,3,0,-8,7,20,18] # 앞뒤값 비교해서 바꿔두고 결과값 도출
print(random())
print(randint(1,7)) #7포함
print(max(1,2,10))
print("*"*50)
for i in listB:
    print(abs(i))
print("*"*50)
for i in listB:
    print(int(abs(pow(i,3)))) #i 3번 곱하기
print("*"*50)

listC=[-1,3,0,-8,7,20,18]
print(randrange(1,10))
print(pi)
print(ceil(pi))
print(floor(pi))

# lambda 간단가능 함수에 많이 쓰임 함수를 편리하고 간단하게 표현

# x = lambda a, b : a * b
# print(x(5, 6))
#
# def mul(a,b):
