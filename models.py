from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    mobile = db.Column(db.String(10), unique=True)
    aadhaar = db.Column(db.String(12))
    pan = db.Column(db.String(10))
    bank_account = db.Column(db.String(20))
    ifsc = db.Column(db.String(11))
    role = db.Column(db.String(20))  # 'user' or 'developer'
    aadhaar_image = db.Column(db.String(100))
    live_image = db.Column(db.String(100))

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    status = db.Column(db.String(20))  # pending, approved, rejected
    interest_rate = db.Column(db.Float)
    total_due = db.Column(db.Float)
