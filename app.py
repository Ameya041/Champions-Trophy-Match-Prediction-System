
### 4. app.py
#python
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
from utils.feature_engineering import preprocess_input

app = Flask(__name__)

# Load models
try:
    score_model = joblib.load('models/score_model.pkl')
    outcome_model = joblib.load('models/outcome_model.pkl')
except Exception as e:
    print(f"Error loading models: {e}")
    raise

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Preprocess input
        features = preprocess_input(data)
        
        # Make predictions
        score_pred = score_model.predict([features['score_features']])[0]
        outcome_prob = outcome_model.predict_proba([features['outcome_features']])[0]
        
        # Adjust score for overs
        adjusted_score = score_pred * (data['overs'] / 50)
        
        return jsonify({
            'score_prediction': round(adjusted_score),
            'win_probability': {
                'team1': round(outcome_prob[1] * 100, 1),
                'team2': round(outcome_prob[0] * 100, 1)
            },
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)