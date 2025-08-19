from random import randint

user_choice = input("Make your choice! \n").lower()
choices = ["rock", "paper", "scissors"]

random_index = randint(0, 2)
computer_choice = choices[random_index]
print("Computer's choice: ")
print(computer_choice)
if (user_choice == "rock" and computer_choice == "paper"):
    print("You lose")
elif (user_choice == "rock" and computer_choice == "scissors"):
    print("You won")
elif (user_choice == "paper" and computer_choice == "scissors"):
    print("You lose")
elif (computer_choice == "rock" and user_choice == "paper"):
    print("You won")
elif (computer_choice == "rock" and user_choice == "scissors"):
    print("You lose")
elif (computer_choice == "paper" and user_choice == "scissors"):
    print("You lose")
elif user_choice == computer_choice:
    print("Draw")
else:
    print("Invalid choice")
