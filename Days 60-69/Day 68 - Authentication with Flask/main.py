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
class User(UserMixin, db.Model):
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

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

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

        login_user(new_user)

        # Can redirect() and get name from the current_user
        return redirect(url_for("secrets"))    
    
    return render_template("register.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_emal = request.form.get('email')
        user_password = request.form.get('password')
        user = db.session.execute(db.select(User).where(User.email == user_emal)).scalar()

        if check_password_hash(user.password, user_password):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            pass
    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name) # what?? current_user? where does the program know what that is??
    return render_template("secrets.html", name = current_user.name)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download', methods = ['GET'])
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
