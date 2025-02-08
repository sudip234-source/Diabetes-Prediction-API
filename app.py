import streamlit as st
import requests

st.title("Diabetes Prediction")

pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.2f")
age = st.number_input("Age", min_value=0)

if st.button("Predict"):
    input_data = {
        "pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": bp,
        "SkinThickness": skin,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }
    response = requests.post(api_url = "https://your-fastapi-app.onrender.com/diabetes_prediction", json=input_data)
    st.write("Prediction:", response.text)
