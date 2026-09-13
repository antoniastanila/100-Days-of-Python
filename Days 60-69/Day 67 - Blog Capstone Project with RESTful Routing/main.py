from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from dotenv import load_dotenv
import os
from pathlib import Path
import datetime

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "instance" / "posts.db"
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)

class BlogPostForm(FlaskForm):
    title = StringField(label='Blog Post Title', validators=[DataRequired()])
    subtitle = StringField(label='Subtitle', validators=[DataRequired()])
    name = StringField(label='Your Name', validators=[DataRequired()])
    img_url = StringField(label='Blog Image URL', validators=[DataRequired()])
    body = CKEditorField(label = 'Body', validators=[DataRequired()])
    submit = SubmitField(label = 'Submit Post')

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH.as_posix()}"
db = SQLAlchemy(model_class=Base)

ckeditor = CKEditor(app)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()

    return render_template("index.html", all_posts=posts)

@app.route('/<post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new_post", methods = ['GET', 'POST'])
def add_new_post():
    new_blog_post_form = BlogPostForm()
    heading_title = "New Post"
    if new_blog_post_form.validate_on_submit():
        title = new_blog_post_form.title.data
        subtitle = new_blog_post_form.subtitle.data
        name = new_blog_post_form.name.data
        body = new_blog_post_form.body.data
        img_url = new_blog_post_form.img_url.data

        today = datetime.datetime.now()
        date = f"{today.strftime('%B')} {today.strftime('%d')}, {today.year}" 
        
        new_blog = BlogPost(title = title, subtitle = subtitle, author = name, date = date, body = body, img_url = img_url)
        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form = new_blog_post_form, heading_title = heading_title)


@app.route("/edit-post/<post_id>", methods = ['GET', 'POST'])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = BlogPostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        name=post.author,
        body=post.body
    )
    heading_title = "Edit Post"
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.name.data
        post.body= edit_form.body.data

        db.session.commit() 

        return redirect(url_for('show_post', post_id = post_id))

    return render_template("make-post.html", form = edit_form, heading_title = heading_title)

# TODO: delete_post() to remove a blog post from the database

@app.route("/delete/<post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
