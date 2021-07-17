from pybricksdev.connections import BLEPUPConnection
import asyncio

HUB_ID = '00:16:53:AE:63:91'
KEY = 'p'

async def receiver(remote_hub, key):
    while True:
        if len(remote_hub.output) > 0:
            line = remote_hub.output[-1]
            remote_hub.output = []
            print(key, end = '', flush=True)
        await asyncio.sleep(0.01)

async def main():
    hub = BLEPUPConnection()
    await hub.connect(HUB_ID)      
    await hub.run('/home/jxpereira/Documents/Personal/LEGO/AirDrum/airdrum-move.py',
        print_output=False)    
    await receiver(hub, KEY)
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
