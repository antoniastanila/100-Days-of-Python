from flask import Flask, render_template
from age_gender import get_gender, get_age
app = Flask(__name__)


@app.route("/")
def main():
    return "Hello World!"


@app.route("/guess/<name>")
def guess(name):
    gender = get_gender(name)
    age = get_age(name)
    name = name.capitalize()
    return render_template("index.html",
                           name=name,
                           age=age,
                           gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
