# Itay Shachar - Flask Final Project

from datetime import datetime
from FlaskFinalProject_Itay import app
from FlaskFinalProject_Itay.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines
from flask import render_template, redirect, request, Flask, flash

from flask_wtf import FlaskForm

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json
import requests

import io
import base64

from os import path

from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField, StringField
from wtforms import ValidationError
from wtforms.validators import DataRequired

from FlaskFinalProject_Itay.Models.Forms import LoginFormStructure 
from FlaskFinalProject_Itay.Models.Forms import UserRegistrationFormStructure
from FlaskFinalProject_Itay.Models.Forms import ExpandForm, CollapseForm
from FlaskFinalProject_Itay.Models.Forms import SingleDataBaseForm

from FlaskFinalProject_Itay.Models.plot_service_functions import plot_to_img


from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

db_Functions = create_LocalDatabaseServiceRoutines() 

# Secret Key
app.config['SECRET_KEY'] = '2871'

# This is rout to the home page 

@app.route('/')
@app.route('/home')
def home():
    # build the file name relative to the project folder
    f1 = open(path.join(path.dirname(__file__), 'static/TextFiles/Home.txt') , encoding="utf8") # Reads Text File
    s1 = f1.read()
    return render_template(
        'index.html',
        title='Home',
        img_DataBase = '/static/Pictures/DataBase.jpg',
        year=datetime.now().year,
        Home = s1,
    )

# This is rout to the contact page 

@app.route('/contact')
def contact():
    # Renders the contact page.
    return render_template(
        'contact.html',
        title = 'Ways to contact',
        img_RoadTripMe2 = '/static/Pictures/RoadTripMe2.jpg',
        year=datetime.now().year,
    )

# This is rout to the about page 

@app.route('/about')
def about():
    """Renders the about page."""
    f1 = open(path.join(path.dirname(__file__), 'static/TextFiles/AboutTheProject.txt') , encoding="utf8")
    s1 = f1.read()
    return render_template(
        'about.html',
        title=':פרטים אודות הפרוייקט',
        img_Tichonet = '/static/Pictures/tichonet.jpg',
        year=datetime.now().year,

        AboutTheProject = s1,
    )
# This is rout to the project resources page 

@app.route('/projectresources')
def projectresources():
    # Renders the project resources page.
    f1 = open(path.join(path.dirname(__file__), 'static/TextFiles/Kaggle.txt') , encoding="utf8") # Reads Text File
    s1 = f1.read()
    return render_template(
        'projectresources.html',
        title = 'Project Resources:',
        year=datetime.now().year,
        img_Kaggle = '/static/Pictures/Kaggle.jpg',


        Kaggle = s1,
    )

# This is rout to the album page 

@app.route('/Album')
def Album():
    # Renders the photo album page.
    return render_template(
        'PictureAlbum.html',
        title='Pictures',
        year=datetime.now().year,
        message='Welcome to my Photo Album',
        img_gunfight = '/static/Pictures/gunfight.jpg',
        img_povertyline = '/static/Pictures/poverty_line.jpg',
        img_CrimePanel = '/static/Pictures/Crime-Panel-Image.jpg',
        img_CrimeTypes = '/static/Pictures/CrimeTypes.jpg',
        img_UsaFlagCrime = '/static/Pictures/UsaFlag-Crime.jpg',
        img_CrimeTypes_NoColor = '/static/Pictures/CrimeTypes_NoColor.jpg',
        img_SyberCrime = '/static/Pictures/SyberCrime.jpg',
        img_WordCloud = '/static/Pictures/WordCloud.jpg',
        img_TheBlackList_1 = '/static/Pictures/TheBlackList_1.jpg',
        img_OneDollar_Pocket = '/static/Pictures/OneDollar_Pocket.jpg',
        img_poverty_USA = '/static/Pictures/poverty_USA.jpg',
        img_DataBaseHomePic = '/static/Pictures/DataBaseHomePic.jpg',
        img_BurningMoney = '/static/Pictures/BurningMoney.jpg',
        img_Homeless_Jobless = '/static/Pictures/Homeless_Jobless.jpg',
        img_USAFlag = '/static/Pictures/usa.jpg',

    )

# This is rout to the DataModel page 

