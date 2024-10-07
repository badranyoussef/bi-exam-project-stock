import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

    # Let users select columns for the y-axis
    columns_to_plot = st.multiselect("Select columns to plot on Y-axis", df.columns.tolist(), default=df.columns[1:4])

    # Check if Date column is present and if at least one column is selected for the Y-axis
    if 'Date' in df.columns and columns_to_plot:
        # Create the figure and axis
        fig, ax1 = plt.subplots(figsize=(10, 6))

        # Plot the first selected column
        ax1.set_xlabel('Date')
        ax1.set_ylabel(columns_to_plot[0], color='tab:blue')
        ax1.plot(df['Date'], df[columns_to_plot[0]], color='tab:blue', label=columns_to_plot[0])
        ax1.tick_params(axis='y', labelcolor='tab:blue')

        # Create additional y-axes for the second and third selected columns
        if len(columns_to_plot) > 1:
            ax2 = ax1.twinx()
            ax2.set_ylabel(columns_to_plot[1], color='tab:red')
            ax2.plot(df['Date'], df[columns_to_plot[1]], color='tab:red', label=columns_to_plot[1])
            ax2.tick_params(axis='y', labelcolor='tab:red')

        if len(columns_to_plot) > 2:
            ax3 = ax1.twinx()
            ax3.spines['right'].set_position(('outward', 60))  # Offset the third y-axis
            ax3.set_ylabel(columns_to_plot[2], color='tab:green')
            ax3.plot(df['Date'], df[columns_to_plot[2]], color='tab:green', label=columns_to_plot[2])
            ax3.tick_params(axis='y', labelcolor='tab:green')

        plt.title('Data Visualization')
        fig.tight_layout()
        st.pyplot(fig)
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

        fig, axs = plt.subplots(1, len(box_plot_columns), figsize=(15, 6))
        
        # If only one column is selected, axs will not be an array
        if len(box_plot_columns) == 1:
            axs = [axs]  # Make it iterable

        for ax, col in zip(axs, box_plot_columns):
            sns.boxplot(x=df[col], ax=ax)
            ax.set_title(f'Box Plot of {col}')
            ax.set_xlabel(col)

        plt.tight_layout()
        st.pyplot(fig)

    # Histogram
    st.write("### Histogram")
    hist_columns = st.multiselect("Select up to 3 columns for Histograms", df.columns.tolist())
    
    if len(hist_columns) > 0:
        # Limit to 3 selections
        if len(hist_columns) > 3:
            st.warning("Please select up to 3 columns only.")
            hist_columns = hist_columns[:3]  # Take only the first 3

        fig, axs = plt.subplots(1, len(hist_columns), figsize=(15, 6))

        # If only one column is selected, axs will not be an array
        if len(hist_columns) == 1:
            axs = [axs]  # Make it iterable

        for ax, col in zip(axs, hist_columns):
            ax.hist(df[col], bins=30, color='skyblue', edgecolor='black')
            ax.set_title(f'Histogram of {col}')
            ax.set_xlabel(col)
            ax.set_ylabel('Frequency')

        plt.tight_layout()
        st.pyplot(fig)