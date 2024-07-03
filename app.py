from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, flash
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import os
import dotenv

# Use dotenv to load environment variables from .env file
dotenv.load_dotenv()

# Get the DATABASE_URL environment variable
database_url = os.getenv('DATABASE_URL')

app = Flask(__name__)

# Configure SQLAlchemy with the database URL
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)


class AddUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Create')


# Create all database tables
with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    # Retrieve the list of "Person" from the mariadb database
    persons = Person.query.all()
    return render_template('index.html', persons=persons)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = AddUserForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f'Utilisateur {name} avec l\'email {email} a été ajouté avec succès!', 'success')
        return redirect(url_for('add_user'))
    return render_template('createForm.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
