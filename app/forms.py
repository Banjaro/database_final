from app.models import Employee
from flask_wtf import FlaskForm
from wtforms import StringField, \
    PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,\
     EqualTo, Email, ValidationError, Length


class EmployeeLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class CompanyLoginForm(FlaskForm):
    company_id = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class EmployeeRegistrationForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    company = StringField(
        'Employer Company ID',
        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordcheck = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Employee.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please pick a different username.')

    def validate_email(self, email):
        email = Employee.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('This email address is already in use.')


class EditEmployeeForm(FlaskForm):
    username = StringField('New Username')
    password = PasswordField('New Password', validators=[Length(min=1)])
    submit = SubmitField('Save Changes')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')
