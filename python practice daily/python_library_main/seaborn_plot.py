import matplotlib.pyplot as plt
import seaborn as sns
import math
import pandas as pd

class SeabornBoxPlotter:
    def __init__(self, num_rows=1, num_cols=4, figsize=(18, 5)):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.figsize = figsize

    def _calculate_subplot_layout(self, num_features_count):
        num_rows = math.ceil(num_features_count / self.num_cols)
        return num_rows, self.num_cols

    def plot_boxplots(self, df, num_features):
        try:
            num_features_count = len(num_features)
            num_rows, num_cols = self._calculate_subplot_layout(num_features_count)
            
            fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(self.figsize[0],self.figsize[1]*num_rows))

            for i, column in enumerate(num_features):
                row = i // num_cols
                col = i % num_cols
                sns.boxplot(x=df[column], ax=axes[row, col])
                axes[row, col].set_title(f'Boxplot of {column}')
                axes[row, col].set_xlabel(column)

            for i in range(num_features_count, num_rows * num_cols):
                row = i // num_cols
                col = i % num_cols
                fig.delaxes(axes[row, col])

            plt.tight_layout()
            plt.show()


        except Exception as e:
            print(f"An error occurred: {e}")



    def plot_histplots(self, df):
        df.hist(figsize=[30,30])
        plt.show()


class SeabornHistPlotter:
    def __init__(self, figsize=(18, 5)):
        self.figsize = figsize


