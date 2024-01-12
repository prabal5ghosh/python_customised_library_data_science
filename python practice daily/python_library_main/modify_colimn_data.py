import pandas as pd

class ModifyColumn():
    def __init__(self, dataframe):
        self.df = dataframe
    def modify_column(self,column_name, modification_func):
        try:
            self.df[column_name] = self.df[column_name].apply(modification_func)
            return self.df
        except Exception(e):
            print(f"it is suffering from the following issue: {str(e)}")

