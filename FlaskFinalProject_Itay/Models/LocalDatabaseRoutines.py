"""
Used structures and classes
"""
from os import path
import json
import pandas as pd

def create_LocalDatabaseServiceRoutines():
    return LocalDatabaseServiceRoutines()

class LocalDatabaseServiceRoutines(object):
    def __init__(self):
        self.name = 'Data base service routines'
        self.index = {}
        self.UsersDataFile = path.join(path.dirname(__file__), '..//static/data/users.csv')

# -------------------------------------------------------
# Read users data into a dataframe
# -------------------------------------------------------
    def ReadCSVUsersDB(self):
        df = pd.read_csv(self.UsersDataFile)
        return df

# -------------------------------------------------------
# Saves the DataFrame (input parameter) into the users csv
# -------------------------------------------------------
    def WriteCSVToFile_users(self, df):
        df.to_csv(self.UsersDataFile, index=False)

# -------------------------------------------------------
# Check if username is in the data file
# -------------------------------------------------------
    def IsUserExist(self, Username):
        # Load the database of users
        df = self.ReadCSVUsersDB()
        df = df.set_index('Username')
        return (Username in df.index.values)

# -------------------------------------------------------
# return boolean if username/password pair is in the DB
# -------------------------------------------------------
    def IsLoginGood(self, Username, Password):
        # Load the database of users
        df = self.ReadCSVUsersDB()
        df=df.reset_index()
        selection = [Username]
        df = df[pd.DataFrame(df.Username.tolist()).isin(selection).any(1)]

        df = df.set_index('Password')
        return (Password in df.index.values)
     
# -------------------------------------------------------
# Add a new user to the DB
# -------------------------------------------------------
    def AddNewUser(self, User):
        # Load the database of users
        df = self.ReadCSVUsersDB()
        dfNew = pd.DataFrame([[User.FirstName.data, User.LastName.data, User.PhoneNum.data, User.EmailAddr.data, User.Username.data, User.Password.data]], columns=['FirstName', 'LastName', 'PhoneNum', 'EmailAddr',  'Username', 'Password'])
        dfComplete = df.append(dfNew, ignore_index=True)
        self.WriteCSVToFile_users(dfComplete)