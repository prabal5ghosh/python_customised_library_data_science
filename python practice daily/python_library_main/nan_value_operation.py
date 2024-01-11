import pandas as pd
import numpy as np

class Handling_Nan:
    def __init__(self, dataframe):
        self.df = dataframe

    def handle_missing_values(self, strategy='mean'):
        try:
            # Find the number of null values for each column
            null_counts = self.df.isnull().sum()

            # Replace null values based on the provided strategy
            for column in self.df.columns:
                if self.df[column].dtype == 'object':
                    # Categorical column
                    most_frequent_value = self.df[column].mode()[0]
                    self.df[column].fillna(most_frequent_value, inplace=True)
                else:
                    # Numerical column
                    if strategy == 'mean':
                        replacement_value = self.df[column].mean()
                    elif strategy == 'median':
                        replacement_value = self.df[column].median()
                    elif strategy == 'mode':
                        replacement_value = self.df[column].mode()[0]
                    else:
                        raise ValueError("Invalid strategy. Use 'mean', 'median', or 'mode'.")

                    self.df[column].fillna(replacement_value, inplace=True)

            return null_counts

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
        
    def chack_columns_with_nan(self):
        try:
            missing_columns = len(self.df) - self.df.loc[:, np.sum(self.df.isnull())>0].count()
            return missing_columns
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
    def is_null_value_present(self):
        try:
            # null_counts = self.df.isnull().sum().sum()
            null_counts = self.df.isnull().any().any()
            return null_counts
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None



