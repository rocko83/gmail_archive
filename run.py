# Python 3.8.0
import smtplib
import time
import datetime
import imaplib
import email
import traceback
from src.argmenu import ArgMenu
from src.configs import Config

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

def read_email_from_gmail():
    try:
        argmenu = ArgMenu()
        args = argmenu.get_args()
        credentials = Config(args.cred)
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(credentials.get_data("mail"),credentials.get_data("password"))
        mail.select('inbox',readonly=True)

        # data = mail.search(None, 'UNSEEN')
        data = mail.search(None, '(FROM "no-reply@accounts.google.com")')
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for id in id_list:
            index = str(id, 'UTF-8')
            data = mail.fetch(index, '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):

                    msg = email.message_from_string(str(arr[1],"ISO-8859-1",))
                    # print(msg)
                    myFile = open(f"mails/{msg['Message-ID']}.eml", 'w')
                    myFile.writelines(str(msg))
                    myFile.close()
                    # print(dir(msg))
                    # print(msg)
                    print(msg['date'])
                    print(msg['Message-ID'])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    # date_mod = 0
                    if "," in msg['date']:
                        date_mod = 0
                    else:
                        date_mod = -1
                    date_year = str(msg['date']).split()[3 + date_mod]
                    date_month = str(msg['date']).split()[2 + date_mod]
                    date_day = str(msg['date']).split()[1 + date_mod]
                    date_time = str(msg['date']).split()[4 + date_mod]
                    date2 = datetime.datetime.strptime(
                        f"{date_year}/{date_month}/{date_day}/{date_time}",
                        '%Y/%b/%d/%H:%M:%S')
                    # print(str(msg['Received']).split(";")[1].split(",")[1])
                    print(f"ID={id}, MSGID={msg['Message-ID']}")

    except Exception as e:
        traceback.print_exc() 
        print(str(e))

read_email_from_gmail()