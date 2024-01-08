import numpy as numpy
import pandas as pd

class Data_drop():
    def __init__(self,data,col_row,axis):
        self.data = data
        self.col_row=col_row
        self.axis=axis
    def drop_column(self):
        df = self.data.drop(self.col_row, self.axis)
        return df
    def drop_row(self):
        df = self.data.drop(self.col_row, self.axis)
        return df


def drop_row(data,col_row):
    object_drop = Data_drop(data,col_row,axis=0)
    return object_drop.drop_row()

def drop_column(data,col_row):
    object_drop = Data_drop(data,col_row,axis=1)
    return object_drop.drop_column()

    