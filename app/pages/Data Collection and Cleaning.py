import streamlit as st

st.markdown("# Data Collection and Cleaning")

st.markdown("## Different Data Sets")
st.markdown("""
    We worked with different data sets and needed to merge them on='Date'.
    This involved some cleaning and challenges merging.
""")

st.markdown("## Times Series Data")

st.write("Working with time series, we needed to convert dtype: object to datetime.")
st.code("df_gold['Date'] = pd.to_datetime(df_gold['Date'])")

st.write("In one case the date was divided in three columns: 'Year', 'Month', 'Day'.")
st.code("df_interest_inflation_dropped['Date'] = pd.to_datetime(df_interest_inflation_dropped[['Year', 'Month', 'Day']])")

st.markdown("## Renaming Columns")
st.write("""
    A lot of columns from different data sets had the same names, like 'Close', 'Open', 'High', 'Low'
    To distinguish between these column when merged, we needed to rename them either before or on merge.
""")
st.code("df_sp500.columns = [col + ' SP500' if col != 'Date' else col for col in df_sp500.columns]")

st.markdown("## Handling missing values")

st.write("Our original data set had a lot of missing values, due to it being a set of daily data.")
st.code("""
    def fill_missing_values(df, exclude_column):
        #Saving the desired column which doesnt need to be filled
        excluded_data = df[exclude_column]
    
        # Removing the column which doesnt need to be filled
        df = df.drop(columns=[exclude_column])
    
        # Filling the missing values
        df = df.ffill().bfill()

        # Adding the saved column from first step
        df[exclude_column] = excluded_data
        return df
""")

st.markdown("## Merging Cleaned Data Frames")

st.code("""
    # merging sp500 into interest and inflation df
    df_combined = pd.merge(df_sp500, df_interest_combined, on='Date', how='outer')
    # cpi into combined
    df_combined = pd.merge(df_combined, cpi, on='Date', how='left')
    # russell into combined
    df_combined = pd.merge(df_combined, russell2000_df, on='Date', how='outer')
    # oil into combined
    df_combined = pd.merge(df_combined, oil_df, on='Date', how='left')
    # gold into combined
    df_combined = pd.merge(df_combined, df_gold, on='Date', how='left')
""")