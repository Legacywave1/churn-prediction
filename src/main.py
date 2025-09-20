from fastapi import FastAPI
import joblib
import pandas as pd

model = joblib.load('/workspaces/churn-prediction/models/churn_model.joblib')
scaler = joblib.load('/workspaces/churn-prediction/models/scaler.joblib')

app = FastAPI()

@app.post('/predict')
def predict(features: dict):
    df = pd.DataFrame([features])
    numeric_col = ["tenure", "MonthlyCharges", "TotalCharges"]
    df[numeric_col] = scaler.transform(df[numeric_col])

    pred = model.predict(df)
    pred_prob = model.predict_proba(df)[:, 1]

    return {
        'Churn prediction': int(pred[0]),
        'Churn probability': int(pred_prob[0])
    }
