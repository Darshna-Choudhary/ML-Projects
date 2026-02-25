# ❤️ Heart Disease Risk Prediction (End-to-End ML Deployment)

## 📌 Project Overview

This project predicts the **10-year risk of Coronary Heart Disease (CHD)** using the Framingham Heart Study dataset.

The goal was not only to train a machine learning model, but to build a **complete end-to-end ML system**, including:

- Data preprocessing
- Model tuning
- Handling imbalanced classification
- Threshold optimization
- REST API deployment
- Frontend integration
- Cloud deployment (Render)

---

## 🚀 Live Demo

🔹 **Frontend (Streamlit UI):**  
https://your-frontend-url.onrender.com  

🔹 **Backend API (FastAPI):**  
https://your-backend-url.onrender.com  

---

## 🧠 Problem Statement

Early detection of cardiovascular disease risk is critical.

This project builds a **screening-oriented model** that prioritizes **recall**, reducing false negatives in high-risk patients.

---

## 📊 Dataset

- Source: Framingham Heart Study
- Target Variable: `TenYearCHD`
- Total Features: 14 clinical & lifestyle parameters including:

  - Age  
  - Gender  
  - Blood Pressure (Systolic & Diastolic)  
  - BMI  
  - Total Cholesterol  
  - Glucose  
  - Smoking status  
  - Diabetes  
  - Heart Rate  

## 🧠 Problem Statement

Early detection of cardiovascular risk is crucial.
This project focuses on building a screening-oriented model that prioritizes recall, reducing false negatives in high-risk patients.

## 📊 Dataset

Source: Framingham Heart Study

Target Variable: TenYearCHD

Features: 14 clinical & lifestyle parameters including:
- Age
- Blood Pressure
- BMI
- Cholesterol
- Glucose
- Smoking status
- Diabetes
- Heart rate
etc.

## ⚙️ ML Pipeline

A production-ready Scikit-learn Pipeline was used:

Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("lr", LogisticRegression(max_iter=3000, class_weight="balanced"))
])

## 🔍 Model Optimization
- Train/Test Split (Stratified)
- 5-Fold Cross Validation
- GridSearchCV for hyperparameter tuning

### Evaluation metrics:
- ROC-AUC
- Precision-Recall Curve
- F1 Score
- Confusion Matrix
- Calibration Curve

## 📈 Model Performance
- Metric	Score
- Cross-Validated ROC-AUC	~0.73
- Test ROC-AUC	~0.70
- F1 Score (Positive Class)	~0.35
- Recall (Threshold = 0.4)	~0.77
- Threshold Optimization

Instead of using default 0.5 threshold, a lower threshold (0.4) was chosen to:
- Increase recall
- Reduce false negatives
- Suit screening use-case

## 🔒 Production Considerations
- Preprocessing pipeline saved using joblib
- No data leakage
- Class imbalance handled via class_weight="balanced"
- Proper exception handling in frontend
- Status code validation before JSON parsing


## 🎯 Key Learnings
- Importance of ML pipelines in production
- Handling imbalanced datasets
- Threshold tuning for business objectives
- Cold-start behavior in cloud deployments
- Debugging API errors in live environment
- Separation of frontend and backend services

## 🔮 Future Improvements
- Compare with XGBoost / LightGBM
- Add SHAP interpretability
- Improve calibration
- Add model versioning
- Add monitoring & logging
