from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'randomString101010'

debug = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()


@app.route('/')
def display_home():
    """[summary]displays list of pets in adoption agency db as well as button to add new pet

    Returns:
        [render template]: [passes all pets from db to html template]
    """
    pets = Pet.query.order_by(Pet.available.desc()).all()
    return render_template('home.html', pets = pets)


@app.route('/add', methods=['GET', 'POST'])
def add_new_pet():
    """[summary]handles both display and processing of form to add new pet to db

    Returns:
        if valid post request:
            [redirect]: [sends user back to home page with full list of pets]
        if not a valid post request:
            [render template]: [displays form to add new pet to db]
    """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('add.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """[summary]display detail and handle processing of editing individual pet by id

    Args:
        pet_id ([int]): [pet id from db]

    Returns:
        if valid post request:
            [redirect]: [updates db and sends user back to home page with full list of pets]
        if not a valid post request:
            [render template]: [displays form to edit current pet]
    """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect('/')
    else:
        return render_template('info.html', pet=pet, form=form)