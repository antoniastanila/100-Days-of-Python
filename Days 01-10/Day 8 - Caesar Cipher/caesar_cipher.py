from caesar_cipher_art import logo
from caesar_cipher_alphabet import alphabet


def caesar(encode_or_decode, original_text, shift_amount):
    altered_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            altered_text += alphabet[(alphabet.index(letter) +
                                     shift_amount) % len(alphabet)]
        else:
            altered_text += letter

    print(f"Here is the {encode_or_decode}d result: {altered_text}")


print(logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(direction, text, shift)

    restart = input("Do you want to continue? yes/no \n")

    if restart.lower() == "no":
        should_continue = False
        print("Goodbye")
