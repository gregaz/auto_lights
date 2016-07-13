class Status:
    currentStatus = 1
    home, away = 0, 1

    def isHome(self):
        return self.currentStatus == self.home

    def isAway(self):
        return self.currentStatus == self.away

    def setHome(self):
        self.currentStatus = self.home

    def setAway(self):
        self.currentStatus = self.away