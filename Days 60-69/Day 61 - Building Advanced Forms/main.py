from flask import Flask, redirect, render_template
import os
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

app = Flask(__name__)

load_dotenv()

app.secret_key = os.getenv("secret_key")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    form = MyForm()
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
