#!/usr/bin/env python3
from ev3dev2.port import LegoPort
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, DcMotor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.led import Leds

from time import sleep
from datetime import datetime as dt
import datetime

ESPEAK = '-a200 -s115 -p55'

leds = Leds()
leds.animate_cycle(('RED','ORANGE','GREEN','AMBER','YELLOW'), duration = None, block=False)

# 2020 Advent Sundays
sunday1 = datetime.datetime(2020, 11, 30)
sunday2 = datetime.datetime(2020, 12, 6)
sunday3 = datetime.datetime(2020, 12, 13)
sunday4 = datetime.datetime(2020, 12, 20)
xmaseve = datetime.datetime(2020, 12, 24)
xmasday = datetime.datetime(2020, 12, 25)

####
# A is shortest Candle
# D is longer Candle
####

pA = LegoPort(OUTPUT_A)
pA.mode = 'dc-motor'
pB = LegoPort(OUTPUT_B)
pB.mode = 'dc-motor'
pC = LegoPort(OUTPUT_C)
pC.mode = 'dc-motor'
pD = LegoPort(OUTPUT_D)
pD.mode = 'dc-motor'

sleep(1)

sound = Sound()

lightA = DcMotor(OUTPUT_A)
lightA.duty_cycle_sp=100

lightB = DcMotor(OUTPUT_B)
lightB.duty_cycle_sp=100

lightC = DcMotor(OUTPUT_C)
lightC.duty_cycle_sp=100

lightD = DcMotor(OUTPUT_D)
lightD.duty_cycle_sp=100

# cycle all candles

lightA.run_direct()
sleep(2)
lightA.stop()
lightB.run_direct()
sleep(2)
lightB.stop()    
lightC.run_direct()
sleep(2)
lightC.stop()    
lightD.run_direct()
sleep(2)
lightD.stop()    

# check current date

today = dt.today()
print('Today is:', today)
speech = today.strftime("%A") + ' ' + today.strftime("%-d") + ' ' + today.strftime("%B")
sound.speak('Todays is ' + speech)

# light up candles

if today >= sunday4:
    print("4")
    lightA.run_direct()
    lightB.run_direct()
    lightC.run_direct()
    lightD.run_direct()
    if today >= xmasday:
        sound.speak("Merry Christmas!", espeak_opts=ESPEAK)
    elif today >= xmaseve:
        sound.speak("It is the Christmas Eve, Merry Christmas!", espeak_opts=ESPEAK)
    else:
        sound.speak("It is the fourth week of the Advent", espeak_opts=ESPEAK)
elif today >= sunday3:
    print("3")
    lightA.run_direct()
    lightB.run_direct()
    lightC.run_direct()
    sound.speak("It is the third week of the Advent", espeak_opts=ESPEAK)
elif today >= sunday2:
    print("2")
    lightA.run_direct()
    lightB.run_direct()
    sound.speak("It is the second week of the Advent", espeak_opts=ESPEAK)
elif today >= sunday1:
    print("1")
    lightA.run_direct()
    sound.speak("It is the fisrt week of the Advent", espeak_opts=ESPEAK)

# play a xmas music
# .wav file needs to be PCM mono 22050 Hz
sleep(2)
sound.play_file('./We_Wish_You_A_Merry_Christmas_pcm_mono.wav')
sleep(2)

print("OFF")
lightA.duty_cycle_sp=0
lightB.duty_cycle_sp=0
lightC.duty_cycle_sp=0
lightD.duty_cycle_sp=0

leds.animate_stop()
leds.all_off()
