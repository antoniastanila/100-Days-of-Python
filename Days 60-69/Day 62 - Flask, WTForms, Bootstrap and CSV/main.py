from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from werkzeug.datastructures import ImmutableMultiDict


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30AM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[(1,"☕️"),(2,"☕️☕️"), (3,"☕️☕️☕️"), (4,"☕️☕️☕️☕️"), (5,"☕️☕️☕️☕️☕️")], validators=[DataRequired()])
    wifi_rating = SelectField('WiFi Strength Rating', choices=[(1,"💪"),(2,"💪💪"), (3,"💪💪💪"), (4,"💪💪💪💪"), (5,"💪💪💪💪💪")], validators=[DataRequired()])
    socket_availability = SelectField('Power Socket Availability', choices=[(1, '🔌'), (2, '🔌🔌'), (3, '🔌🔌🔌'), (4, '🔌🔌🔌🔌'), (5, '🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods = ['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")

        cafe_dictionary = request.form.to_dict()
        print(cafe_dictionary)
 
        cafe_dictionary.pop('submit')
        cafe_dictionary.pop('csrf_token')
 
        data_list = [cafe_dictionary[elem] for elem in cafe_dictionary]
        print(data_list)

        with open("cafe-data.csv", "a", encoding="utf-8") as f:
            f.write(",".join(data_list) + "\n")
       
        return redirect(url_for("cafes"))    
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        cafes_number = len(list_of_rows)
        columns_number = len(list_of_rows[0])
    return render_template('cafes.html', cafes=list_of_rows, cafes_number=cafes_number, columns_number=columns_number)


if __name__ == '__main__':
    app.run(debug=True)
