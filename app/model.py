from app import db
from flask_security import UserMixin, RoleMixin

# Models for logging in
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    # confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class BulkUpload(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True)
    uploaded_time = db.Column(db.DateTime())
    uploaded_file = db.Column(db.String(1024))
    current_status = db.Column(db.Integer())
    errorfile = db.Column(db.String(1024))

class NewHireStudent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uin = db.Column(db.BigInteger)
    name = db.Column(db.String(1024))
    email = db.Column(db.String(1024))
    department = db.Column(db.String(1024))
    term = db.Column(db.String(1024))
    year = db.Column(db.Integer)
    position = db.Column(db.String(1024))
    fte = db.Column(db.Integer)
    stipend = db.Column(db.Float)
    begin_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    jd = db.Column(db.String(1024))
    orientation = db.Column(db.String(1024))
    orientation_date = db.Column(db.DateTime)
    orientation_loc = db.Column(db.String(1024))
    supervisor_name = db.Column(db.String(1024))
    supervisor_email = db.Column(db.String(1024))
    supervisor_phone = db.Column(db.String(1024))
    respond_name = db.Column(db.String(1024))
    respond_email = db.Column(db.String(1024))
    respond_date = db.Column(db.Date)
    waiver = db.Column(db.Boolean)
    proficiency = db.Column(db.Boolean)
    international = db.Column(db.Boolean)
    cbc_needed = db.Column(db.Boolean)
    approved = db.Column(db.Boolean)

