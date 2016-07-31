import datetime

class Status:
    currentStatus = 1
    home, away, leaving = 0, 1, 2
    departure_time = datetime.datetime.now()

    def is_home(self):
        return self.currentStatus == self.home

    def is_away(self):
        return self.currentStatus == self.away

    def is_leaving(self):
        return self.currentStatus == self.leaving

    def set_home(self):
        self.currentStatus = self.home

    def set_away(self):
        self.currentStatus = self.away

    def set_leaving(self):
        self.currentStatus = self.leaving
        self.set_departure_time_to_now()

    def set_departure_time_to_now(self):
        self.departure_time = datetime.datetime.now()