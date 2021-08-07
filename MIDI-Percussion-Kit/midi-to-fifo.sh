#!/bin/bash
#
# this script parses MIDI stream and writes some KEYS on
# a FIFO file whenever some instruments are played on 
# MIDI channel 10 (percussion)
#
# see 'https://www.pgmusic.com/tutorial_gm.htm'
# for the General MIDI Drum Kit Map (list of instruments)
#
# more than one instrument can trigger the same event
# for instance '35' and '36' (tow types of Bass Drums)
# will both trigger 'C'
#
# we assume 'percussionkit.fifo' as the FIFO file used by the
# associated python script
#
# you should edit the next line according to the port to where
# you will send MIDI music (i.e. 129:1)
# check with 'aconnect -l' command
aseqdump -p 129:1 | \
while IFS=" ," read src ev1 ev2 ch label1 data1 label2 data2 rest; do
    case "$ev1 $ev2 $ch $data1" in
    # Bass Drum
        "Note on 9 35" ) echo -n C > percussionkit.fifo ;;
        "Note on 9 36" ) echo -n C > percussionkit.fifo ;;
    # Hand Clap, Castanets
        "Note on 9 85" ) echo -n B > percussionkit.fifo ;;
        "Note on 9 39" ) echo -n B > percussionkit.fifo ;;
    # Hi-Hat
        "Note on 9 42" ) echo -n B > percussionkit.fifo ;;
        "Note on 9 46" ) echo -n B > percussionkit.fifo ;;
    # Snares
        "Note on 9 38" ) echo -n A > percussionkit.fifo ;;
        "Note on 9 40" ) echo -n A > percussionkit.fifo ;;
    # Cymbals
        "Note on 9 49" ) echo -n D > percussionkit.fifo ;;
    esac
done
