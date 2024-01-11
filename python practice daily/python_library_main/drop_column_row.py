import numpy as numpy
import pandas as pd

class Data_drop():
    def __init__(self,data,col_row,axis):
        self.data = data
        self.col_row=col_row
        self.axis=axis
    def drop_column(self):
        try:
            df = self.data.drop(labels= self.col_row, axis= self.axis)
            return df
        except Exception as e:
            print(f"Error occured: {str(e)}")
            # raise
    def drop_row(self):
        try:
            df = self.data.drop(labels = self.col_row,axis =  self.axis)
            return df
        except Exception as e:
            print(f"Error occured: {str(e)}")
            # raise


def drop_row(data,col_row):
    try:
        object_drop = Data_drop(data,col_row,axis=0)
        return object_drop.drop_row()
    except Exception as e:
            print(f"Error occured: {str(e)}")
            # raise

def drop_column(data,col_row):
    try:
        object_drop = Data_drop(data,col_row,axis=1)
        return object_drop.drop_column()
    except Exception as e:
        print(f"Error occured: {str(e)}")
        # raise
    