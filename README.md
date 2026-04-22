# Brain Tumor Detection Web App

## Overview
Flask web application for detecting brain tumors from MRI images using a pre-trained deep learning model (Keras/TensorFlow). Features image upload, prediction, and basic auth (signup/login).

## Prerequisites
- Python 3.8 (64-bit)
- Visual C++ Redistributable (for TensorFlow on Windows):
  [Download x64](https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0) → vc_redist.x64.exe

## Setup & Execution Instructions (Windows CMD)

1. **Open Command Prompt (CMD)**:
   - Press `Win + R`, type `cmd`, Enter.

2. **Navigate to project directory**:
   ```
   cd /d "c:\Users\Vinay\OneDrive\MPIP06-20250613T114624Z-1-001\MPIP06"
   ```

3. **Create & activate virtual environment** (recommended):
   ```
   python -m venv venv
   venv\Scripts\activate.bat
   ```
   Prompt changes to `(venv)`.

4. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```
   python app_fixed.py
   ```
   - Look for: `Model loaded successfully`
   - Server starts at `http://127.0.0.1:5000` or `http://localhost:5000`

6. **Access the app**:
   - Open browser: http://localhost:5000
   - Signup/Login → /index → Upload MRI image → Get prediction.

## Routes
- `/` or `/first`: Landing
- `/index`: Upload & Predict
- `/login`, `/signup`: Auth
- `/chart`, `/performance`: Pages

## Troubleshooting
- TF warnings: Normal, ignore.
- Model load slow: ~100MB, first run compiles.
- Image: Use MRI scans (224x224 resized).
- Stop server: Ctrl+C

## Files
- `app_fixed.py`: Main Flask app
- `save.h5`: Trained model
- `templates/`: HTML
- `static/`: CSS/JS/Images
- `requirements.txt`: Deps

Enjoy detecting brain tumors safely!
