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

game_images = [rock, paper, scissors]
wants_to_play = True
while wants_to_play:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if user_choice >= 3 or user_choice < 0:
      print("You typed an invalid number, you lose!")
      break
    else:
      print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
      print("You win!")
    elif computer_choice == 0 and user_choice == 2:
      print("You lose")
    elif computer_choice > user_choice:
      print("You lose")
    elif user_choice > computer_choice:
      print("You win!")
    elif computer_choice == user_choice:
      print("It's a draw")
    should_continute  = input('Do you want to play again? (y/n): ')
    if should_continute != 'y':
        wants_to_play= False
