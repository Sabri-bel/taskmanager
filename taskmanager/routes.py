from flask import render_template # for use some flask functionality
from taskmanager import app, db

#For simplicity to get the app running, we'll create a basic app route using the root-level directory of slash.
#This will be used to target a function called 'home', which will just return the rendered_template
@app.route("/")
def home():
    return render_template("base.html")