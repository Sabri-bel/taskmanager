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
    # retrieve the categorylisted in the database and display them
    # 1 query the Category model imported at the beginning (category.query.all())
    # 2 add to the category model the sorting method order_by() for retrieve information added later
    # 3 sorting by category_name 
    # add the list() python function because .all return a cursor object that cannot be rendered correctly with the fromt end templates
    categories = list(Category.query.order_by(Category.category_name).all())
    #categories=categories -> first one is the name of the html file and the second one is the name of the variable specified above
    return render_template("categories.html", categories=categories)


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


# this function will allow the user to edit a category
#the category id is required because we specified that in the categories.html file
#it must be wrapped with the angle brackets and specify int for the integer result
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id) # get_or_404 is a sqlalchemy method
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category) # return the basic template 



#this is the fucntion for delete categories
#it is important to add a defensive code because it will delete all data from the database
#it is also important to add a sign in in order to avoid random people mess up with the code 
@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    # add the list() python function because .all return a cursor object that cannot be rendered correctly with the fromt end templates
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST": #this is the post method 
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit() #commit to seqlalchemy database
        return redirect(url_for("home")) #redirect to the categories.html page
    return render_template("add_task.html", categories=categories) #this is the get method that render the basic template
