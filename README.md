# 🏏 Cricket Match Prediction System

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

