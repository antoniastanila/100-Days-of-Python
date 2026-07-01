from flask import Flask, render_template
# from age_gender import get_gender, get_age
from blog import get_all_posts
app = Flask(__name__)


@app.route("/")
def main():
    return "Hello World!"


# @app.route("/guess/<name>")
# def guess(name):
#     gender = get_gender(name)
#     age = get_age(name)
#     name = name.capitalize()
#     return render_template("index.html",
#                            name=name,
#                            age=age,
#                            gender=gender)
# #

@app.route("/blog")
def blog_post():
    allPosts = get_all_posts()
    return render_template("blog.html", allPosts=allPosts)


@app.route("/link/<num>")
def get_link(num):
    print(num)
    return render_template("link.html")


if __name__ == "__main__":
    app.run(debug=True)
