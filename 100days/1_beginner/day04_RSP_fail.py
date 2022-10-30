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

me = int(input('''
What do you choose? 
0 for Rock
1 for Paper
2 for Scissors
>>> '''))

if me == 0 :
    print(f'{rock} \n')
elif me == 1 :
    print(f'{paper} \n')
else :
    print(f'{scissors} \n')

computer = random.randint(0, 2)
print('Computer chose: ')

if computer == 0 :
    print(f'{rock} \n')
elif computer == 1 :
    print(f'{paper} \n')
else :
    print(f'{scissors} \n')

if me == computer :
    print('Draw!!!\n')
elif me == 0:
    if computer == 1 :
        print('You lose..\n')
    else :
        print('You win!!!\n')
elif me == 1 :
    if computer == 2 :
        print('You lose..\n')
    else :
        print('You win!!!\n')
else :
    if computer == 0 :
        print('You lose..\n')
    else :
        print('You win!!!\n')
