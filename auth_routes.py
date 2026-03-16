from flask import Blueprint, request, redirect, render_template
from app.models import User
from app import db
from app.utils.face_match import save_and_compare
import os

bp = Blueprint('auth', __name__)

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        file = request.files['aadhaar_image']
        aadhaar_path = f"uploads/{file.filename}"
        file.save(aadhaar_path)

        verified = save_and_compare(aadhaar_path, request.form['live_photo'])

        if not verified:
            return "Face mismatch. Try again."

        user = User(
            name=request.form['name'],
            mobile=request.form['mobile'],
            aadhaar=request.form['aadhaar'],
            pan=request.form['pan'],
            bank_account=request.form['bank_account'],
            ifsc=request.form['ifsc'],
            role='user',
            aadhaar_image=aadhaar_path,
            live_image='temp_live.jpg'
        )
        db.session.add(user)
        db.session.commit()
        return redirect("/dashboard")
    return render_template("register.html")
