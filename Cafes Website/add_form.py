from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL


class AddForm(FlaskForm):
    name = StringField('Cafe Name: ', validators=[DataRequired()])
    map_url = StringField('Cafe Location URL: ', validators=[DataRequired(), URL()])
    img_url = StringField('Cafe Image URL: ', validators=[URL()])
    location = StringField('Cafe Location Name: ')
    has_sockets = BooleanField('Does the cafe have power sockets? ')
    has_wifi = BooleanField('Does the cafe have WIFI? ')
    has_toilet = BooleanField('Does the cafe have a bathroom? ')
    can_take_calls = BooleanField('Can you talk on the phone? ')
    seats = StringField('How many seats does the cafe have? (e.g. 14 - 20)')
    coffee_price = StringField('How much does a cup of coffee cost? (e.g. $5)')
    add = SubmitField('Add Cafe')
