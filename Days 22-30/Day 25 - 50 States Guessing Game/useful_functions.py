from turtle import Turtle
import pandas as pd
NUMBER_OF_STATES = 50


def manage_answer(correct_guesses, answer_state, states_file, guessed_states, missed_states):
    """Place the guessed state on the map at the right coordinates if valid."""

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
    return correct_guesses


def missed_states_file(missed_states):
    """Create a CSV with the states the user didn't guess."""

    if len(missed_states) > 0:
        missed_states_dict = {
            "state": missed_states,
        }

        missed_states_data = pd.DataFrame(missed_states_dict)
        missed_states_data.to_csv("missed_states.csv")


def manage_end_of_game(guessed_states):
    """Show a final message based on the user's score."""

    congratulations = Turtle()
    congratulations.hideturtle()
    congratulations.penup()

    if len(guessed_states) == NUMBER_OF_STATES:
        congratulations.color("green")
        congratulations.write("CONGRATULATIONS!! \nYou guessed all the 50 states!",  move=False, align='center',
                              font=('Arial', 20, 'bold'))

    elif len(guessed_states) < NUMBER_OF_STATES / 2:
        congratulations.color("red")
        congratulations.write("You guessed less than half of the states...\n Better luck next time!",  move=False, align='center',
                              font=('Arial', 20, 'bold'))

    elif len(guessed_states) >= NUMBER_OF_STATES / 2:
        congratulations.color("#8B8000")
        congratulations.write("You guessed more than half of the states! \n You're doing good.",  move=False, align='center',
                              font=('Arial', 20, 'bold'))