@app.route('/DataModel')
def DataModel():
    # Renders the DataModel page.
    return render_template(
        'DataModel.html',
        year=datetime.now().year,
        title = 'Data Sets Page',
        message='Welcome to my Data Model Page',
        img_gunfight = '/static/Pictures/gunfight.jpg',
        img_povertyline = '/static/Pictures/poverty_line.jpg',
        img_CrimePanel = '/static/Pictures/Crime-Panel-Image.jpg',
        img_CrimeTypes = '/static/Pictures/CrimeTypes.jpg',
        img_UsaFlagCrime = '/static/Pictures/UsaFlag-Crime.jpg',
        img_CrimeTypes_NoColor = '/static/Pictures/CrimeTypes_NoColor.jpg',
        img_SyberCrime = '/static/Pictures/SyberCrime.jpg',
        img_WordCloud = '/static/Pictures/WordCloud.jpg',
        img_TheBlackList_1 = '/static/Pictures/TheBlackList_1.jpg',
        img_OneDollar_Pocket = '/static/Pictures/OneDollar_Pocket.jpg',
        img_poverty_USA = '/static/Pictures/poverty_USA.jpg',
        img_DataBaseHomePic = '/static/Pictures/DataBaseHomePic.jpg',
        img_USAFlag = '/static/Pictures/usa.jpg',

   )


# This is rout to the Data Crime page 

@app.route('/data/DataCrime' , methods = ['GET' , 'POST'])
def DataCrime():
    # Renders the Data Crime page.
    form1 = ExpandForm()
    form2 = CollapseForm()

    # Reads the DataCrime DataSet
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/DataCrime.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit(): # Expand button action
            raw_data_table = df.head(6).to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit(): # Collapse button action
            raw_data_table = ''


    return render_template(
        'DataCrime.html',
        year=datetime.now().year,
        title = 'Data Crime Page:',
        img_gunfight = '/static/Pictures/gunfight.jpg',
        img_povertyline = '/static/Pictures/poverty_line.jpg',
        img_CrimePanel = '/static/Pictures/Crime-Panel-Image.jpg',
        img_CrimeTypes = '/static/Pictures/CrimeTypes.jpg',
        img_UsaFlagCrime = '/static/Pictures/UsaFlag-Crime.jpg',
        img_CrimeTypes_NoColor = '/static/Pictures/CrimeTypes_NoColor.jpg',
        img_SyberCrime = '/static/Pictures/SyberCrime.jpg',
        img_WordCloud = '/static/Pictures/WordCloud.jpg',
        img_TheBlackList_1 = '/static/Pictures/TheBlackList_1.jpg',
        img_OneDollar_Pocket = '/static/Pictures/OneDollar_Pocket.jpg',
        img_poverty_USA = '/static/Pictures/poverty_USA.jpg',
        img_USAFlag = '/static/Pictures/usa.jpg',
        raw_data_table = raw_data_table,
        form1 = form1, # Expand Form
        form2 = form2 # Collapse Form
    )

# This is rout to the Unemployment Rate page 

@app.route('/data/unemploymentrateusa' , methods = ['GET' , 'POST'])
def UnemploymentRate():
     # Renders the Unemployment Rate page.
    form1 = ExpandForm()
    form2 = CollapseForm()

    # Reads the Unemployment Rate DataSet
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/unemploymentrateusa.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit(): # Expand button action
            raw_data_table = df.head(6).to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit(): # Collapse button action
            raw_data_table = ''



    return render_template(
        'UnemploymentRateUsa.html',
        title='Unemployment Rate Page',
        year=datetime.now().year,
        img_gunfight = '/static/Pictures/gunfight.jpg',
        img_povertyline = '/static/Pictures/poverty_line.jpg',
        img_CrimePanel = '/static/Pictures/Crime-Panel-Image.jpg',
        img_CrimeTypes = '/static/Pictures/CrimeTypes.jpg',
        img_UsaFlagCrime = '/static/Pictures/UsaFlag-Crime.jpg',
        img_CrimeTypes_NoColor = '/static/Pictures/CrimeTypes_NoColor.jpg',
        img_SyberCrime = '/static/Pictures/SyberCrime.jpg',
        img_WordCloud = '/static/Pictures/WordCloud.jpg',
        img_TheBlackList_1 = '/static/Pictures/TheBlackList_1.jpg',
        img_OneDollar_Pocket = '/static/Pictures/OneDollar_Pocket.jpg',
        img_poverty_USA = '/static/Pictures/poverty_USA.jpg',
        img_BurningMoney = '/static/Pictures/BurningMoney.jpg',
        img_Homeless_Jobless = '/static/Pictures/Homeless_Jobless.jpg',
        img_USAFlag = '/static/Pictures/usa.jpg',
        raw_data_table = raw_data_table,
        form1 = form1, # Expand Form
        form2 = form2 # Collapse Form
    )

