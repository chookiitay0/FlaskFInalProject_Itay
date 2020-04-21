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



class ExpandForm(FlaskForm):
    submit1 = SubmitField('Expand')
    name="Expand" 
    value="Expand"

class CollapseForm(FlaskForm):
    submit2 = SubmitField('Collapse')
    name="Collapse" 
    value="Collapse"


    #    User Registration and User Login

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
    
  

    #       Query Forms

class SingleDataBaseForm(FlaskForm):
    DataSet = SelectField('DataSet' , validators = [DataRequired] , choices=[('unemploymentrateusa', 'Unemployment Rate')])
    year = SelectField('Year:' , validators = [DataRequired])
    state = SelectField('State:' , validators = [DataRequired])
    submit = SubmitField('Submit')

   