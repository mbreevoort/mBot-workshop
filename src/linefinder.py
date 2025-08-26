from lib.mBot import *
from lib.LineFollower import *

line = 0

def processLine(value):
    global line
    line = value

if __name__ == '__main__':
    bot = findMBot()
    follower = LineFollower(bot)
    try:
        while True:
            line = follower.get_line_status()

            if line == LINE_NONE:       # no line detected
                bot.doMove(100, -100)
            elif line == LINE_RIGHT:    # line detected right
                bot.doMove(100, 0)
            elif line == LINE_LEFT:     # line detected left
                bot.doMove(0, 100)
            elif line == LINE_CENTER:   # line centered
                bot.doMove(100, 100)

    finally:
        bot.doMove(0,0)
        bot.close()
        print("Exit")
