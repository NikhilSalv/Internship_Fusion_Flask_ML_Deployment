import streamlit as st
import requests
import pandas as pd
import io

st.title("Predicting Real Estate Selling Prices: A Data-Driven Approach Using Historical Trends")

# Define the model evaluation metrics
metrics = {
    "Mean Absolute Error": 17883.41,
    "Mean Squared Error": 843147321.38,
    "Root Mean Squared Error": 29037.00,
    "R-squared": 0.8901,
    "Adjusted R-squared": 0.8893
}

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the file into a DataFrame
    data = pd.read_csv(uploaded_file)
    
    # Convert DataFrame to CSV
    csv_buffer = io.StringIO()
    data.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    # Send the file to Flask API
    response = requests.post("http://127.0.0.1:5000/predict", files={"file": csv_buffer})
    
    if response.status_code == 200:
        # Read the response CSV
        predicted_output = pd.read_csv(io.StringIO(response.text))

        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Predicted Output")
            st.write(predicted_output.style.set_table_styles(
                [{'selector': 'thead th', 'props': [('background-color', '#f0f0f0'), ('font-weight', 'bold')]},
                 {'selector': 'td', 'props': [('padding', '8px')]},
                 {'selector': 'tr:nth-of-type(odd)', 'props': [('background-color', '#f9f9f9')]},
                 {'selector': 'tr:nth-of-type(even)', 'props': [('background-color', '#ffffff')]}]
            ).set_properties(**{'text-align': 'center'}))

        # Display model evaluation metrics
        with col2:
            st.subheader("Model Evaluation Metrics")
            for metric, value in metrics.items():
                st.write(f"**{metric}:** {value:,.2f}")


        # Provide download link
        st.download_button(
            label="Download Predictions",
            data=response.text,
            file_name='predictions.csv',
            mime='text/csv',
        )
    else:
        st.error("There was an error with the prediction.")
