# These are all of the forms that are used for various things
#  around the website

from app.models import Employee, Company, Product
from flask_wtf import FlaskForm
from wtforms import StringField, \
    PasswordField, BooleanField, SubmitField, TextAreaField,\
    IntegerField, SelectField
from wtforms.validators import DataRequired,\
     EqualTo, ValidationError, Length


class EmployeeLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


jobtypes = [
    ('internal', 'Internal Affairs'),
    ('external', 'External Affairs'),
    ('dev', 'Development')
]


# Form to register new employee
class EmployeeRegistrationForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    company = StringField(
        'Employer ID',
        validators=[DataRequired()])
    job_type = SelectField(
        'Job Type', choices=jobtypes,
        validators=[DataRequired()])
    hourly = IntegerField('Hourly Wage', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    passwordcheck = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Employee.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please pick a different username.')

    def validate_company(self, company):
        check = Company.query.get(int(company.data))
        if check is None:
            raise ValidationError('Please use an existing company ID')


# Used to get all the products for the selectField
query = Product.query.all()
choices = [("", "")]
for item in query:
    thing = (item.name, item.name)
    choices.append(thing)


# Form to add product to employee
class ProductEmpForm(FlaskForm):
    name = SelectField("Product", choices=choices)
    submit = SubmitField('Add Product')


# New company form
class CompanyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Create New Company')

    def validate_name(self, name):
        company = Company.query.filter_by(company_name=name.data).first()
        if company is not None:
            raise ValidationError('Company name already in use')


# New product registration form
class ProductForm(FlaskForm):
    name = StringField("Name")
    description = TextAreaField("Description")
    company = IntegerField("Manufacturer ID")
    submit = SubmitField('Create New Product')

    def validate_company(self, company):
        check = Company.query.get(int(company.data))
        if check is None:
            raise ValidationError('Please use an existing company ID')


# Form to add hours to employee
class AddHourForm(FlaskForm):
    hours = IntegerField('Add Hours')
    submit = SubmitField('GO')


# Form to edit employee
class EditEmployeeForm(FlaskForm):
    username = StringField('New Username')
    password = PasswordField('New Password', validators=[Length(min=1)])
    submit = SubmitField('Save Changes')
