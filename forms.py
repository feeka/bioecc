from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class Encoder(FlaskForm):
	dna_seq = TextAreaField('DNA Sequence', validators=[DataRequired()])
	degree = IntegerField('Polynomial Degree', validators=[DataRequired()])
	positions = TextAreaField('Positions for Generator matrix',validators=[DataRequired()])
	submit = SubmitField('Calculate')