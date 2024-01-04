# from python_library_main import area_cal as ac

# ac.area_rectangle(4,5)

from python_library_main.area_cal import *
from python_library_main.open_file import *
from python_library_main.plot_matplotlib_1 import *
area_rectangle(4,5)


file1 = file_opening(file_path='C:\\Users\\praba\\Desktop\\uca1\\M1\\python-ml\\file_example_XLSX_50.XLSX', file_type='XLSX')
file2 = file_opening(file_path='C:\\Users\\praba\\Desktop\\uca1\\M1\\python-ml\\sales_data.csv', file_type='csv')

# print(file1.head(10))
# print(file2.head(10))



plot_line_bar_scatter(data=file2, x_axis='Year', y_axis='Customer_Age', plot_type='bar')