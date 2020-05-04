# Team corporate sellout
# These are all of the views for the application


from app import app, db
from app.forms import EmployeeLoginForm,\
    EmployeeRegistrationForm, EditEmployeeForm, AddHourForm,\
    ProductForm, CompanyForm, ProductEmpForm
from app.models import Company, Employee, Product
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = EmployeeLoginForm()
    if form.validate_on_submit():
        user = Employee.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            return redirect(url_for('home'))
        next_page = url_for('home')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/addproduct/<company>', methods=['GET', 'POST'])
def add_product(company):
    compname = Company.query.filter_by(company_name=company).first()
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            description=form.description.data,
            manf_id=form.company.data
        )
        db.session.add(product)
        db.session.commit()
        flash('Successfully added product')
        return redirect(url_for('home'))
    if request.method == 'GET':
        form.company.data = compname.id
    return render_template('add_product.html', form=form)


@app.route('/addcompany', methods=['GET', 'POST'])
def add_company():
    form = CompanyForm()
    if form.validate_on_submit():
        company = Company(
            company_name=form.name.data,
            description=form.description.data
        )
        db.session.add(company)
        db.session.commit()
        flash('Successfully added company')
        return redirect(url_for('home'))
    return render_template('add_company.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = EmployeeRegistrationForm()
    if form.validate_on_submit():
        employee = Employee(
            username=form.username.data,
            name=form.name.data,
            job_title=form.job_type.data,
            hourly_wage=form.hourly.data,
            employer_id=form.company.data
            )
        employee.set_password(form.password.data)
        db.session.add(employee)
        db.session.commit()
        flash('Account registered successfully')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.route('/employee/<username>', methods=['GET', 'POST'])
@login_required
def employee(username):
    form = AddHourForm()
    user = Employee.query.filter_by(username=username).first_or_404()
    if form.validate_on_submit():
        current_user.add_hours(form.hours.data)
        return redirect(url_for('employee', username=username))
    return render_template('employee.html', user=user, form=form)


@app.route('/add_product_to/<username>', methods=['GET', 'POST'])
@login_required
def add_product_to(username):
    form = ProductEmpForm()
    if form.validate_on_submit():
        product = Product.query.filter_by(name=form.name.data).first()
        current_user.add_product(product)
        flash("You are working on a new product")
        redirect(url_for('employee', username=username))
    return render_template('add_product_employee.html', form=form)


@app.route('/remove_product_to/<username>', methods=['GET', 'POST'])
@login_required
def remove_product_to(username):
    form = ProductEmpForm()
    if form.validate_on_submit():
        product = Product.query.filter_by(name=form.name.data).first()
        current_user.remove_product(product)
        flash("You are no longer working on that product")
        redirect(url_for('employee', username=username))
    return render_template('add_product_employee.html', form=form)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditEmployeeForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.set_password(form.password.data)
        db.session.commit()
        flash('Changes Saved')
        return redirect(url_for('employee', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
    return render_template('edit_profile.html', form=form)


@app.route('/company/<company>')
def company(company):
    current_company = Company.query.filter_by(company_name=company).first()
    return render_template(
        'company.html', company=current_company)


@app.route('/company_explore')
def company_explore():
    companies = Company.query.all()
    return render_template('company_explore.html', companies=companies)


@app.route('/deletee/<username>', methods=['GET', 'POST'])
def deletee(username):
    employee = Employee.query.filter_by(username=username).first()
    if employee is None:
        flash('Employee {} not found.'.format(username))
        return redirect(url_for('home'))
    db.session.delete(employee)
    db.session.commit()
    logout_user()
    return redirect(url_for('home'))


@app.route('/deletec/<company_name>', methods=['GET', 'POST'])
def deletec(company_name):
    company = Company.query.filter_by(company_name=company_name).first()
    if company is None:
        flash('Company {} not found.'.format(company_name))
        return redirect(url_for('home'))
    db.session.delete(company)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/deletep/<product_name>', methods=['GET', 'POST'])
def deletep(product_name):
    company = Product.query.filter_by(name=product_name).first()
    if company is None:
        flash('Product {} not found.'.format(product_name))
        return redirect(url_for('home'))
    db.session.delete(company)
    db.session.commit()
    return redirect(url_for('home'))
