from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
import os
from app.schema import PatientData

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace "*" with your Streamlit URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))

@app.get("/")
def home():
    return {"message": "Heart Disease Risk Prediction API"}

@app.post("/predict")
def predict(data: PatientData):
    input_data = np.array([[ 
        data.male, data.age, data.currentSmoker, data.cigsPerDay,
        data.BPMeds, data.prevalentStroke, data.prevalentHyp,
        data.diabetes, data.totChol, data.sysBP,
        data.diaBP, data.BMI, data.heartRate, data.glucose
    ]])

    input_scaled = scaler.transform(input_data)
    probability = model.predict_proba(input_data)[0][1]
    
    return {
        "predicted_risk_probability": float(probability),
        "risk_label": "High Risk" if probability >= 0.4 else "Low Risk"
    }