import pandas as pd
from sklearn.preprocessing import OneHotEncoder

class DataFrameOperations:
    def __init__(self, dataframe):
        self.df = dataframe

    def drop_missing_values_row_column(self,axis = 0,inplace=False):
        try:
            return self.df.dropna(axis= axis, inplace= inplace)
        except Exception as e:
            print(f"Error occured: {str(e)}")
            # raise

    def calculate_summary_statistics(self):
        try:
            return self.df.describe()
        except Exception as e:
            print(f"Error occured: {str(e)}")
            # raise

    def count_unique_values(self, column_name):
        try:
            return self.df[column_name].nunique()
        except Exception as e:
            print(f"Error occured: {str(e)}")
            # raise

    def filter_rows(self, condition):
        try:
            return self.df[self.df.eval(condition)]
        except Exception as e:
            print(f"Error occured: {str(e)}")
            # raise
        

    # def encode_categorical_variable(self, column_name):
    #     return pd.get_dummies(self.df[column_name], prefix=column_name, drop_first=True)


    def encode_categorical_variable(self, column_name):
        try:
            # Extract the specified column
            column_data = self.df[[column_name]]

            # Use OneHotEncoder
            encoder = OneHotEncoder(sparse_output=False, drop='first')
            encoded_data = encoder.fit_transform(column_data)

            # Create new column names based on categories
            column_names = [f"{column_name}_{category}" for category in encoder.get_feature_names_out([column_name])]

            # Create a DataFrame with the encoded columns
            encoded_df = pd.DataFrame(encoded_data, columns=column_names)

            # Concatenate the original DataFrame with the encoded DataFrame
            self.df = pd.concat([self.df, encoded_df], axis=1)

            return self.df

        except Exception as e:
            print(f"Error encoding categorical variable: {str(e)}")
            # raise

    
    def dataframe_one_hot(self, column_name):
        try:
            one_hot_column = self.encode_categorical_variable(column_name)
            return one_hot_column.drop(column_name, axis=1)
        except Exception as e:
            print(f"Error encoding categorical variables in a dataframe:{str(e)}")
            # raise
