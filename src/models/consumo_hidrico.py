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


