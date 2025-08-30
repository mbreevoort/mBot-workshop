from lib.mBot import *
import random

if __name__ == '__main__':
    bot = _________()   # <--- Fill in: connect to your mBot
    try:
        bot.doRGBLedOnBoard(1, ___, ___, ___)   # <--- Fill in: color 1
        sleep(0.5)
        bot.doRGBLedOnBoard(1, ___, ___, ___)   # <--- Fill in: color 2
        sleep(0.5)
        bot.doRGBLedOnBoard(1, ___, ___, ___)   # <--- Fill in: color 3
        sleep(0.5)
    finally:
        bot.doRGBLedOnBoard(1, 0, 0, 0) # turn off the right led light
        bot.doRGBLedOnBoard(2, 0, 0, 0) # turn off the left led light

