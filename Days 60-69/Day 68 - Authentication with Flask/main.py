from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    # is_authenticated: Mapped[bool] 
    # is_active: Mapped[bool]
    # is_anonymous: Mapped[bool]

    # def get_id(self):
    #     return self.id


with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        password = request.form['password']
        hash_and_salted_password = generate_password_hash(password, method='pbkdf2', salt_length=8)

        new_user = User(email = request.form['email'], password = hash_and_salted_password, name = request.form['name'])
        # to tap into a field of the form, you could also do it like this: request.form.get('name')
        db.session.add(new_user)
        db.session.commit()
        return render_template("secrets.html", name = new_user.name)
    return render_template("register.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_emal = request.form.get('email')
        user_password = request.form.get('password')
        user = db.session.execute(db.select(User).where(User.email == user_emal)).scalar()

        if check_password_hash(user.password, user_password):
            return render_template("secrets.html", name = user.name)
        else:
            pass
    return render_template("login.html")

@login_required
@app.route('/secrets')
def secrets():
    # if User.get(user_id):
    #     return render_template("secrets.html")
    return render_template("secrets.html")

@login_manager.user_loader
@app.route('/logout')
def logout(user_id):
    id = User.get(user_id)
    return render_template("index.html")

@login_required
@app.route('/download', methods = ['GET'])
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
