import streamlit as st

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
volume = st.slider("Set Volume", 10000, 100000, 20000)
interest = st.slider("Set Interest Rate Change", -1.0, 10.0, 3.5)
inflation = st.slider("Inflation Rate Change", -1.0, 10.0, 2.0)