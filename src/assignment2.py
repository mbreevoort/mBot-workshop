from lib.mBot import *

if __name__ == '__main__':
    bot = findMBot()  # Connect with the mBot

    try:
        bot.doMove(___, ___)
        sleep(1)
        bot.doMove(___, ___)
        sleep(1)
    finally:
        bot.doMove(0, 0) # stop the motor
