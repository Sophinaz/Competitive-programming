class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.averages = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkinTime, checkinStation = self.checkins[id]
        timeTook = t - checkinTime
        route = (checkinStation, stationName)

        if route in self.averages:
            self.averages[route][0] += timeTook
            self.averages[route][1] += 1
        else:
            self.averages[route] = [timeTook, 1]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.averages[route][0] / self.averages[route][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)