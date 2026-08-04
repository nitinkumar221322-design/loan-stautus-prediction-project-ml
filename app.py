import streamlit as st
import pandas as pd
import joblib

model = joblib.load("loan_model.pkl")

st.title("🏦 Loan Status Prediction")

no_of_dependents = st.number_input("Number of Dependents", 0, 20, 2)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["No", "Yes"]
)

income_annum = st.number_input("Annual Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term", min_value=1, max_value=50)
cibil_score = st.number_input("CIBIL Score", 300, 900, 650)

residential_assets_value = st.number_input(
    "Residential Assets Value", min_value=0
)

commercial_assets_value = st.number_input(
    "Commercial Assets Value", min_value=0
)

luxury_assets_value = st.number_input(
    "Luxury Assets Value", min_value=0
)

bank_asset_value = st.number_input(
    "Bank Asset Value", min_value=0
)

if st.button("Predict Loan Status"):

    input_data = pd.DataFrame({
        "no_of_dependents": [no_of_dependents],
        "education": [education],
        "self_employed": [self_employed],
        "income_annum": [income_annum],
        "loan_amount": [loan_amount],
        "loan_term": [loan_term],
        "cibil_score": [cibil_score],
        "residential_assets_value": [residential_assets_value],
        "commercial_assets_value": [commercial_assets_value],
        "luxury_assets_value": [luxury_assets_value],
        "bank_asset_value": [bank_asset_value]
    })

    prediction = model.predict(input_data)[0]

    if prediction == "Approved":
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")