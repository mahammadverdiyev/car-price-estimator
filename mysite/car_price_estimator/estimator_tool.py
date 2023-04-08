import numpy as np
import pandas as pd
import pickle

import sklearn.preprocessing as sp
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import sklearn.metrics as met
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline


def perform_scaling(train_data, new_data):
    scaler = RobustScaler()

    train_scaled = scaler.fit_transform(train_data)
    test_scaled = scaler.transform([new_data])

    return test_scaled


def predict_price(data):
    with open('car_price_estimator/model.pkl', 'rb') as f:
        model = pickle.load(f)
        estimated_price = np.exp(model.predict(data))
        return estimated_price


def prepare_data(data):
    data['brand'] = data['brand'].split('->')[1]
    data['model'] = data['model'].split('->')[1]
    data['distance_traveled'] = int(data['distance_traveled'])
    data['engine_power'] = int(data['engine_power'])
    data['is_damaged'] = int(data['is_damaged'])
    data['is_painted'] = int(data['is_painted'])
    data['year'] = int(data['year'])
    data['engine_volume'] = int(data['engine_volume'])/1000

    data = pd.Series(data)

    df = pd.read_csv('car_price_estimator/turbo_data.csv')

    data['fuel_type_avg'] = df[df['fuel_type'] ==
                               data['fuel_type']].fuel_type_avg.iloc[0]

    data['gearbox_avg'] = df[df['gearbox'] ==
                             data['gearbox']].gearbox_avg.iloc[0]

    data['brand_avg'] = df[df['brand'] == data['brand']].brand_avg.iloc[0]
    data['model_avg'] = df[df['model'] == data['model']].model_avg.iloc[0]

    data['body_type_avg'] = df[df['body_type'] ==
                               data['body_type']].body_type_avg.iloc[0]
    data['color_avg'] = df[df['color'] == data['color']].color_avg.iloc[0]
    data['powertrain_avg'] = df[df['powertrain'] ==
                                data['powertrain']].powertrain_avg.iloc[0]

    data['new_Xeyr'] = 1 if data['new'] == 'Xeyr' else 0
    df = df.drop(['brand', 'model', 'body_type', 'color', 'fuel_type', 'gearbox',
                  'powertrain'], axis=1)
    data = data.drop(['brand', 'model', 'body_type', 'color', 'fuel_type', 'gearbox',
                      'powertrain', 'new'])

    scaled_data = perform_scaling(df, data)

    return scaled_data
