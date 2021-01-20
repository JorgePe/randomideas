LEGO MIDI Drum Kit

Made with LEGO MINDSTORMS EV3 

Files included:
- the python files are mine
- the 'midipipe' isn't necessary, the main script creates it if needed
- 'amidicat' is the binary file for the EV3 ARM compiled from the original source code of Josh Lehan http://krellan.com/amidicat/
- 'multimidcast' is the binary file for the EV3 ARM compiled from the original source code of Dirk Jagdmann https://llg.cubic.org/tools/multimidicast/

There are two versions:
- 'mididrum.py' assumes the EV3 is connected to other MIDI devices through a USB MIDI adapter
- 'ipmididrum.py' uses sends MIDI messages through Wi-Fi using the ipMIDI protocol
