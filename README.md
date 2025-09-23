# 📊 Customer Churn Prediction

An end-to-end machine learning application that predicts whether a customer will churn (leave) or stay, based on their service usage and demographic data.  
This project demonstrates the full ML lifecycle — from data preprocessing and modeling to deployment and interactive frontend.  


<img width="1777" height="901" alt="Screenshot 2025-09-23 231254" src="https://github.com/user-attachments/assets/f1e8ca3e-d566-4773-a72e-d93a26636a95" />


---

## 🚀 Project Overview

- **Goal:** Predict customer churn for a telecom company.  
- **Dataset:** [Telco Customer Churn (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  
- **Tech Stack:**  
  - Python, Pandas, Scikit-learn  
  - SHAP (model explainability)  
  - FastAPI (model serving)  
  - Docker (containerization)  
  - [Render](https://dashboard.render.com/) (API deployment)  
  - Streamlit + [Hugging Face Spaces](https://huggingface.co/) (interactive demo)  

---

## ⚙️ Features

✅ Train ML models (Logistic Regression, Random Forest, XGBoost)  
✅ Model explainability using **SHAP values**  
✅ REST API with **FastAPI** for real-time predictions  
✅ Interactive **Streamlit app** for demo  
✅ Fully deployed: API on **Render**, Frontend on **Hugging Face Spaces**  

---

## 📂 Project Structure
```
churn-prediction/
│
├── data/ # Dataset
│ ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│ ├── sample_test_data.json
├── models/ # Saved ML model + scaler
│ ├── churn_model.joblib
│ ├── columns.joblib
│ ├── scaler.joblib
├── notebooks/
│ ├── Notebook.ipynb
│ ├── unknown33.py (EDA, training, explainability)
├── src/
│ ├── main.py # FastAPI app
├── streamlit_app.py # Streamlit frontend
├── requirements.txt # Dependencies
└── README.md # Project documentation
```
---

## 🧑‍💻 How to Run Locally

1. Clone the repo:
    ```bash
    git clone https://github.com/Legacywave1/churn-prediction.git
    ch churn-prediction
2. Create and activate environment
   ```bash
   python -m venv venv
   source venv/bin/activate #MAC/Linus
   venv/Scripts/activate #Windows
3. Install dependencies
    ```bash
   pip install -r requirements.txt
4. Run Fast API
    ```bash
   uvicorn src.main:app --reload
   API will be available at: http://127.0.0.1:8000/docs
5. Run streamlit app
   ```bash
   streamlit run streamlit_app.py
   
## 🌐 Live Demo
* FastAPI(Render): https://churn-prediction-rlu7.onrender.com/
* Streamlit(Hugging Face Spaces): https://huggingface.co/spaces/Cyprian121/Churn-Prediction

## 🧪 Example Prediction
Request(JSON):

  ```bash
{
  "SeniorCitizen": 0.0,
  "tenure": 1.0,
  "MonthlyCharges": 80.0,
  "TotalCharges": 0.0,
  "gender_Male": 0.0,
  "Partner_Yes": 0.0,
  "Dependents_Yes": 0.0,
  "PhoneService_Yes": 0.0,
  "MultipleLines_No phone service": 0.0,
  "MultipleLines_Yes": 0.0,
  "InternetService_Fiber optic": 1.0,
  "InternetService_No": 0.0,
  "OnlineSecurity_No internet service": 0.0,
  "OnlineSecurity_Yes": 0.0,
  "Contract_Month-to-month": 1.0,
  "PaymentMethod_Electronic check": 1.0
}
```
Response(JSON)
```bash
{
  "churn_prediction": 1,
  "churn_probability": 0.86
}
```

## 📊 Explainability (SHAP)
The model highlights key features influencing churn such as:
* Contract type
* Monthly charges
* Tenure
* Internet service type


  <img width="798" height="940" alt="SHAP" src="https://github.com/user-attachments/assets/3fbf61df-e9e3-4c2f-b3f3-d5c01f4a4bad" />



## 📄 Resume Highlights
* Built an end-to-end Customer Churn Prediction System using Python, scikit-learn, and SHAP.
* Deployed a FastAPI microservice with Docker on Render for real-time predictions.
* Developed an interactive Streamlit frontend and hosted it on Hugging Face Spaces.
* Implemented explainable AI (XAI) with SHAP to highlight customer risk factors.

## 🙌 Acknowledgements
* Dataset: Kaggle - [Telco customer churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
* Hugging Face Spaces for hosting Streamlit apps.
* Render for free API deployment.
---

