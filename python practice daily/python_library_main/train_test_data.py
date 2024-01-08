# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 00:47:30 2024

@author: praba
"""


import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np


class Data_split:
    def __init__(self, data, target,test_size, random_state):
        self.X = data
        self.y = target
        self.test_size = test_size
        self.random_state = random_state

    def train_test_data(self):
        #X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=self.random_state)
        #return X_train, X_test, y_train, y_test
        try:
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y,test_size=self.test_size, random_state = self.random_state)
            return X_train, X_test, y_train, y_test
        except Exception as e:
            print(f"Error occurred: {e}")
            return None, None, None, None  # Return placeholders if an exception occurs


def split_data(data, target,test_size=0.2, random_state=0):
    object_data_split = Data_split(data, target,test_size, random_state)
    return object_data_split.train_test_data()

