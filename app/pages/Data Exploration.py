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
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

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

st.subheader("Correlation Matrix for data frame")
corr_matrix_img = Image.open("../app/images/Correlation.png")
st.image(corr_matrix_img)

st.subheader("Confusion Matrix for trained model")
conf_matrix_img = Image.open("../app/images/confusion matrix.png")
st.image(conf_matrix_img)