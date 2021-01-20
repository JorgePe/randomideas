#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
#from pybricks.iodevices import Ev3devSensor
from pybricks.parameters import Port
from pybricks.tools import wait
#from math import log10

import os

# before start:
# - ensure midipipe exists - mkfifo midipipe
# - two choices: 
#   + use USB MIDI adapter at 20:0
#     - start amidicat - ./amidicat --port 20:0 --hex < /.midipipe
#   + use ipMIDI
#     - start multimidicast [&]
#     - start amidicat - ./amidicat --port 128:0 --hex < ./midipipe

import midi_notes

# check if midipipe was created
if os.popen('ls midipipe').read().strip() == 'midipipe':
    print('midipipe exists')
else:
    os.system('mkfifo midipipe')
    print('midipipe created')

wait(500)

# check if multimidicast is running and start it if not
if os.popen('pgrep multimidicast').read().strip() == '':
    os.system('./multimidicast -i wlxd03745176d00 -q &')
    print('multimidicast started')
else:
    print('multidicast was running')

wait(500)

# check if amidicat is running and start it if not
print(os.popen('pgrep amidicat').read().strip())

if os.popen('pgrep amidicat').read().strip() == '':
    os.system('./amidicat --port 128:0 --hex < ./midipipe &')
    print('amidicat started')
else:
    print('amidicat was running')

wait(500)


ev3 = EV3Brick()
pad1 = ColorSensor(Port.S1)
pad2 = ColorSensor(Port.S2)
pad3 = ColorSensor(Port.S3)
pad4 = ColorSensor(Port.S4)

#DRUM = "08"    # need to see other instruments but some don't stop note
#DRUM = "10"

#DRUM_PATCH = "08"   # Room kit ? 9
DRUM_PATCH = "10"    # Power kit ? 17

# CHANNEL 10 = A
ALL_NOTES_OFF = "B9 7B 00"

def send_note_on(note, velocity="64"):
    pipe.write("99 " + note + " " + velocity)
#    print('Note ON: ', note, velocity)

def send_note_off(note):
    pipe.write("89 " + note + " 00")
#    print('Note OFF: ', note)
    
def mute():
    pipe.write(ALL_NOTES_OFF)
#    print('Mute')


def select_instrument(instr):
    pipe.write("C9 " + instr)
#    print('Instrument: ', instr)


def calc_velocity(pressure, reference):
    # convert pressure to a velocity value
    # a string with the hexdecimal representation
    
    # this should be logarithmic instead of linear
#    velocity = int(VELOCITY_FACTOR * pressure) + VELOCITY_THRESHOLD
#    velocity = int( log10(pressure) * 54 ) 
    velocity = (pressure - reference) * 2
    # cap velocity
    if velocity > 127 :
        velocity = 127    
    
    if velocity > 15:
        vel = hex(velocity)[2:] 
    else:
        vel = "0" + hex(velocity)[2:]
        
    return vel


pipe = open("./midipipe", "w")
wait(100)

mute()
select_instrument(DRUM_PATCH)


wait(1000)

# instrumento 47h parecem todos igais ao BASS DRUM

HIGHQ = "1B"
SLAP = "1C"
BASS_DRUM_1 = "24"    # baaaaad  -  maybe velocity or duration
BASS_DRUM_2 = "23"    # baad 
SNARE_DRUM = "26"   #
HIGH_TOM = "32" #
MID_TOM = "2F" # 
LOW_TOM = "2B" # ?
OPEN_HIHAT = "2E" #?
FOOT_HIHAT = "2C"
CLOSED_HIHAT = "2A"
RIDE_CYMBAL = "33"
CRASH_CYMBAL = "2A"
HAND_CLAP = "27"


mute()

note1 = BASS_DRUM_1
note2 = HAND_CLAP
note3 = SNARE_DRUM
note4 = RIDE_CYMBAL


while True:
    p1 = pad1.reflection()
    p2 = pad2.reflection()
    p3 = pad3.reflection()
    p4 = pad4.reflection()
      
#    print(p1, p2, p3, p4)
    # 63 56 46 71
           
    if p1 > 65:
        print("#1", p1)
#        send_note_on(note1, calc_velocity(p1, 36))
        send_note_on(note1, "31")
        wait(1)
        send_note_on(note1, "6D")
    if p2 > 58:
        print("#2", p2)
        send_note_on(note2, calc_velocity(p2, 29))

    if p3 > 49:
        print("#3", p3)
        send_note_on(note3, calc_velocity(p3, 19))

    if p4 > 76:
        print("#4", p4)
        send_note_on(note4, calc_velocity(p4, 34))

#it never gets here but it is important to do this on exit
mute()
pipe.close()
