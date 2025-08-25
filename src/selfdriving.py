from lib.mBot import *
from lib.DistanceSensor import *

if __name__ == '__main__':
    bot = findMBot()
    distance_sensor = DistanceSensor(bot)

    try:
        while True:
            distance = distance_sensor.get_distance()
            if (distance < 20):
                bot.doMove(-200,200)
            else:
                bot.doMove(100,100)
            sleep(0.05)
    finally:
        bot.doMove(0,0)
        bot.close()
        print("Exit")
