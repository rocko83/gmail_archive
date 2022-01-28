# Python 3.8.0
import smtplib
import time
import datetime
import imaplib
import email
import traceback


# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
ORG_EMAIL = "@"
FROM_EMAIL = "" + ORG_EMAIL
FROM_PWD = ""
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox',readonly=True)

        data = mail.search(None, 'UNSEEN')
        print(dir(data))
        print(data)
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        print(first_email_id)
        print(latest_email_id)

        for i in range(latest_email_id,first_email_id, -1):
            # print("newmsg")
            # print(dir(i))
            # print(i)
            data = mail.fetch(str(i), '(RFC822)' )
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
                    email_subject = msg['subject']
                    email_from = msg['from']
                    date_year = str(msg['date']).split()[3]
                    date_month = str(msg['date']).split()[2]
                    date_day = str(msg['date']).split()[1]
                    date_time = str(msg['date']).split()[4]
                    date2 = datetime.datetime.strptime(
                        f"{date_year}/{date_month}/{date_day}/{date_time}",
                        '%Y/%b/%d/%H:%M:%S')

                    print(msg['date'])
                    # print(str(msg['Received']).split(";")[1].split(",")[1])
                    print(f"ID={i}, MSGID={msg['Message-ID']}")

    except Exception as e:
        traceback.print_exc() 
        print(str(e))

read_email_from_gmail()