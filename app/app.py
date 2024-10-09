import streamlit as st

#st.markdown("# Can you predict the stock market?")

#st.image('images/data-line-plot.png')    

# Titel og hovedindhold
st.title("Stock Price Prediction Based on Macroeconomic Factors")
st.markdown("""
    **Initial problem formulation:**
    How does changes in macroeconomic factors, like interest rates and inflation, 
    affect the stock market development, and how can we predict these changes using historical data?

    **Why is it important:**
    Macroeconomic changes have a direct impact on companies' borrowing costs and earnings, 
    which in turn affect their stock prices. Being able to predict these changes 
    can help investors make informed decisions and reduce market risks.

    **Expectations:**
    This study will help us determine if the macroeconomic factors have a influence on the stock prices, 
    and whether investors should invest or not, based macroecomomic factors.

    We will work towards developing a machine learning model that predicts stock price 
    changes based on historical macroeconomic factors. In this study we mainly focus on 
    interest rate and inflation.   

    **Solution impact:**
    The solution will provide investors and financial analysts with valuable 
    insights that enhance their ability to forecast market movements. 
    This will enable them to make more accurate decisions regarding their investments.         
""")
st.header("Reflections and learnings along the way")

# Introduktion til opgaven
st.write("""
    This project focuses on the analysis and prediction of stock market trends, 
    particularly for the S&P 500 and Russell 2000 stock indicies. We explore historical data and utilize 
    machine learning models to predict future market movements.
""")

# Kort om data exploration
st.subheader("Data Exploration")
st.markdown("""
    The data exploration section allows users to dive deep into the historical data, 
    visualize trends, and analyze key metrics that influence stock market performance.
    You can upload your own data set and get it visualized.
    
    **Datasets we've worked with:**
    
    * S&P 500
    * Russell 2000
    * Gold
    * Oil
    * Macroeconomic data
""")

# Kort om predictions
st.subheader("Predictions")
st.markdown("""
    In the prediction section, you can explore the performance of the trained models 
    and see how well they forecast stock price movements based on the data trends.

    **Models we tried**
    
    * DescissionTreeClassifier
    * RandomForrestClassifier
    * GaussianNB (Nayve Bayes)
                
    **Features we used**
    
    * CPI
    * Inflation Rate
    * Interest Rate
    * Market
""")

st.subheader("Future objectives")
st.markdown("""
    During the project we have only had so much time and have come across new things,
    that could be interesting to explore:
    * What other macroeconomic factors can we find, to include?
    * Other kinds of feature engineering
    * Introduction of new data sets (other indicies)
    * The effect of movement in different indicies on other indicies
""")

# Bemærkning om brug af modellen
# st.subheader("Objective")
# st.write("""
# The goal of this project is to demonstrate the use of data analytics and machine 
# learning techniques to predict future stock movements and provide valuable insights 
# for investors and researchers.
# """)