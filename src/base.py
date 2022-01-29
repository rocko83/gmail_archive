import sqlite3
import logging
class Base:
    def __init__(self,dbname="default", dbinmemory=True, dbpath="archive"):
        if dbinmemory == True:
            self.con = sqlite3.connect(":memory")
        else:
            self.con = sqlite3.connect(f"{dbpath}/database-{dbname}.db")

        self.__execute_query(f'''
            CREATE TABLE IF NOT EXISTS MAIL(
            MTO text,
            MFROM text,
            MSUBJECT text,
            MDATE text,
            MTZ, text,
            MFILENAME text,
            MFILEPATH text,
            MFULLFILEPATH text,
            MMSGID TEXT PRIMARY KEY)''')

    def __execute_query(self, query):
        try:
            self.cur = self.con.cursor()
            self.cur.execute(query)
            self.con.commit()
            self.cur.close()
        except Exception as e:
            logging.error(f"Failed to execute query \'{query}\'. MSG=\'{e}\'")
        else:
            logging.debug(f"Database record written successfull {query}")
    def register_mail(
            self,
            MAIL_TO,
            MAIL_FROM,
            MAIL_SUBJECT,
            MAIL_DATE,
            MAIL_TZ,
            MAIL_FILENAME,
            MAIL_FILEPATH,
            MAIL_FULLFILEPATH,
            MAIL_MSGID
        ):
        # self.__execute_query(f'''
        #     INSERT INTO MAIL(MTO,MFROM,MSUBJECT,MDATE,MTZ,MFILENAME,MFILEPATH,MFULLFILEPATH,MMSGID)
        #     VALUES (
        #     '{MAIL_TO}',
        #     '{MAIL_FROM}',
        #     '{MAIL_SUBJECT}',
        #     '{MAIL_DATE}',
        #     '{MAIL_TZ}',
        #     '{MAIL_FILENAME}',
        #     '{MAIL_FILEPATH}',
        #     '{MAIL_FULLFILEPATH}',
        #     '{MAIL_MSGID}')
        # ''')
        self.__execute_query(f'''
            INSERT INTO MAIL(MTO,MFROM,MSUBJECT,MDATE,MTZ,MFILENAME,MFILEPATH,MFULLFILEPATH,MMSGID)
            SELECT '{MAIL_TO}',
                    '{MAIL_FROM}',
                    '{MAIL_SUBJECT}',
                    '{MAIL_DATE}',
                    '{MAIL_TZ}',
                    '{MAIL_FILENAME}',
                    '{MAIL_FILEPATH}',
                    '{MAIL_FULLFILEPATH}',
                    '{MAIL_MSGID}'
                    WHERE NOT EXISTS (
                        SELECT 1 FROM MAIL
                        WHERE MMSGID = '{MAIL_MSGID}'
                        )
                ''')



