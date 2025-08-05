from lib.mBot import *

if __name__ == '__main__':
    # Connect with the mBot
    bot = findMBot()
    try:
        bot.doMove(100, 100)
        sleep(1)
        bot.doMove(-100, -100)
        sleep(1)
        sys.exit()
    finally:
        bot.doMove(0, 0)
