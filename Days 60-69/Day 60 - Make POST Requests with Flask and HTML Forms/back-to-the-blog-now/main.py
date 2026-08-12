from flask import Flask, render_template, request
import requests
import datetime
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

OWN_EMAIL = os.getenv("EMAIL")
OWN_PASSWORD = os.getenv("PASSWORD")

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

@app.route("/contact", methods = ['POST', 'GET'])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]

    if request.method == "POST":
        send_email(name,email,phone,message)
        return f"<h1>{name} has this email: {email}, phone: {phone}, msg: {message}</h1> "
    elif request.method == "GET":
        return render_template("contact.html")

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\n Phone: {phone}\nMessage : {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)