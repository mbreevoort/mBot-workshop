from lib.mBot import *
from lib.LineSensor import *

line = 0

if __name__ == '__main__':
    bot = findMBot()
    follower = LineSensor(bot)
    try:
        while True:
            line = follower.get_line_status()

            if line == LINE_NONE:       # no line detected
                ___
            elif line == LINE_RIGHT:    # line detected right
                ___
            ___

    finally:
        bot.doMove(0,0)
        bot.close()
        print("Exit")
