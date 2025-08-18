from menu import MENU, resources
from useful_functions import check_if_enough_resources, insert_coins, validate_sum, calculate_ingredients_left

machine_state = "on"
money_in_machine = 0

while machine_state == "on":
    introduced_sum = 0
    user_input = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input in MENU:
        if not check_if_enough_resources(user_input):
            continue

        introduced_sum = insert_coins()

        if not validate_sum(introduced_sum, user_input):
            continue

        money_in_machine += MENU[user_input]["cost"]
        print(f"Here is your {user_input} ☕ Enjoy!")

        calculate_ingredients_left(user_input)

    elif user_input == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${money_in_machine}")

    elif user_input == "off":
        print("Coffee machine turned off. Have a great day!")
        machine_state = "off"

    else:
        print("Invalid input. Please enter a valid one!")
