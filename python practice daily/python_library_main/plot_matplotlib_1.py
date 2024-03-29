import pandas as pd
#%matplotlib inline

import matplotlib.pyplot as plt
from matplotlib import cm

class CSVPlotter:
    # def __init__(self, file_path):
    #     self.file_path = file_path

    # def load_data(self):
    #     try:
    #         data = pd.read_csv(self.file_path)
    #         return data
    #     except FileNotFoundError:
    #         print("File not found. Please check the file path.")
    #         return None

    def __init__(self, data):
        self.data = data

    def plot_line_chart(self, x_column, y_column, title="Line Chart"):
        # data = self.load_data()
        data = self.data
        if data is not None:
            plt.figure(figsize=(8, 6))
            #plt.plot(data[x_column], data[y_column])
            data.plot(kind='line', x=x_column, y=x_column)

            plt.title(title)
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.grid(True)
            plt.show()

    def plot_bar_chart(self, x_column, y_column, title="Bar Chart"):
        # data = self.load_data()
        data = self.data

        if data is not None:
            plt.figure(figsize=(8, 6))
            #plt.bar(data[x_column], data[y_column])
            #plt.bar(data[x_column], data[x_column].value_counts())
            data[x_column].value_counts().plot(kind='bar',color='red')

            plt.title(title)
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    def plot_scatter_plot(self, x_column, y_column, title="Scatter Plot"):
        # data = self.load_data()
        data = self.data

        if data is not None:
            plt.figure(figsize=(8, 6))
            #plt.scatter(data[x_column], data[y_column])
            data.plot(kind='scatter', x=x_column, y=y_column)
            plt.title(title)
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.grid(True)
            plt.show()
            
    def plot_pair_plot(self,data,c=None, marker='o',bins=15):
        cmap = cm.get_cmap('gnuplot')
        pd.plotting.scatter_matrix(data, c=c, marker= marker, hist_kwds={'bins': bins}, cmap=cmap, figsize=(12,12))
        plt.show()

# file_path = 'C:\\Users\\praba\\Desktop\\uca1\\M1\\python-ml\\sales_data.csv'

# csv_plotter = CSVPlotter(file_path)

# Plot Line Chart
# csv_plotter.plot_line_chart('x_axis', 'y_axis', title='Line Chart Example')

# Plot Bar Chart
# csv_plotter.plot_bar_chart('categories', 'values', title='Bar Chart Example')

# Plot Scatter Plot
# csv_plotter.plot_scatter_plot('Year', 'Customer_Age', title='Scatter Plot Example')

def plot_line_bar_scatter(data, x_axis, y_axis=None,c=None, marker= None, bins=None, plot_type='bar'):

    csv_plotter = CSVPlotter(data)
    if plot_type == 'line':
        csv_plotter.plot_line_chart(x_axis , y_axis, title='Line Chart Example')
    elif plot_type == 'bar':
        csv_plotter.plot_bar_chart(x_axis , y_axis, title='Bar Chart Example')
    elif plot_type == 'scatter':
        csv_plotter.plot_scatter_plot(x_axis , y_axis, title='Scatter Plot Example')
    elif plot_type == 'pair':
        csv_plotter.plot_pair_plot(data ,c, marker, bins)
    else:
        print("please choose type= line or bar or scatter")






