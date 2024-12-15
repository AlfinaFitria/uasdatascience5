# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13rkE-sSkRl46j0laYibHKAtOJQz1-m6g
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

import streamlit as st
import numpy as np
import joblib

def main():
    st.title("Wine Quality Prediction")
    st.write("Enter the wine's physicochemical properties below:")

    # Input form
    fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, step=0.1)
    volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, step=0.001)
    citric_acid = st.number_input("Citric Acid", min_value=0.0, step=0.001)
    residual_sugar = st.number_input("Residual Sugar", min_value=0.0, step=0.1)
    chlorides = st.number_input("Chlorides", min_value=0.0, step=0.0001)
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0, step=1.0)
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0, step=1.0)
    density = st.number_input("Density", min_value=0.0, step=0.0001)
    pH = st.number_input("pH", min_value=0.0, step=0.01)
    sulphates = st.number_input("Sulphates", min_value=0.0, step=0.01)
    alcohol = st.number_input("Alcohol", min_value=0.0, step=0.1)

    # Prediction button
    if st.button("Predict Quality"):
        try:
            # Load model and scaler
            model = joblib.load('wine_quality_model.pkl')
            scaler = joblib.load('scaler.pkl')

            # Prepare input data
            input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                                     chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                                     density, pH, sulphates, alcohol]])
            input_data_scaled = scaler.transform(input_data)

            # Predict
            prediction = model.predict(input_data_scaled)
            quality = {0: 'Low', 1: 'Medium', 2: 'High'}

            st.success(f"Predicted Wine Quality: {quality[prediction[0]]}")
        except Exception as e:
            st.error(f"Error in prediction: {e}")

if __name__ == '__main__':
    main()