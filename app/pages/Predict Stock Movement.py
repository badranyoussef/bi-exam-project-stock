import streamlit as st
import joblib
import pandas as pd
import numpy as np

def load_model(stock):
    model_mapping = {
        "SP500": '../models/dt_model_sp500.pkl',
        "RUSSELL2000": '../models/dt_model_russell2000.pkl',
    }
    
    if stock in model_mapping:
        with open(model_mapping[stock], 'rb') as file:
            return joblib.load(file)
    else:
        st.error("Model not found!")
        return None

# Function to get user input based on selected stock index
def get_input_values(stock):
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

# Streamlit app starts here
st.markdown("# Predict Market Movement")
st.markdown("Here you can try our ML model, which we have trained to predict the stock market.")

# Choose stock index
st.markdown("**Which stock index will you predict?**")
stock = st.selectbox("Choose stock index", ("SP500", "RUSSELL2000"))

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

st.subheader("Model Selection and Results")
st.write("Working with time series data, we needed to be aware of this when training model.")
st.markdown("""
    * DescissionTreeClassifier ()
    * RandomForrestClassifier
    * GaussianNB
    * (Neural Networks)
""")

st.subheader("Cross Validation")
st.code("""
    def evaluate_model(model, X, y, max_splits):
        best_n_splits = None
        best_accuracy = 0
        results = {}

        # Test different n_splits values
        for n_splits in range(2, max_splits):  # Testing from 2 to max_splits
            tscv = TimeSeriesSplit(n_splits=n_splits)
            accuracies = []

            for train_index, test_index in tscv.split(X):
                X_train, X_test = X.iloc[train_index], X.iloc[test_index]
                y_train, y_test = y.iloc[train_index], y.iloc[test_index]

                # Train the model
                model.fit(X_train, y_train)

                # Predict on test data
                y_pred = model.predict(X_test)

                # Evaluate the model
                accuracy = accuracy_score(y_test, y_pred)
                accuracies.append(accuracy)

            # Calculate the average accuracy for this n_splits
            average_accuracy = np.mean(accuracies)
            results[n_splits] = average_accuracy

            # Update the best n_splits if the current one is better
            if average_accuracy > best_accuracy:
                best_accuracy = average_accuracy
                best_n_splits = n_splits

        return best_n_splits, best_accuracy
""")

st.subheader("Descission Tree Classifier")
df = pd.DataFrame({
    'Pros':['Easy to understand - straight forward', 'Ideal for visualization', 'Nomalization not necessary', 'Handle numerical and catogorical data', 'Resistant to outliers'],
    'Cons':['Overfitting', 'Greedy model (small changes big differences)', 'Not good for continues variables', 'Biased towards imbalanced data', '']
})
st.dataframe(df, hide_index=True, use_container_width=True)