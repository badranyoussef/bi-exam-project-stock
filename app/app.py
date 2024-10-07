import streamlit as st

#st.markdown("# Can you predict the stock market?")

#st.image('images/data-line-plot.png')    

# Titel og hovedindhold
st.title("Data Analysis and Prediction Project")
st.header("Welcome to the Project Overview")

# Introduktion til opgaven
st.write("""
This project focuses on the analysis and prediction of stock market trends, 
particularly for the S&P 500 index. We explore historical data and utilize 
machine learning models to predict future market movements.
""")

# Kort om data exploration
st.subheader("Data Exploration")
st.write("""
The data exploration section allows users to dive deep into the historical data, 
visualize trends, and analyze key metrics that influence stock market performance.
""")

# Kort om predictions
st.subheader("Predictions")
st.write("""
In the prediction section, you can explore the performance of the trained models 
and see how well they forecast stock price movements based on the data trends.
""")

# Bemærkning om brug af modellen
st.subheader("Objective")
st.write("""
The goal of this project is to demonstrate the use of data analytics and machine 
learning techniques to predict future stock movements and provide valuable insights 
for investors and researchers.
""")