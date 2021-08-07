from pybricks.tools import wait
from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from usys import stdin
from uselect import poll

# This needs a LEGO Powered Up hub with at least 4 ports
# I used a Technic Hub (Control+)

# I used a Large Angular Motor on Ports A, C and D ("hammers" or "mallets")
# but anymotor with a zero reference can be used.
# If you don't have any see the code for the motor on Port B
# 
# I used a Technic Medium Motor on Port B ("solenoid").
# Initially I used a BOOST motor, smaller and less powerful).
# Since it doesn't have a zero reference I need to position
# the motor at a known position (-90º) before start

# Some constants, tuned after several attempts with different
# "instruments"

# ANG_X is the extention of the movement for each desired motor action
ANG_A = 47
ANG_B = 66
ANG_C = 40
ANG_D = 37

# REST_X is the rest position, the position to where the actuar returns
# after each action
REST_A = 0
REST_B = -9
REST_C = 0
REST_D = 0

# DELAY_X is the time we let the actuator move and also return to
# rest position (bad coding)
DELAY_A = 50
DELAY_B = 30
DELAY_C = 55
DELAY_D = 44

# KEY_X is the single character we expect to receive for each action
KEY_A = 'A'
KEY_B = 'B'
KEY_C = 'C'
KEY_D = 'D'

# expect input from stdin (the keyboard when running the Chrome-based
# Pybricks IDE)
keyboard = poll()
keyboard.register(stdin)

# Define motors
mA = Motor(Port.A)
mB = Motor(Port.B)
mC = Motor(Port.C)
mD = Motor(Port.D)

# Assume this motor is at expected position
mB.reset_angle(-90)

# change PID parameters for each motor so they behave better
mA.control.pid(20000, 100, 800, 45, 5)
mB.control.pid(20000, 100, 800, 45, 5)
mC.control.pid(20000, 100, 800, 45, 5)
mD.control.pid(20000, 100, 800, 45, 5)

# move motors to rest position
mA.run_target(1200, REST_A, wait=True)
mB.run_target(1200, REST_B, wait=True)
mC.run_target(1200, REST_C, wait=True)
mD.run_target(1200, REST_D, wait=True)

# keep processing input
while True:
    if keyboard.poll(0):
        key = stdin.read(1)
        if key == KEY_A:
            mA.track_target(ANG_A)
            wait(DELAY_A)
            mA.track_target(REST_A)
            wait(DELAY_A)
        elif key == KEY_B:
            mB.track_target(ANG_B)
            wait(DELAY_B)
            mB.track_target(REST_B)
            wait(DELAY_B)
        elif key == KEY_C:
            mC.track_target(ANG_C)
            wait(DELAY_C)
            mC.track_target(REST_C)
            wait(DELAY_C)
        elif key == KEY_D:
            mD.track_target(ANG_D)
            wait(DELAY_D)
            mD.track_target(REST_D)
            wait(DELAY_D)    
