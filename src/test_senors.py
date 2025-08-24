from lib.mBot import *
import random

def process_line(value):
    detected = ""
    if value == 1:
        detected = "Right"
    elif value == 2:
        detected = "Left"
    elif value == 3:
        detected = "Both"
    
    print(f"LineFollower {detected} response {value} ")
    

def process_sensor(value):
    print(f"UltrasonicSensor response {value}")

def process_light(value):
    print(f"Light on board response {value}") # light is 1000+

if __name__ == '__main__':
    # Connect with the mBot
    bot = findMBot()
    try:
        while True:
            bot.requestLineFollower(1, 2, process_line)
            bot.requestUltrasonicSensor(2, 3, process_sensor)
            bot.requestLightOnBoard(3, process_light)
            sleep(1)
    finally:
        print("Exit")
