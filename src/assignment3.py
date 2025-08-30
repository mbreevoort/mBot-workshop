from lib.mBot import *
from lib.Keyboard import *
from lib.DistanceSensor import *

if __name__ == '__main__':
    bot = findMBot()  # Connect with the mBot
    keyboard = Keyboard()

    try:
        while True:
            key = keyboard.get_key()

            if key == "UP":
                bot.doMove(200, 200)

            if key == ___   # <--- Fill in
                ___         # <--- Fill in

    finally:
        bot.doMove(0, 0) # stop the motor
