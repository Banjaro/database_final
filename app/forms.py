from app.models import Employee, Company
from flask_wtf import FlaskForm
from wtforms import StringField, \
    PasswordField, BooleanField, SubmitField, TextAreaField,\
    IntegerField, SelectField
from wtforms.validators import DataRequired,\
     EqualTo, Email, ValidationError, Length


class EmployeeLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


jobtypes = [
    ('internal', 'Internal Affairs'),
    ('external', 'External Affairs'),
    ('dev', 'Development')
]


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


class CompanyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Create New Company')

    def validate_company_name(self, company_name):
        company = Company.query.filter_by(company_name=company_name).first()
        if company is not None:
            raise ValidationError('Company name already in use')


class ProductForm(FlaskForm):
    name = StringField("Name")
    description = StringField("Description")
    company = IntegerField("Manufacturer ID")
    submit = SubmitField('Create New Product')

    def validate_company(self, company):
        check = Company.query.get(int(company.data))
        if check is None:
            raise ValidationError('Please use an existing company ID')


class AddHourForm(FlaskForm):
    hours = IntegerField('Add Hours')
    submit = SubmitField('GO')


class EditEmployeeForm(FlaskForm):
    username = StringField('New Username')
    password = PasswordField('New Password', validators=[Length(min=1)])
    submit = SubmitField('Save Changes')
