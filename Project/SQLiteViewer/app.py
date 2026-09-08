import sqlite3

class Viewer:
    def __init__(self,db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()


    def get_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        # [('users',), ('orders',), ('products',)]
        return [table[0] for table in tables]

    def get_table_data(self,table_name):
        result = {}
        for name in table_name:
            self.cursor.execute(f"SELECT * FROM {name};")
            result[name] = self.cursor.fetchall()
        return result

    def get_table_columns(self,table_name):
        self.cursor.execute(f"PRAGMA table_info({table_name});")
        columns = self.cursor.fetchall()
        # [(0, 'id', 'INTEGER', 1, None, 1), (1, 'name', 'TEXT', 0, None, 0)]
        return [column[1] for column in columns]

    def get_table_schema(self, table_name):
        self.cursor.execute(f"PRAGMA table_info({table_name});")
        return self.cursor.fetchall()

    def search_table(self, table_name, column_name, value):
        quoted_table = '"' + table_name.replace('"', '""') + '"'
        quoted_column = '"' + column_name.replace('"', '""') + '"'
        self.cursor.execute(
            f"SELECT * FROM {quoted_table} WHERE {quoted_column} = ?;",
            (value,),
        )
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
