import pandas as pd
import numpy as np

def check_duplicated(dataframe):
    return dataframe[dataframe.duplicated()]


def find_outliers_3sigma(data):
    outliers = []
    for column in data.columns:
        mean = np.mean(data[column])
        std = np.std(data[column])
        for value in data[column]:
            z_score = (value - mean) / std
            if np.abs(z_score) > 3:  # it is an outlier
                outliers.append((value, column))
    return outliers

def most_common_velocity(dataframe):
    dataframe['Mayor velocidad'] = dataframe.iloc[:, 4:].idxmax(axis=1)
    dataframe['Mayor velocidad'] = dataframe['Mayor velocidad'].str.replace(' Mbps','')
    dataframe['Mayor velocidad'] = dataframe['Mayor velocidad'].str.replace(',','.')
    dataframe['Mayor velocidad'] = dataframe['Mayor velocidad'].astype('float')
    return dataframe

    