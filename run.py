#!/usr/bin/python3
from app import app, db
from app.models import Company, Employee, Product

# This is the script that kickstarts the whole operation
# Run it to get started

# "flask shell" in termial to get into python environment with
#   db specific moduels already imported
@app.shell_context_processor
def make_shell_context():
    return{
        'db': db,
        'Company': Company,
        'Employee': Employee,
        'Product': Product
        }


if __name__ == "__main__":
    app.run(debug=True)
