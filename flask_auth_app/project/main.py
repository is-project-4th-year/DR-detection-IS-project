from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
import os
import datetime

# Import your model inference functions
from .model_inference import load_model, predict_image

main = Blueprint('main', __name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model once at startup
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'dr_model.pth')
model = load_model(MODEL_PATH)

# Store recent images in a simple list (for demo; use DB for production)
recent_images = []

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
    global recent_images
    prediction = None
    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename:
            filename = file.filename
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            pred_class = predict_image(filepath, model)
            class_names = ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative']
            prediction = f"Prediction: {class_names[pred_class]}"
            # Add to recent images (keep only last 4)
            recent_images.insert(0, {
                "name": filename,
                "uploaded": "Now",
                "status": "Analyzed",
                "img_url": url_for('static', filename=f'uploads/{filename}'),
                "prediction": class_names[pred_class]
            })
            recent_images = recent_images[:4]
        else:
            flash('No file selected!')
    return render_template('upload.html', recent_images=recent_images, prediction=prediction)

@main.route('/results/<filename>')
@login_required
def view_results(filename):
    # Find the image in recent_images (or fetch from DB in production)
    img = next((img for img in recent_images if img["name"] == filename), None)
    if not img:
        flash("Image not found.")
        return redirect(url_for('main.upload'))
    # Example: pass recommendations and other details
    recommendations = [
        {"priority": "High", "title": "Consult an Ophthalmologist", "desc": "Schedule a comprehensive eye exam..."},
        {"priority": "Medium", "title": "Monitor Blood Sugar Levels", "desc": "Maintain strict glycemic control..."},
        {"priority": "Low", "title": "Patient Education", "desc": "Read more about managing diabetic retinopathy..."}
    ]
    return render_template('results.html', img=img, recommendations=recommendations)

