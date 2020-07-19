#!/usr/bin/env python3

from imapclient import IMAPClient
from bluepy.btle import *
from time import sleep

HUB_ID = "90:84:2B:05:F3:1C "  # My City Hub

# NUS (Nordic UART Service) is used to communicate with the Hub when running Pybricks firmware
NORDIC_UART_SERVICE = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
RX_CHARACTERISTIC = '6e400002-b5a3-f393-e0a9-e50e24dcca9e' #RX Write no response (handle: 0x000e)
TX_CHARACTERISTIC = '6e400003-b5a3-f393-e0a9-e50e24dcca9e' #TX notify (handle: 0x0010)
CR = '\x0D'                               # a Carriage Return should end each message sent to NUS

# commands that Pybricks-side script should understand
CMD_LEFT = 'l'                            # Rotate left
CMD_RIGHT = 'r'                           # Rotate right
CMD_STOP = 's'                            # Stop

# do not forget to define 2-key auth an then App Password in your google account
HOST = 'imap.gmail.com'
USERNAME = '<gmailaccount>'
PASSWORD = '<AppPassword>'
CHECK_MAIL_TIME = 0.5                     # time between each mailbox check
NOTICATION_TIME = 3.85                    # time for Owl to flap its wings


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

# IMAP Client Initialization
server = IMAPClient(HOST, use_uid=True, ssl=True)
server.login(USERNAME, PASSWORD)
server.select_folder('INBOX', readonly=True)

# get the UID of the last mail at mailbox so we we know when a new one arrived
last_uid = server.folder_status('INBOX')[b'UIDNEXT']
#print("Last UID:", last_uid)

print ("IMAP Client initialized")

# now keep checking for new mails and do the magic
while True:
    # check mailbox
#    print("Checking Mail...")
    new_last_uid = server.folder_status('INBOX')[b'UIDNEXT']
#    print(new_last_uid)
    if new_last_uid != last_uid:
        print("Got Mail")
        last_uid = new_last_uid
        send_command(hub, hub_rx_handle, CMD_LEFT)
        sleep(NOTICATION_TIME)
        send_command(hub, hub_rx_handle, CMD_STOP)
    else:
#         print("No mail")
         sleep(CHECK_MAIL_TIME)
    
# we never get here but we should            
server.logout()
