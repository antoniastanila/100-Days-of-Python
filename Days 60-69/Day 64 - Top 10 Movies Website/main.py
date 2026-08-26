from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")
token = os.getenv("bearer_token")

class UpdateForm(FlaskForm):
    rating = StringField(label='Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your review', validators=[DataRequired()])
    submit = SubmitField(label='Update')

class AddMovieForm(FlaskForm):
    title = StringField(label='Title',validators=[DataRequired()])
    submit = SubmitField(label='Add')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] =  mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False) 
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] =  mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    # READ A PARTICULAR RECORD By Query
    with app.app_context():
        movies = db.session.execute(db.select(Movie)).scalars().all()
    return render_template("index.html", movies=movies)

# @app.route("/<int:number>")

@app.route("/edit", methods = ['POST', 'GET'])
def edit():
    form = UpdateForm()
    id = request.args.get("id")

    # with app.app_context(): <- nu ai nevoie cand esti in interiorul unei rute Flask, deoarece application context exista deja aici

    movie = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
    # sau aici mai puteam sa fac: movie = db.get_or_404(Movie, id)

    if form.validate_on_submit():
        movie.review = form.review.data
        movie.rating = float(form.rating.data)
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("edit.html", form=form)

@app.route("/delete")
def delete():
    id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods = ['GET', 'POST'])
def add():
    addForm = AddMovieForm()
    if addForm.validate_on_submit():
        movieTitle = addForm.title.data

        params = {
            "query" : movieTitle
        }
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}"
        }

        res = requests.get(url="https://api.themoviedb.org/3/search/movie", params=params, headers=headers)
        res.raise_for_status()
        results = res.json()['results']

        return render_template("select.html", results = results)
        
    return render_template("add.html", form = addForm)

@app.route("/select")
def select():
    return render_template("select.html")

if __name__ == '__main__':
    app.run(debug=True)
