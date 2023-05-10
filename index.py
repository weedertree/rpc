import random


rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper= '''
     _______
---'    ____)____
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

gameimages= [rock, paper, scissors]


user_choice = int(input("What do you want to choose? Type 0 for rock 1 for paper 2 for scissors.\n "))
print(gameimages[user_choice])


computer_choice =  random.randint(0,2)
print(f"Computer Chose:")
print(gameimages[computer_choice])




if user_choice >=3 or user_choice< 0:
    print("You chose an invalid Number ")


elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You Lose!")
    
elif computer_choice < user_choice:
    print("You Win")
    
elif computer_choice == user_choice:
    print("its a draw \n")
else:
    print("You typed an invalid number")































