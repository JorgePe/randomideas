from pybricksdev.connections import BLEPUPConnection

import asyncio
import subprocess

HUB_ID1 = '00:16:53:AB:C6:3D'
HUB_ID2 = '00:16:53:AE:63:91'

KEY1 = 'p'
KEY2 = 'q'

async def receiver(remote_hub, key):
    while True:
        if len(remote_hub.output) > 0:
            line = remote_hub.output[-1]
            remote_hub.output = []
            # we don't really need to know the output
            # value = line.decode()
            # print(value)
            subprocess.run(["xdotool", "type", key])
            print(key, end = '', flush=True)
        await asyncio.sleep(0.01)

async def main():
    hub1 = BLEPUPConnection()
    hub2 = BLEPUPConnection()
    
    print("Please turn your LEGO AirDrums ON")
    await hub1.connect(HUB_ID1)
    await hub2.connect(HUB_ID2)
      
    # transfer program to the Hubs
    await asyncio.gather(
        hub1.run('/home/jxpereira/Documents/Personal/LEGO/AirDrum/airdrum-move.py', print_output=False),
        hub2.run('/home/jxpereira/Documents/Personal/LEGO/AirDrum/airdrum-move.py', print_output=False)
    )
    
    print("You may Rock!")
    # get phocus on VMPK window (assumes Desktop #0)
    subprocess.run(["xdotool", "search", "--desktop", "0", "--name", "Virtual MIDI Piano Keyboard", "windowactivate"])
    
    await asyncio.gather(
        receiver(hub1, KEY1),
        receiver(hub2, KEY2)
    )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
