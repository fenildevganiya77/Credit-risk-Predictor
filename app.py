import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model/model.pkl")

st.set_page_config(
    page_title="Credit Risk Predictor",
    page_icon="💳"
)

st.title("💳 Credit Risk Prediction System")

st.write(
    "Predict whether a loan applicant is likely to default."
)

person_age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=25
)

person_income = st.number_input(
    "Annual Income",
    min_value=0.0
)

person_home_ownership = st.selectbox(
    "Home Ownership",
    ["OWN", "RENT", "MORTGAGE", "OTHER"]
)

person_emp_length = st.number_input(
    "Employment Length (Years)",
    min_value=0.0
)

loan_intent = st.selectbox(
    "Loan Purpose",
    [
        "EDUCATION",
        "MEDICAL",
        "PERSONAL",
        "VENTURE",
        "HOMEIMPROVEMENT",
        "DEBTCONSOLIDATION"
    ]
)

loan_grade = st.selectbox(
    "Loan Grade",
    ["A","B","C","D","E","F","G"]
)

loan_amnt = st.number_input(
    "Loan Amount",
    min_value=0.0
)

loan_int_rate = st.number_input(
    "Interest Rate",
    min_value=0.0
)

loan_percent_income = st.number_input(
    "Loan Percent Income",
    min_value=0.0
)

cb_person_default_on_file = st.selectbox(
    "Previous Default",
    ["N", "Y"]
)

cb_person_cred_hist_length = st.number_input(
    "Credit History Length",
    min_value=0
)

if st.button("Predict"):

    data = pd.DataFrame({
        "person_age":[person_age],
        "person_income":[person_income],
        "person_home_ownership":[person_home_ownership],
        "person_emp_length":[person_emp_length],
        "loan_intent":[loan_intent],
        "loan_grade":[loan_grade],
        "loan_amnt":[loan_amnt],
        "loan_int_rate":[loan_int_rate],
        "loan_percent_income":[loan_percent_income],
        "cb_person_default_on_file":[cb_person_default_on_file],
        "cb_person_cred_hist_length":[cb_person_cred_hist_length]
    })

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0]

    if prediction == 1:
        st.error(
            f"⚠️ High Credit Risk\n\nProbability: {probability[1]:.2%}"
        )
    else:
        st.success(
            f"✅ Low Credit Risk\n\nProbability: {probability[0]:.2%}"
        )
