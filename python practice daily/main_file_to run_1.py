# from python_library_main import area_cal as ac

# ac.area_rectangle(4,5)

"""IMPORT MODULES"""
from python_library_main.area_cal import *
from python_library_main.open_file import *
from python_library_main.plot_matplotlib_1 import *
from python_library_main.train_test_data import *
from python_library_main.drop_column_row import *
from python_library_main.my_regex_library import *
from python_library_main.nan_value_operation import *
# area_rectangle(4,5)


""" OPEN CSV JSON EXCEL DATA"""
# df_file1 = file_opening(file_path='C:\\Users\\praba\\Desktop\\uca1\\M1\\python-ml\\file_example_XLSX_50.XLSX', file_type='XLSX')
# df_file2 = file_opening(file_path='C:\\Users\\praba\\Desktop\\uca1\\M1\\python-ml\\sales_data.csv', file_type='csv')
#complaints = file_opening(file_path='C:\\Users\\praba\\Desktop\\uca1\\M1\\python-ml\\311_small.csv', file_type='csv')
# print(file1.head(10))
# print(file2.head(10))

energy_df = file_opening("C:\\Users\\praba\\Desktop\\uca1\\M1\\ML\\final project\\data.csv\data.csv",file_type='csv')



""" DIFFERENT PLOTS USING MATPLOTLIB"""

# plot_line_bar_scatter(data=df_file2, x_axis='Year', y_axis='Customer_Age', plot_type='pair',c=file2['Revenue'], marker= "*", bins=30)


# x_data = df_file2.iloc[:, 0:-1]  
# # Extracting 'target' data using iloc
# target_data = df_file2.iloc[:, -1]  # Assuming the target column is the last column



"""DATA SPLITTING OPERATION"""
# # Splitting the data
# X_train, X_test, y_train, y_test = split_data(data=x_data, target=target_data,test_size=0.3, random_state=32)

# # Now you can use X_train, X_test, y_train, y_test for further processing

# if X_train is not None:
#     # if the data split was successful
#     print(y_test)
# else:
#     # Handle the case where the data split failed
#    print("data was not splited")
#    pass



"""ROW COLUMN DROP OPERATIONS"""
# df_file_2_new_col = drop_column(df_file2, df_file2.columns[[1,2]])

# df_file_2_new_row = drop_row(df_file2, [0,1])


"""REGEX OPERATIONS"""
#df = pd.DataFrame({'text_column': ['abc', 'def456', 'ghi789', 'jkl012']})
#regex_operations = RegexDataFrameOperations(energy_df)

# selected_rows = regex_operations.select_rows('State_Factor', r'\d+')
# print(selected_rows)

#regex_operations.modify_data(column_name = 'State_Factor', pattern=r'\d+', replacement= 'REPLACED')
#print(energy_df)


""" HANDLING MISSING VALUES IN DATAFRAME"""


#utils = Handling_Nan(energy_df)
#null_counts = utils.is_null_value_present()
#null_counts = utils.chack_columns_with_nan()

#null_counts = utils.handle_missing_values(strategy='mode')

#print("Number of null values:")
#print(null_counts)



"""DATABASE OPERATIONS"""

# Example usage:
# from database_utils import DatabaseUtils
#
# db = DatabaseUtils('example.db')
# db.create_table('example_table', ['id INTEGER', 'name TEXT', 'age INTEGER'])
# db.insert_data('example_table', (1, 'John Doe', 25))
# db.update_data('example_table', {'age': 26}, 'id = 1')
# result = db.select_data('example_table')
# print("Selected data:", result)
# db.close_connection()