import math

import pandas as pd
import numpy as np

class MathOperations:
    def __init__(self, dataframe):
        try:
            self.df = dataframe
            if not isinstance(self.df, pd.DataFrame):
                raise ValueError("Input must be a pandas DataFrame.")
            print("MathOperations initialized successfully.")

        except Exception as e:
            print(f"Error initializing MathOperations: {str(e)}")
            raise

    def calculate_mean(self, column_name):
        try:
            mean_value = self.df[column_name].mean()
            return mean_value

        except Exception as e:
            print(f"Error calculating mean: {str(e)}")
            raise

    def calculate_mode(self, column_name):
        try:
            mode_value = self.df[column_name].mode()[0]
            return mode_value

        except Exception as e:
            print(f"Error calculating mode: {str(e)}")
            raise

    def calculate_median(self, column_name):
        try:
            median_value = self.df[column_name].median()
            return median_value

        except Exception as e:
            print(f"Error calculating median: {str(e)}")
            raise

    def calculate_sum(self, column_name):
        try:
            sum_value = self.df[column_name].sum()
            return sum_value

        except Exception as e:
            print(f"Error calculating sum: {str(e)}")
            raise


