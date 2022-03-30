# gmail_archive

This tool sync your e-mail from google or any other service providing IMAP protocol.

It can just sync or sync and delete (move).

It'll save your mails in files *.iml and has a sqlite3 database with index about every synced mail.

# TODO

* database
* excel
* htlm build
* multi thread
* flask web interface

# Links

* https://stackoverflow.com/questions/6225763/downloading-multiple-attachments-using-imaplib
* https://gist.github.com/martinrusev/6121028
* https://gist.github.com/johnpaulhayes/106c3e40dc04b6a6b516
* https://docs.python.org/3/library/imaplib.html
* https://stackoverflow.com/questions/3180891/imap-how-to-delete-messages
* https://stackoverflow.com/questions/52498373/retrieve-search-for-emails-using-message-id-through-python-imap
* https://pypi.org/project/imap-tools/


# Examples


```bash
python run.py --cred etc/credentials.json --output_dir archive_mail  --search 'ALL'
python run.py --cred etc/credentials.json --output_dir archive_mail  --search '(FROM "mail@from.com")'  --delete
python run.py --cred etc/credentials.json --output_dir archive_mail  --search '(UID "<0100018826430649-4c257cec-45af-43d4-9161-34492ebe33bd-000000@email.amazonses.com>")'  --delete
python run.py --cred etc/credentials.json --output_dir archive_mail  --search '(NOT SINCE "1-Jan-2019")'
python run.py --cred etc/credentials.json --output_dir archive_mail  --search '(HEADER Message-ID "<0100018826430649-4c257cec-45af-43d4-9161-34492ebe33bd-000000@email.amazonses.com>")' 
```


# Know Bugs

* If LABEL DATE do not have Timezone attached will set GMT by code.
