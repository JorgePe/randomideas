# LEGO MIDI Drum Kit

## A MIDI Drum Kit made with LEGO MINDSTORMS EV3

[![DrumKit v0.5](https://img.youtube.com/vi/dTuFZ_FHsHQ/0.jpg)](https://www.youtube.com/watch?v=dTuFZ_FHsHQ)

### Introduction

This allows using a single LEGO MINDSTORMS EV3 with 4 color sensors as a MIDI instrument.
Configurations were made for a Drum Kit with 4 pads  but with small modifications it can be used as any other instrument
like a 4-key keyboard.
Thanks to MIDI nature, several EV3 can be used, assigning each 'pad' to a different note or percussion instrument.
I am using 2 EV3 and 8 color sensors for a 8-pad MIDI Drum Kit but you can (in theory) add how many you want.

### Files included
- the python files are mine
- the 'midipipe' isn't necessary, the main script creates it if needed
- 'amidicat' is the binary file for the EV3 ARM compiled from the original source code of Josh Lehan http://krellan.com/amidicat/
- 'multimidcast' is the binary file for the EV3 ARM compiled from the original source code of Dirk Jagdmann https://llg.cubic.org/tools/multimidicast/

### MIDI Connections

The LEGO MINDSTORMS EV3 is a small computer. When using it with a microSD card with ev3dev linux, it supports MIDI:
- the kernel recognizes several USB MIDI adaptors (like the M-Audio UNO USB)
- the ALSA sound system includes several tools like 'aconnect', 'aseqdump', 'amidi' and 'aseqnet' to deal with MIDI devices

A simpler version of my project assume the EV3 is connected to a USB MIDI adapter. Usually this devices show up as 'Client 20'
with at least one port:

```
$ aconnect -l
client 0: 'System' [type=kernel]
    0 'Timer           '
    1 'Announce        '
client 14: 'Midi Through' [type=kernel]
    0 'Midi Through Port-0'
client 20: 'USB Uno MIDI Interface' [type=kernel,card=1]
    0 'USB Uno MIDI Interface MIDI 1'
```

This gives our MINDSTORMS EV3 a MIDI Out port in the form of a DIN5 cable that can be connected to conventional MIDI devices
like a synthesizer to generate audible sound from the MIDI music messages we sent him.

This works quite well and has very little overhead - playing a MIDI file with 'amidi' uses 5% or less of the EV3 CPU and
depending on your synth quality audio can sound quite good (I also found out that the USB adapter also plays a role here
- playing complexe MIDI songs on the same synth sounds **quite** different depending on the USB MIDI adapter used) 

But if you don't have a USB MIDI adapter or you don't want to deal with a mess of cables and gadgets directly attached to your
MINDSTORMS there is a wireless option: ipMIDI. Instead of sending MIDI messages to a physical MIDI port we send the very same
messages to a virtual MIDI port that multicasts those messages through WiFi. ipMIDI is not officially MIDI so there aren't commercial 
devices that can use it but it is wide used with computers and smart devices like phones or tablets (TouchDAW, for instance, can run 
on my smartphone and send and receive ipMIDI messages).

So I prepared two versions of my script:

- 'mididrum.py' assumes the EV3 is connected to other MIDI devices through a USB MIDI adapter
- 'ipmididrum.py' sends MIDI messages through Wi-Fi using the ipMIDI protocol

[to be done]
- explain how to use
- explain how to change configuration
- give real world examples of both scenarios
