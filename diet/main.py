from user import *
from step import *
from checkData import *
from returnAb import *
#오프닝
print()
print("☆☆☆☆☆☆Dieter☆☆☆☆☆☆")
print(input("대화창을 넘길 때는 엔터키를 눌러주세요."))
print("""[3일뒤, 여름 휴가를 맞이하여 새로 개장하는 워터파크에 가기로 했다.
티켓과 여행갈 모든 준비는 완료! 거기다 오늘은..! 인터넷으로 주문한 수영복이 도착하는 날이다.
칼퇴하고 바로 집에 가서 입어봐야지!]""")
print(input())

print("""--------------    집    ----------------
[이럴수가! 수영복이 작다니!!\n교환을 하기에는 너무 늦는데...\n어쩔 수 없지. 살을 빼야겠다!]""")
print("☆"*25)
print(input())

#게임시작
question = "etc"
while question != 'a' or question !='b':
    question = input(f"게임을 시작하시겠습니까?\n [a: Yes / b: No]\n")
    if question == "a":
        print(input("게임을 시작합니다.\n엔터키를 눌러주세요."))
        break
    elif question == "b":
        print("게임을 종료합니다.")
        break
        exit()
    else:
        print("잘못 선택되었습니다. 다시 입력해주세요.")

#입력창
print("당신의 이름을 입력해주세요 : ")
name = str(input())
print("당신의 현재 몸무게를 입력해주세요 : ")
weight = int(input())
print("당신의 목표 체중을 설정하세요.(단, 목표 감량값은 현재 체중의 (-1) ~ (-10)kg 입니다.) : ")
goal = int(input())
print()
print(f"3일 뒤 워터파크를 가야한다!\n{name}! 다이어트를 시작해 보자!")
print(input())


#스토리시작
#Day1
print("Day1")
user = user(name, weight, goal)
ch = False
while ch==False:
    print(step01.question)
    print(step01.selector)
    data = input()
    ch = checkData(data)

if data == "a":
    print(f"\n역시 바쁠 땐 샌드위치지!\n{name}(은)는 바쁘니까 대충 샌드위치를 먹기로 했다.\n이것도 나름 맛있네.")
    print()
    user.wei(step01.point1)
else:
    print(f"\n역시 한국인은 밥심이지!\n{name}(은)는 건강하게 한 상 차려먹기로 했다.\n 음~ 건강해지는 느낌이야.")
    print()
    user.wei(step01.point2)

#step02
print(step02.question)
print(step02.selector)
data = input()
while ch==False:
    print(step02.question)
    print(step02.selector)
    data = input()
    ch = checkData(data)
if data == "a":
    print(f"\n{name}(은)는 휴대폰을 꺼내 카카오 택시 앱을 열었다.\n기사님 빨리 부탁드려요! 지각이에요!")
    print()
    user.wei(step02.point1)
else:
    print(f"\n역시 거리에 차가 많다.\n{name}(은)는 신발 끈을 꽉 매고 달리기 시작했다.\n헉헉, 힘들어.. 그래도 지각은 면했다!")
    print()
    user.wei(step02.point2)
# print(step02.question)
# print(step02.selector)
# data = input()

#step03
print(step03.question)
print(step03.selector)
data = input()
while ch==False:
    print(step01.question)
    print(step01.selector)
    data = input()
    ch = checkData(data)
if data == "a":
    print(f"{name}(은)는 도서관으로 가기로 했다.\n이 동네 도서관은.. 도대체 왜 산 꼭대기에 지어져 있는 거야...\n공부를 하러 가는 건지, 등산을 하는 건지..헉헉")
    print()
    user.wei(step03.point1)
else:
    print(f"\n{name}(은)는 집 앞 카페로 가기로했다.\n역시 카페야! 잔잔한 음악과 맛있는 음료의 조합.\n공부가 잘될 것 같은 느낌인걸!")
    print()
    user.wei(step03.point2)

#step04
#Day2
print("Day2")
print(step04.question)
print(step04.selector)
data = input()
while ch==False:
    print(step01.question)
    print(step01.selector)
    data = input()
    ch = checkData(data)
