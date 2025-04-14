import numpy as np
from sklearn.preprocessing import MinMaxScaler

def preprocess_input(input_data):
    """Preprocess input data for model prediction"""
    # Calculate derived features
    batting_strength_diff = input_data['team1_batting'] - input_data['team2_batting']
    bowling_strength_diff = input_data['team1_bowling'] - input_data['team2_bowling']
    experience_diff = input_data['team1_ct_participated'] - input_data['team2_ct_participated']
    
    # Score prediction features
    score_features = np.array([
        input_data['team1_batting'],
        input_data['team2_bowling'],
        input_data['wl_ratio'],
        input_data['team1_ct_participated'],
        batting_strength_diff,
        bowling_strength_diff
    ])
    
    # Outcome prediction features
    outcome_features = np.array([
        input_data['team1_batting'],
        input_data['team2_batting'],
        input_data['team1_bowling'],
        input_data['team2_bowling'],
        input_data['wl_ratio'],
        input_data['team1_ct_won'],
        input_data['team2_ct_won'],
        batting_strength_diff,
        bowling_strength_diff,
        experience_diff
    ])
    
    return {
        'score_features': score_features,
        'outcome_features': outcome_features
    }