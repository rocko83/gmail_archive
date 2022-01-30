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
        # print(args.delete)
        # print(args.verbose)
        # exit(1)
        #Initialize mail
        if args.delete == True:
            mymail = MyMail(
                mail_account=credentials.get_data("mail"),
                password=credentials.get_data("password"),
                apiserver=credentials.get_data("apiserver"),
                port=credentials.get_data("port"),
                readonly=False
            )
        else:
            mymail = MyMail(
                mail_account=credentials.get_data("mail"),
                password=credentials.get_data("password"),
                apiserver=credentials.get_data("apiserver"),
                port=credentials.get_data("port")
            )

        mails = mymail.search_mail(args.search)

        #Initialize archive
        archive = Archive(basedir=args.output_dir)

        #Get all mails and archive

        if len(mails) == 0:
            logging.info("No mail returned")
            exit(0)
        else:
            logging.info(f"Progress {len(mails)}")

        # index = [ 1,9,3,4,5,6]
        # print(index)
        # print(sorted(index))
        # print(sorted(index,reverse=True))
        index = []
        for id in mails:
            index.append(int(str(id, 'UTF-8')))
        index=sorted(index)
        if index[0] < index[-1]:
            index = sorted(index,reverse=True)
        count=0
        for id in index:
            count = count + 1
            if args.mails is not None:
                if count == args.mails + 1 :
                    exit(0)
                else:
                    logging.info(f"{args.mails - count}/{args.mails} Messages to process.")
            else:
                logging.info(f"{len(index) - count}/{len(index)} Messages to process.")
            b = str(id).encode('utf-8')

            mail = mymail.get_mails(b)
            archive.archive_mail(mail)
            if args.delete == True:
                mymail.delete_mail(id=b, msgid=mail['Message-ID'])
        mymail.close()


    except Exception as e:
        traceback.print_exc() 
        print(str(e))
if __name__ == "__main__":
    read_email_from_gmail()