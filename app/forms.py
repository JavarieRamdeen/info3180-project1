from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, validators, SelectField, IntegerField, FileField
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

p_type = [('House'),('Apartment')]

class PropertyForm(FlaskForm):
    title = StringField('Title',validators=[InputRequired()])
    bedrooms = IntegerField('Bedrooms',validators=[InputRequired()])
    bathrooms = IntegerField('Bathrooms',validators=[InputRequired()])
    location = StringField('Location',validators=[InputRequired()])
    price = StringField('Price',validators=[InputRequired()])
    type = SelectField('Type', choices=p_type, validators=[InputRequired()])
    title = StringField('Title',validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Image', validators=[FileRequired(),FileAllowed(['jpg','png'], 'Images only!')])
    submit = SubmitField("Send")

