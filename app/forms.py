# project/user/forms.py
from flask_wtf import Form
from wtforms import TextField, PasswordField, FieldList, FormField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional

class OneDescription(Form):
	des = TextField('description', validators=[Length(50), Optional()])

	def validate(self):
		return True

class InputForm(Form):
	desList = FieldList(FormField(OneDescription), min_entries=6, max_entries=6)

	def validate(self):
		return True