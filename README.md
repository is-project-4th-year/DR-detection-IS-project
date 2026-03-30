# TazamaDR :Diabetic Retinopathy Detection Project

## Overview
This project is a web-based application designed to assist in the detection of Diabetic Retinopathy (DR) using deep learning models. The application allows users to upload fundus images, analyze them for signs of DR, and view detailed results, including severity levels and recommendations for further action.

## Features
- **User Authentication:** Secure login and profile management.
- **Image Upload:** Upload fundus images for analysis.
- **DR Detection:** Predicts the severity of Diabetic Retinopathy using a hierarchical model.
- **Analysis History:** View past analyses with filtering options.
- **Detailed Results:** Displays predictions, confidence scores, and recommendations.
- **Permanent Storage:** Uploaded images are stored permanently in the `static/images` folder.

## Technologies Used
- **Backend:** Flask, Flask-Login, SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript
- **Machine Learning:** PyTorch, EfficientNet, ResNet
- **Database:** SQLite (or any SQLAlchemy-supported database)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/is-project-4th-year/DR-detection-IS-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd DR-detection-IS-project
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv drvenv
   source drvenv/Scripts/activate  # On Windows
   source drvenv/bin/activate      # On macOS/Linux
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the database:
   ```bash
   flask db upgrade
   ```
6. Run the application:
   ```bash
   flask run
   ```

## Usage
1. Open the application in your browser at `http://127.0.0.1:5000/`.
2. Register or log in to your account.
3. Upload a fundus image for analysis.
4. View the results, including severity level and recommendations.
5. Access the history page to review past analyses.

## Project Structure
```
DR-detection-IS-project/
├── flask_auth_app/
│   ├── project/
│   │   ├── main.py          # Main application routes
│   │   ├── models.py        # Database models
│   │   ├── model_inference.py # DR prediction logic
│   │   ├── templates/       # HTML templates
│   │   ├── static/          # Static files (CSS, JS, images)
│   └── migrations/          # Database migrations
├── drvenv/                  # Virtual environment
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- Inspired by the need for early detection of Diabetic Retinopathy.
- Special thanks to the contributors and open-source libraries used in this project.
