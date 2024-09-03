# Real Estate Price Prediction

**Overview**

This project consists of a Machine Learning model for predicting real estate property prices using historical data. The backend is implemented in Flask, while the frontend is built using Streamlit. Users can upload CSV files containing property data, and the model will generate predictions for the selling prices.

## Demo Video

<video width="640" height="360" controls>
  <source src="videos/IternshipFusion_resized.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Features**

- File Upload: Upload CSV files containing property data.

- Prediction: Get predicted selling prices based on the historical data.

- Metrics Display: View model evaluation metrics.

- Download Predictions: Download the predictions as a CSV file.

**Getting Started**

**Prerequisites**

- Python 3.x
- Flask
- Streamlit
- Pandas
- Scikit-Learn
- Requests

You can install the necessary packages using pip:

<img width="705" alt="Screenshot 2024-09-03 at 11 25 05" src="https://github.com/user-attachments/assets/227e1912-bc94-46f2-a3d1-4293e9403fdb">


**Model**

The machine learning model used for predictions is saved in a file named model.pkl. It should be placed in the same directory as the Flask app.

**Flask Application**

The Flask application serves as the backend for the predictions. To run the Flask app:

1. Navigate to the directory containing the Flask application.

2. Run the following command:

<img width="671" alt="Screenshot 2024-09-03 at 11 25 16" src="https://github.com/user-attachments/assets/0cf477e0-cb63-4b34-b0d4-13cfe37252d0">


The Flask server will start and listen on http://127.0.0.1:5000.

**Streamlit Application**

The Streamlit application provides the user interface for interacting with the model. To run the Streamlit app:

1. Navigate to the directory containing the Streamlit script.

2. Run the following command:

<img width="669" alt="Screenshot 2024-09-03 at 11 25 24" src="https://github.com/user-attachments/assets/65eb1c0c-2c7c-4086-85e8-f6cb20ae8b5a">


The Streamlit application will open in your web browser.

**API Endpoints**

**'/predict'**

***Method: POST***

***Description:***

Accepts a CSV file and returns predictions for the property selling prices.

***Parameters:***

- file: The CSV file containing property data.

**Response:**

- A CSV file containing the predictions with columns Id and Predicted_SalePrice.

#### Metrics

The following metrics are used to evaluate the performance of the model:

- Mean Absolute Error: 17883.41

- Mean Squared Error: 843147321.38

- Root Mean Squared Error: 29037.00

- R-squared: 0.8901

- Adjusted R-squared: 0.8893

**Folder Structure**

<img width="675" alt="Screenshot 2024-09-03 at 11 25 33" src="https://github.com/user-attachments/assets/77264a8e-cf27-4903-8509-94f151c3c1b9">


***Usage***

1. Start the Flask server by running python app.py.

2. Start the Streamlit application by running streamlit run streamlit_app.py.

3. Open the Streamlit application in your browser, upload a CSV file, and view the predictions.


**Acknowledgements**

- The model was trained using historical real estate data.

- The Flask and Streamlit frameworks were used to build the web applications.
