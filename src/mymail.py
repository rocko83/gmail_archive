import imaplib
import email
import smtplib


class MyMail:
    def __init__(self,mail_account, password, box = 'inbox', readonly = True):
        SMTP_SERVER = "imap.gmail.com"
        SMTP_PORT = 993
        self.mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        self.mail.login(mail_account, password)
        self.mail.select(box, readonly=readonly)
    def search_mail(self,search):
        self.data = self.mail.search(None, search )
        return self.data[1][0].split()
    def get_mails(self,id):
        index = str(id, 'UTF-8')
        responses = self.mail.fetch(index,'(RFC822)')
        multi_response = []
        # print(f"one responses = {responses}")
        for response in responses:
            arr = response[0]
            if isinstance(arr, tuple):
                msg = email.message_from_string(str(arr[1],"ISO-8859-1",))
                multi_response.append(msg)
        return multi_response[0]


