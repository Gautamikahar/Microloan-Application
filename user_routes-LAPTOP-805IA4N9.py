from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Loan

user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'dev':
        return redirect(url_for('user.dev_dashboard'))
    return redirect(url_for('user.user_dashboard'))

@user_bp.route('/user-dashboard')
@login_required
def user_dashboard():
    return render_template('user_dashboard.html', name=current_user.username)

@user_bp.route('/dev-dashboard')
@login_required
def dev_dashboard():
    return render_template('dev_dashboard.html', name=current_user.username)

@user_bp.route('/apply-loan', methods=['GET', 'POST'])
@login_required
def apply_loan():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        purpose = request.form['purpose']
        loan = Loan(amount=amount, purpose=purpose, user_id=current_user.id)
        db.session.add(loan)
        db.session.commit()
        return redirect(url_for('user.view_loans'))
    return render_template('apply_loan.html')

@user_bp.route('/my-loans')
@login_required
def view_loans():
    loans = Loan.query.filter_by(user_id=current_user.id).all()
    return render_template('my_loan.html', loans=loans)
