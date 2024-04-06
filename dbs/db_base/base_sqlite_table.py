from dbs.db_base.sqlite_connector import SqliteConnector


@staticmethod
def execute_sql_query(fn):
    def wrapper(*args, **kwargs):
        with SqliteConnector() as cursor:
            return cursor.execute(fn(*args, **kwargs)).fetchall()

    return wrapper
