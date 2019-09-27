from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class EntryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', validators=[DataRequired()], choices=[('w','Work'), ('p','Personal')])
    task = TextAreaField('Task Details')
    submit = SubmitField('Create Task')

