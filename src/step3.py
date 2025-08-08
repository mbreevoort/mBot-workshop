from lib.mBot import *
import random

if __name__ == '__main__':
    # Connect with the mBot
    bot = findMBot()
    try:
        while True:
            bot.doBuzzer(300, 250)
            sleep(0.5)
            bot.doBuzzer(200, 250)
            sleep(0.5)
            bot.doBuzzer(64, 1)
            sleep(0.5)
            bot.doBuzzer(60, 1)
    finally:
        print("Exit")

