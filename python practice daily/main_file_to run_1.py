# from python_library_main import mathes_operation as ac



"""IMPORT MODULES"""
from python_library_main.mathes_operation import *
from python_library_main.open_file import *
from python_library_main.plot_matplotlib_1 import *
from python_library_main.train_test_data import *
from python_library_main.drop_column_row import *
from python_library_main.my_regex_library import *
from python_library_main.nan_value_operation import *
from python_library_main.dataframe_operation import *
from python_library_main.modify_colimn_data import *
from python_library_main.seaborn_plot import *
from python_library_main.numerical_categorial_text import *
from python_library_main.check_outlaiers import *

""" OPEN CSV JSON EXCEL DATA"""
# df_file1 = file_opening(file_path='C:\\Users\\praba\\Desktop\\uca1\\M1\\python-ml\\file_example_XLSX_50.XLSX', file_type='XLSX')
df_file2 = file_opening(file_path='C:\\Users\\praba\\Desktop\\uca1\\M1\\python-ml\\sales_data.csv', file_type='csv')
#complaints = file_opening(file_path='C:\\Users\\praba\\Desktop\\uca1\\M1\\python-ml\\311_small.csv', file_type='csv')
# print(file1.head(10))
# print(file2.head(10))

energy_df = file_opening("C:\\Users\\praba\\Desktop\\uca1\\M1\\ML\\final project\\data.csv\data.csv",file_type='csv')



""" DIFFERENT PLOTS USING MATPLOTLIB"""

# plot_line_bar_scatter(data=df_file2, x_axis='Year', y_axis='Customer_Age', plot_type='pair',c=file2['Revenue'], marker= "*", bins=30)




"""DATA SPLITTING OPERATION"""
# # Splitting the data


x_data = energy_df.iloc[:, 0:-1]  
# Extracting 'target' data using iloc
target_data = energy_df.iloc[:, -1]  # Assuming the target column is the last column

X_train, X_test, y_train, y_test = split_data(data=x_data, target=target_data,test_size=0.3, random_state=32)

# # Now you can use X_train, X_test, y_train, y_test for further processing

if X_train is not None:
    # if the data split was successful
    print(y_test.shape)
    print(X_test.shape)

else:
    # Handle the case where the data split failed
    print("data was not splited")
    pass





"""ROW COLUMN DROP OPERATIONS"""
df_file_2_new_col = drop_column(df_file2, df_file2.columns[[1,2]])

df_file_2_new_row = drop_row(df_file2, [0,1])




"""REGEX OPERATIONS"""
# df = pd.DataFrame({'text_column': ['abc', 'def456', 'ghi789', 'jkl012']})
regex_operations = RegexDataFrameOperations(energy_df)

# selected_rows = regex_operations.select_rows('State_Factor', r'\d{1}')
# print(selected_rows)
after_removal_rows = regex_operations.remove_rows(column_name='State_Factor', pattern = r'^\D*\d\D*$')

print(after_removal_rows)

regex_operations.modify_data(column_name = 'State_Factor', pattern=r'\d+', replacement= 'REPLACED')
print(energy_df)




""" HANDLING MISSING VALUES IN DATAFRAME"""


utils = Handling_Nan(energy_df)
null_counts = utils.is_null_value_present()
null_counts = utils.chack_columns_with_nan()

null_counts = utils.handle_missing_values(strategy='mode')

print("Number of null values:")
print(null_counts)



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



"""Different maths operation"""

math_operations = MathOperations(energy_df)

mean_value = math_operations.calculate_mean(column_name="energy_star_rating")
mode_value = math_operations.calculate_mode(column_name="energy_star_rating")
median_value = math_operations.calculate_median(column_name="energy_star_rating")
sum_value = math_operations.calculate_sum(column_name="energy_star_rating")

print("Mean:", mean_value)
print("Mode:", mode_value)
print("Median:", median_value)
print("Sum:", sum_value)




"""Different dataframe operations"""
# data = {'A': [1, 2, 3, None, 5],
#         'B': ['X', 'Y', 'Z', 'X', 'Y']}
# df = pd.DataFrame(data)


df_operations = DataFrameOperations(energy_df)

cleaned_data = df_operations.drop_missing_values_row_column(axis=1)
summary_stats = df_operations.calculate_summary_statistics()
# unique_values = df_operations.count_unique_values('Year_Factor')
filtered_rows = df_operations.filter_rows('Year_Factor == 2 ')
# encoded_column = df_operations.encode_categorical_variable('Year_Factor')
encoded_df = df_operations.dataframe_one_hot('Year_Factor')




"MODIFY COLUMNS DATA"
# Use the custom library function to modify a specific column
modify_col_obj= ModifyColumn(energy_df)

def modify_building_class(building_class):
    return 1 if building_class == 'Commercial' else 0

modified_df = modify_col_obj.modify_column( 'building_class', modify_building_class)

print("DataFrame after applying the function to column 'building_class':")
print(modified_df)


"""NUMERICAL CATEGORICAL TEXT DATA COLUMNS NAME """

feature_categorizer = FeatureCategorizer(energy_df)

    # Call the categorize_features method
result = feature_categorizer.categorize_features()

# Print the result
if isinstance(result, dict):
    for category, features in result.items():
        print(f"{category}:\n{features}")
else:
    print(result)




"""SEABORN PLOTS - BOX PLOT HIST PLOT"""

plotter = SeabornBoxPlotter()
Num_features = result['Numerical_Features']
# plotter.plot_boxplots(energy_df, Num_features)

# plotter.plot_histplots(energy_df)



"""Chcek OUTLAIERS"""

outliers_checker = OutlaiersCheck(energy_df)
num_features = result['Numerical_Features']
outliers = outliers_checker.check_outlaiers(num_features)
# Print the outliers
print("Outliers:")
for feature, values in outliers.items():
    print(f"{feature}: {values}")
    print("\n")
