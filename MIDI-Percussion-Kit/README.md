# LEGO MIDI Percussion Kit

A LEGO MIDI device that can play real instruments.

## Intro
Inspired in [Dada Machines Automat Tool kit](https://dadamachines.com/products/automat-toolkit/)

This is a mix of hardware and software. All hardware is (or can be) 100% LEGO, while software is a mixture of micropython,
python, bash and a few linux ALSA utils.

Non-linux users may try to port this to their own environment but linux makes it very easy. But for now they can manually
play the Percussion Kit by using Chrome and with the Pybricks script bellow (loosing the MIDI feature).

## Why LEGO?

Because I can :)

LEGO Technic is a nice (although expensive) mechanical framework. I find it excellent for fast proof of concepts - the
first version of this Percussion Kit was working just a few days after I found Dada Machines kickstarter video on Google...
and the tough part was the MIDI integration (dispite what people tend to say, I am not a programmer nor a musician, just
a curious engineer).


## Video
[![Percussion Toolkit v0.3.1](https://img.youtube.com/vi/EGJ1ZUnht8I/0.jpg)](https://www.youtube.com/watch?v=EGJ1ZUnht8I)


## Description

A LEGO Powered Up Hub is used to control motors as "musical actuators". as in Dada Machines' Automat Toolkit.
For instance a motor connected to Port A can be used with a mallet to play a drum and a motor connected to Port B can be
used as a solenoid to "bang" against a bell.
LEGO Powered Up Hubs supports up to 6 ports but several hubs can be used at the same time, depending on your "controller"
BT BLE capacity - my laptop allows at least 4 hubs at the same time so technically 26 actuators are possible but for now
I am already happy with 4.

Each Hub uses [Pybricks](https://pybricks.com), a 3rd party open source firmware that allows a common micropython API to
be used with all LEGO hubs and also MINDSTORMS EV3 as well.

A linux "controller" (I use an Ubuntu laptop but a Raspberry Pi sounds like a good idea) uses a Pybricks python library
('pybricksdev') to communicate with the Hub. It also uses a short bash script to parse MIDI events on the ALSA MIDI
system and pass the proper events to the python script (with a proper python MIDI library like 'mido' one can probably
skip the need for this bash script and also more easily port this concept to non-linux environments).

Everything else is just plain ALSA MIDI. For example you can play a MIDI song with 'aplaymidi' directly to the MIDI port
where the bash script is listening or you can improve your setup and use a MIDI synth and 'qmidiroute' to split the MIDI
data so all instruments are played on the synth except for those you want to route to the actuators (this way you can
listen to the whole music, like in the video above).

## Files

Please note tht these are the files used specifically for the video above (version 0.3.1). I will try, on future versions, to make 
more general and easy to customise scripts.

### Pybricks

This is a micropython script that uses 4 ports so it requires a Technic Hub or a SPIKE/Robot Inventor Hub but
you can use with City Hub if you comment the lines that use Port C and Port D. For the moment it is not possible
to use the Move Hub (BOOST) because it lacks enough flash space for some libraries required to communicate with it.

The script waits for a single character ('A', 'B', 'C', 'D') and performs a basic pre-defined action on each actuator
according to it. When this script runs through the Crome-based Pybricks IDE one can use the keyboard to manually
control the Percussion Tool Kit and forget all the python/bash/ALSA/linux/MIDI voodoo.

FILE

### Pybricksdev

This is a python script that sends the Pybricks script to the Hub, starts it and then sends a single char ('A', B', 'C', 'D')
through Bluetooth BLE to the LEGO Hub whenever it receives another single char from a help bash script.

FILE

### bash

This is a bash script that uses an ALSA utility ('aseqdump') to listen to live MIDI events and reacts to the intended
ones (like 'Note ON' for the Bass Drum) sending a single char to the python script above.

It is based on a nice script I found [here](https://superuser.com/questions/1170136/translating-midi-input-into-computer-keystrokes-on-linux)

It uses a FIFO file to pass data to the python script. I use this trick a lot with my MIDI LEGO instruments, isn't pretty
but it works.

FILE

## Joining everything

On my linux laptop I start a soft MIDI synth (timidity) and a ALSA util ('qmidiroute') that routes MIDI data.

On a command line we can use 'aconnect -l' to show the MIDI ports in use by these tools.

So let's suppose the soft synth (or your MIDI adapter connected to a real synth) is listening at '128:0'
and 'qmidiroute' is listening at '129:0'.

On 'qmidiroute' we define a rule that forwards all Channels 1 to 9 (the non-percussion instruments) to 'port 2'
(this is the second output port of 'qmidiroute' so if it is listening at '129:0' should show up as '129:2')

We also define that 'Unmatched' events should not be discarded and be sent to 'port 1' (so '129:1').

This way if we send a MIDI stream to 'qmidiroute' it will split it in two streams (non-percussion and percussion).

Now we edit the bash helper script to listen to the percussion stream ('129:1') and we start it.

And we connect the non-percussion stream to our synth ('aconnect 192:2 128:0')

Everything is now ready. Just start the python script ('poetry run python [path]percussionkit02.py') and then
play a MIDI file though 'qmidiroute' ('aplaymidi -p 129:0 SundayBloodySunday.mid'
