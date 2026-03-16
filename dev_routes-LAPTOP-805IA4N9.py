from flask import Blueprint, render_template
from flask_login import login_required, current_user

dev_bp = Blueprint('dev', __name__)

@dev_bp.route('/developer-tools')
@login_required
def developer_tools():
    if current_user.role != 'dev':
        return "Unauthorized", 403
    return render_template('dev_dashboard.html')
