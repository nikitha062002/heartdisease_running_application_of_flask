import pickle
import numpy as np

def load_model():
    with open('all_models.pkl', 'rb') as file:
        model = pickle.load(file)
    return model
