from lib.mBot import *
import random

if __name__ == '__main__':
    # Connect with the mBot
    bot = findMBot()
    try:
        while True:
            bot.doRGBLedOnBoard(1, 255, random.randint(0, 255), random.randint(0, 255))
            sleep(0.5)
            bot.doRGBLedOnBoard(2, random.randint(0, 255), 255, 0)
            sleep(0.5)
            bot.doRGBLedOnBoard(1, random.randint(0, 255), 0, 255)
            sleep(0.5)
            bot.doRGBLedOnBoard(2, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            sleep(0.5)
    finally:
        bot.doRGBLedOnBoard(1, 0, 0, 0) # Right turn off the led lights
        bot.doRGBLedOnBoard(2, 0, 0, 0)  #Left turn off the led lights

