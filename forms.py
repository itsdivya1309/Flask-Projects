# This file contains the forms needed in your application

from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, DateField, BooleanField,RadioField)
from wtforms.validators import InputRequired, Length

class MoviesForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    plot = TextAreaField('Plot Summary',
                                validators=[InputRequired(),
                                            Length(max=200)])
    released = DateField('Release date', format='%d-%m-%Y', validators=[InputRequired()])
    platform = RadioField('OTT Platform',
                       choices=['Disney+Hotstar', 'Netflix', 'Amazon Prime Video','Other'],
                       validators=[InputRequired()])
    available = BooleanField('Available', default='checked')
