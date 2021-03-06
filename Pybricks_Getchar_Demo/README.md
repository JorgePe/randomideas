# Will explain here how to use "getchar()" on Pybricks micropython to send commands to a Powered Up hub.

The easiest way is using the I/O Window of the Pybricks IDE (Chrome-based) while running the micropython script since 
the standard input (i.e. the keyboard) is already being redirected to the hub (through a BLE connection to the Nordic UART Service, managed by
a Chrome extension)

But the keyboard is not the only device that send events to the stdin - there are other devices, like the Makey Makey, that generate keyboard-like
events. And there are programs that can be used to map the buttons of some HID devices (like gamepads or mouses) to keyboard events.

These explanations use the LEGO set [42109 App-Controlled Top Gear Rally Car](https://www.lego.com/en-pt/product/app-controlled-top-gear-rally-car-42109)

![Top Gear Rally Car](https://github.com/JorgePe/randomideas/blob/master/Pybricks_Getchar_Demo/TopGear.jpg)

without modifications except for flashing the [Pybricks](https://pybricks.com/) firmware on the Technic Hub so I can use micropython instead of the LEGO App.

The script used is always the same: [Top Gear script](https://github.com/JorgePe/randomideas/blob/master/Pybricks_Getchar_Demo/TopGearRallyCar.mpy) but
in some demos I will be using a basic "emulator" of the LEGO Top Gear Rally Car:

<img alt="Top Gear Car Emulator" src="https://github.com/JorgePe/randomideas/blob/master/Pybricks_Getchar_Demo/TopGear-Emulator.jpg" width="480">

it uses two XL motors instead of a L and a XL but the code works exactly the same way.

# Some videos

Part 1 - showing the basic concept with just my laptop keyboard and the emulator:


[![Pybrick and getchar() - part 1](https://img.youtube.com/vi/yys5QrDj9A8/0.jpg)](https://www.youtube.com/watch?v=yys5QrDj9A8)


Part 2 - showing the same thing now with the full Top Gear Rally Car model


[![Pybrick and getchar() - part 2](https://img.youtube.com/vi/sd1N2H8AURU/0.jpg)](https://www.youtube.com/watch?v=sd1N2H8AURU)


Part 3 - showing a basic Makey Makey setup with the emulator:


[![Pybrick and getchar() - part 3](https://img.youtube.com/vi/njr63D6O7Ow/0.jpg)](https://www.youtube.com/watch?v=njr63D6O7Ow)


# Roadmap

- Xbox Adaptive Controller and some foot pedal and microswitches
- Android Nordic Tollbox and the UART tool instead of the Chrome IDE
- some python for direct accessing the Nordic UART Service instead of the Chrome IDE (linux, Raspberry Pi and MINDSTORMS EV3 clients)
- probably a few more gadgets
