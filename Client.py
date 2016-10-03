from random import randint
import datetime


class Client:
    medias = ["alfa.lt", "delfi.lt", "facebook.com", "somesite.net", "orai.lt", "15min.lt", "reddit.com"]

    def __init__(self, name):
        self.name = name
        self.trans_setup = name + "'s Trans Setup"
        self.campaigns = []
        for campaign_id in range(randint(5, 10)):
            self.campaigns.append(self.name + "'s campaign Nr." + str(campaign_id + 1))
        self.banners = []
        for banner_id in range(randint(5, 10)):
            self.banners.append(self.name + "'s banner Nr." +str(banner_id + 1))


class User:
    def __init__(self, id):
        self.id = id
        self.date = datetime.datetime.now() - datetime.timedelta(weeks=randint(5, 25))
        self.incr_date()
        self.paths = []

    def incr_date(self, weak=False):
        if weak:
            self.date = self.date + \
                        datetime.timedelta(minutes=randint(0, 30), seconds=randint(0, 60))
        else:
            self.date = self.date + \
                        datetime.timedelta(days=randint(1, 30), minutes=randint(0, 1200), seconds=randint(0, 60))

    def add_info(self, info):
        self.paths.append(info)

