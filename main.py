import streamlit as st
import pandas as pd
import numpy as np

# Define the Streamlit app

st.title("Multiple Sclerosis Disease Steps Calculator")

# Inputs
age = st.number_input('Patient age', min_value=0, max_value=120)
years_since_diagnosis = st.number_input('Years since diagnosis', min_value=0, max_value=100)
relapses_last_year = st.number_input('Number of relapses in the last year', min_value=0, max_value=100)

# Function to calculate disease steps
def calculate_disease_step(age, years_since_diagnosis, relapses_last_year):
    # This is a placeholder model. A real model would use complex bioinformatics algorithms and data.
    # We'll use a simplistic calculation just for demonstration.
    disease_step = (years_since_diagnosis / 10) + (relapses_last_year / 5)
    
    # Older patients may progress more quickly
    if age > 50:
        disease_step += 1

    return round(disease_step)


# Button to run the model
if st.button('Calculate Disease Steps'):
    disease_step = calculate_disease_step(age, years_since_diagnosis, relapses_last_year)
    st.write(f'The estimated disease step is {disease_step}')


