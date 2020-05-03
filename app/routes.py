from app import app, db
from app.forms import EmployeeLoginForm,\
     EmployeeRegistrationForm, EditEmployeeForm
# PostForm
from app.models import Company, Employee, Product
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = EmployeeRegistrationForm()
    if form.validate_on_submit():
        employee = Employee(
            username=form.username.data,
            name=form.name.data,
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


@app.route('/employee/<username>')
@login_required
def employee(username):
    user = Employee.query.filter_by(username=username).first_or_404()
    return render_template('employee.html', user=user)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditEmployeeForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.set_password(form.password.data)
        db.session.commit()
        flash('Changes Saved')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
    return render_template('edit_profile.html', form=form)


# @app.route('/follow/<username>')
# @login_required
# def follow(username):
#     user = User.query.filter_by(username=username).first()
#     if user is None:
#         flash('User {} not found.'.format(username))
#         return redirect(url_for('home'))
#     if user == current_user:
#         flash('You cannot follow yourself.')
#         return redirect(url_for('user', username=username))
#     current_user.follow(user)
#     db.session.commit()
#     flash('You are now following {}'.format(username))
#     return redirect(url_for('user', username=username))


# @app.route('/unfollow/<username>')
# @login_required
# def unfollow(username):
#     user = User.query.filter_by(username=username).first()
#     if user is None:
#         flash('User {} not found.'.format(username))
#         return redirect(url_for('home'))
#     if user == current_user:
#         return redirect(url_for('user', username=username))
#     current_user.unfollow(user)
#     db.session.commit()
#     flash('You are no longer following {}'.format(username))
#     return redirect(url_for('user', username=username))


# @app.route('/explore')
# def explore():
#     posts = Post.query.order_by(Post.timestamp.desc()).all()
#     return render_template('home.html', title='Explore', posts=posts)
