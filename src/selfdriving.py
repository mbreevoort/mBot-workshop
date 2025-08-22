from lib.mBot import *

distance = 0

def processSensor(value):
    global distance
    distance = value

if __name__ == '__main__':
    bot = findMBot()
    try:
        while True:
            bot.requestUltrasonicSensor(2, 3, processSensor)
            if (distance < 20):
                bot.doMove(-200,200)
            else:
                bot.doMove(100,100)
            sleep(0.05)
    finally:
        bot.doMove(0,0)
        bot.close()
        print("Exit")
