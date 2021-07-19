# LEGO Air Drums with LEGO Move Hub

A short holiday project that uses two LEGO Move Hubs as wireless MIDI Drum Sticks.

[![LEGO AirDrums Video](https://img.youtube.com/vi/bZcKz5frq9k/0.jpg)](https://www.youtube.com/watch?v=bZcKz5frq9k)

[![LEGO AirDrums Video](https://img.youtube.com/vi/3BFpTzSQscc/hqdefault.jpg)](https://www.youtube.com/watch?v=3BFpTzSQscc)

These are the scripts used on the tutorial video:
- 'airdrum-move.py' is a Pybricks script that runs on each Move Hub
- 'airdrum-demo.py' is the first python script used as demo
- 'airdrum.py' is the full python video and uses 2x Move Hubs

You need to flash Pybricks firwmare on your Move Hubs. See 'https://pybricks.com'
You will also need a linux computer with python and 'pybricksdev' installed as a library. See 'https://github.com/pybricks/pybricksdev'.
And finally you will need to install 3 linux programs:
- xdotool
- VMPK
- Hydrogen

Yes, linux. Yes, geeky. But you want your LEGO to do nice things like playing virtual MIDI Air Drums right? So you need to embrace The Force.

## Notes

Turnsout Hydrogen /the drum engine) accepts keyboard input so VMPK is not needed. Will soon add a version of 'airdrum-demo.py' and 'airdrum.py'
that forwards directly to Hydrogen without using VMPK as a MIDI gateway. This is simpler and faster but VMPK still has the advantage of MIDI
(so instead of Hydrogen pretty much anything can be used as long as it has a MIDI input).

Also been trying using the IMU sensor to read which side is facing up when "hitting" the drum. This allows more instruments to be played (a
request from one of my kids). With a little training from the musician each Air Drum can play two different instruments (pointing UP or
pointing DOWN when "hitting") at the cost of a few beats per minute. Will also add these versions soon.
