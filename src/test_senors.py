from lib.mBot import *
import random

def processLine(value, pbot):
    detected = ""
    if value == 1:
        detected = "Right"
    elif value == 2:
        detected = "Left"
    elif value == 3:
        detected = "Both"
    
    print(f"LineFollower {detected} response {value} ")
    

def processSensor(value, pbot):
    print(f"UltrasonicSensor response {value}")


if __name__ == '__main__':
    # Connect with the mBot
    bot = findMBot()
    try:
        while True:
            bot.requestLineFollower(1, 2, processLine)
            bot.requestUltrasonicSensor(2, 3, processSensor)
            sleep(1)
    finally:
        print("Exit")
