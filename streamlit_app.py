import streamlit as st
import requests

API_URL = "https://churn-prediction-rlu7.onrender.com/predict"

st.set_page_config(page_title="Chun Prediction Demo", layout = "centered")

st.title("Customer churn prediction")
st.write("Enter customer details below to predict if they are likely to churn")

senior_citizen = st.number_input("Senior Citizen (0 = No, 1 = Yes)", min_value=0, max_value=1, value=0)
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=600.0)

gender_male = st.selectbox("Gender", ["Female", "Male"]) == "Male"
partner_yes = st.checkbox("Has Partner")
dependents_yes = st.checkbox("Has Dependents")

if st.button("Predict Churn"):
    payload = {
        "SeniorCitizen": senior_citizen,
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "gender_Male": int(gender_male),
        "Partner_Yes": int(partner_yes),
        "Dependents_Yes": int(dependents_yes),
        # TODO: Add other categorical features here...
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            churn_pred = result["churn_prediction"]
            churn_prob = result["churn_probability"]

            st.success(f"Prediction: {'Churn' if churn_pred == 1 else 'Not Churn'}")
            st.info(f"Probability: {churn_prob:.2%}")
        else:
            st.error(f"API Error: {response.status_code} {response.text}")
    except Exception as e:
        st.error(f"Connection failed: {e}")
