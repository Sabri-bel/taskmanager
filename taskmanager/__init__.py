# this file __init__.py ,ake sure to initialize the taskmanager app as a package
# allowing to use the imports and our own imports 

import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# the below code will import env if the env file is present in the path (this is not committed)
# this is for use the hidden environmental variables
if os.path.exists("env.py"):
    import env #noqa -> no quality assurance



# create an instance of the flask() class imported, stored in a variable called app
app = Flask(__name__)
# specify the app configuration 
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# create an instancce for the sqlalchemy() class imported, stored in a cariable called db

db = SQLAlchemy(app) # argument is the flask variable above


# this import must be performed after the instances, if not it will throw an error
from taskmanager import routes #noqa -> no quality assurance

