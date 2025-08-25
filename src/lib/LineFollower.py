from lib.mBot import *
from time import sleep

# Named constants for readability
LINE_CENTER = 0
LINE_LEFT   = 1
LINE_RIGHT  = 2
LINE_NONE   = 3

_line_value = LINE_NONE

def _process_line(value):
    global _line_value
    _line_value = value

class LineFollower:
    def __init__(self, bot, port1=1, port2=2):
        self.bot = bot
        self.line_value = LINE_NONE
        self.port1 = port1
        self.port2 = port2

    def update(self):
        self.bot.requestLineFollower(self.port1, self.port2, _process_line)
        sleep(0.1)  # small delay to let callback update

    def get_line_status(self):
        self.update()
        return _line_value
