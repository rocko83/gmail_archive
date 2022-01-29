# Python 3.8.0


import logging
import traceback
from src.argmenu import ArgMenu
from src.configs import Config
from src.mymail import MyMail

from src.archive import Archive
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------


def read_email_from_gmail():
    try:
        #Import arguments
        argmenu = ArgMenu()
        args = argmenu.get_args()
        credentials = Config(args.cred)

        #Initialize logging
        logging.basicConfig(format='%(asctime)-15s %(levelname)s %(message)s')
        if args.verbose == True:
            logging.getLogger().setLevel(logging.DEBUG)
        else:
            logging.getLogger().setLevel(logging.INFO)

        #Initialize mail
        mymail = MyMail(
            mail_account=credentials.get_data("mail"),
            password=credentials.get_data("password"),
            apiserver=credentials.get_data("apiserver"),
            port=credentials.get_data("port")

        )
        mails = mymail.search_mail('(FROM "no-reply@accounts.google.com")')

        #Initialize archive
        archive = Archive(basedir=args.output_dir)

        #Get all mails and archive
        for id in mails:
            mail = mymail.get_mails(id)
            archive.archive_mail(mail)
        mymail.close()


    except Exception as e:
        traceback.print_exc() 
        print(str(e))
if __name__ == "__main__":
    read_email_from_gmail()