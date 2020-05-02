from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


f_table = db.Table(
    "f_table",
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class Company(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(64), index=True, unique=True)
    # Password will be stored as a hash
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # I'm a reference, delete me later!
    # tbd
    # followed = db.relationship(
    #     'User', secondary=f_table,
    #     primaryjoin=(f_table.c.follower_id == id),
    #     secondaryjoin=(f_table.c.followed_id == id),
    #     backref=db.backref('followers', lazy='dynamic'),
    #     lazy='dynamic'
    # )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            f_table.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        following = Post.query.join(
            f_table, (f_table.c.followed_id == Post.user_id))\
                .filter(f_table.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return following.union(own).order_by(Post.timestamp.desc())

    def __repr__(self):
        return'<User {}>'.format(self.username)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Product(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(300))

    def __repr__(self):
        return '<Product {}'.format(self.name)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
