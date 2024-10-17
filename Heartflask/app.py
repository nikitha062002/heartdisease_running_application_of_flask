from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__, static_folder='static', template_folder='templates')

# Sample user data for login
users = {
    "user@example.com": "password123"
}

# Load models and preprocessors
with open('all_models.pkl', 'rb') as file:
    saved_objects = pickle.load(file)

trained_models = saved_objects[0]  # Dictionary of trained models
scaler = saved_objects[1]           # Scaler for normalization
imputer = saved_objects[2]          # Imputer for handling missing values

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email in users and users[email] == password:
            return render_template('homepage.html')
        else:
            return redirect(url_for('index'))
    return render_template('homepage.html')

@app.route('/predict', methods=['GET'])
def predict_page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form

        # Extract data from the form and convert to DataFrame
        input_data = pd.DataFrame([{
            'age': int(data['age']),
            'sex': int(data['sex']),
            'cp': int(data['cp']),
            'trestbps': int(data['trestbps']),
            'chol': int(data['chol']),
            'fbs': int(data['fbs']),
            'restecg': int(data['restecg']),
            'thalach': int(data['thalach']),
            'exang': int(data['exang']),
            'oldpeak': float(data['oldpeak']),
            'slope': int(data['slope']),
            'ca': int(data['ca']),
            'thal': int(data['thal']),
        }])

        # Data preprocessing
        input_data.replace('?', np.nan, inplace=True)
        input_data_imputed = imputer.transform(input_data)
        input_data_scaled = scaler.transform(input_data_imputed)

        # Selecting a model from the trained models
        model_name = list(trained_models.keys())[0]
        prediction = trained_models[model_name].predict(input_data_scaled)[0]

        # Simulating probability as placeholder
        probability = np.random.randint(50, 100)

        # Redirect to the predicted result page with prediction and probability
        return redirect(url_for('result', heart_disease=prediction, probability=probability))

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/predicted')
def result():
    heart_disease = request.args.get('heart_disease')
    probability = request.args.get('probability')
    
    # Render result page with prediction results
    return render_template('predicted.html', heart_disease=heart_disease, probability=probability)

if __name__ == '__main__':
    app.run(debug=True)
