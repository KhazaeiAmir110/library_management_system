import psycopg2

from base import secret


class Database:
    instance = None
    _create_table_query = None

    def __init__(self, *args, **kwargs):
        self.db_path = secret.DATABASE_URL

    def create_table(self):
        if self._create_table_query is None:
            raise ValueError("Create table query is not defined.")
        with self:
            self.execute_raw(self._create_table_query)

    @classmethod
    def _create_instance(cls, *args, **kwargs):
        cls.instance = super().__new__(cls, *args, **kwargs)

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls._create_instance(*args, **kwargs)
        return cls.instance

    def connect(self):
        print(f"Connecting to PostgreSQL database at: {self.db_path}")
        conn = psycopg2.connect(self.db_path)
        return conn

    def execute_queries(self, queries):
        with self:
            for query in queries:
                self.execute_raw(query)

    def execute_raw(self, query):
        if self.conn is None or self.conn.closed:
            self.conn = self.connect()
        cursor = self.conn.cursor()
        cursor.execute(query)

        if query.strip().upper().startswith("SELECT"):
            res = cursor.fetchall()
            return res
        else:
            return None

    def __enter__(self):
        self.conn = self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()
