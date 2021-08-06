# LEGO MIDI Percussion Kit

A LEGO MIDI device that can play real instruments.

## Intro
Inspired in [Dada Machines Automat Tool kit](https://dadamachines.com/products/automat-toolkit/)

This is a mix of hardware and software. All hardware is (or can be) 100% LEGO, while software is a mixture of micropython, python,
bash and a few linux ALSA utils.
Non-linux users may try to port this to their own environment but linux makes it very easy.

## Video
[![Percussion Toolkit v0.3.1](https://img.youtube.com/vi/EGJ1ZUnht8I/0.jpg)](https://www.youtube.com/watch?v=EGJ1ZUnht8I)


## Description

A LEGO Powered Up Hub is used to control motors as "musical actuators". as in Dada Machines' Automat Toolkit.
For instance a motor connected to Port A can be used with a mallet to play a drum and a motor connected to Port B can be
used as a solenoid to "bang" against a bell.
LEGO Powered Up Hubs support up to 6 ports but several hubs can be used at the same time, depending on your "controller"
BT BLE capacity - my laptop allows at least 4 hubs at the same time so technically 26 actuators are possible but for now
I am already happy with 4.

Each Hub uses [Pybricks](https://pybricks.com), a 3rd party open source firmware that allows a common micropython API to be used with all LEGO
hubs.

A linux "controller" (I use an Ubuntu laptop but a Raspberry Pi sounds like a good idea) used a Pybricks python library
('pybricksdev') to communicate with the Hub. It also uses a bash script to parse MIDI events on the ALSA MIDI system and
send proper actions to the Hubs.

Everything else is just plain ALSA MIDI. For instance you can play a MIDI song with 'aplaymidi' directly to the MIDI port
where the bash script is listening or you can improve your setup and use a MIDI synth and 'qmidiroute' to split the MIDI
data so all instruments are played on the synth except for those you want to route to the actuators.

