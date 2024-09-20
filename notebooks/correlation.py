import pandas as pd
import numpy as np

def interest_sp500(days, df):
    # Calculate interest rate changes an save in new column
    df['InterestRateChange'] = df['Effective Federal Funds Rate'].diff()
    # Flag days where there is a change in interest rate with 1
    df['InterestRateChangeFlag'] = np.where(df['InterestRateChange'] != 0, 1, 0)
    # Calculate the change of the "Close" value X days from the interest rate change
    # and place it the same number of days back on the potential interest change day
    df[f'{days}_DAYS_Change'] = df['Close'].pct_change(periods=days).shift(-days)
    # Drop NaN rows
    df = df.dropna(subset=['InterestRateChange', 'SP500_10DAY_Change'])
    # Find all points with a change in interest rate
    df_rate_change = df[df['InterestRateChangeFlag'] == 1].copy()
    return df_rate_change