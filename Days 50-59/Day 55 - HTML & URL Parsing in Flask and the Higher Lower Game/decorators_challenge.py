from flask import Flask

app = Flask(__name__)
print(__name__)


def make_bold(func):
    def wrapper_func():
        return f"<b>{func()}</b>"
    return wrapper_func


def make_emphasised(func):
    def wrapper_func():
        return f"<em>{func()}</em>"
    return wrapper_func


def make_underlined(func):
    def wrapper_func():
        return f"<u>{func()}</u>"
    return wrapper_func


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
        '<p>Paragraph.</p>' \
        '<h2>Doar atat</h2>' \
        '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDFyZ3JsZWQ5aTlkOWtlMXYwZTBpa3FpcW9oZWd4Z2ZsZzFqYmg3ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dRcMsUUrnR8He/giphy.gif" width=200>'


@app.route("/bye")
@make_bold
@make_emphasised
@make_underlined
def bye():
    return "Bye"


@app.route("/username/<name>/<int:num>")
def hi(name, num):
    return f"Hi {name} you are {num}"


if __name__ == "__main__":
    app.run(debug=True)
