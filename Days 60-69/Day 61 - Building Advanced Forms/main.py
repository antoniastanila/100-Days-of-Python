from flask import Flask, redirect, render_template
import os
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), validators.Email()])
    password = PasswordField(label='password', validators=[DataRequired(), validators.Length(8, message="At leat 8 characters!")])
    submit = SubmitField(label='Log In')

        
app = Flask(__name__)

load_dotenv()

app.secret_key = os.getenv("secret_key")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ['POST', 'GET'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        return render_template("denied.html")
    return render_template("login.html", form=form)

@app.route("/succes")
def succes():
    render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)
