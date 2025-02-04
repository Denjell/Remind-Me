import datetime as dt
from remind.util import website_schema


class Round:
    def __init__(self, contest):
        self.id = contest['id']
        self.name = contest['event']
        self.start_time = dt.datetime.strptime(contest['start'], '%Y-%m-%dT%H:%M:%S')
        self.duration = dt.timedelta(seconds=contest['duration'])
        self.url = contest['href']
        self.website = contest['resource']['name']
        self.website_id = contest['resource']['id']

    def __str__(self):
        st = "ID = " + str(self.id) + ", "
        st += "Name = " + self.name + ", "
        st += "Start_time = " + str(self.start_time) + ", "
        st += "Duration = " + str(self.duration) + ", "
        st += "URL = " + self.url + ", "
        st += "Website = " + self.website + ", "
        st += "Website_id = " + str(self.website_id) + ", "
        st = "(" + st[:-2] + ")"
        return st

    def is_eligible(self, site):
        return site == self.website

    def is_desired(self, websites):

        for disallowed_pattern in websites[self.website].disallowed_patterns:
            if disallowed_pattern in self.name.lower():
                return False

        for allowed_pattern in websites[self.website].allowed_patterns:
            if allowed_pattern in self.name.lower():
                return True

        return False

    def __repr__(self):
        return "Round - " + self.name
