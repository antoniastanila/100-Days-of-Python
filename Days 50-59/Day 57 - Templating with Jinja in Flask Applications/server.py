from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)


@app.route("/")
def main():
    random_nr = random.randint(1, 10)
    curr_year = datetime.datetime.now().year
    my_name = "Anto"
    return render_template("index.html", num=random_nr, curr_year=curr_year, my_name=my_name)


if __name__ == "__main__":
    app.run(debug=True)
