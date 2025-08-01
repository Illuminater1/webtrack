from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ..db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50), unique=True)

    def __rept__(self):
        return f'User {self.username}'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def check_password(self, password):
        return check_password_hash(self.password, password)
