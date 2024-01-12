import sqlite3

DB_FILE = 'knights.db'

# # 'id', 'surname', 'complement', 'name', 'sex', 'birth', 'death'

# s1 = """CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY, surname TEXT, 
# complement TEXT, name TEXT, sex TEXT, birth INTEGER, death INTEGER)"""

# # 'id', 'father', 'mother', 'brothers', 'sisters'

# s2 = """CREATE TABLE IF NOT EXISTS family (id INTEGER PRIMARY KEY, father INTEGER,
# mother INTEGER, brothers BLOB, sisters BLOB, FOREIGN KEY(id) REFERENCES person(id))"""


class DBMS:
    def __init__(self, dbfile=DB_FILE):
        self.conn = sqlite3.connect(dbfile)
        # self._create_tables()

    # def _create_tables(self,s1):
    def create_tables(self,s1):
    
        cur = self.conn.cursor()
        cur.execute(s1)
        # cur.execute(s2)
        self.conn.commit()
        print(f"Table  created successfully.")


    def insert_data(self, **kwargs):
        table = kwargs.pop('table', None)
        data = kwargs.pop('data', None)

        if not table:
            raise RuntimeError('Specify a table name!')
        if not data:
            raise RuntimeError('Add some data. None provided!')
    
        # data = [(x1, x2, x3), (x4,x5,x6),.....]
        # data[0] = (x1, x2, x3)
        placeholder_str = ','.join('?' * len(data[0]))
        template = f"INSERT INTO {table} VALUES ({placeholder_str})"
        cur = self.conn.cursor()
        
        # map(print(template), data)
        cur.executemany(template, data)
        
        self.conn.commit()

    def raw_query(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchall()

    def query_data(self, **kwargs):
        table = kwargs.pop('table', None)
        clause = kwargs.pop('where', None)
        attr_list = kwargs.pop('attrs', None)
        if not table:
            raise AttributeError('Nope')
        if not attr_list:
            attr_str = '*'
        else:
            attr_str = ','.join(attr_list)

        query = f"SELECT {attr_str} from {table} WHERE {clause}"
        return self.raw_query(query)

