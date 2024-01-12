import pandas as pd

class ModifyColumn():
    def __init__(self, dataframe):
        self.df = dataframe
    def modify_column(self,column_name, modification_func):

        self.df[column_name] = self.df[column_name].apply(modification_func)
        return self.df

