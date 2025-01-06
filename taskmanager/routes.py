from flask import render_template, request, redirect, url_for # for use some flask functionality
from taskmanager import app, db
from taskmanager.models import Category, Task # then create taskmanager database: enter python3 and commands: "from taskmanager import db" then "db.create_all()"

#For simplicity to get the app running, we'll create a basic app route using the root-level directory of slash.
#This will be used to target a function called 'home', which will just return the rendered_template
@app.route("/")
def home():
    return render_template("task.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")