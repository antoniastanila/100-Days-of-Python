import random
import time
from tkinter import *
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"

current_word = {}
flip_timer = None


def remove_word():
    print(current_word)
    french_words_dict.remove(current_word)
    french_words = pd.DataFrame(french_words_dict)
    french_words.to_csv("./data/words_to_learn.csv", index=False)
    print(french_words)
    next_card()


def flip_card():
    canvas.itemconfig(current_card, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")


def next_card():
    global current_word, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    current_word = random.choice(french_words_dict)
    canvas.itemconfig(current_card, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


try:
    french_words_df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    french_words_df = pd.read_csv("./data/french_words.csv")
french_words_dict = french_words_df.to_dict(orient="records")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

current_card = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="", font=("Ariel", 60, "bold"))

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(
    image=check_image, highlightthickness=0, command=remove_word)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
