from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []



@app.route('/')
def home():
    return render_template("index.html", all_books = all_books, books_number = len(all_books))


@app.route("/add", methods = ['POST', 'GET'])
def add():
    if request.method == 'POST':
        book = request.form.to_dict()
        all_books.append(book)
        print(all_books)
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

