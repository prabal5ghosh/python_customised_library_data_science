import sqlite3

class DatabaseUtils:
    def __init__(self, database_name):
        try:
            self.connection = sqlite3.connect(database_name)
            self.cursor = self.connection.cursor()
            print("Connected to the database successfully.")

        except Exception as e:
            print(f"Error connecting to the database: {str(e)}")
            raise

    def create_table(self, table_name, columns):
        try:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
            self.cursor.execute(query)
            self.connection.commit()
            print(f"Table '{table_name}' created successfully.")

        except Exception as e:
            print(f"Error creating table: {str(e)}")
            raise

    def insert_data(self, table_name, values):
        try:
            query = f"INSERT INTO {table_name} VALUES ({', '.join(['?' for _ in values])})"
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Data inserted successfully.")

        except Exception as e:
            print(f"Error inserting data: {str(e)}")
            raise

    def update_data(self, table_name, set_values, condition):
        try:
            query = f"UPDATE {table_name} SET {', '.join([f'{column} = ?' for column in set_values.keys()])} WHERE {condition}"
            self.cursor.execute(query, list(set_values.values()))
            self.connection.commit()
            print("Data updated successfully.")

        except Exception as e:
            print(f"Error updating data: {str(e)}")
            raise

    def delete_row(self, table_name, condition):
        try:
            query = f"DELETE FROM {table_name} WHERE {condition}"
            self.cursor.execute(query)
            self.connection.commit()
            print("Row deleted successfully.")

        except Exception as e:
            print(f"Error deleting row: {str(e)}")
            raise

    def select_data(self, table_name, columns="*", condition=None, group_by=None, order_by=None):
        try:
            query = f"SELECT {columns} FROM {table_name}"

            if condition:
                query += f" WHERE {condition}"

            if group_by:
                query += f" GROUP BY {group_by}"

            if order_by:
                query += f" ORDER BY {order_by}"

            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result

        except Exception as e:
            print(f"Error selecting data: {str(e)}")
            raise

    def close_connection(self):
        try:
            self.connection.close()
            print("Connection closed successfully.")

        except Exception as e:
            print(f"Error closing connection: {str(e)}")
            raise

