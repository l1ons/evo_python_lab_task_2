from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Main_form(FlaskForm):
    name = StringField("Ім'я: ", validators=[DataRequired()])
    submit = SubmitField("Привітатись")