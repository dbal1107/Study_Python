import random
from day07_hangman_art import stages
from day07_hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

for game in range(7):
  guess = input("Guess a letter: ").lower()
  for letter in chosen_word:
    for i in range(len(chosen_word)):
      if guess == chosen_word[i]:
        display[i] = guess
    cut = 0
  if guess not in display :
    cut += 1
    print(stages[cut])
    # if 
  print(display)
  print(stages[cut])

  if ''.join(display) == chosen_word:
    print('You win!!!\n')
    break

print('You lose..\n')
