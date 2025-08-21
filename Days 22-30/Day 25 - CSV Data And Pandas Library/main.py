from turtle import Turtle, Screen
import pandas as pd
import turtle

NUMBER_OF_STATES = 50

screen = Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_file = pd.read_csv("50_states.csv")
game_in_on = True
correct_guesses = 0

guessed_states = []
missed_states = states_file.state.to_list()
print(missed_states)

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

    states_list = states_file.state.to_list()
    if answer_state in states_list and answer_state not in guessed_states:
        correct_guesses += 1
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        x_coordinate = states_file[states_file.state == answer_state].x.item()
        y_coordinate = states_file[states_file.state == answer_state].y.item()

        print(f"({x_coordinate},{y_coordinate})")

        new_state.goto(x_coordinate, y_coordinate)

        new_state.write(answer_state, move=False, align='left',
                        font=('Arial', 8, 'normal'))

        guessed_states.append(answer_state)
        missed_states.remove(answer_state)

if len(missed_states) > 0:
    missed_states_dict = {
        "state": missed_states,
    }

    missed_states_data = pd.DataFrame(missed_states_dict)
    missed_states_data.to_csv("missed_states.csv")


if len(guessed_states) == NUMBER_OF_STATES:
    congratulations = Turtle()
    congratulations.color("green")
    congratulations.hideturtle()
    congratulations.penup()
    congratulations.write("CONGRATULATIONS!! \nYou guessed all the 50 states!",  move=False, align='center',
                          font=('Arial', 20, 'bold'))

screen.exitonclick()
