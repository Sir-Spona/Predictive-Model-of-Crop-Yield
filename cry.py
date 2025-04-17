import streamlit as st
import pandas as pd 
import numpy as np
import pickle
import os



#Creating logic for prediction application

st.title("Crop Yield Prediction App")
st.write("This app predicts the yield of a crop based on environmental and farming features.")

#input features
rainfall_mm = st.number_input('rainfall_mm', value=1000, max_value=2000, min_value=500, step=1)
soil_quality_index = st.number_input('soil_quality_index', value=3, max_value=10, min_value=1, step=1)
farm_size_hectares = st.number_input('farm_size_hetares', value=50, max_value=1000, min_value=10, step=1)
sunlight_hours = st.number_input('sunlight_hours', value=5, max_value=12, min_value=4, step=1)
fertilizer_kg = st.number_input('fertilizer_kg', value=500, max_value=3000, min_value=100, step=1)

#loading serialized model
mod = pickle.load(open('model.pkl', 'rb'))
scl = pickle.load(open('scaler.pkl', 'rb'))
fse = pickle.load(open('feature_selector.pkl', 'rb'))

#create a DataFrame with the input features
input_data = pd.DataFrame([[rainfall_mm, soil_quality_index, farm_size_hectares,
                            sunlight_hours, fertilizer_kg]],
                          columns=['rainfall_mm', 'soil_quality_index', 'farm_size_hectares',
                                   'sunlight_hours', 'fertilizer_kg'])

input_data_scaled = scl.transform(input_data)
input_data_selected = fse.transform(input_data_scaled)

#Creating logic for prediction application
if st.button('Predict Crop Yield'):
    with st.spinner('Predicting Data'):
        prediction = mod.predict(input_data_selected)

        st.write("Raw prediction:", prediction)
        
        if prediction[0] >= 70:
            st.success("The crop yield is high.")
        elif prediction[0] < 70 and prediction[0] >= 30:
            st.warning("The crop yield is moderate.")
        elif prediction[0] < 30 and prediction[0] >= 0:
            st.error("The crop yield is low.")
        else:
            st.error("Invalid prediction.")
        st.balloons()
        st.success("Prediction complete!")

    








