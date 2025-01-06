# this is the file that defines the database and we need to import db for that 

from taskmanager import db

# we will create 2 separate tables using sqlalchemy's ORM
# table 1 = category schema
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True) #applied automatically by default
    category_name =  db.Column(db.String(25), unique= True, nullable=False) #need to be collected with the categories.html
    # the following create a relationship between the table category and the table task
    # it allow the cascade when delete the category ID (delete all the field related)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True) #independent task

    def __repr__(self):
        #__Repr__ to repreent iself form of a string
        return self.category_name


#table 2 = task schema
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    
    def __repr__(self):
        #__Repr__ to repreent iself form of a string
        return "##{0} - Task: {1} | Urgent: {2}"
