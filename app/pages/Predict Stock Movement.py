import streamlit as st
import joblib
import numpy as np

# Function to load model based on chosen stock to predict
def load_model(stock):
    if stock == "SP500":
        with open('../models/dt_model_sp500.pkl', 'rb') as file: # <-- test = 0.65 accuracy train = 0.55, max_depth=10
            model = joblib.load(file)
    elif stock == "RUSSELL2000":
        with open('../models/dt_model_russell2000.pkl', 'rb') as file: # <-- test = 0.63 accuracy train = 0.56, max_depth=4
            model = joblib.load(file)
    return model

# Intro
st.markdown("# Predict Market Movement")
st.markdown("Here you can try our ML model, ww have trained to predict the stock market.")

# Choose stock index
st.markdown("**Which stock index will you predict?**")
stock = st.selectbox(
    "Choose stock index",
    ("SP500", "RUSSELL2000"),
)

# Info section
st.markdown('''
            To predict the stock market with our model, you first need to input data about the past to predict the future.

            Our model uses CPI, Volume, Interest Rate Change, Inflation Rate Change to predict if the stock market goes up or down.

            You need to enter these numbers for the current month, and then you can see if our model forecasts the stock market to go up or down next month.
            ''')

# Input feature values
st.markdown("**What where the values the current month**")
cpi = st.slider("Set CPI", 100, 1000, 110) # or use .number_input("Set CPI")

if stock == "RUSSELL2000":
    volume = st.slider("Set Volume", 10000, 100000, 20000)

unemployment = st.slider("Set Unemployment Rate", 0.0, 10.0, 4.5)
interest = st.slider("Set Interest Rate Change", -1.0, 10.0, 3.5)
inflation = st.slider("Inflation Rate Change", -1.0, 10.0, 2.0)
st.markdown("**Is the stock rising in current month?**")
flagged = st.radio(
    "Choose Yes or No",
    ("Yes", "No")
)

# Convert flagged to 1 or 0 based on user choice
flagged_value = 1 if flagged == "Yes" else 0

# When the user click on the predict button
if st.button("Predict"):
    # Indlæs den valgte model
    model = load_model(stock)

    # Forbered input-data til modellen
    if stock == "SP500":
        input_data = np.array([[interest, unemployment, inflation, cpi, flagged_value]])
    else:
        input_data = np.array([[interest, unemployment, inflation, cpi, volume, flagged_value]])

    # Brug modellen til at forudsige
    prediction = model.predict(input_data)

    # Vis resultatet
    if prediction[0] == 1:
        st.success(f"The model predicts that the {stock} will go UP next month!")
    else:
        st.warning(f"The model predicts that the {stock} will go DOWN next month.")