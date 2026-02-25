import streamlit as st
import requests

st.set_page_config(page_title="Heart Disease Risk Predictor")

st.title("❤️ Heart Disease Risk Prediction")
st.write("Enter patient details below to estimate 10-year CHD risk.")

# --- INPUT FIELDS ---
male = st.selectbox("Gender (Male=1, Female=0)", [0, 1])
age = st.number_input("Age", min_value=20, max_value=100, value=50)
currentSmoker = st.selectbox("Current Smoker", [0, 1])
cigsPerDay = st.number_input("Cigarettes per Day", min_value=0, max_value=100, value=0)
BPMeds = st.selectbox("On BP Medication", [0, 1])
prevalentStroke = st.selectbox("History of Stroke", [0, 1])
prevalentHyp = st.selectbox("Hypertension", [0, 1])
diabetes = st.selectbox("Diabetes", [0, 1])
totChol = st.number_input("Total Cholesterol", min_value=100, max_value=600, value=200)
sysBP = st.number_input("Systolic BP", min_value=80, max_value=300, value=120)
diaBP = st.number_input("Diastolic BP", min_value=50, max_value=200, value=80)
BMI = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
heartRate = st.number_input("Heart Rate", min_value=40, max_value=200, value=70)
glucose = st.number_input("Glucose", min_value=50, max_value=500, value=90)

if st.button("Predict Risk"):

    data = {
        "male": male,
        "age": age,
        "currentSmoker": currentSmoker,
        "cigsPerDay": cigsPerDay,
        "BPMeds": BPMeds,
        "prevalentStroke": prevalentStroke,
        "prevalentHyp": prevalentHyp,
        "diabetes": diabetes,
        "totChol": totChol,
        "sysBP": sysBP,
        "diaBP": diaBP,
        "BMI": BMI,
        "heartRate": heartRate,
        "glucose": glucose
    }

    API_URL = "https://your-backend-name.onrender.com/predict"

    try:
        response = requests.post(API_URL, json=data, timeout=30)

        result = response.json()

        probability = result["predicted_risk_probability"]
        label = result["risk_label"]

        st.subheader("Prediction Result")

        if label == "High Risk":
            st.error(f"High Risk ⚠️\nProbability: {probability:.2f}")
        else:
            st.success(f"Low Risk ✅\nProbability: {probability:.2f}")
    
    except Exception as e:
        st.error(f"API Error: {e}")