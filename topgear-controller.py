#!/usr/bin/env python3

from bluepy.btle import *
from time import sleep

#HUB_OUI = "90:84:2B:4B:BF:59"
HUB_OUI = "90:84:2B:52:DA:8B"

CR = '\x0D'

#iface identifiers - check wich is your BLE adapter with "hciconfig -a"
HID0 = 0      # /dev/hid0
HID1 = 1      # /dev/hid1

class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        # ... initialise here

    def handleNotification(self, cHandle, data):
        # ... perhaps check cHandle
        # ... process 'data'
        print(data.decode("utf-8").rstrip())

#handle: 0x000e, char properties: 0x04, char value handle: 0x000f, uuid: 6e400002-b5a3-f393-e0a9-e50e24dcca9e
#handle: 0x0010, char properties: 0x10, char value handle: 0x0011, uuid: 6e400003-b5a3-f393-e0a9-e50e24dcca9e

NORDIC_UART_SERVICE = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
RX_CHARACTERISTIC = '6e400002-b5a3-f393-e0a9-e50e24dcca9e' #RX Write no response
TX_CHARACTERISTIC = '6e400003-b5a3-f393-e0a9-e50e24dcca9e' #TX notify

def send_command(hub, handle, command):
    hub.writeCharacteristic(handle, bytes(command+CR, 'utf-8'), withResponse=False)


# Initialisation  -------
hub = Peripheral(HUB_OUI, iface=HID0)
hub.setDelegate( MyDelegate( ))
hub_svcs = hub.getServices()    # without this cannot get ServiceByUUID to work ????
hub_svcs = hub.getServiceByUUID( UUID(NORDIC_UART_SERVICE) )
hub_tx = hub_svcs.getCharacteristics( UUID(TX_CHARACTERISTIC) )[0]
hub_tx_handle = hub_tx.valHandle
hub_rx = hub_svcs.getCharacteristics( UUID(RX_CHARACTERISTIC) )[0]
hub_rx_handle = hub_rx.valHandle

#turn notifications ON
hub.writeCharacteristic(hub_tx_handle + 1, b'\x01\x00', withResponse=False)

commands = ['z','f','b','l','f','f','f','f','f','f','f','z','b','l','b','b','b','b','b','b','b']
cmd_count = 0
rcv_count = 0
prompt = False

sleep(1.0)    # sometimes it doesn't start properly so maybe this helps
              # very scientific :)
              
send_command(hub, hub_rx_handle, commands[cmd_count])

while True:
    if hub.waitForNotifications(0.2):
        # handleNotification() was called
        rcv_count+=1
        if rcv_count > 1:
            rcv_count = 0
            prompt = True
        continue

    if prompt == True:
        cmd_count+=1
        if cmd_count == len(commands):
            cmd_count = 0
        send_command(hub, hub_rx_handle, commands[cmd_count])
        sleep(0.4)
    else:
        print("waiting")