# This is rout to the Data Query page 

@app.route('/query' , methods = ['GET' , 'POST'])
def query():
     # Renders the Data Query page.
    form1 = SingleDataBaseForm() 
    chart = '/static/Pictures/Homeless_Jobless.jpg'
    height_case_1 = "250"
    width_case_1 = "900"
    f1 = open(path.join(path.dirname(__file__), 'static/TextFiles/Query.txt') , encoding="utf8") # Reads Text File
    s1 = f1.read()

    # Reads the Unemployment Rate DataSet
    df_Unim = pd.read_csv(path.join(path.dirname(__file__), 'static/data/unemploymentrateusa.csv'))

    # A Function that removes the word 'County' from a specific column in the DataSet before every county name.
    # For Example, "County Los Angeles" will be shown as "Los Angeles".

    def chop_county(x):
        if 'County' in x:
            y = x.index('County')
            return x[:y - 1]
        else:
            return x
    df_Unim['County'] = df_Unim['County'].apply(lambda x: chop_county(x))

    # States List for Selection - Python code from Jupiter
    country_choices = list(set(df_Unim['State']))
    clean_country_choices = [x for x in country_choices if x == x]
    s = list(zip(clean_country_choices , clean_country_choices))
    form1.state.choices = s

    # Years List for Selection - Python code from Jupiter
    year_choices = list(set(df_Unim['Year']))
    clean_year_choices = [x for x in year_choices if x == x]
    y = list(zip(clean_year_choices , clean_year_choices))
    form1.year.choices = y

    if request.method == 'POST':
        DataSet = form1.DataSet.data # Action if Selected
        year = int(form1.year.data) # Action if Selected
        state = form1.state.data # Action if Selected
        height_case_1 = "100" # Plot Height
        width_case_1 = "900" # Plot Width

       # Python Plot Code from Jupiter
        df_Unim = df_Unim.set_index("Year")
        df_Unim = df_Unim.loc[year]
        df_Unim = df_Unim.set_index("State")
        df_Unim = df_Unim.loc[state]
        df_Unim = df_Unim.reset_index()
        df_Unim = df_Unim.groupby(['County']).mean()

        l = df_Unim["Rate"]
        s = pd.Series(l)
        fig = plt.figure()
        fig.subplots_adjust(bottom = 0.5)
        ax = fig.add_subplot(111)
        s.plot(ax = ax, kind = 'bar', figsize = (10,8), fontsize = 14, color = 'dodgerblue') # Plot Design
        chart = plot_to_img(fig)


    return render_template(
        'query.html',
        title = 'Data Query Page',
        message = 'Please enter the required parameters to see the plot.',
        form1 = form1,
        chart = chart,
        height_case_1 = height_case_1 ,
        width_case_1 = width_case_1 ,
        img_USAFlag = '/static/Pictures/usa.jpg',
        img_Timer = '/static/Pictures/timer.jpg',
        
        QueryText = s1,
        )


# This is rout to the register page 

@app.route('/register', methods=['GET', 'POST'])
def Register():
    # Renders the register page.
    form = UserRegistrationFormStructure(request.form)

    # Register Conditions
    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.Username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data + ". Please Login in the next Page.")
            # I decided to not redirect from the register page to the login page after successful registeration 
        else:
            flash('Error: User with this Username already exist ! - '+ form.Username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User or Login',
        year=datetime.now().year,
        )


# This is rout to the login page 

@app.route('/login', methods=['GET', 'POST'])
def Login():
    # Renders the login page.
    form = LoginFormStructure(request.form)

    # Login Conditions
    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.Username.data, form.Password.data)):
            flash('You Have Successfully Logged in! Enjoy the Site content and features.') # Good Login message
            return redirect('query')
        else:
            flash('Error in - Username and/or password') # Error message
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
    )


