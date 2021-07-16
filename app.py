"""Flask app for adopt app."""

import requests
from flask import Flask
from flask.templating import render_template
from werkzeug.utils import redirect
from models import Pet
from handle_pet_api import *

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db
from forms import PetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)
auth_token = None


@app.before_first_request
def refresh_credentials():
    """Just once, get token and store it globally."""
    global auth_token
    auth_token = get_token()


@app.route("/")
def home_page():
    """Render a page about pets"""

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def show_add_pet_form():
    """Show user form and update pet list on database"""

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        #adding pet instance into database
        pet = Pet(name=name, 
                  species=species, 
                  photo_url=photo_url, 
                  age=age, 
                  notes=notes)

        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=["GET","POST"])
def render_pet_info_page(pet_id):
    """Show pet information"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        availability = form.availability.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.availibility = availability

        db.session.commit()
        return redirect(f'/{pet.id}')

    return render_template('pet_info.html', pet=pet, form=form)
