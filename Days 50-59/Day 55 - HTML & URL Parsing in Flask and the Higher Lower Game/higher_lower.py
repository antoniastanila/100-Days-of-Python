from flask import Flask
import random

app = Flask(__name__)
print(__name__)

random_number = random.randint(1, 9)


@app.route("/")
def hello_world():
    return "<h1>Guess a number between 1 and 9 !!!</h1>" \
        "<img src=https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcG5sem12Z2Job2FleHJsbW9td3Y5MHRscXVxZTN3NGtqNTJkdTRkMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JdFEeta1hLNnO/giphy.gif>"


@app.route("/<int:number>")
def check_number(number):
    if number == random_number:
        return "<h1 style=color:green>YOU GUESSES IT!!</h1>" \
            "<img src=https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnVwbTducDUxazZndDc2ZWdiZXVrZWFzOHQweGE2ZXcwbWdwaHpscCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/geslvCFM31sFW/giphy.gif>"
    elif number < random_number:
        return "<h1 style=color:red>Too low... Try again!</h1>" \
            "<img src=https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHE1eWx1NjdkN2oyNmNyNmJqdXRjbzhlZnR6YmQ0bGhsNzRoa2xqbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZliiEvT7b6xnwt77r7/giphy.gif>"
    elif number > random_number:
        return "<h1 style=color:red>Too high... Try again!</h1>" \
            "<img src=https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3cwdmdxcXV1dmZwYXNqZnNnY3d0NWo2YXY5NmdhNjdmcmxsemVzeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HOW1XRB5qaZDLqaSUW/giphy.gif>"


if __name__ == "__main__":
    app.run(debug=True)
