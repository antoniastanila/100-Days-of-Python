from calculator_art import logo


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


print(logo)

should_continue = True

f_nr = int(input("What's the first number?: "))
while should_continue:
    for op in operations:
        print(op)
    picked_operation = input("Pick an operation: ")
    s_nr = int(input("What's the second number?: "))
    result = operations[picked_operation](f_nr, s_nr)
    print(
        f"{f_nr} {picked_operation} {s_nr} = {result}")
    user_says = input(
        "Type 'y' to continue calculating with {result}, or 'n' to start a new calculation.")
    if user_says == "y":
        f_nr = result
    else:
        f_nr = int(input("What's the first number?: "))
