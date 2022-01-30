import os.path
import time
import datetime
import logging
from src.myfile import MyFile
from src.base import Base
from src.myfile import MyFile

class Archive:
    def __init__(self, basedir="archive"):
        self.basedir = basedir
        self.__create_directory(basedir)
        try:
            self.data = Base(dbinmemory=False, dbpath=self.basedir)
        except Exception as e:
            logging.error(f"Fail to create database on path: {basedir}")
        else:
            logging.debug(f"Database create with success")

    def __create_directory(self,diretory):
        if not os.path.isdir(diretory):
            os.makedirs(diretory,exist_ok=True)
            logging.debug(f"Created_directory {diretory}")
        else:
            logging.debug(f"Directory {diretory} allready exist")
    def archive_mail(self,mail):
        logging.debug(f"Starting process for mail {mail['Message-ID'] }")
        if mail['date'] is not None:
            if "," in mail['date']:
                date_mod = 0
            else:
                date_mod = -1
        else:
            logging.error("Fail to get mail information. This mail was not archived neither deleted.")
            logging.error(f"Dumping all data: {mail}")
            return

        date_year = str(mail['date']).split()[3 + date_mod]
        date_month = str(mail['date']).split()[2 + date_mod]
        date_day = str(mail['date']).split()[1 + date_mod]
        date_time = str(mail['date']).split()[4 + date_mod]
        date_timezone = str(mail['date']).split()[5 + date_mod]
        date = datetime.datetime.strptime(
            f"{date_year}/{date_month}/{date_day}/{date_time}",
            '%Y/%b/%d/%H:%M:%S')
        mail_path_to_archive = f"{self.basedir}/{date.year}/{date.month}/{date.day}"
        mail_file_to_archive = f"{mail['Message-ID'].replace(' ','_').replace('<','').replace('>','')}.eml".replace('/','_')
        mail_file_fullpath_to_archive = f"{mail_path_to_archive}/{mail_file_to_archive}"
        self.__create_directory(mail_path_to_archive)
        try:
            if self.data.get_mail_by_msgid(mail['Message-ID']) == []:
                logging.debug(f"Mail {mail['Message-ID'] } dot not exist in archive. Preparing to archive now.")
                mailfile = MyFile(mail_file_fullpath_to_archive)
                mailfile.write(str(mail))
                mailfile.close()
                self.data.register_mail(
                    MAIL_TO=str(mail['To']).replace('\'','\'\''),
                    MAIL_FROM=str(mail['From']).replace('\'','\'\''),
                    MAIL_SUBJECT=str(mail['Subject']).replace('\'','\'\''),
                    MAIL_DATE=date,
                    MAIL_TZ=date_timezone,
                    MAIL_FILENAME=mail_file_to_archive,
                    MAIL_FILEPATH=mail_path_to_archive,
                    MAIL_FULLFILEPATH=mail_file_fullpath_to_archive,
                    MAIL_MSGID=mail['Message-ID']
                )
                logging.info(f"Mail {mail['Message-ID'] } Archived")
            else:
                logging.info(f"Mail {mail['Message-ID'] } allready exist")
            # self.__delete_email(mail=mail)

        except Exception as e:
            logging.error(f"Fail to archive mail {mail['Message-ID']} to path {mail_file_fullpath_to_archive}, MSG={e}")
            exit(1)
        else:
            logging.info(f"Mail {mail['Message-ID']} processed.")
            logging.info(f"Mail {mail['Message-ID']}, {mail['To']}, {mail['From']}, {mail['Subject']}.")





        # logging.info(f"DATE={date}, FROM={str(mail['FROM']).replace(' ','_').replace('<','').replace('>','')}, MSGID={mail['Message-ID']}")



