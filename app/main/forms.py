from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from ..models import Pitch,Comment
from wtforms.validators import DataRequired

class UpdateProfileForm(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class InterviewForm(FlaskForm):
    body = TextAreaField("Pitch Description",validators=[DataRequired()])
    submit = SubmitField('Submit')

class PickupForm(FlaskForm):
    body = TextAreaField("Pitch Description",validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProductForm(FlaskForm):
    body = TextAreaField("Pitch Description",validators=[DataRequired()])
    submit = SubmitField('Submit')

class PromotionForm(FlaskForm):
    body = TextAreaField("Pitch Description",validators=[DataRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    body = TextAreaField("Comment Description",validators=[DataRequired()])
    submit = SubmitField('Submit')