############### METHOD I #######################

# print("Treasure!")
# game_over = False
# question = input("left or right? ")
# if question.lower() == "right":
#     game_over = True
#     print("Game over")
# elif question.lower() == "left":
#     question = question = input("swim or wait? ")

# if question.lower() == "swim" and game_over == False:
#     game_over = True
#     print("Game over")
# elif question.lower() == "wait":
#     question = question = input("Which door? Red Yellow Blue? ")

# if (question.lower() == "red" or question.lower() == "blue") and game_over == False:
#     game_over = True
#     print("Game over")
# elif game_over != True:
#     print("You won!")


############### METHOD II #######################

print("Welcome to Treasure Island!")

choise1 = input("left or right?")

if choise1.lower() == "left":
    choise2 = input("swim or wait?")
    if choise2.lower() == "wait":
        choise3 = input("Choose door: red, blue, yellow -> ")
        if choise3.lower() == "yellow":
            print("You won!")
        elif choise3.lower() == "blue" or choise3.lower() == "red":
            print("Game over.")
        else:
            print("Invalid input...")
    elif choise2.lower() == "swim":
        print("Game over.")
    else:
        print("Invalid input...")
elif choise1.lower() == "right":
    print("Game over.")
else:
    print("Invalid input...")