if data == "a":
    print(f"{name}(은)는 회사까지 걸어서 가기로 했다.\n날씨가 너무 좋네~")
    print()
    user.wei(step04.point1)
else:
    print(f"{name}(은)는 회사까지 자전거를 타고 가기로 했다.\n바람이 너무 상쾌해~")
    print()
    user.wei(step04.point2)

#step05
print(step05.question)
print(step05.selector)
data = input()
while ch==False:
    print(step01.question)
    print(step01.selector)
    data = input()
    ch = checkData(data)
if data == "a":
    print(f"\n사람이 하루에 한끼는 제대로 먹어야지!\n{name}(은)는 초밥을 먹기로 했다.\n초밥은 생선이라 살 안쪄~~")
    print()
    user.wei(step05.point1)
else:
    print(f"\n수영복을 생각하자!\n{name}(은)는 샐러드를 먹기로 했다.\n너.무.맛.있.다.하.하.하.하.")
    print()
    user.wei(step05.point2)

#step06
print("[★랜덤이벤트★]")
print(step06.question)
print(step06.selector)
print("랜덤으로 선택됩니다. 엔터키를 눌러 진행해주세요.")
print(input())
data = reAb()
if data == "a":
    print(f"{name}(은)는 동기와 카페로 갔다.\n오랜만에 만나서 얘기하니 너무 좋다~")
    print()
    user.wei(step06.point1)
else:
    print(f"{name}(은)는 동기와 저녁식사를 하기로 했다.\n 삼겹살에 소주라니... 다이어트 괜찮을까?")
    print()
    user.wei(step06.point2)

#step07
print(step07.question)
print(step07.selector)
data = input()
while ch==False:
    print(step01.question)
    print(step01.selector)
    data = input()
    ch = checkData(data)
if data == "a":
    print(f"{name}는 헬스장에 가서 운동을 하기로 했다.")
    print()
    user.wei(step07.point1)
else:
    print(f"{name}는 집에서 유튜브로 홈트를 하기로 했다.")
    print()
    user.wei(step07.point2)

#step08
#Day3
print("Day3")
print(step08.question)
print(step08.selector)
data = input()
while ch==False:
    print(step01.question)
    print(step01.selector)
    data = input()
    ch = checkData(data)
if data == "a":
    print(f"\n{name}(은)는 집 근처 산책을 하기로 했다. \n여름이라 그런지 모기가 너무 많아!")
    print()
    user.wei(step08.point1)
else:
    print(f"\n{name}(은)는 헬스장에 가기로 했다. \n이른 아침에도 사람이 많네. 나도 더 부지런해져야겠다.")
    print()
    user.wei(step08.point2)

#step09
print(step09.question)
print(step09.selector)
data = input()
while ch==False:
    print(step01.question)
    print(step01.selector)
    data = input()
    ch = checkData(data)
if data == "a":
    print(f"\n{name}(은)는 자바칩 프라푸치노를 먹기로 했다.\n역시 당분이 최고야. 이제야 좀 살 것 같네")
    print()
    user.wei(step09.point1)
else:
    print(f"\n{name}(은)는 블랙밀크티를 먹기로 했다.\n쫄깃쫄깃한 펄! 아침은 안먹어도 되겠어.")
    print()
    user.wei(step09.point2)

#step10
print(step10.question)
print(step10.selector)
print(input())
user.wei(step10.point1)

#step11
print("[★랜덤이벤트★]")
print(step11.question)
print(step11.selector)
print("랜덤으로 선택됩니다. 엔터키를 눌러 진행해주세요.")
print(input())
data = reAb()
if data == "a":
    print(f"{name}(은)는 웨이트를 시작했다.\n너무 고통스러워!")
    print()
    user.wei(step11.point1)
else:
    print(f"{name}(은)는 유산소를 시작했다.\n나 제대로 숨쉬고 있는거 맞나..?")
    print()
    user.wei(step11.point2)

print(f"이제 체중계에 올라가볼까?!")
print(input())

print(input(f"{name}의 최종 몸무게는 {user.weight}입니다"))

user.result(weight, goal)
print(input())
print("게임을 플레이 해주셔서 감사합니다. 모든 사람들의 다이어트를 응원합니다!")
exit()
