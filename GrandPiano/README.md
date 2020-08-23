# Crazy ideas with LEGO "Grand Piano" set

My wife had great ideas for hacking her "Grand Piano" set. For the moment, I'm just testing concepts so will just put some samples of code here.
Most will reuse ideas from my [LEGO ipMIDI instrument](https://github.com/JorgePe/multicastMIDI-EV3)

## LEGO Grand Piano with a LEGO MIDI keyboard

[![Youtube video](https://img.youtube.com/vi/gyGDLCBsgnA/0.jpg)](https://www.youtube.com/watch?v=gyGDLCBsgnA)

MINDSTORMS ipMIDI keyboard + Raspberry Pi softsynth + Grand Piano running Pybricks

A script running in the RPi captures incoming MIDI notes and actuates the Grand Piano keys through the Nordic UART Service of the Pybricks firmware.


## LEGO Grand Piano Westworld Theme

[![Youtube video](https://img.youtube.com/vi/bJun4xo4aLo/0.jpg)](https://www.youtube.com/watch?v=bJun4xo4aLo)

The virtual piano (VMPK) and the Raspberry Py MIDI synth (yoshimi) are both receiving the same MIDI notes.

At the RPi side, a script listens to MIDI and actuates the LEGO Grand Piano each time a "Note ON" arrives so the keyboard motion is
somewhat synchronized with the music.

