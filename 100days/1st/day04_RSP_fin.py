rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

# 잘못 입력했을 때 예외처리
try :
    user = int(input('''
- What did you choose? -
| 0 for Rock          |
| 1 for Paper         |
| 2 for Scissors      |
>>> '''))

    # 이미지 단순하게 불러오기
    image = [rock, paper, scissors]
    print(image[user])

    computer = random.randint(0, 2)
    print('Computer chose: \n')
    print(image[computer])

    if user == computer :
        print('Draw!!!\n')
    elif user == 0:
        if computer == 1 :
            print('You lose..\n')
        else :
            print('You win!!!\n')
    elif user == 1 :
        if computer == 2 :
            print('You lose..\n')
        else :
            print('You win!!!\n')
    else :
        if computer == 0 :
            print('You lose..\n')
        else :
            print('You win!!!\n')

except Exception as ex : 
    print('''
| You lose....!         |
| Please insert 0, 1, 2 |
''')
