"""Forms for adopt app."""

from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from sqlalchemy.orm import relation, relationship
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, AnyOf
from wtforms.widgets.core import Option


class PetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species",
                          validators=[InputRequired(),
                                      AnyOf(values=["cat", "dog", "porcupine", "Cat", "Dog", "Porcupine"],
                                            message="Must be cat, dog, or porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField(
        "Age",
        choices=[('baby', 'Baby'), ('young', 'Young'),
                 ('adult', 'Adult'), ('senior', 'Senior')],
        validators=[InputRequired()])

    notes = StringField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    availability = BooleanField("Availability",
                                validators=[Optional()])
