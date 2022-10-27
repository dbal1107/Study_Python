#구름) 고장난 컴퓨터 반복문
# https://level.goorm.io/exam/49095/%EA%B3%A0%EC%9E%A5%EB%82%9C-%EC%BB%B4%ED%93%A8%ED%84%B0/quiz/1
# 실행후 6 5 입력
# example 1
# #수치화 ctrl / 주석 not(!연산자)
# myData=input("input your data:") #input =str
# if type(myData) != int:
#     print("입력된 데이터 타입이 다릅니다.")
# print(type(myData), myData)

"-------------------------------------------------"

# number, delayTime = map(int,input().split())
# print(number, delayTime)

#반복문
# for(int i=0; i<10; i+=2){
#
# # } C++
# fruits =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # for i in range(0,7):
#     print(fruits[i])

# number, delayTime = map(int,input().split())
# print(number, delayTime)
#
# for i in range(0,number):
#     print(i)

# ex1
# 6 5
# 1 3 8 14 19 20 입력
number, delayTime = map(it,input().split())
times=list(input().split())
print(number,delayTime,times)

cnt = 0   #count

for i in range(number-1):
    if (int(times[i+1]) - int(times[i])) > delayTime:
        cnt = 1
    else:
        cnt = cnt + 1

print(cnt)

print("-------------------------------------------------")
# 2교시 and(&),or(|) t,f / if, elif, else 조건문

# print(not((5 > 2 or 3>3) and not (10<4)))
#
# age =18
# if age <= 8:
#     print("어린이")
# elif age >8 and age <= 13:
#     print("초등학생")
# elif age >13 and age <= 16:
#     print("중학생")
# elif age > 16 and age <= 19:
#     print("고등학생")
# else:
#     print("으른")
#
# print("-------------------------------------------------")
#
# age="Age"
# print(age)
# if not (age != "Age"):
#     print("네에 술 마실수 있어요")
#
# print("-------------------------------------------------")
#
# #3교시 반복문 loop
#
# for i in range(6):
#     print(i, end=" ") #end 옆으로 "구분법 가능 공백,."
#
# for i in range(1, 6):
#     print(i, end=" ") #end 옆으로 "구분법 가능 공백,."
#
# for i in range(6):
#     print(i+1, end=" ") #end 옆으로 "구분법 가능 공백,."
# print()
#
# for i in range(6):
#     print("*"*2) #end 옆으로 "구분법 가능 공백,."
#
# for i in range(6):
#     print(f"a{i}")
# print()
#
# for i in range(1,11):
#     print("*"*i)
# print()
#
# for i in range(10):
#     for j in range(10):
#         print("*", end="")
#     print()
# print("-------------------------------------------------")
# for i in range(10):
#     for j in range(10):
#         print(f"({j}{i})", end=" ")
#     print()
# print("-------------------------------------------------")
# for i in range(10):
#     for j in range(10):
#         print(f"({i}{j})", end=" ")
#     print()
#
# print("-------------------------------------------------")
# cnt=0
# for i in range(5):
#     for j in range(5):
#         cnt +=1
#         print(f"({cnt})", end=" ")
#     print()
#
# print("-------------------------------------------------")
# cnt=0
# for i in range(5):
#     cnt +=1
#     for j in range(5):
#         print(f"({cnt})", end=" ")
#     print()
#
# print("-------------------------------------------------") #뽑아쓰기
# word ="banana"
# for x in word:
#     print(x)
#


