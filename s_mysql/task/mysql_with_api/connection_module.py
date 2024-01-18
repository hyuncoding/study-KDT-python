import pymysql
from pymysql.cursors import Cursor


def connect():
    conn = pymysql.connect(host='43.201.45.73', user='mysql', password='1234', db='test', charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor


def execute(crud):
    result = None

    def manage(*args):
        nonlocal result
        conn, cursor = connect()
        try:
            result = crud(cursor, *args)
            conn.commit()
        except Exception as e:
            print(e.__str__())
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

        return result

    return manage




