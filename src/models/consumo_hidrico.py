from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
import random
from preprocessing import preprocess_plants

def garden_water_compsumption(features, targets, user_data):

    X_train, X_val, y_train, y_val = train_test_split(features, targets['water_consumption'], test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_val_pred = model.predict(X_val)
    mse = mean_squared_error(y_val, y_val_pred)
    print(f"Mean Squared Error: {mse}")

    return model.predict(user_data)


if __name__ == '__main__':
    plants = pd.read_csv('src/bdd/plantas.csv')
    
    plants = preprocess_plants(plants)
    plants = plants.drop('type', axis=1)
    print(plants)
    targets_data = {
        'water_consumption': [random.randint(1, 5) for _ in range(15)],
        'colorfulness': [random.randint(1, 5) for _ in range(15)],
        'pollinator_attraction': [random.choice([True, False]) for _ in range(15)],
        'bird_attraction': [random.choice([True, False]) for _ in range(15)],
        'aroma': [random.choice([True, False]) for _ in range(15)],
        'care_intensity': [random.randint(1, 5) for _ in range(15)],
        'year_round_floral': [random.choice([True, False]) for _ in range(15)]
    }
    targets = pd.DataFrame(targets_data)
    user_data = {
    }
    wc_pred = garden_water_compsumption(plants, targets, user_data)
    print(wc_pred)
