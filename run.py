# Python 3.8.0

import time
import datetime

import traceback
from src.argmenu import ArgMenu
from src.configs import Config
from src.mymail import MyMail
from src.myfile import MyFile
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------


def read_email_from_gmail():
    try:
        argmenu = ArgMenu()
        args = argmenu.get_args()
        credentials = Config(args.cred)
        mymail = MyMail(
            mail_account=credentials.get_data("mail"),
            password=credentials.get_data("password")
        )
        mails = mymail.search_mail('(FROM "no-reply@accounts.google.com")')

        for id in mails:
            mail = mymail.get_mails(id)
            mailfile = MyFile(f"mails/{mail['Message-ID']}.eml")
            mailfile.write(str(mail))
            if "," in mail['date']:
                date_mod = 0
            else:
                date_mod = -1
            date_year = str(mail['date']).split()[3 + date_mod]
            date_month = str(mail['date']).split()[2 + date_mod]
            date_day = str(mail['date']).split()[1 + date_mod]
            date_time = str(mail['date']).split()[4 + date_mod]
            date_timezone = str(mail['date']).split()[5 + date_mod]


            date = datetime.datetime.strptime(
                f"{date_year}/{date_month}/{date_day}/{date_time}",
                '%Y/%b/%d/%H:%M:%S')
            print(f"ID={id}, {date}, timezone={date_timezone}, MSGID={mail['Message-ID']}")


    except Exception as e:
        traceback.print_exc() 
        print(str(e))

read_email_from_gmail()