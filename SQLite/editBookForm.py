from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, HiddenField
from wtforms.validators import DataRequired, NumberRange

class BookForm(FlaskForm):
    id = HiddenField()
    title = StringField(label='Title', validators=[DataRequired()])
    author = StringField(label='Author', validators=[DataRequired()])
    rating = FloatField(label='Rating', validators=[DataRequired(),NumberRange(min=0, max=10 ,message='Rating must be between 0 and 10')])
    submit = SubmitField(label='Submit')
