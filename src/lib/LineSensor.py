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

class LineSensor:
    def __init__(self, bot, extID=1, port=2):
        self.bot = bot
        self.line_value = LINE_NONE
        self.extID = extID
        self.port = port

    def update(self):
        self.bot.requestLineFollower(self.extID, self.port, _process_line)
        sleep(0.1)  # small delay to let callback update

    def get_line_status(self):
        self.update()
        return _line_value
