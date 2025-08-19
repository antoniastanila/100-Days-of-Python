from menu import MENU, resources


def calculate_introduced_sum(quarters, dimes, nickels, pennys):
    return quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennys * 0.01


def calculate_change(introduced_sum, actual_cost):
    return introduced_sum - actual_cost


def calculate_ingredients_left(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    if "milk" in MENU[drink]["ingredients"]:
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]


def check_if_enough_resources(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
        return False
    if "milk" in MENU[drink]["ingredients"] and (resources["milk"] < MENU[drink]["ingredients"]["milk"]):
        print("Sorry, there is not enough milk.")
        return False
    if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    return True


def insert_coins():
    print("Please insert coins:")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennys = int(input("How many pennys?: "))
    return calculate_introduced_sum(
        quarters, dimes, nickels, pennys)


def validate_sum(introduced_sum, drink):
    if introduced_sum == MENU[drink]["cost"]:
        return True

    elif introduced_sum > MENU[drink]["cost"]:
        print(
            f"Here is ${round(calculate_change(introduced_sum, MENU[drink]["cost"]), 2)} in change.")
        return True

    elif introduced_sum < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
