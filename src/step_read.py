from lib.mBot import *
import random

def processInput(input):
    print(f"Input : {input}")

if __name__ == '__main__':
    # Connect with the mBot
    bot = findMBot()
    try:
        while True:
            bot.requestLineFollower(1, 2, processInput)
            sleep(1)

    finally:
        print("Exit")

