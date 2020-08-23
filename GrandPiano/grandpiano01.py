#!/usr/bin/env python3

#
# 2020-08-13 Jorge Pereira
# checks for MIDI notes and plays a key on Grand Piano each time a note arrives
# use an external bash script based on aseqdump to check for MIDI notes
# use Pybricks on Grand Piano to listen for commands through NUS

from bluepy.btle import *
from time import sleep

HUB_ID = "90:84:2B:06:4B:53"  # My City Hub

CHECK_MIDI_TIME = 0.001
CHECK_MIDI_FILE = "checkmidi.txt"

# NUS (Nordic UART Service) is used to communicate with the Hub when running Pybricks firmware
NORDIC_UART_SERVICE = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
RX_CHARACTERISTIC = '6e400002-b5a3-f393-e0a9-e50e24dcca9e' #RX Write no response (handle: 0x000e)
TX_CHARACTERISTIC = '6e400003-b5a3-f393-e0a9-e50e24dcca9e' #TX notify (handle: 0x0010)
CR = '\x0D'                               # a Carriage Return should end each message sent to NUS

# commands that Pybricks-side script should understand
CMD_PLAY = 'p'                            # Play a key
CMD_RST = 'r'                             # Reset keys
CMD_STOP = 's'                            # Stop

class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        # ... initialise here

    def handleNotification(self, cHandle, data):
        # ... perhaps check cHandle
        # ... process 'data'
        # we are so lazy that don't care for messages comming from Hub and keep notifications OFF
        #print(data.decode("utf-8").rstrip())
        pass


def send_command(hub, handle, command):
    hub.writeCharacteristic(handle, bytes(command+CR, 'utf-8'), withResponse=False)

# Hub Initialization  -------
hub = Peripheral(HUB_ID)
hub.setDelegate( MyDelegate( ))
hub_svcs = hub.getServices()    # without this I cannot get ServiceByUUID to work ????
hub_svcs = hub.getServiceByUUID( UUID(NORDIC_UART_SERVICE) )
hub_tx = hub_svcs.getCharacteristics( UUID(TX_CHARACTERISTIC) )[0]
hub_tx_handle = hub_tx.valHandle
hub_rx = hub_svcs.getCharacteristics( UUID(RX_CHARACTERISTIC) )[0]
hub_rx_handle = hub_rx.valHandle

#we are so lazy the don't care for messages comming from Hub and keep notifications OFF
#hub.writeCharacteristic(hub_tx_handle + 1, b'\x01\x00', withResponse=False)

print("Hub initialized")
playing = False

# now keep checking for new notes and do the magic
while True:
    # check MIDI input
    print("Checking MIDI...")
    f = open(CHECK_MIDI_FILE,"rt")
    line = f.readline().strip()
    f.close()
#    print(line)
    if line == "ON" :
        print("Got MIDI")
        if playing == False:
            send_command(hub, hub_rx_handle, CMD_PLAY)
            playing = True
    else:
        print("No MIDI")
        #send_command(hub, hub_rx_handle, CMD_STOP)
        playing = False
    sleep(CHECK_MIDI_TIME)
    
# we never get here but we should            
send_command(hub, hub_rx_handle, CMD_RST)
