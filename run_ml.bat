@echo off
python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install tensorflow opencv-python pandas scikit-learn tf-keras
python ml_pipeline\train.py
