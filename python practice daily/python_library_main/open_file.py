import pandas as pd

class FileOpener:
    def __init__(self, file_path):
        self.file_path = file_path

    def open_csv(self):
        try:
            data = pd.read_csv(self.file_path)

            return data
        except FileNotFoundError:
            print("File not found. Please check the file path.")
            return None

    def open_excel(self, sheet_name=None):
        try:
            data = pd.read_excel(self.file_path, sheet_name=sheet_name)
            return data
        except FileNotFoundError:
            print("File not found. Please check the file path.")
            return None

    def open_json(self):
        try:
            data = pd.read_json(self.file_path)
            return data
        except FileNotFoundError:
            print("File not found. Please check the file path.")
            return None

    def open_file(self, file_type, **kwargs):
        if file_type == 'csv':
            return self.open_csv()
        elif file_type == 'XLSX':
            sheet_name = kwargs.get('sheet_name')
            return self.open_excel(sheet_name)
        elif file_type == 'json':
            return self.open_json()
        else:
            print("Unsupported file type. Please use 'csv', 'excel', or 'json'.")
            return None

# Example usage:

def file_opening(file_path, file_type):
    file_path = file_path
    file_type = file_type
    # file_path = 'C:\\Users\\praba\\Desktop\\uca1\\M1\\python-ml\\file_example_XLSX_50.XLSX'
    file_opener = FileOpener(file_path)

    # Open CSV file
    if file_type == 'csv':
        csv_data = file_opener.open_file('csv')
        if csv_data is not None:
            print("CSV File Content:")
            print(csv_data.head())
            return csv_data

    # Open Excel file
    elif file_type == 'XLSX':
        excel_data = file_opener.open_file('XLSX', sheet_name='Sheet1')
        if excel_data is not None:
            print("\nExcel File Content:")
            print(excel_data.head())
            return excel_data

    # Open JSON file
    elif file_type == 'json':
        json_data = file_opener.open_file('json')
        if json_data is not None:
            print("\nJSON File Content:")
            print(json_data.head())
            return json_data
    else:
            print("Unsupported file type. Please use 'csv', 'excel', or 'json'.")
            return None
