from lib.mBot import *
from time import sleep

_distance_value = 0

def _process_distance(value):
    global _distance_value
    _distance_value = value

class DistanceSensor:
    def __init__(self, bot, port1=2, port2=3):
        self.bot = bot
        self.distance = 0
        self.port1 = port1
        self.port2 = port2

    def update(self):
        self.bot.requestUltrasonicSensor(self.port1, self.port2, _process_distance)
        sleep(0.1)  # small delay to let callback update

    def get_distance(self):
        self.update()
        return _distance_value
