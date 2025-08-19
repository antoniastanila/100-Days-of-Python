# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

print("Password - easy version: ", end=" ")

letters_list = []
for index in range(nr_letters):
    random_letter_index = random.randint(0, len(letters) - 1)
    letters_list.append(letters[random_letter_index])

for index in range(nr_letters):
    print(letters_list[index], end='')

symbols_list = []
for index in range(nr_symbols):
    random_symbol_index = random.randint(0, len(symbols) - 1)
    symbols_list.append(symbols[random_symbol_index])

for index in range(nr_symbols):
    print(symbols_list[index], end='')

numbers_list = []
for index in range(nr_numbers):
    random_number_index = random.randint(0, len(numbers) - 1)
    numbers_list.append(numbers[random_number_index])

for index in range(nr_numbers):
    print(numbers_list[index], end='')

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print("\n")

letters_symbols_numbers = [letters_list, symbols_list, numbers_list]

password = ""

while len(letters_symbols_numbers) != 0:
    if len(letters_list) == 0 and letters_list in letters_symbols_numbers:
        letters_symbols_numbers.remove(letters_list)
    if len(symbols_list) == 0 and symbols_list in letters_symbols_numbers:
        letters_symbols_numbers.remove(symbols_list)
    if len(numbers_list) == 0 and numbers_list in letters_symbols_numbers:
        letters_symbols_numbers.remove(numbers_list)

    if len(letters_symbols_numbers) > 0:
        list_to_choose_from = random.randint(
            0, len(letters_symbols_numbers) - 1)

        position_in_list = random.randint(
            0, len(letters_symbols_numbers[list_to_choose_from]) - 1)

        password += letters_symbols_numbers[list_to_choose_from][position_in_list]

        letters_symbols_numbers[list_to_choose_from].remove(
            letters_symbols_numbers[list_to_choose_from][position_in_list])

print("Password - hard version: ", end=" ")
print(password + "\n")


# Hard Level - Angela's way easier version using random.shuffle(x)

print("Angela's version of solving the hard level: ")

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
