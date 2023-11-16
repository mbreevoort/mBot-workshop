from lib.mBot import *
import math
import pygame
import sys

# Constants for the usb game controller
AXIS_GAMEPAD_JOYLEFT_UPDOWN = 1
AXIS_GAMEPAD_JOYLEFT_LEFTRIGHT = 0
AXIS_GAMEPAD_JOYRIGHT_UPDOWN = 3
AXIS_GAMEPAD_JOYRIGHT_LEFTRIGHT = 2
BUTTON_GAMEPAD_RIGHT_THUMB_1 = 0
BUTTON_GAMEPAD_SELECT = 8

# Game state
select_button_released = False # True if the button was released (to detect edges)
control_mode = 0
control_mode_max = 2

def findJoystick():
        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
                print("No joystick detected :-(")
                print("Connect a joystick or game controller and start again...")
                return None

        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print( "Yes! I found " + str(joystick_count) + " joystick" + ("" if joystick_count == 1 else "s"))
        print( "I will use this one: '" + joystick.get_name() + "'")
        return joystick

def findMBot():
    try:
        bot = mBot()
        bot.startWithHID()
        return bot
    except Exception as err:
        print(f"Could not initialize mBot {err=}, {type(err)=}")
        print("Insert a 2.4GHz-dongle, turn on the mBot and start again...")
        return None

def joystickToTank(inputLeft, inputRight, minJoystick, maxJoystick, minSpeed, maxSpeed):
    leftOut = map(inputLeft, minJoystick, maxJoystick, minSpeed, maxSpeed)
    rightOut = map(inputRight, minJoystick, maxJoystick, minSpeed, maxSpeed)
    return (leftOut, rightOut)

# Credits to https://www.instructables.com/Joystick-to-Differential-Drive-Python/
def joystickToDiff(x, y, minJoystick, maxJoystick, minSpeed, maxSpeed):
    # If x and y are 0, then there is not much to calculate...
	if x == 0 and y == 0:
		return (0, 0)
    
	# First Compute the angle in deg
	# First hypotenuse
	z = math.sqrt(x * x + y * y)

	# angle in radians
	rad = math.acos(math.fabs(x) / z)

	# and in degrees
	angle = rad * 180 / math.pi

	# Now angle indicates the measure of turn
	# Along a straight line, with an angle o, the turn co-efficient is same
	# this applies for angles between 0-90, with angle 0 the coeff is -1
	# with angle 45, the co-efficient is 0 and with angle 90, it is 1

	tcoeff = -1 + (angle / 90) * 2
	turn = tcoeff * math.fabs(math.fabs(y) - math.fabs(x))
	turn = round(turn * 100, 0) / 100

	# And max of y or x is the movement
	mov = max(math.fabs(y), math.fabs(x))

	# First and third quadrant
	if (x >= 0 and y >= 0) or (x < 0 and y < 0):
		rawLeft = mov
		rawRight = turn
	else:
		rawRight = mov
		rawLeft = turn

	# Reverse polarity
	if y < 0:
		rawLeft = 0 - rawLeft
		rawRight = 0 - rawRight

	# minJoystick, maxJoystick, minSpeed, maxSpeed
	# Map the values onto the defined rang
	rightOut = map(rawLeft, minJoystick, maxJoystick, minSpeed, maxSpeed)
	leftOut = map(rawRight, minJoystick, maxJoystick, minSpeed, maxSpeed)

	return (leftOut, rightOut)

def map(v, in_min, in_max, out_min, out_max):
	# Check that the value is at least in_min
	if v < in_min:
		v = in_min
	# Check that the value is at most in_max
	if v > in_max:
		v = in_max
	return (v - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

if __name__ == '__main__':

    # Initialize PyGame & joystick
    pygame.init()
    pygame.joystick.init()
    joystick = findJoystick()

    ctrl0_axis_throttle = AXIS_GAMEPAD_JOYLEFT_UPDOWN
    ctrl0_axis_turn = AXIS_GAMEPAD_JOYLEFT_LEFTRIGHT
    ctrl1_axis_throttle = AXIS_GAMEPAD_JOYLEFT_UPDOWN
    ctrl1_axis_turn = AXIS_GAMEPAD_JOYRIGHT_LEFTRIGHT
    ctrl2_axis_throttle_l = AXIS_GAMEPAD_JOYLEFT_UPDOWN
    ctrl2_axis_throttle_r = AXIS_GAMEPAD_JOYRIGHT_UPDOWN
    button_select_control = BUTTON_GAMEPAD_SELECT

    # Connect with the mBot
    bot = findMBot()

    # Main loop
    while True:

        # Process PyGame events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
            
                # ESC => Quit game
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        motor_out = (0, 0) 
        if (joystick is not None):

             # Button not pushed? Remember it! Than you're allowed to select a driving mode once the button is pushed
            if( joystick.get_button(button_select_control) == 0 ):
                    select_button_released = True
            else:
                    # The button is pushed => Only select a driving mode if it was not yet pushed before
                    if( select_button_released ):
                            # switch to the next control mode
                            control_mode = (control_mode + 1) % (control_mode_max + 1)
                            print( "control_mode: " + str(control_mode))
                    select_button_released = False

            # Calculate the speed of each wheel
            motor_out=(0,0)

            if( control_mode == 0 ):
                # Differential drive - 1 joystick
                throttle = -joystick.get_axis(ctrl0_axis_throttle)
                turn = -joystick.get_axis(ctrl0_axis_turn)
                motor_out = joystickToDiff(turn, throttle, -1.0, 1.0, -255, 255)
                print( "Differential drive (0) -- throttle: " + str(throttle) + " -- turn: " + str(turn) + " => left: " + str(motor_out[0]) + " -- right: " + str(motor_out[1]))
            elif( control_mode == 1 ):
                # Differential drive
                throttle = -joystick.get_axis(ctrl1_axis_throttle)
                turn = -joystick.get_axis(ctrl1_axis_turn)
                motor_out = joystickToDiff(turn, throttle, -1.0, 1.0, -255, 255)
                print( "Differential drive (1) -- throttle: " + str(throttle) + " -- turn: " + str(turn) + " => left: " + str(motor_out[0]) + " -- right: " + str(motor_out[1]))
            else:
                # Tank mode
                throttle_l = -joystick.get_axis(ctrl2_axis_throttle_r)
                throttle_r = -joystick.get_axis(ctrl2_axis_throttle_l)
                motor_out = joystickToTank(throttle_r, throttle_l, -1.0, 1.0, -255, 255)
                print( "Tank drive (2) -- Throttle L: " + str(throttle_l) + " -- Throttle R: " + str(throttle_r) + " => left: " + str(motor_out[0]) + " -- right: " + str(motor_out[1]))

        if (bot is not None):
             # Send the speeds to the mBot / mBoot
            bot.doMove( (int)(motor_out[0]), (int)(motor_out[1]))