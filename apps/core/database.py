import psycopg2

from base import secret


class Database:
    instance = None
    _create_table_query = None

    def __init__(self, *args, **kwargs):
        self.db_config = {
            'dbname': secret.DATABASE_NAME,
            'user': secret.DATABASE_USER,
            'password': secret.DATABASE_PASSWORD,
            'host': secret.DATABASE_HOST,
            'port': secret.DATABASE_PORT,
        }
        self._initialize_instance(*args, **kwargs)

    def _initialize_instance(self, *args, **kwargs):
        pass

    def create_table(self):
        self.instance.db_config = self.db_config
        with self.instance:
            self.instance.execute_raw(self._create_table_query)

    @classmethod
    def _create_instance(cls, *args, **kwargs):
        cls.instance = super().__new__(cls, *args, **kwargs)

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls._create_instance(*args, **kwargs)

        return cls.instance

    def connect(self):
        # اتصال به پایگاه داده PostgreSQL
        return psycopg2.connect(**self.db_config)

    def execute_queries(self, queries):
        for query in queries:
            self.execute_raw(query)

    def execute_raw(self, query, params=None):
        """
        اجرای یک کوئری دلخواه.
        :param query: دستور SQL
        :param params: پارامترهای جایگزین برای دستور (اختیاری)
        :return: نتایج کوئری
        """
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                try:
                    res = cursor.fetchall()
                    return res
                except psycopg2.ProgrammingError:
                    # برای کوئری‌هایی که مقدار برنمی‌گردانند
                    return None

    def __enter__(self):
        self.conn = self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
