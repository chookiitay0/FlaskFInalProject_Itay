from datetime import datetime
from flask import render_template
from FlaskFinalProject_Itay import app
from FlaskFinalProject_Itay.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json
import requests

import io
import base64

from os import path

from flask import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError

from FlaskFinalProject_Itay.Models.QueryFormStructure import QueryFormStructure 
from FlaskFinalProject_Itay.Models.QueryFormStructure import LoginFormStructure 
from FlaskFinalProject_Itay.Models.QueryFormStructure import UserRegistrationFormStructure 
from FlaskFinalProject_Itay.Models.QueryFormStructure import ExpandForm
from FlaskFinalProject_Itay.Models.QueryFormStructure import CollapseForm
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

db_Functions = create_LocalDatabaseServiceRoutines() 

app.config['SECRET_KEY'] = '2871'

@app.route('/')
@app.route('/home')
def home():
    """Renders the contact page."""
    f1 = open(path.join(path.dirname(__file__), 'static/TextFiles/Home.txt') , encoding="utf8")
    s1 = f1.read()
    return render_template(
        'index.html',
        title='Home',
        img_DataBase = '/static/Pictures/DataBase.jpg',
        year=datetime.now().year,

        Home = s1,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        img_RoadTripMe2 = '/static/Pictures/RoadTripMe2.jpg',
        year=datetime.now().year,
    )

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

@app.route('/projectresources')
def projectresources():
    """Renders the contact page."""
    f1 = open(path.join(path.dirname(__file__), 'static/TextFiles/Kaggle.txt') , encoding="utf8")
    s1 = f1.read()
    return render_template(
        'projectresources.html',
        title = 'Project Resources:',
        year=datetime.now().year,
        img_Kaggle = '/static/Pictures/Kaggle.jpg',


        Kaggle = s1,
    )

@app.route('/Album')
def Album():
    """Renders the about page."""
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



    )

@app.route('/DataModel')
def DataModel():
    """Renders the contact page."""
    return render_template(
        'DataModel.html',
        year=datetime.now().year,
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

   )


@app.route('/data/DataCrime' , methods = ['GET' , 'POST'])
def DataCrime():
    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/DataCrime.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.head(101).to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''


    return render_template(
        'DataCrime.html',
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
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )


@app.route('/data/unimploymentrateusa' , methods = ['GET' , 'POST'])
def UnimploymentRate():
    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/unimploymentrateusa.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.head(101).to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''



    return render_template(
        'UnimploymentRateUsa.html',
        title='Unimployment Rate Page',
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
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )


@app.route('/Query', methods=['GET', 'POST'])
def Query():

    Name = None
    Country = ''
    capital = ''
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/capitals.csv'))
    df = df.set_index('Country')
    
    
    form = QueryFormStructure(request.form)
     
    if (request.method == 'POST' ):
        name = form.name.data
        Country = name
        if (name in df.index):
            capital = df.loc[name,'Capital']
        else:
            capital = name + ', no such country'
        form.name.data = ''

    df = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/capitals.csv'))

    raw_data_table = df.to_html(classes = 'table table-hover')

    return render_template('Query.html', 
            form = form, 
            name = capital, 
            Country = Country,
            raw_data_table = raw_data_table,
            title='Query Page',
            year=datetime.now().year,
            message='This page will use the web forms to get user input'
        )

# -------------------------------------------------------
# Register new user page
# -------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.Username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.Username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

