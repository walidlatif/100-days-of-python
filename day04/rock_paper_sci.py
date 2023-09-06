import random

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

choose = int(input("Please choose, 0 for rock, 1 for paper, 2 for scissors:"
                   "\n"))
_game = [rock, paper, scissors]
if choose in range(3):
    computer = random.choice(_game)
    if choose == 0:
        print(rock)
    elif choose == 1:
        print(paper)
    elif choose == 2:
        print(scissors)
    print("Computer chose:")
    print(computer)

    # "\" : Using pycodestyle
    # Documentation Link : https://pycodestyle.pycqa.org/en/latest/

    if (computer == rock and choose == 0) or \
       (computer == paper and choose == 1) or \
       (computer == scissors and choose == 2):
        print("It's a draw")
    elif (computer == paper and choose == 2) or \
         (computer == scissors and choose == 0) or \
         (computer == rock and choose == 1):
        print("You win")
    elif (computer == scissors and choose == 1) or \
         (computer == rock and choose == 2) or \
         (computer == paper and choose == 0):
        print("You lose")
else:
    print("Please choose, 0 for rock, 1 for paper, 2 for scissors ")
