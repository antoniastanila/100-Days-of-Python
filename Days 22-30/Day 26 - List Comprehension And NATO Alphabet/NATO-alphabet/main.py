import pandas as pd

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("./NATO-alphabet/nato_phonetic_alphabet.csv")
print(data)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input = input("What's your name? ").upper()
code_list = [phonetic_dict[letter] for letter in input]

print(code_list)
