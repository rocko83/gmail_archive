import argparse


class ArgMenu:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="GMAIL Archive or any other mail account with IMAP")
        self.parser.add_argument('--cred', type=str, help="Path to a credential json")
        self.parser.add_argument('--mails', type=str, help="Number of mails to fetch")
        self.parser.add_argument('--search', type=str, help="Search patter to get mail. https://gist.github.com/martinrusev/6121028#file-imap-search")
        self.parser.add_argument("--excel", type=str, help="Generate excel file")
        self.parser.add_argument("--html", type=str, help="Generate HTML file")
        self.parser.add_argument("--webserver", type=str, help="Start WEBSERVER")
        self.parser.add_argument("--socket", type=str, help="Specify socket to start webserver, default 0.0.0.0:8383")

    def get_args(self):
        args = self.parser.parse_args()
        if args.cred is not None:
            return self.parser.parse_args()
        else:
            raise ArgMenuException("Missing credential file")

class ArgMenuException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)