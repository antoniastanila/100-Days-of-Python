from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "instance" / "cafes.db"

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH.as_posix()}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # method I
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # method II - dict comprehension
        return {column.name : getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    print(all_cafes)
    print(len(all_cafes))
    random_cafe = choice(all_cafes)

    random_cafe = random_cafe.to_dict()

    return jsonify(cafe=random_cafe)

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()

    all_cafes = [cafe.to_dict() for cafe in all_cafes]

    print(all_cafes[0])

    return jsonify(
        cafes = all_cafes
    )

@app.route("/search")
def search_cafe():
    location = request.args.get("loc")
    cafes_in_location = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()

    if not cafes_in_location:
        return jsonify({
            "error" : "Sorry, we don't have a cafe in that location."
            }
        )
    
    cafes_in_location = [cafe.to_dict() for cafe in cafes_in_location]
    return jsonify(cafes_in_location)

@app.route("/add", methods = ['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify({"response" : {
        "success" : "Successfully added a new cafe!"
    }})

@app.route("/update-price/<cafe_id>", methods = ['PATCH'])
def update_coffee_price(cafe_id):
    try:
        coffee_to_update = db.get_or_404(Cafe, cafe_id) 
    except:
        return jsonify({"error" : {
            "Not Found" : "Sorry, a cafe with that id was not found in the database."
        }}), 404
    else:
        coffee_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify({"success" : "Successfully updated the price!"}), 200

# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
