# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired, FileField 

class MovieForm(FlaskForm):
    title = StringField('Title', validators= InputRequired)
    description = TextAreaField ('Description', validators= InputRequired)
    poster = FileField('Poster',validators= [FileRequired(), FileAllowed(['jpg','png','gif'], 'Images only!')])
