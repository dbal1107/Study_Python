class user:

    def __init__(self, name, weight, goal):
        self.name = name
        self.weight = weight
        self.goal = goal

    def wei(self, kg):
        self.weight = self.weight + kg
        if kg>0:
            print(f"{self.name}의 체중이 {kg}kg가 증가했습니다.")
            print(f"{self.name}의 현재 체중은 {self.weight} 입니다")
            print(f"목표체중 {self.goal} 까지 {self.weight - self.goal}kg 남았습니다.")
            print(input())
        elif kg<0:
            print(f"{self.name}의 체중이 {kg}kg가 감소했습니다.")
            print(f"{self.name}의 현재 체중은 {self.weight} 입니다")
            print(f"목표체중 {self.goal} 까지 {self.weight - self.goal}kg 남았습니다.")
            print(input())
        else:
            print(f"{self.name}은(는) 체중을 유지했습니다.")
            print(f"{self.name}의 현재 체중은 {self.weight} 입니다")
            print(f"목표체중 {self.goal} 까지 {self.weight - self.goal}kg 남았습니다.")
            print(input())




    # def weiDown(self, kg):
    #     self.weight = self.weight - kg
    #     print(f"{self.name}의 체중이 {kg}kg가 감소했습니다.")


    def result(self, weight, goal):  # result값 추가 (user창)
        if self.weight <= self.goal:
            print(f"수영복이 드디어 들어가!\n 축하합니다\(^__^)/ {self.name}은 다이어트에 '성공'했습니다.")
        else:
            print(f"'아쉽게도 {self.name}은 다이어트에 성공하지 못했습니다.\n{self.name}은 휴대폰을 들어 [당근마켓] 어플로 들어가 글을 작성한다.\n'워터파크 티켓 팝니다.")