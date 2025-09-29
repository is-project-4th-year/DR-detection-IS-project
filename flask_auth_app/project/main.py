from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template(
        'profile.html',
        first_name=current_user.first_name,
        last_name=current_user.last_name
    )

@main.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    recent_images = [
        {"name": "Fundus Image 1", "uploaded": "2025-09-01", "status": "Analyzed"},
        {"name": "Fundus Image 2", "uploaded": "2025-08-30", "status": "Pending"},
        {"name": "Fundus Image 3", "uploaded": "2025-08-28", "status": "Error"},
    ]
    if request.method == 'POST':
        # handle file upload here
        flash('Image uploaded successfully!')
        return redirect(url_for('main.upload'))
    return render_template('upload.html', recent_images=recent_images)

