# my_regex_library.py
import pandas as pd

class RegexDataFrameOperations:
    def __init__(self, dataframe):
        self.df = dataframe

    def select_rows(self, column_name, pattern):
        return self.df[self.df[column_name].str.contains(pattern, na=False)]

    def remove_rows(self, column_name, pattern):
        return self.df[~self.df[column_name].str.contains(pattern, na=False)]

    def modify_data(self, column_name, pattern, replacement):
        self.df[column_name] = self.df[column_name].str.replace(pattern, replacement)

    def extract_data(self, column_name, pattern, new_column_name):
        self.df[new_column_name] = self.df[column_name].str.extract(pattern)

    def remove_characters(self, column_name, pattern):
        self.df[column_name] = self.df[column_name].str.replace(pattern, '')



