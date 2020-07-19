# Hedwig, The Pythonic Robotic Owl

A LEGO Robotic office assistant that flaps its wings whenever a new e-mail arrives at your mailbox.

[![Hedwig Video](https://img.youtube.com/vi/VQ_j7HJwABw/0.jpg)](https://www.youtube.com/watch?v=VQ_j7HJwABw)

I used the LEGO 75979 Hedwig set with a simple modfication to use a LEGO Powered Up M-motor (like seen in 
grohl666's video  ['Motorizing Hedwig in less than a minute. LEGO 75979 MOD'](https://youtu.be/mgUnu70IjcI)

The motor is controlled by a LEGO Powered Up City Hub running [Pybricks](https://pybricks.com) beta firmware.

Two scripts are needed:
- ['hedwig.py'](https://github.com/JorgePe/randomideas/blob/master/Hedwig/hedwig-pybricks.py) is a python script that runs on my laptop (Ubuntu Linux)
and controls the LEGO City Hub through the Nordic UART Service (NUS) implemented by the Pybricks firmware. The script checks a Google Mail mailbox for
the arrival of a new e-mail and sends a command to the NUS to start motion and after a while another command to stop motion.
- ['hedwig-pybricks.py'](https://github.com/JorgePe/randomideas/blob/master/Hedwig/hedwig-pybricks.py) is a micropython script that runs on the LEGO
City Hub and listens for incomming commands from the NUS and turns the motor ON or OFF accordingly.

The micropython script assumes a "DC motor" connected to Port B. Currently only M-Motors and Train motors can be used, all other Powered Up motores
are used another Pybricks class (easy to change on the micropython script).

The python script assumes a Google Mail account is used but other IMAP services should work aswell. You need to edit the USERNAME and PASSWORD
values and you should enable 2-key auth on the GMail account and then set an App Password.

I'm using linux on my laptop and trying to make code that can also run on my MINDSTORMS EV3 brick (running ev3dev). So at the moment I am
using ['bluepy'](https://github.com/IanHarvey/bluepy) python library. This only works on linux (also Raspberry Pi) but not on Windows and most probably
not on Mac. You can try to port my code to a modern and more agnostic library like  ['bleak'](https://bleak.readthedocs.io/en/latest/).


