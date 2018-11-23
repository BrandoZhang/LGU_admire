"""
Admire_Form
author: str
content: str
submit filed
delete filed
like filed
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
