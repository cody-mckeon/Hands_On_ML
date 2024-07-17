import pandas as pd
import os

HOUSING_PATH = "/Users/codymckeon/Desktop/Dev/hands_on_ml/datasets/housing"

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)