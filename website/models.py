from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    data2 = db.Column(db.String(10000))
    data3 = db.Column(db.String(10000))
    state1 = db.Column(db.String(20))
    state2 = db.Column(db.String(20))
    state3 = db.Column(db.String(20))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    date2 = db.Column(db.String(20))
    date3 = db.Column(db.DateTime(timezone=True))
    date4 = db.Column(db.DateTime(timezone=True))
    date5 = db.Column(db.String(20))
    sign1 = db.Column(db.String(150))
    sign2 = db.Column(db.String(150))
    sign3 = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    admin2=db.Column(db.String(12))
    department2=db.Column(db.String(12))
    unit2=db.Column(db.String(12))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    admin=db.Column(db.String(12),default="")
    department=db.Column(db.String(12))
    engineer=db.Column(db.String(12))
    unit=db.Column(db.String(12))
    shift=db.Column(db.String(12))
    notes = db.relationship('Note')