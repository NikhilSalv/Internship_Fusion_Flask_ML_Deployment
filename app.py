from flask import Flask, request, jsonify
import pickle
import numpy as np


app = Flask(__name__)

# Load the trained model (Assuming it's saved as 'model.pkl')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Welcome to the ML model API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Assuming the input is in JSON and matches the model's input structure
    prediction = model.predict(np.array([data['input']]))
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
