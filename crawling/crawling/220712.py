from random import *

num = []
cnt=1000

while cnt>0:
    x = randint(1, 1000000)
    if x in num:
        continue # 중복된게 있으면 else 금지
    else:
        num.append(x)
        cnt -=1
print(num)
num.sort()
print(num)

sPivot=0
ePivot=i

def biSe(cnt,sPivot,ePivot):
    mid = (sPivot + ePivot) //2
    if cnt > num[mid]:
        return biSe(cnt)
