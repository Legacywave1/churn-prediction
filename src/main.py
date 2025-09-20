from fastapi import FastAPI
import joblib
import pandas as pd

model = joblib.load('/workspaces/churn-prediction/models/churn_model.joblib')
scaler = joblib.load('/workspaces/churn-prediction/models/scaler.joblib')
columns = joblib.load("models/columns.joblib")

app = FastAPI()

@app.post("/predict")
def predict(features: dict):
    df = pd.DataFrame([features])
    
    # Ensure columns are aligned to training order
    df = df.reindex(columns=columns, fill_value=0)
    
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