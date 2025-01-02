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
hands = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 0 and choice <= 2:
    print(hands[choice])
    print("Computer chose:\n")
    random_number = random.randint(0,2)
    print(hands[random_number])
    if choice == 0 and random_number == 2:
        print("You Win!")
    elif choice == 2 and random_number == 1:
        print("You Win!")
    elif choice == 1 and random_number == 0:
        print("You Win!")
    elif choice == random_number:
        print("It's a Draw!")
    else:
        print("You Lose!")
else:
    print("You typed an invalid number, you lose!")