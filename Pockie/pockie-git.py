#!/usr/bin/env python3

from bluepy.btle import *
from git import *
from datetime import datetime as dt
from time import sleep

HUB_ID = "00:16:53:B3:E6:5D"  # Pockie Move Hub

# NUS (Nordic UART Service) is used to communicate with the Hub when running Pybricks firmware
NORDIC_UART_SERVICE = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
RX_CHARACTERISTIC = '6e400002-b5a3-f393-e0a9-e50e24dcca9e' #RX Write no response (handle: 0x000e)
TX_CHARACTERISTIC = '6e400003-b5a3-f393-e0a9-e50e24dcca9e' #TX notify (handle: 0x0010)
CR = '\x0D'                               # a Carriage Return should end each message sent to NUS

# commands that Pybricks-side script should understand
CMD_DANCE = 'd'
CMD_WALK = 'w'
CMD_HAPPY = 'h'
CMD_REJECT = 'r'

CHECK_PERIOD = 5     # time between each check (seconds)

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

repo = Repo("randomideas")
o = repo.remotes.origin
o.pull()
master = repo.head.reference

print('Current branch:', master.name)
print('Latest commit id:', master.commit.hexsha)
print('Latest commit message:', master.commit.message)
print('Latest commit date:', dt.fromtimestamp(master.commit.committed_date) )

# the important thing is the 'latest commited date'
last_commit_date = master.commit.committed_date
#print(last_commit_date)

print("Waiting for new commits...")
while True:
    check_commit_date = master.commit.committed_date
    o.pull()
    master = repo.head.reference
    
    if check_commit_date != last_commit_date :
        last_commit_date = check_commit_date
        print("New commit!")
        print("Date   :", dt.fromtimestamp(check_commit_date) )
        print("Message:", master.commit.message)
        send_command(hub, hub_rx_handle, CMD_HAPPY)        
        sleep(CHECK_PERIOD)
        
# we never get here but we should release everything
