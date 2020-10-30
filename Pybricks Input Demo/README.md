Will explain here how to use "input()" on Pybricks micropython to send commands to a Powered Up hub.

The easiest way is using the I/O Window of the Pybricks IDE (Chrome-based) while running the micropython script since 
the standard input (i.e. the keyboard) is already being redirected to the hub (through a BLE connection to the Nordic UART Service, managed by
a Chrome extension)

But the keyboard is not the only device that send events to the stdin - there are other devices, like the Makey Makey, that generate keyboard-like
events. And there are programs that can be used to map the buttons of some HID devices (like gamepads or mouses) to keyboard events.

A video showing a basic Makey Makey setup:
https://youtu.be/njr63D6O7Ow
