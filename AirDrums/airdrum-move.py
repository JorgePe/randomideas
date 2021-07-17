from pybricks.hubs import MoveHub
from pybricks.tools import wait

ACC_THRESHOLD = 170
ACC_MARGIN = 50
TIME = 40
KEY = '1'

hub = MoveHub()
max_v = 0

while True:
    x,y,z = hub.imu.acceleration()
    v = x*x+y+y+z+z
    
    if v > ACC_THRESHOLD:
        max_v = v
    elif v < max_v-ACC_MARGIN:
        print(KEY)
        max_v = 0
        wait(TIME)
