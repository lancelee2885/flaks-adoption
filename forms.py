"""Forms for adopt app."""

from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL
from wtforms.widgets.core import Option

class PetForm(FlaskForm):

	name = StringField("Pet Name", validators=[InputRequired()])
	species = StringField("Species", validators=[InputRequired()])
	photo_url = StringField("Photo URL", validators=[Optional(), URL()])
	age = SelectField("Age", choices=[()],validators=[InputRequired()])  # TODO: add values for choices (data, things_dislayed)
	notes = StringField("Notes", validators=[Optional()])