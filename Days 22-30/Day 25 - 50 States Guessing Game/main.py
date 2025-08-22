from turtle import Screen
import pandas as pd
import turtle
from useful_functions import NUMBER_OF_STATES, manage_answer, missed_states_file, manage_end_of_game

screen = Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


game_in_on = True
correct_guesses = 0


states_file = pd.read_csv("50_states.csv")
states_list = states_file.state.to_list()
guessed_states = []
missed_states = states_file.state.to_list()


while len(guessed_states) < NUMBER_OF_STATES and game_in_on:

    if correct_guesses == 0:
        answer_state = screen.textinput(
            title="Guess the state", prompt="What's a state's name?")
    else:
        answer_state = screen.textinput(
            title=f"{correct_guesses}/50 States Correct", prompt="What's another state's name?")

    try:
        answer_state = answer_state.title()
    except AttributeError:
        game_in_on = False

    correct_guesses = manage_answer(
        correct_guesses, answer_state, states_file, guessed_states, missed_states)

missed_states_file(missed_states)

manage_end_of_game(guessed_states)

screen.exitonclick()
