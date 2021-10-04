from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """[summary]form to add new Pet to DB

    Args:
        FlaskForm ([class]): [inherits from FlaskForm Class]
    """

    name = StringField('Pet Name', 
                validators=[InputRequired()])
    species = SelectField('Species', 
                choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')])
    photo_url = StringField('Image URL Of Your Pet', 
                default="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png", 
                validators=[URL(), Optional()])
    age = IntegerField('Pet Age', 
                validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Any Notes About Your Pet')


class EditPetForm(FlaskForm):
    """[summary]form to edit specific fields on Pet in DB

    Args:
        FlaskForm ([class): [inherits from FlaskForm Class]
    """

    photo_url = StringField('Image URL Of Your Pet', validators=[URL(), Optional()])
    notes = StringField('Any Notes About Your Pet')
    available = BooleanField('Available')