from flask import render_template, request, redirect, url_for # for use some flask functionality
from taskmanager import app, db
from taskmanager.models import Category, Task # then create taskmanager database: enter python3 and commands: "from taskmanager import db" then "db.create_all()"

#For simplicity to get the app running, we'll create a basic app route using the root-level directory of slash.
#This will be used to target a function called 'home', which will just return the rendered_template
@app.route("/")
def home():
    return render_template("task.html")

# this will link the categories.html with a function with the same name
@app.route("/categories")
def categories():
    return render_template("categories.html")


# this will link the add_categories.html with a function with the same name
# get and post methods are required for the form submitted in the database
# when user click to add a new category, it should render the template 
#the process above uses the GET method to get the page to render
# when the customer submit a form, the POST method will push data to the database
# for this reason we need to specify both methods
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST": #this is the post method 
        category = Category(category_name=request.form.get("category_name")) #category name must be the same as the models.py
        db.session.add(category)
        db.session.commit() #commit to seqlalchemy database
        return redirect(url_for("categories")) #redirect to the categories.html page
    return render_template("add_category.html") #this is the get method that render the basic template