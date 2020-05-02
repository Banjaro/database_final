#!/usr/bin/python3
from app import app, db
from app.models import User, Post

# This is the script that kickstarts the whole operation
# Run it to get started

# "flask shell" in termial to get into python environment with
#   db variables already imported
@app.shell_context_processor
def make_shell_context():
    return{'db': db, 'User': User, 'Post': Post}


if __name__ == "__main__":
    app.run(debug=True)
