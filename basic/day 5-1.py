# 인싸가 되고 싶은 민수
#
# 약수의 갯수를 알 수있게 된다. 약수의 종류를 찾아서
# 약수를 구하는 법, 나누어서 떨어지는 수 어떤 수로 n%
# 인덱싱으로 카운트 하기 (like 투표)
#
a, b = map(int, input().split(" ")) #a, b 처음과 끝
num = [] #리스트화
for i in range(0,b+1): # i: a부터 시작되는 숫자.b+1 0부터라서 +1까지 가야한다
    num.append(0)
for i in range(a, b+1): # a넣고 b넣고 반복하겠다.
    for j in range(1, i+1): # j:
        if i%j==0:
            num[j]=num[j]+1

print(num)

mx = 0 # 큰숫자 찾기
maxNumber=0
for i in range(2,b+1): #첫번째 찾고 뒤로 반복해서 큰 숫자 찾기
    if num[i]>mx:
        mx=num[i]
        maxNumber = i

print(mx)
print(maxNumber)