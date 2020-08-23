# Crazy ideas with LEGO "Grand Piano" set

My wife had great ideas for hacking her "Grand Piano" set. For the moment, I'm just testing concepts so will just put some samples of code here.
Most will reuse ideas from my [LEGO ipMIDI instrument](https://github.com/JorgePe/multicastMIDI-EV3) after flashing the LEGO Powered Up hub with [Pybricks](https://pybricks.com/about/)
firmware

## LEGO Grand Piano with a LEGO MIDI keyboard

[![Youtube video](https://img.youtube.com/vi/gyGDLCBsgnA/0.jpg)](https://www.youtube.com/watch?v=gyGDLCBsgnA)

MINDSTORMS ipMIDI keyboard + Raspberry Pi softsynth + Grand Piano running Pybricks

A bash script 'midi-capture.sh' running in the RPi captures incoming MIDI notes (using ALSA 'aseqdump') and changes a status file "checkmidi.txt" everytime a 'Note ON' or 'Note OFF' passes though.

Another (now python) script 'grandpiano.py' checks the status file and sends a 'p' to Nordic UART Service (NUS) running in the 'grandpiano.mpy' micropython
script running on the Pybricks firmware on the Grand Piano' City Hub. This micropython script keep listening for the NUS and actuates the Grand Piano keys
according to the commands receives ('p' for 'Play', 's' for 'Stop', 'r' for 'Reset' or 'Rewind').

With proper timings the Grand Piano (in fact a pianola) follows the notes being played (it looks better for musics with few simultaneous notes) 


## LEGO Grand Piano Westworld Theme

[![Youtube video](https://img.youtube.com/vi/bJun4xo4aLo/0.jpg)](https://www.youtube.com/watch?v=bJun4xo4aLo)

This is a custom demonstration of the above scripts - using my laptop to play the 'Westworld' theme (or just any plain MIDI file) and sending the MIDI stream to the RPi ipMIDI synth (throug QmidiNet) and also to a virtual MIDI pinao (VMPK) so we can see the keys being played in real time.
