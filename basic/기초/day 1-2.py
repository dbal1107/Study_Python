"""
List
set
array
tuple
dictionary
"""

x="시끄러"
a = [1,2,3,4]
print(len(a)) #길이 요소가 4개
print(len(x))
print(a[2]) #0부터 세기시작

#a0 +a3
print(a[0]+a[3])

print(type(a))

b=[1,2,3,["apple","banana"]]
print(b[3][0])
print(b[3][0][0])

#tuple()
sample=10
sample=1,2,3,4
print(sample)

#set[]
sample=list((1,2,3,4))
print(sample)
print(sample[-1]) #마이너스는 되도록 x

#excess
fruits =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[3:8])
print(fruits[2:])
print(fruits[:3])

txt = "abcdefgh"
print(txt[2:])
# :많이 쓰인다.

#change
fruits[0]="watermelon"
print(fruits)

fruits[0:2] = ["peach", "strawberry"]
print(fruits)

fruits.insert(1, "베리베리")
print(fruits)

#append 외 자주씀
fruits.append("과일이름")
print(fruits)

fruits.extend("당떨어짐")
print(fruits)

fruits.pop()
fruits.pop()
fruits.pop()
fruits.pop()
print(fruits)

fruits.pop(3)
print(fruits)

fruits.remove("peach")
print(fruits)

################################################

#tuple 변경할수없


x=(1,2,3) #변경 불가 tuple()
y=[1,3,4] #변경 가능

print(x[0]) #()연산자
print(y[0]) #[]인덱싱호출

y[0] =10
# x[0] =10
print(x)
print(y)

x=7,8,9 #무시하고 통째로 바꿈
print(x)

x=list((1,2,3))
y=list((4,5,6))
print(y)
print(x)

y.reverse()
print(y)

x=list((10,7,1,2,9,5))
x.sort() #정렬 파이썬 금지!
print(x)

#sets 교집합 가능 {}
x={"a","b","c"}
y={"a","e","a"}
z=x.union(y) #같은 소속 합치기
print(z)

list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2 #다른연산자 못씀
print(list3)

#difference 차집합
z=x.difference(y)
print(z) #x 중 y에 있는거 제외

#discard
x.remove("a")
print(x)
y.remove("e")
print(y)










