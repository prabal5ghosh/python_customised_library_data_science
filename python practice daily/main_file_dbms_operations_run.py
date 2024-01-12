

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
from python_library_main.database_utils import *
from python_library_main.dbms_professor import *


""" Database operations"""



db = DatabaseUtils('prabal_dbms.db')
database_table = db.create_table('student_data1', ['id INTEGER', 'name TEXT', 'age INTEGER'])
database_table_data = db.insert_data('student_data1', (2, 'Prabal Ghosh', 28))
updated_database_table_data = db.update_data('student_data1', {'age': 26}, 'id = 1')
# database_table_data_deleted = db.delete_row('student_data1', 'id = 1')
result = db.select_data('student_data1')
print("Selected data:", result)
db.close_connection()






# DB_FILE = 'knights.db'

# # 'id', 'surname', 'complement', 'name', 'sex', 'birth', 'death'

# s1 = """CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY, surname TEXT, 
# complement TEXT, name TEXT, sex TEXT, birth INTEGER, death INTEGER)"""

# # 'id', 'father', 'mother', 'brothers', 'sisters'

# s2 = """CREATE TABLE IF NOT EXISTS family (id INTEGER PRIMARY KEY, father INTEGER,
# mother INTEGER, brothers BLOB, sisters BLOB, FOREIGN KEY(id) REFERENCES person(id))"""


# dbms_object = DBMS(DB_FILE)
# dbms_object.create_tables(s1)
