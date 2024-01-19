from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, BooleanField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, URL, Length

from flask_wtf.file import FileField, FileAllowed, FileRequired

class BreakoutForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    image = FileField(validators=[FileRequired(), FileAllowed(['jpg','jpeg','png'],"We only allow images")])
    status = BooleanField("Status:", validators=[DataRequired()])
    submit = SubmitField("Add Topic")