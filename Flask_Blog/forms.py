from flask_wtf import FlaskForm
from wtforms.fields import html5 as h5fields
from wtforms import StringField,PasswordField,SubmitField,BooleanField,IntegerField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
		productname=StringField('productname',validators=[DataRequired(),Length(min=2,max=20)])
		dairyname=StringField('dairyname',validators=[DataRequired(),Length(min=2,max=20)])
		id1=h5fields.IntegerField('id1')
		price=h5fields.IntegerField('price')
		submit=SubmitField('Upload')

class SearchForm(FlaskForm):
		id1=h5fields.IntegerField('id1')
		search=SubmitField('search')

class LoginForm(FlaskForm):
		email=StringField('E-mail',validators=[DataRequired(),Email()])
		password=PasswordField('Password',validators=[DataRequired()])
		remember=BooleanField('Remember Me')
		submit=SubmitField('Login')