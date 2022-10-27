
# 1교시 자리배치

listA=[]
for i in range(1,5):
    listA.append(i)

print(listA)

# 구름 막대기 (set 중복제거) (tuple 보관용)
# 처음 입력값 num이 나타내야하는 갯수

# num=int(input())
# listNum=[]
#
# for i in range(num):
#     listNum.append(int(input()))
#
# # print(listNum)
#
# cnt=1
# max=listNum[num-1]
# for i in range(num-1,-1,-1):
#     # print(listNum[i], end="")
#     if max < listNum[i]:
#         cnt+=1
#         max=listNum[i]
#
# print(cnt)

# 2교시

class Student:
    name=""
    age=0
    exp=0
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def increExt(self, point):
        self.exp= self.exp + point
        print(f"{self.name}이 경험치 {point}만큼 성장하였습니다.")

    def decreExt(self, point):
        self.exp= self.exp - point


s1 = Student("학생", 20)

print(s1.name, s1.age, s1.exp)
s1.increExt(30)
print(s1.exp)