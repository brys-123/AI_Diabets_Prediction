# 🩺 AI Diabetes Prediction System

A machine learning-powered web application for early diabetes detection and risk assessment using AI-driven analysis. This project combines advanced clinical measurements with personalized health recommendations.

## 📋 Overview

The **AI Diabetes Prediction System** is a Flask-based web application that uses a trained Logistic Regression model to predict diabetes risk based on patient clinical data. The application provides:

- **Risk Assessment**: AI-powered probability prediction for diabetes
- **Clinical Analysis**: Comprehensive evaluation of key health metrics
- **Health Metrics**: Computed values including eAG (Estimated Average Glucose) and overall health score
- **Personalized Recommendations**: Tailored health guidance based on individual risk factors
- **Interactive UI**: Modern, responsive interface with Bootstrap and Font Awesome

## 🎯 Features

### 1. **Patient Information Form**
- Demographics (Gender, Age)
- Medical History (Hypertension, Heart Disease)
- Lifestyle Factors (Smoking History)
- Clinical Measurements (BMI, HbA1c Level, Blood Glucose Level)

### 2. **Risk Assessment Results**
- Color-coded risk badges (Low, Moderate, High, Very High)
- Probability meter with visual representation
- Detailed risk interpretation
- Identified risk factors with explanations

### 3. **Additional Health Metrics**
- **Estimated Average Glucose (eAG)**: Calculated from HbA1c using the formula: eAG = 28.7 × A1c - 46.7
- **Overall Health Score**: Composite score (0-100) based on:
  - HbA1c levels
  - BMI classification
  - Blood glucose levels
  - Age considerations
  - Smoking status
- **Personalized Recommendations**: Context-aware health guidance

### 4. **Enhanced UI/UX**
- Stunning animated multi-color gradient background
- Responsive design for desktop and mobile
- Favicon with health droplet icon
- Smooth animations and transitions
- Clinical reference values display

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **ML Model**: Scikit-learn Logistic Regression
- **Preprocessing**: Scikit-learn (OneHotEncoder, StandardScaler)
- **UI Framework**: Bootstrap 5.3.3
- **Icons**: Font Awesome 6.4.0

## 📦 Project Structure

```
diabetes_flask/
├── app.py                           # Flask application & ML logic
├── LRMDiabets_prediction.joblib    # Trained logistic regression model
├── encoder.joblib                   # Categorical encoder (OneHotEncoder)
├── scaler.joblib                    # Feature scaler (StandardScaler)
├── templates/
│   └── index.html                   # Web UI template
└── README.md                         # This file
```

## 📊 Model Details

- **Algorithm**: Logistic Regression
- **Input Features**:
  - Categorical: Gender, Smoking History
  - Binary: Hypertension, Heart Disease
  - Numerical: Age, BMI, HbA1c Level, Blood Glucose Level
- **Output**: Diabetes risk probability (0-1)

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Flask
- scikit-learn
- pandas
- numpy
- joblib

### Installation

1. Clone the repository:
```bash
git clone https://github.com/brys-123/AI_Diabets_Prediction.git
cd diabetes_flask
```

2. Install dependencies:
```bash
pip install flask scikit-learn pandas numpy joblib
```

3. Run the Flask application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## 📈 How to Use

1. **Enter Patient Information**: Fill in the form with demographic, medical, and clinical data
2. **Submit**: Click "Analyze Risk" button
3. **Review Results**: 
   - Check the risk level badge
   - Review probability meter
   - Examine identified risk factors
   - Read personalized recommendations
   - View computed health metrics

## 📋 Clinical Reference Values

### HbA1c Level (%)
- **Normal**: < 5.7%
- **Prediabetes**: 5.7% - 6.4%
- **Diabetes**: ≥ 6.5%

### Blood Glucose Level (mg/dL) - Fasting
- **Normal**: < 100
- **Prediabetes**: 100 - 125
- **Diabetes**: ≥ 126

### BMI Categories
- **Underweight**: < 18.5
- **Normal**: 18.5 - 24.9
- **Overweight**: 25.0 - 29.9
- **Obese**: ≥ 30.0

## ⚠️ Disclaimer

This application provides **AI-powered analytical predictions** and should **NOT** be used as a substitute for professional medical diagnosis. The results are based on machine learning analysis and clinical metrics. 

**Always consult with a qualified healthcare professional for:**
- Proper medical diagnosis
- Clinical interpretation of results
- Treatment planning
- Medical recommendations

This tool is intended for educational and awareness purposes only.

## 🔍 Risk Level Interpretation

| Risk Level | Probability | Recommendation |
|-----------|------------|-----------------|
| **Low** | < 30% | Continue healthy lifestyle; annual check-ups |
| **Moderate** | 30-60% | Lifestyle modifications; consult healthcare provider |
| **High** | 60-80% | Strong recommendation for medical evaluation |
| **Very High** | > 80% | Immediate medical consultation recommended |

## 🧮 Health Score Calculation

The Overall Health Score (0-100) is calculated based on:
- HbA1c level: ±35 points
- BMI classification: ±30 points
- Blood glucose level: ±20 points
- Age: ±10 points
- Smoking status: ±12 points

## 🎨 UI Features

- **Favicon**: Green droplet icon representing health
- **Background**: Dynamic multi-color gradient (purple → pink → blue → cyan)
- **Cards**: Clean white cards with subtle shadows
- **Badges**: Color-coded risk indicators
- **Progress Bars**: Visual representation of metrics
- **Responsive**: Fully responsive across devices

## 📝 License

This project is provided as-is for educational purposes.

## 👨‍💻 Author

Created as part of a machine learning and data science project for diabetes risk prediction.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements.

---

**Stay Healthy! 🏃‍♂️🥗💪**
