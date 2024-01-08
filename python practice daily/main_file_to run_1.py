# from python_library_main import area_cal as ac

# ac.area_rectangle(4,5)

from python_library_main.area_cal import *
from python_library_main.open_file import *
from python_library_main.plot_matplotlib_1 import *
from python_library_main.train_test_data import *


area_rectangle(4,5)


df_file1 = file_opening(file_path='C:\\Users\\praba\\Desktop\\uca1\\M1\\python-ml\\file_example_XLSX_50.XLSX', file_type='XLSX')
df_file2 = file_opening(file_path='C:\\Users\\praba\\Desktop\\uca1\\M1\\python-ml\\sales_data.csv', file_type='csv')

# print(file1.head(10))
# print(file2.head(10))



#plot_line_bar_scatter(data=df_file2, x_axis='Year', y_axis='Customer_Age', plot_type='pair',c=file2['Revenue'], marker= "*", bins=30)


x_data = df_file2.iloc[:, 0:-1]  
# Extracting 'target' data using iloc
target_data = df_file2.iloc[:, -1]  # Assuming the target column is the last column



# Splitting the data
X_train, X_test, y_train, y_test = split_data(data=x_data, target=target_data, random_state=32)

# Now you can use X_train, X_test, y_train, y_test for further processing

if X_train is not None:
    # if the data split was successful
    print(y_test)
else:
    # Handle the case where the data split failed
    pass