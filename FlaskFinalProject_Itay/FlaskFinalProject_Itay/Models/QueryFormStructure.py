from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import validators, ValidationError

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
    FirstName  = StringField('First name:  ' , validators = [DataRequired()])
    LastName   = StringField('Last name:  ' , validators = [DataRequired()])
    PhoneNum   = StringField('Phone number:  ' , validators = [DataRequired()])
    EmailAddr  = StringField('E-Mail:  ' , validators = [DataRequired()])
    Username   = StringField('Username:  ' , validators = [DataRequired()])
    Password   = PasswordField('Password:  ' , validators = [DataRequired()])
    Submit = SubmitField('Submit')

    
class ExpandForm(FlaskForm):
    submit1 = SubmitField('Expand')
    name="Expand" 
    value="Expand"

class CollapseForm(FlaskForm):
    submit2 = SubmitField('Collapse')
    name="Collapse" 
    value="Collapse"


