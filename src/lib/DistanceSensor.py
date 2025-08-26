from lib.mBot import *
from time import sleep

_distance_value = 0

def _process_distance(value):
    global _distance_value
    _distance_value = value

class DistanceSensor:
    def __init__(self, bot, extID=2, port=3):
        self.bot = bot
        self.distance = 0
        self.extID = extID
        self.port = port

    def update(self):
        self.bot.requestUltrasonicSensor(self.extID, self.port, _process_distance)
        sleep(0.1)  # small delay to let callback update

    def get_distance(self):
        self.update()
        return _distance_value
