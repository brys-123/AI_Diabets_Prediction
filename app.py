from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from joblib import load

app = Flask(__name__)

# Load model and preprocessing objects
model = load("LRMDiabets_prediction.joblib")
encoder = load("encoder.joblib")
scaler = load("scaler.joblib")

# Columns
cat_col = ['gender','smoking_history']
num_cols = ['age','bmi','HbA1c_level','blood_glucose_level']
bin_cols = ['hypertension','heart_disease']

def get_risk_level(probability):
    """Categorize risk based on probability"""
    if probability < 0.3:
        return "low"
    elif probability < 0.6:
        return "moderate"
    elif probability < 0.8:
        return "high"
    else:
        return "very-high"

def get_risk_interpretation(probability, data):
    """Provide detailed interpretation based on risk level and patient data"""
    risk_level = get_risk_level(probability)
    
    interpretations = {
        "low": {
            "title": "Low Risk",
            "message": "The analysis suggests a low probability of diabetes.",
            "recommendation": "Continue maintaining a healthy lifestyle with regular exercise and balanced diet. Annual check-ups are recommended.",
            "color": "success"
        },
        "moderate": {
            "title": "Moderate Risk",
            "message": "The analysis indicates a moderate probability of diabetes.",
            "recommendation": "Consider lifestyle modifications including diet improvements and increased physical activity. Consult with your healthcare provider for a comprehensive evaluation.",
            "color": "warning"
        },
        "high": {
            "title": "High Risk",
            "message": "The analysis shows a high probability of diabetes.",
            "recommendation": "We strongly recommend consulting with a healthcare professional for proper diagnosis and testing. Consider immediate lifestyle changes and medical evaluation.",
            "color": "danger"
        },
        "very-high": {
            "title": "Very High Risk",
            "message": "The analysis indicates a very high probability of diabetes.",
            "recommendation": "Immediate medical consultation is strongly recommended. Your healthcare provider may suggest blood tests (fasting glucose, HbA1c) and develop a management plan.",
            "color": "danger"
        }
    }
    
    return interpretations[risk_level]

def get_risk_factors(data, probability):
    """Identify contributing risk factors"""
    factors = []
    
    # Age risk
    age = float(data['age'])
    if age >= 45:
        factors.append(f"Age ({age} years) - Diabetes risk increases with age, especially after 45")
    
    # BMI risk
    bmi = float(data['bmi'])
    if bmi >= 30:
        factors.append(f"BMI ({bmi:.1f}) - Obesity (BMI ≥ 30) significantly increases diabetes risk")
    elif bmi >= 25:
        factors.append(f"BMI ({bmi:.1f}) - Overweight (BMI 25-29.9) increases diabetes risk")
    
    # HbA1c risk
    hba1c = float(data['HbA1c_level'])
    if hba1c >= 6.5:
        factors.append(f"HbA1c Level ({hba1c}%) - Elevated (≥6.5% indicates diabetes)")
    elif hba1c >= 5.7:
        factors.append(f"HbA1c Level ({hba1c}%) - Prediabetic range (5.7-6.4%)")
    
    # Blood glucose risk
    glucose = float(data['blood_glucose_level'])
    if glucose >= 200:
        factors.append(f"Blood Glucose ({glucose} mg/dL) - Very high (≥200 indicates diabetes)")
    elif glucose >= 140:
        factors.append(f"Blood Glucose ({glucose} mg/dL) - Elevated (140-199 suggests prediabetes)")
    elif glucose >= 100:
        factors.append(f"Blood Glucose ({glucose} mg/dL) - Above normal (100-139)")
    
    # Hypertension
    if int(data['hypertension']) == 1:
        factors.append("Hypertension - High blood pressure is associated with increased diabetes risk")
    
    # Heart disease
    if int(data['heart_disease']) == 1:
        factors.append("Heart Disease - Cardiovascular conditions often coexist with diabetes")
    
    # Smoking
    if data['smoking_history'] in ['current', 'ever']:
        factors.append(f"Smoking History ({data['smoking_history']}) - Smoking increases diabetes risk")
    
    return factors

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Receive user input
    data = {
        "gender": request.form['gender'],
        "age": float(request.form['age']),
        "hypertension": int(request.form['hypertension']),
        "heart_disease": int(request.form['heart_disease']),
        "smoking_history": request.form['smoking_history'],
        "bmi": float(request.form['bmi']),
        "HbA1c_level": float(request.form['HbA1c_level']),
        "blood_glucose_level": float(request.form['blood_glucose_level'])
    }

    # Create dataframe
    new_df = pd.DataFrame([data])

    # Apply SAME preprocessing
    cat_encoded = encoder.transform(new_df[cat_col])
    num_scaled = scaler.transform(new_df[num_cols])
    bin_vals = new_df[bin_cols].values
    new_processed = np.hstack([num_scaled, cat_encoded, bin_vals])

    # Predict
    prediction = model.predict(new_processed)[0]
    probability = model.predict_proba(new_processed)[0][1]  # probability of diabetes

    # Get interpretation
    interpretation = get_risk_interpretation(probability, data)
    
    # Get risk factors
    risk_factors = get_risk_factors(data, probability)
    
    # Prepare result data
    result = {
        'prediction': int(prediction),
        'probability': probability * 100,
        'interpretation': interpretation,
        'risk_factors': risk_factors,
        'patient_data': data
    }

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)