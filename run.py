# this is the main python file that run the application
# this should be created at root level (not inside a folder)


import os
from taskmanager import app

#if there is a match, retrieve the environmental variables
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )



