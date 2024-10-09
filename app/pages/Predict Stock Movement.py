import streamlit as st
import joblib
import numpy as np

def load_model(stock):
    model_mapping = {
        "SP500": '../models/dt_model_sp500.pkl',
        "RUSSELL2000": '../models/dt_model_russell2000.pkl',
        "C25": '../models/model_c25.pkl'
    }
    
    if stock in model_mapping:
        with open(model_mapping[stock], 'rb') as file:
            return joblib.load(file)
    else:
        st.error("Model not found!")
        return None

# Function to get user input based on selected stock index
def get_input_values(stock):
    if stock == "C25":
        return get_c25_input()
    else:
        return get_other_stock_input(stock)

def get_other_stock_input(stock):
    cpi = st.slider("Set CPI", 100, 1000, 110) 
    unemployment = st.slider("Set Unemployment Rate", 0.0, 10.0, 4.5)
    interest = st.slider("Set Interest Rate Change", -1.0, 10.0, 3.5)
    inflation = st.slider("Inflation Rate Change", -1.0, 10.0, 2.0)
    flagged = st.radio("Is the stock rising in the current month?", ("Yes", "No"))
    
    # Convert flagged to 1 or 0 based on user choice
    flagged_value = 1 if flagged == "Yes" else 0
    
    if stock == "RUSSELL2000":
        volume = st.slider("Set Volume", 10000, 100000, 20000)
        return np.array([[interest, unemployment, inflation, cpi, volume, flagged_value]])
    
    return np.array([[interest, unemployment, inflation, cpi, flagged_value]])

def get_c25_input():
    LAST_CLOSE_SP500 = st.slider("Set CLOSE value for SP500", 0, 6500, 5000)
    Open = st.slider("Set Open value for SP500", 0, 6500, 5000)
    High_sp500 = st.slider("Set HIGH value for SP500", 0, 6500, 5000)
    Low_sp500 = st.slider("Set LOW value for SP500", 0, 6500, 5000)
    CHANGE_SP500 = st.slider("Set CHANGE value for SP500", 0, 6500, 5000)

    LAST_CLOSE_C25 = st.slider("Set LAST CLOSE value for C25", 0, 6500, 5000)
    CHANGE_C25 = st.slider("Set CHANGE value for C25", 0, 6500, 5000)
    High_c25 = st.slider("Set HIGH value for C25", 0, 6500, 5000)
    Low_c25 = st.slider("Set LOW value for C25", 0, 6500, 5000)

    flagged = st.radio("Is the C25 stock rising in the current month?", ("Yes", "No"))
    flagged_value = 1 if flagged == "Yes" else 0

    return np.array([[LAST_CLOSE_SP500, Open, High_sp500, Low_sp500, CHANGE_SP500,
                      LAST_CLOSE_C25, CHANGE_C25, High_c25, Low_c25, flagged_value]])

# Streamlit app starts here
st.markdown("# Predict Market Movement")
st.markdown("Here you can try our ML model, which we have trained to predict the stock market.")

# Choose stock index
st.markdown("**Which stock index will you predict?**")
stock = st.selectbox("Choose stock index", ('C25', "SP500", "RUSSELL2000"))

# Info section
st.markdown('''
            To predict the stock market with our models, you first need to input data about the past to predict the future.
            Our models use different features based on the stock you want to predict whether the stock market goes up or down.
            You need to enter these numbers for the current month, and then you can see if our model forecasts the stock market to go up or down next month.
            ''')

# Input feature values
st.markdown("**Enter the known values:**")
input_data = get_input_values(stock)

# When the user clicks on the predict button
if st.button("Predict"):
    model = load_model(stock)  # Load the selected model

    # Use the model to make predictions
    prediction = model.predict(input_data)

    # Display the prediction result
    if prediction[0] == 1:
        st.success(f"The model predicts that the {stock} will go UP next month!")
    else:
        st.warning(f"The model predicts that the {stock} will go DOWN next month.")