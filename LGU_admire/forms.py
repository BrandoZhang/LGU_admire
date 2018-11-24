"""
Admire_Form
author: str
content: str
submit filed
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class AdmireForm(FlaskForm):
    author_name = StringField("Name", validators=[DataRequired(), Length(1, 50)])
    body = TextAreaField("Message", validators=[DataRequired(), Length(1, 140)])
    submit = SubmitField()
