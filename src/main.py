from fastapi import FastAPI
import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "churn_model.joblib")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.joblib")
COLUMN_PATH = os.path.join(BASE_DIR, "models", "columns.joblib")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
column = joblib.load(COLUMN_PATH)

app = FastAPI()

@app.post("/predict")
def predict(features: dict):
    df = pd.DataFrame([features])
    
    # Ensure columns are aligned to training order
    df = df.reindex(columns=column, fill_value=0)
    
    # Scale numeric columns (must be in same order as training)
    numeric_cols = ["SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges"]
    df[numeric_cols] = scaler.transform(df[numeric_cols])
    
    # Predict
    pred = model.predict(df)
    prob = model.predict_proba(df)[:, 1]
    
    return {
        "churn_prediction": int(pred[0]),
        "churn_probability": float(prob[0])
    }