from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired
from wtforms.validators import InputRequired




class QueryFormStructure(FlaskForm):
    name   = StringField('I am Looking for the capitol of:' , validators = [DataRequired()])
    submit = SubmitField('Submit')


class LoginFormStructure(FlaskForm):
    Username   = StringField('Username:  ' , validators = [DataRequired()])
    Password   = PasswordField('Password:  ' , validators = [DataRequired()])
    Submit = SubmitField('Submit')

class UserRegistrationFormStructure(FlaskForm):
    FirstName  = StringField('First name:  ' , [validators.Length(min=2)])
    LastName   = StringField('Last name:  ' , [validators.Length(min=2)])
    PhoneNum   = StringField('Phone number:  ' , [validators.Length(min=10, max=10)])
    EmailAddr  = StringField('E-Mail:  ' , [validators.Email()])
    Username   = StringField('Username:  ' , [validators.Length(min=5, max=16)])
    Password   = PasswordField('Password:  ' , [validators.Length(min=5, max=16)])
    Submit = SubmitField('Submit')

    
class ExpandForm(FlaskForm):
    submit1 = SubmitField('Expand')
    name="Expand" 
    value="Expand"

class CollapseForm(FlaskForm):
    submit2 = SubmitField('Collapse')
    name="Collapse" 
    value="Collapse"



