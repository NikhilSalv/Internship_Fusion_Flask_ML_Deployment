from flask import Flask, request, jsonify, render_template, send_file
import pandas as pd
import pickle
import numpy as np
import io


app = Flask(__name__)

# Load the trained model (Assuming it's saved as 'model.pkl')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    
    # If the user does not select a file, the browser also submits an empty part without filename
    if file.filename == '':
        return "No file selected", 400
    
    # Read the file into a DataFrame
    data = pd.read_csv(file)
    # print(data.columns)

    categorical_features = data.select_dtypes(include=['object']).columns
    numerical_features = data.select_dtypes(include=['int64', 'float64']).columns

    # For categorical features, fill missing values with the most frequent value
    data[categorical_features] = data[categorical_features].fillna(data[categorical_features].mode().iloc[0])

    # For numerical features, fill missing values with the median value
    data[numerical_features] = data[numerical_features].fillna(data[numerical_features].median())

    data = pd.get_dummies(data, drop_first=True)
    
    # Make predictions using the model
    predictions = model.predict(data)
    # print("___Model Predicted___")
    # print(predictions)
    predicted_output = pd.DataFrame({"Id":data["Id"], "Predicted_SalePrice" : predictions})

    # Convert DataFrame to CSV in memory
    output = io.BytesIO()
    predicted_output.to_csv(output, index=False)
    output.seek(0)
    
    # Send the CSV file as a downloadable response
    return send_file(output, mimetype="text/csv", download_name="predictions.csv", as_attachment=True)

    
    # Return the predictions as JSON
    # return jsonify({'predictions': predictions.tolist()})
    # return "File Received"

if __name__ == '__main__':
    app.run(debug=True)
