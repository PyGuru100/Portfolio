from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
import random
from add_form import AddForm


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# noinspection SpellCheckingInspection
app.config['SECRET_KEY'] = 'SOME RANDOM BULLSHIT WEJHUIOFWEHNDN'
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    map_url = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=True)
    location = db.Column(db.String, nullable=True)
    has_sockets = db.Column(db.Boolean, nullable=True)
    has_wifi = db.Column(db.Boolean, nullable=True)
    has_toilet = db.Column(db.Boolean, nullable=True)
    can_take_calls = db.Column(db.Boolean, nullable=True)
    seats = db.Column(db.String, nullable=True)
    coffee_price = db.Column(db.String, nullable=True)


db.create_all()


@app.route('/')
def home():
    # TODO: fix this garbage. Don't query all cafes and pick 5, query 5 random cafes.
    cafes = []
    all_cafes = Cafe.query.all()
    while len(cafes) < 5:
        cafe = random.choice(all_cafes)
        if (cafe not in cafes) and cafe.img_url:
            cafes.append(cafe)
    return render_template('home.html', cafes=cafes, last_cafe=cafes[4])


@app.route('/cafe/<cafe_id>')
def cafe_page(cafe_id: int):
    cafe = Cafe.query.get(cafe_id)
    if cafe is None:
        return "<h1> 404: Cafe Not Found. </h1>"
    return render_template('cafe_page.html', cafe=cafe)


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    # TODO: make this not garbage
    form = AddForm()
    something_wrong = ""
    if request.method == 'POST':
        if form.validate_on_submit():  # the code here was generated using generators/form_to_db.py
            new_cafe = Cafe()
            new_cafe.name = form.name.data
            new_cafe.map_url = form.map_url.data
            new_cafe.img_url = form.img_url.data
            new_cafe.location = form.location.data
            new_cafe.has_sockets = form.has_sockets.data
            new_cafe.has_wifi = form.has_wifi.data
            new_cafe.has_toilet = form.has_toilet.data
            new_cafe.can_take_calls = form.can_take_calls.data
            new_cafe.seats = form.seats.data
            new_cafe.coffee_price = form.coffee_price.data
            db.session.add(new_cafe)
            db.session.commit()
            return "<h1> Cafe added successfully! <a href='/'> HOME </a> </h1>"
        else:
            something_wrong = 'Invalid cafe data.'
            return render_template('add_cafe.html', form=form, message=something_wrong)
    return render_template('add_cafe.html', form=form, message=something_wrong)


if __name__ == '__main__':
    app.run(debug=True)
