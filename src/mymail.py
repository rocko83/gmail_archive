import imaplib
import email
import email.parser
import smtplib
import logging


class MyMail:
    def __init__(self,mail_account, password, box = 'inbox', readonly = True, apiserver="imap.gmail.com", port=993):
        self.mail = imaplib.IMAP4_SSL(host=apiserver ,port=port)
        self.mail.login(mail_account, password)
        self.mail.select(box, readonly=readonly)
    def search_mail(self,search):
        self.data = self.mail.search(None, search )
        # self.data = self.data[0].split(b' ')
        # return self.data
        return self.data[1][0].split()
    def get_folders(self):
        # for folder in self.mail.list()[1]:
        #     print(folder)
        for i in self.mail.list()[1]:
            l = i.decode().split(' "/" ')
            print(l[0] + " = " + l[1])
    def delete_mail(self,id,msgid):
        index = str(id, 'UTF-8')
        try:
            # logging.info("Fake mail delete")
            self.mail.store(index, '+FLAGS', '\\Deleted')
            self.mail.expunge()
        except Exception as e:
            logging.error(f"Mail {msgid} Could not be delete, MSG={e}")
        finally:
            logging.info(f"Mail {msgid} deleted with success")
    def get_mails(self,id):
        index = str(id, 'UTF-8')
        responses = self.mail.fetch(index,'(RFC822)')
        # encode = email.parser.BytesParser().parsebytes(responses)
        multi_response = []
        # print(f"one responses = {responses}")
        for response in responses:
            arr = response[0]
            if isinstance(arr, tuple):
                # msg = email.message_from_string(str(arr[1],"ISO-8859-1",))
                msg = email.message_from_string(str(arr[1],"ISO-8859-1",))
                multi_response.append(msg)
        return multi_response[0]
    def close(self):
        self.mail.close()
        self.mail.logout()


