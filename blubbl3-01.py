#!/usr/bin/env python3

from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, DcMotor
from ev3dev2.port import LegoPort
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor
#from ev3dev2.led import Leds

from threading import Thread
from time import sleep

running = False
bubble_handle_thread = False

def bubble_handle():
    while bubble_handle_thread == True:
        # every step is tested so we can exit faster
        if running == True:
            m3.on_to_position(SpeedPercent(30),-90)
        if running == True:
            m3.wait_until_not_moving()
        if running == True:
            sleep(0.25)
        if running == True:
            m3.on_to_position(SpeedPercent(30),-6)
        if running == True:
            m3.wait_until_not_moving()
        if running == True:
            sleep(1.9)

# initialize motor on Port A for 'dc-motor' mode (am using a Power Functions L motor through an adapter cable)
pA = LegoPort(OUTPUT_A).mode = 'dc-motor'

sleep(0.6)                      # looks like it needs time for new mode to settle

m1 = DcMotor(OUTPUT_A)          # Airjitsu Propeller
m1.duty_cycle_sp=100

#m2 = DcMotor(OUTPUT_B)          # Peristaltic Pump
#m2.duty_cycle_sp=100

m3 = MediumMotor(OUTPUT_C)      # Bubble Handle
m3.position = 0
ts1 = TouchSensor(INPUT_1)      # Bubble Production
#ts2 = TouchSensor(INPUT_2)      # Liquid refill


t= Thread(target=bubble_handle)
bubble_handle_thread = True
t.start()

while True:
    if ts1.is_pressed:
        running = not running
        sleep(0.25)
        if running == True:
            m1.run_forever()
        else:
            m1.stop()
            # needs to return bubble handle to rest position
            sleep(1.7)
            m3.wait_until_not_moving()
            m3.on_to_position(SpeedPercent(30),0)

# will never reach this
