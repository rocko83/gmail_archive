import json


class Config:
    def __init__(self, configfile):
        try:
            self.data = json.loads(open(configfile).read())
            self.credentials = self.data["credentials"]
        except KeyError as e:
            print(f"Fail to read json key on configfile {configfile}, MSG={e}")

    def get_data(self, key):
        # print(self.credentials)
        return self.credentials[key]