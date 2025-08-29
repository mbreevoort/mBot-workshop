from lib.mBot import *
from lib.Keyboard import *

def main():

    bot = findMBot()
    keyboard = Keyboard()

    try:
        last_beep = 0
        reverse = False

        while True:
            key = keyboard.get_key()

            if key == "ESC":  # ESC key to exit
                break

            if key == "DOWN":
                bot.doMove(-100, -100)
                reverse = True

            if key == "UP":
                bot.doMove(200, 200)
                reverse = False

            if key == "LEFT":
                bot.doMove(-100, 100)
                reverse = False

            if key == "RIGHT":
                bot.doMove(100, -100)
                reverse = False

            if key == "SPACE":
                bot.doMove(0, 0)
                reverse = False

            if (reverse):
                now = time.time()
                if now - last_beep > 1.2:  # every 1.2 seconds
                    bot.doBuzzer(1200, 300)  # 300 milliseconds beep
                    last_beep = now

            sleep(0.1)

    finally:
        bot.doMove(0, 0) # stop the motor
        keyboard.close()
        print ('Bye!')


if __name__ == "__main__":
    main()

