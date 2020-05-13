from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField , HiddenField , DateTimeField , IntegerField , DecimalField , FloatField , RadioField
from wtforms import Form, SelectMultipleField , BooleanField
from wtforms import TextField, TextAreaField, SelectField
from wtforms import validators, ValidationError

from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired


# Expand button for the DataSet table in DataModel's pages.

class ExpandForm(FlaskForm):
    submit1 = SubmitField('Expand')
    name="Expand" 
    value="Expand"

# Collapse button for the DataSet table in DataModel's pages.

class CollapseForm(FlaskForm):
    submit2 = SubmitField('Collapse')
    name="Collapse" 
    value="Collapse"


# User Login form

class LoginFormStructure(FlaskForm):
    Username   = StringField('Username:  ' , validators = [DataRequired()]) # Username Validator
    Password   = PasswordField('Password:  ' , validators = [DataRequired()]) # Password Validator
    Submit = SubmitField('Submit')

# User Registration Form

class UserRegistrationFormStructure(FlaskForm):
    FirstName  = StringField('First name:  ' , [validators.Length(min=2)]) # First Name Validator
    LastName   = StringField('Last name:  ' , [validators.Length(min=2)]) # Last Name Validator
    PhoneNum   = StringField('Phone number:  ' , [validators.Length(min=10, max=10)]) # Phone Number Validator
    EmailAddr  = StringField('E-Mail:  ' ) # Email Validator
    Username   = StringField('Username:  ' , [validators.Length(min=5, max=16)]) # Username Validator
    Password   = PasswordField('Password:  ' , [validators.Length(min=5, max=16)]) # Password Validator
    Submit = SubmitField('Submit') # Submit Button Field
  

# Data Query Choises Form

class SingleDataBaseForm(FlaskForm):
    DataSet = SelectField('DataSet' , validators = [DataRequired()] , choices=[('unemploymentrateusa', 'Unemployment Rate')]) # DataSet Select Field
    year = SelectField('Year:' , validators = [DataRequired()]) # Year Select Field
    state = SelectField('State:' , validators = [DataRequired()]) # State Select Field
    submit = SubmitField('Submit')

   