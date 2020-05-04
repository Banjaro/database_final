from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(400))
    employees = db.relationship('Employee', backref='employer', lazy='dynamic')
    products = db.relationship('Product', backref='producer ', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return'<Company {}>'.format(self.company_name)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(300))
    # Manufacturer ID
    manf_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __repr__(self):
        return '<Product {}'.format(self.name)


# Association table to link employees with the prodcuts that they work on
works_on = db.Table(
    "works_on",
    db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
    db.Column('employee_id', db.Integer, db.ForeignKey('employee.id'))
)


class Employee(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64))
    # Password will be stored as a hash
    password_hash = db.Column(db.String(128))
    current_hours = db.Column(db.Integer, default=0)
    # This can be a dropdown and replace the internal external project dev sections
    job_title = db.Column(db.String(64))
    hourly_wage = db.Column(db.Integer)
    employer_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    product_list = db.relationship(
        'Product', secondary=works_on,
        primaryjoin=(works_on.c.employee_id == id),
        secondaryjoin=(works_on.c.product_id == Product.id),
        backref=db.backref('works_on', lazy='dynamic'), lazy='dynamic'
    )

    def add_hours(self, hours):
        self.current_hours = self.current_hours + hours
        db.session.commit()

    def reset_hours(self):
        self.current_hours = 0
        db.session.commit()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_paycheck(self):
        return (self.current_hours*self.hourly_wage)

    def all_products(self):
        return Product.query.join(
            works_on, (works_on.c.product_id == Product.id)
            ).filter(works_on.c.employee_id == self.id).all()

    def __repr__(self):
        return '<Employee {}>'.format(self.name)


# Used to load users
@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))
