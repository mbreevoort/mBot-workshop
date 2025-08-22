from lib.mBot import *

line = 0

def processLine(value):
    global line
    line = value

if __name__ == '__main__':
    bot = findMBot()
    try:
        while True:
            bot.requestLineFollower(1, 2, processLine)

            if line == 3: #no line detected
                bot.doMove(70, -70)

            if line == 2: #line detected right
                bot.doMove(70,0)

            if line == 1: #line detected left
                bot.doMove(0,70)

            if line == 0: #line detected
                bot.doMove(70,70)

            sleep(0.02)
    finally:
        bot.doMove(0,0)
        bot.close()
        print("Exit")
