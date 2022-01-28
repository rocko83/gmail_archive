import sqlite3
import logging
class Base:
    def __init__(self,dbname="default", dbinmemory=True):
        if dbinmemory == True:
            self.con = sqlite3.connect(":memory")
        else:
            self.con = sqlite3.connect(f"database-{dbname}.db")
        self.cur = self.con.cursor()
        self.__execute_query(f'''
            CREATE TABLE IF NOT EXISTS MAIL(
            TO text,
            FROM text,
            SUBJECT text,
            DATE text,
            MSGID TEXT PRIMARY KEY''')
    def __execute_query(self, query):
        data = ""
        try:
            self.cur.execute(query)
            self.con.commit()
            data = self.cur.fetchall()
        except Exception as e:
            logging.error(f"Failed to execute query \'{query}\'. MSG=\'{e}\'")
        return data