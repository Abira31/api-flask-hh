from . import db
from werkzeug.security import generate_password_hash
from sqlalchemy.sql import func
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True)
)

job_skills = db.Table(
    'job_skills',
    db.Column('skills_id', db.Integer, db.ForeignKey('skills.id'), primary_key=True),
    db.Column('resume_id', db.Integer, db.ForeignKey('resume.id'), primary_key=True)
)
user_resumes = db.Table(
    'user_resumes',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('resume_id', db.Integer, db.ForeignKey('resume.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),nullable=False,unique=True)
    password = db.Column(db.String(120),nullable=False)
    is_active = db.Column(db.Boolean(),nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    # resumes = db.relationship('Resume', secondary=user_resumes, lazy='subquery', backref=db.backref('user_resumes', lazy=True))
    roles = db.relationship('Role', secondary=roles_users, lazy='subquery', backref=db.backref('user_roles', lazy=True))
    is_admin = db.Column(db.Boolean, default=False)

    # def __init__(self,email,password,first_name,last_name,phone,roles=None,active=True,is_admin=False):
    #     self.email = email
    #     self.password = generate_password_hash(password)
    #     self.active = active
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     # self.resumes = resumes
    #     # if not resumes:
    #     #     self.resumes = []
    #     # else:
    #     #     self.resumes = resumes

    #     self.phone = phone
    #     if not roles:
    #         self.roles = []
    #     else:
    #         self.roles = roles
    #     self.is_admin = is_admin

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120), nullable=False)

class Vacancy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    vacancy = db.relationship('Resume', backref='job_vacancy',lazy=True)

class Skills(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_vacancy_id = db.Column(db.Integer, db.ForeignKey('vacancy.id'))
    salary = db.Column(db.Integer(),nullable=False)
    description = db.Column(db.String(120), nullable=False)
    skills = db.relationship('Skills', secondary=job_skills, lazy='subquery', backref=db.backref('resume_skills', lazy=True))
    publication_date = db.Column(db.DateTime(timezone=True),default=func.now())
    is_active = db.Column(db.Boolean(), nullable=False)

