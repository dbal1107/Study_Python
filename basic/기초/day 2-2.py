# 4교시 for loop 반복 미쳤다 하하하

# 사각형
# num=int(input("Input number: ")) #apstrection 추상화
# for i in range(5):
#     for j in range(num):
#         print("*", end="")
#     print()

# 대각선 줄어들기
# num=int(input("insert number:"))
# for i in range(num):
#     print("*"*(i+1))
#     # for j in range(i+1):
#     #     print("*",end=" ")
# print()

# num=int(input("insert number:"))
# for i in range(num):
#     for j in range(num-i):
#         print("*",end="")
#     print()

# num= int(input("insert number:"))
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*",end ="")
#     print()

# 삼각
# num= int(input("insert number:"))
# for i in range(1,num+1):
#     for j in range(num-i):
#         print(" ", end="")
#     for j in range(i*2-1):
#         print("*",end ="")
#     print()

# 역삼각
# num=int(input("insert number:"))
# for i in range(1,num+1):
#     for j in range(i-1):
#         print(" ", end="")
#     for j in range((num*2-1)-(i+1)*2):
#         print("*", end="")
#     print()

# 마름모 틀
# num = int(input("insert number:"))
#
# for i in range(int(num/2)):
#     print("up-tri")
# if num%2==1:
#     print("middle line")
# for j in range(int(num/2)):
#     print("upper-tri")


#5교시 ######## 함수 키워드 사용금지 ins....외
#   리턴 처리 연산
# 안에서는 밖에 이용변경가능 밖에서는 안에 이용변경불가 모르도록 하는것
# 한가지 함수만 작용하도록 만든다

# data=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# #그냥 다 더할때
# for i in data:
#     sum += i
#
# # 골라서 더할때
# # for x in range(len(data)):
# #     sum=sum+data[x]
# print(sum)

#### 함수화 리스트의 모든 값을 더해서 리턴하는 함수 만들기
data=[1,2,3,4,5,6,7,8,9,10]
sum=0

def addSum(listIn): #이름 마음대로 적기
    a=0
    for x in listIn:
        a= a+x
    return a

print(addSum(data))

# 리턴: 함수 종료 값이 있을때만 동작

print("---------------------------------------------")
#6교시 재귀 미러링 recul 속도 개빠름

def recul(num):
    if num < 1:
        return 0
    return recul(num-1)+num

print(recul(10))


print("---------------------------------------------")


############# while loop 그냥 실행시 강종해야함

# num=10
# while num>0:
#     print(num)
#     num=num-1

# num=10
# while num > 0:
#     print(num)
#     if num == 5:
#         break
#     num=num-1
#
# print(num)

# num=11
# while num > 0:
#
#     num=num-1
#     if num == 5:
#         continue
#     print(num)

# 홀수 찾기
# for i in range(1, 100):
#     if i%2==0: #짝수면
#         continue
#     print(i)

#7교시 약수의 합

# num=int(input("insert:"))
# sum=0
#
# for i in range(1,num+1): #자기자신까지 +1
#     if num%i==0:
#         print(i, end=" ")
#         sum+=i
# print()
# print("-"*30)
# print(f"{num}의 약수의 합은 {sum}입니다.")


# num=int(input("insert:"))
# sum=0
#
# for i in range(1,num+1):
#     if num%i==0 and i%2==0:
#         print(i, end=" ")
#         sum += i
# print()
# print("-"*30)
# print(f"{num}의 약수 중 짝수의 합은 {sum}입니다.")

# 윤년 4년씩
# num=int(input("년도: "))
#
# if num%4==0 and num%100!=0 or num%400==0:
#     print(f"{num}년은 윤년입니다.")
# else:
#     print(f"{num}년은 평년입니다.")