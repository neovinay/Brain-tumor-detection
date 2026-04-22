# 🧠 Brain Tumor Detection Web App

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)](https://www.tensorflow.org/)

## Overview
A Flask web application for **detecting brain tumors from MRI images** using a pre-trained Convolutional Neural Network (CNN) model built with Keras/TensorFlow. 

**Key Features:**
- Upload MRI scans (auto-resized to 224x224)
- Binary classification: **Tumor** (with symptoms list) vs **Normal** (safe with precaution)
- **Model Accuracy: 97.7%** (on validation set)
- User authentication (signup/login, in-memory storage)
- Responsive UI with charts, performance pages
- Instant results with confidence probability

**Dataset:** [Kaggle Brain MRI Images for Brain Tumor Detection](https://www.kaggle.com/navoneel/brain-mri-images-for-brain-tumor-detection)

## Model Details
- **Architecture:** CNN with Conv2D (32/32/64 filters), MaxPooling, Dense layers, Softmax output (2 classes).
- **Training:** 5 epochs, Adam optimizer, categorical crossentropy, ImageDataGenerator.
- **Input:** 224x224x3 RGB images.
- **Output:** 
  | Class | Prediction Text |
  |-------|----------------|
  | Tumor (0) | "Result: Brain Tumor Symptoms: unexplained weight loss, ..." |
  | Normal (1) | "You Are Safe, But Do keep precaution" |
- Pre-trained weights: `save.h5` (~100MB)
- Validation: Confusion matrix, Precision/Recall/F1 high.

## Project Structure
```
MPIP06/
├── app.py / app_fixed.py      # Flask apps (use app_fixed.py)
├── requirements.txt           # Dependencies
├── save.h5                    # Trained model
├── model/
│   └── model.ipynb           # Training notebook
├── static/                    # CSS/JS/images (note: consolidate duplicate CSS)
├── templates/                 # Jinja2 HTML
├── upload/                    # Sample MRI images (tumor/normal)
├── README.md
└── TODO.md
```

## Prerequisites
- **Python 3.8+ (64-bit)**
- **Visual C++ Redistributable** (for TensorFlow on Windows): [Download x64 vc_redist.x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe)

## Quick Setup & Run (Windows CMD/PowerShell)

1. **Navigate to project:**
   ```
   cd "c:/Users/Vinay/OneDrive/MPIP06-20250613T114624Z-1-001/MPIP06"
   ```

2. **Virtual Environment (recommended):**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run App:**
   ```
   python app_fixed.py
   ```
   - ✅ "Model loaded successfully"
   - Open: **http://localhost:5000**

5. **Usage Flow:**
   - `/` or `/first` → Signup/Login → `/index` → Upload MRI → **Result page** with prediction/probability/base64 image.

## Routes
| Route | Description |
|-------|-------------|
| `/` `/first` | Landing |
| `/index` | Image upload & predict |
| `/login` `/signup` | Auth |
| `/register` (POST) `/login_verify` (POST) | Auth handlers |
| `/chart` `/performance` | Visualizations |

## Demo
1. Signup (e.g., user:test / pass:test)
2. Login → Index → Upload sample from `upload/`
3. Get prediction like: **Tumor** (97%) or **Safe** (92%)

**Sample Images:** `upload/Brain Tumor/*.png` or `upload/Normal/*.png`

## Troubleshooting
- **Model slow first load:** TF compilation, normal.
- **TensorFlow warnings:** Safe to ignore.
- **Image errors:** Use PNG/JPG MRI scans.
- **Port busy:** Kill processes or `app.run(port=5001)`
- **CSS issues:** Multiple files (styles.css etc.); consider merging.

**Cleanup Suggestion:** Delete duplicate CSS (styl.css, sty.css → use styles.css).

## Deployment Guide

### Option 1: Render.com (Free Tier, Recommended - 5min)
1. **Push to GitHub:**
   - Create repo, commit all files (`.gitignore`: venv/, __pycache__/).
   - `git init; git add .; git commit -m "Initial"; gh repo create brain-tumor-app --public`

2. **Deploy on Render:**
   - Sign up: https://render.com
   - New → Web Service → Connect GitHub repo
   - Settings:
     | Field | Value |
     |-------|-------|
     | Name | brain-tumor-app |
     | Environment | Python 3 |
     | Region | Oregon (free) |
     | Branch | main |
     | Build Command | `pip install -r requirements.txt` |
     | Start Command | `gunicorn app_fixed:app` |
   - Deploy → Live URL in 2min!

3. **Custom Domain (Optional):** Add via Render dashboard.

### Option 2: Heroku (CLI)
1. **Install Heroku CLI:** https://devcenter.heroku.com/articles/heroku-cli
2. **Procfile:** Create `Procfile` (no ext):
   ```
   web: gunicorn app_fixed:app
   ```
3. **requirements.txt:** Ensure `gunicorn` present (already is).
4. **Deploy:**
   ```
   heroku create brain-tumor-app
   git push heroku main
   heroku open
   ```
   - Free dyno: Sleeps after 30min idle.

### Option 3: Railway.app (GitHub → Deploy)
- Similar to Render, auto-detects Python/Flask.

**Notes:**
- Model `save.h5` uploads with repo (~100MB ok).
- In-memory users reset on restart → Use Redis/DB for prod.
- Free tiers: Render/Heroku (1GB RAM sufficient).

**Live Demo Command (after deploy):** Share your Render/Heroku URL!

## Future Improvements
- Persistent DB (SQLite/Flask-Login)
- Multi-model support
- API endpoints (JSON predict)
- Mobile-responsive enhancements

## License
MIT - Feel free to use/modify!

---

*Built with ❤️ for early detection awareness.*


