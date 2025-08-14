# app/main.py

from fastapi import FastAPI
from app.schemas import HeartDiseaseInput, PredictionOutput
import joblib
import numpy as np

# Load the model once at startup
model = joblib.load("model/heart_disease_model.joblib")

# Heart disease class names for readability
class_names = [0, 1]

# Create FastAPI app
app = FastAPI(
    title="Heart Disease Prediction API",
    description="API for predicting heart disease using FastAPI",
    version="1.0"
)

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "API is running"}

@app.get("/info")
def model_info():
    """Basic model info"""
    return {
        "model_type": "RandomForestClassifier",
        "classes": class_names
    }

@app.post("/predict", response_model=PredictionOutput)
def predict_heart_disease(data: HeartDiseaseInput):
    """Make prediction from input features"""
    features = np.array([[data.age, data.sex, data.cp, data.trestbps, data.chol, data.fbs, data.restecg, data.thalach, data.exang, data.oldpeak, data.slope, data.ca, data.thal]])
    prediction = model.predict(features)[0]
    predicted_class = class_names[prediction]
    return {"predicted_class": predicted_class}
