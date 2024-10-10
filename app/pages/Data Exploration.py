import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler
from PIL import Image

def normalize_data(df):
    # Initialize MinMaxScaler
    scaler = MinMaxScaler()

    # Extract 'Date' column and keep it separate
    date_column = df['Date']

    # Scale the rest of the columns except 'Date'
    df_scaled = scaler.fit_transform(df.drop(columns=['Date']))

    # Convert the scaled data back into a DataFrame
    # Use the original column names except for 'Date'
    df_scaled = pd.DataFrame(df_scaled, columns=df.drop(columns=['Date']).columns)

    # Concatenate the 'Date' column back to the scaled DataFrame
    df_scaled = pd.concat([date_column, df_scaled], axis=1)
    
    return df_scaled

# Set up the page
st.markdown("# Data Exploration")

# Upload CSV file
st.markdown("**Upload a file to explore the data**")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Select from our files
file_list = {
    'Oil prices':'https://raw.githubusercontent.com/badranyoussef/bi-exam-project-stock/refs/heads/main/datasets/BrentOilPrices.csv',
    'S&P 500 (original)':'https://raw.githubusercontent.com/badranyoussef/bi-exam-project-stock/refs/heads/main/datasets/SP500-data.csv',
    'S&P (cleaned)':'https://raw.githubusercontent.com/badranyoussef/bi-exam-project-stock/refs/heads/main/datasets/df_sp500_cleaned.csv',
    'Gold (cleaned)':'https://raw.githubusercontent.com/badranyoussef/bi-exam-project-stock/refs/heads/main/datasets/cleaned_gold_data.csv',
    'Gold (original)':'../app/data/XAU_USD Historical Data.xlsx',
    'Interest Rate (cleaned)':'../app/data/interest_rate_2017_now_cleaned.xlsx',
    'Interest Rate (original)':'../app/data/interest_rate_2017_now.xlsx',
    'RUSSELL 2000':'https://raw.githubusercontent.com/badranyoussef/bi-exam-project-stock/refs/heads/main/datasets/russell_2000.csv',
    'All data from 1987-2018':'https://raw.githubusercontent.com/badranyoussef/bi-exam-project-stock/refs/heads/main/datasets/data_1987_2018.csv',
    'All data monthly':'https://raw.githubusercontent.com/badranyoussef/bi-exam-project-stock/refs/heads/main/datasets/monthly_combined_data.csv',
    'CPI data':'https://raw.githubusercontent.com/badranyoussef/bi-exam-project-stock/refs/heads/main/datasets/cpi_data.csv'
}

# Add a dropdown to choose a file
st.markdown("**Or select a file to explore**")
st.write("Here you can see original and cleaned data files, we have used to work out our model.")
selected_title = st.selectbox("Select a file to load", list(file_list.keys()), None)
is_file_chosen = False
if uploaded_file is not None:
    # Load the uploaded file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    is_file_chosen = True
elif selected_title is not None:
    # If no file is uploaded, load the selected predefined file
    selected_file = file_list[selected_title]

    if selected_file.endswith('.csv'):
        df = pd.read_csv(selected_file)
    elif selected_file.endswith('.xlsx'):
        df = pd.read_excel(selected_file)
    is_file_chosen = True

if is_file_chosen is True:
    # Read the CSV file
    #df = pd.read_csv(uploaded_file)

    # Show the first few rows of the DataFrame
    st.write("### Data Preview")
    st.dataframe(df.head())

    # Ensure 'Date' is a datetime object
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df_scaled = normalize_data(df)

        # Let users select columns for the y-axis
        columns_to_plot = st.multiselect("Select columns to plot on Y-axis", df_scaled.columns.tolist(), default=df_scaled.columns[1:4])

        # Check if Date column is present and if at least one column is selected for the Y-axis
        if 'Date' in df_scaled.columns and columns_to_plot:
            st.line_chart(df_scaled, x='Date', y=columns_to_plot)  # Use df_scaled here
        else:
            st.warning("Please ensure that the Date column is present and select at least one column for the Y-axis.")

    # Box Plot
    st.write("### Box Plot")
    box_plot_columns = st.multiselect("Select up to 3 columns for Box Plots", df.columns.tolist())
    
    if len(box_plot_columns) > 0:
        # Limit to 3 selections
        if len(box_plot_columns) > 3:
            st.warning("Please select up to 3 columns only.")
            box_plot_columns = box_plot_columns[:3]  # Take only the first 3
        fig = px.box(df, y=box_plot_columns)
        st.plotly_chart(fig, use_container_width=True)

    # Histogram
    st.write("### Histogram")
    hist_columns = st.multiselect("Select up to 3 columns for Histograms", df.columns.tolist())
    
    if len(hist_columns) > 0:
        # Limit to 3 selections
        if len(hist_columns) > 3:
            st.warning("Please select up to 3 columns only.")
            hist_columns = hist_columns[:3]  # Take only the first 3
        
        fig = px.histogram(df, x=hist_columns)
        st.plotly_chart(fig, use_container_width=True)


    # TABS for Confusion Matrix and Correlation
    st.write("### Additional Analysis")
    tab1, tab2 = st.tabs(["Correlation Matrix", "Confusion Matrix"])

    with tab1:
        # Correlation matrix
        st.write("### Correlation Matrix")
        st.image('../app/images/Correlation.png')

    with tab2:
        # Placeholder for confusion matrix - requires actual and predicted labels
        st.write("### Confusion Matrix")
        st.image('../app/images/confusion matrix.png')
else:
    st.warning("You need to upload or select a file to see something here...")
