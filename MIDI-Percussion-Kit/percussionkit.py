# no python shebang here because I've been using poetry to execute this script
# see 'pybricksdev' project at 'https://github.com/pybricks/pybricksdev'
from pybricksdev.connections import BLEPUPConnection

import asyncio
import subprocess
import os

# ID of the LEGO Powered Up hub used
# Must be a Technic Hub or higher because it uses 4 instruments

HUB_ID1 = '90:84:2B:61:0B:94'

# expected input from the bash helper script
KEY1 = 'A'
KEY2 = 'B'
KEY3 = 'C'
KEY4 = 'D'
KEYS = [KEY1, KEY2, KEY3, KEY4]

# location and name of the FIFO file to be used to pass data
# from the bash helper script to this python script
FIFO_PATH = './'
FIFO_NAME = 'percussionkit.fifo'

# location and name of the Pybricks micropython script to be
# executed on the LEGO hub
SCRIPT_PATH = './'
SCRIPT_NAME = 'main-hub.py'

# the sender function keeps reading the FIFO and if one of
# the expected KEYS is receive it forwards it to the LEGO hub
async def sender(remote_hub, keys):
    # bad coding
    # the FIFO file shouldn't exist so if it does, we delete it
    try:
        os.remove(FIFO_PATH + FIFO_NAME)
    except OSError:
        pass
      
    # create the FIFO file and open it in READ mode
    os.mkfifo(FIFO_PATH + FIFO_NAME)
    fifo = open(FIFO_PATH + FIFO_NAME, 'r')
    
    # keep reading from it
    while True:
        line = fifo.read()
        if line in keys :
            # forward proper KEYS to the LEGO hub
            await remote_hub.write(bytearray(line,'utf-8'))

# the main function connects to the LEGO hub,
# transfers and starts the Pybricks script to be executed,
# and starts the sender function
async def main():
    hub1 = BLEPUPConnection()
    print("Please turn your LEGO Percussion Kit ON")
    await hub1.connect(HUB_ID1)
    await hub1.run(SCRIPT_PATH + SCRIP_NAME, print_output=False)    
    await asyncio.sleep(1.0)
    print('\nYou may now Rock!')    
    await sender(hub1, KEYS)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
