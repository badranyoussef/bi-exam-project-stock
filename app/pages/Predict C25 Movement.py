import streamlit as st
import pandas as pd
import joblib
import numpy as np
from datetime import date

df = pd.read_csv("../app/data/sp500_c25.csv")
st.dataframe(df.tail())

st.markdown(f"You can find the latest closing price of S&P500 [here](https://www.nasdaq.com/market-activity/index/spx/historical)")
LAST_CLOSE_SP500 = st.number_input("Last closing price of S&P500")
st.markdown(f"You can find the latest data of C25 [here](https://indexes.nasdaqomx.com/Index/History/OMXC25)")
LAST_CLOSE_C25 = st.number_input("Last closing price of C25")
CHANGE_C25 = st.number_input("Last change of C25")

if st.button("Add data"):
    CHANGE_SP500 = LAST_CLOSE_SP500 - df['LAST_CLOSE_SP500'].shift(1)
    C25_MOVEMENT = (df['CHANGE_C25'] > 0).astype(int)
    SP500_MOVEMENT_SAME_DAY = df['CHANGE_SP500'].shift(1)
    C25_MOVEMENT_YESTERDAY = df['C25_MOVEMENT'].shift(1)
    SP500_MOVEMENT_YESTERDAY = df['CHANGE_SP500'].shift(2)

new_data = pd.DataFrame({
    'Date':[date.today()],
    'LAST_CLOSE_SP500':[LAST_CLOSE_SP500],
    'LAST_CLOSE_C25':[LAST_CLOSE_C25],
    'CHANGE_C25':[CHANGE_C25],
    'CHANGE_SP500':[CHANGE_SP500],
    'C25_MOVEMENT':[C25_MOVEMENT],
    'SP500_MOVEMENT_SAME_DAY':[SP500_MOVEMENT_SAME_DAY],
    'C25_MOVEMENT_YESTERDAY':[C25_MOVEMENT_YESTERDAY],
    'SP500_MOVEMENT_YESTERDAY':[SP500_MOVEMENT_YESTERDAY],
})

# Append the new_data dictionary to the DataFrame first
df = pd.concat([df, new_data], ignore_index=True)

# Create rolling averages
days = [3, 5, 10, 15, 20, 65, 130, 260] # 3 days, 1,2,3,4 weeks, 3,6,12 months

# for num in days:
#     # To calculate the rolling average for days for the data frame
#     rolling_avg = df.drop(columns='Date').rolling(num).mean()
#     # Then we use the rolling average for the LAST_CLOSE_SP500 and _C25
#     # to see the ratio between the close today and days ago
#     #df[f'SP500_CLOSE_RATIO_{num}'] = df['LAST_CLOSE_SP500'] / rolling_avg['LAST_CLOSE_SP500']
#     ratio_feature = f'C25_CLOSE_RATIO_{num}'
#     c25_close_ratio_value = df['LAST_CLOSE_C25'] / rolling_avg['LAST_CLOSE_C25']
    
#     # Takes the trend of the change over X-days and adds the result to next row
#     trend_feature = f'Trend_{num}'
#     trend_value = df.drop(columns='Date').shift(1).rolling(num).sum()['C25_MOVEMENT']
    
#     # Add the calculated values to the new_data dictionary
#     new_data[ratio_feature] = c25_close_ratio_value
#     new_data[trend_feature] = trend_value

st.dataframe(df.tail())