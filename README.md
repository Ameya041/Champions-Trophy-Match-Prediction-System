# 🏏 Champions Trophy Match Prediction System

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A machine learning system that predicts cricket match scores and outcomes using historical Champions Trophy data.

## Features
- Score prediction using Random Forest Regressor
- Win probability estimation using Random Forest Classifier
- Interactive Jupyter Notebook interface
- Flask web application
- Comprehensive feature engineering

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Ameya041/cricket-match-prediction.git
cd cricket-match-prediction
Install dependencies:

bash
Copy
pip install -r requirements.txt
💻 Usage
Jupyter Notebook
bash
Copy
jupyter notebook notebooks/Cricket_Prediction_System.ipynb
Web Application
bash
Copy
python app.py
Then open http://localhost:5000 in your browser.

📂 Project Structure
Copy
cricket-match-prediction/
├── app.py                # Flask application
├── data/                 # Match datasets
├── models/               # Trained models
├── notebooks/            # Jupyter notebooks
├── templates/            # HTML templates
└── utils/                # Utility functions
📊 Sample Data Format
csv
Copy
Team1,Team2,Winner,Team1 Avg Batting Ranking,Team2 Avg Batting Ranking,...
India,Australia,India,85.2,82.1,...
🤝 Contributing
Pull requests are welcome! Please open an issue first to discuss changes.

📜 License
MIT
# Champions-Trophy-Match-Prediction-System
Champions Trophy(Cricket) Match Prediction System Using Machine Learning

## Overview
This project provides a machine learning framework for predicting cricket match scores and outcomes in ICC Champions Trophy matches. It evaluates regression models (XGBoost, Random Forest) for score forecasting and ensemble classifiers for win probability estimation. The system processes 8,500+ ODI matches with 25+ dynamic features, achieving 78.9% prediction accuracy.

![System Architecture](docs/system_architecture.png)

## Features
- **Score Prediction**: Forecasts match scores using advanced regression techniques
- **Win Probability**: Estimates match outcome probabilities with ensemble classifiers
- **Real-time Analysis**: Flask-based web interface for live predictions
- **Comprehensive Features**: 25+ dynamic features including batting context, player form, and environmental factors

## Installation

### Prerequisites
- Python 3.8+
- pip

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Ameya041/cricket-prediction-system.git
   cd cricket-prediction-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the dataset:
   - Place your match data CSV file in the `data/` directory
   - Or use the sample data provided

## Usage

### Training Models
```bash
python train.py --data_path data/matches.csv --model_dir models/
```

### Running the Web Interface
```bash
python app.py
```
Then open `http://localhost:5000` in your browser.

### Making Predictions
You can either:
1. Use the web interface
2. Call the prediction API directly:
   ```python
   import requests
   
   data = {
       'overs': 50,
       'wickets': 0,
       'run_rate': 5.5,
       'team1': 'India',
       'team2': 'Australia',
       'venue': 'Melbourne'
   }
   
   response = requests.post('http://localhost:5000/predict', json=data)
   print(response.json())
   ```

## Project Structure
```
cricket-prediction-system/
├── app.py                # Flask web application
├── train.py              # Model training script
├── predict.py            # Prediction functions
├── requirements.txt      # Python dependencies
├── data/                 # Match datasets
├── models/               # Trained models
├── static/               # Web static files
├── templates/            # Web templates
└── notebooks/            # Jupyter notebooks for analysis
```

## Models
| Model Type       | Algorithm          | Performance  |
|------------------|--------------------|--------------|
| Score Prediction | XGBoost            | MAE: 12.8    |
| Score Prediction | Random Forest      | MAE: 14.1    |
| Win Probability  | Stacked Ensemble   | Accuracy: 78.9% |

## Dataset
The system uses ODI match data from 2000-2023 with the following key features:
- Batting context (overs remaining, wickets fallen, current run rate)
- Player form (30-day weighted averages)
- Environmental factors (venue-specific par scores, dew impact)
- Temporal data (powerplay status, innings phase)

## API Endpoints
- `POST /predict` - Get match predictions
- `GET /features` - List available features
- `GET /model_info` - Get model performance metrics

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.


