from pybricks.pupdevices import DCMotor
from pybricks.hubs import CityHub
from pybricks.parameters import Port

hub = CityHub()
mOwl = DCMotor(Port.B)

OWL_SPEED = 40

while True:
    i = input("?")
    if i == "l":
        mOwl.dc(-OWL_SPEED)
    elif i == 'r':
        mOwl.dc(OWL_SPEED)
    elif i == 's':
        mOwl.stop()
    else:
        print("!")
