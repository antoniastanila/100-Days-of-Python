from flask import Flask, render_template
import requests
import datetime

res = requests.get("https://api.npoint.io/002e90ad79f718da35e7")
res.raise_for_status()
res = res.json()

today = datetime.date.today()

app=Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html", res=res, today=today)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:id>")
def post(id):
    return render_template("post.html", posts_list=res, post_id = id, today=today)

if __name__ == "__main__":
    app.run(debug=True)