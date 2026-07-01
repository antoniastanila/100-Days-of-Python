from flask import Flask, render_template
from post import allPosts, get_posts_list

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", allPosts=allPosts)


@app.route('/post/<int:blog_id>')
def display_post(blog_id):
    posts_list = get_posts_list()
    return render_template("post.html", blog_id=blog_id, posts_list=posts_list)


if __name__ == "__main__":
    app.run(debug=True)
