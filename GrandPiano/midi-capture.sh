#!/bin/bash
echo -e "OFF\r" > checkmidi.txt
aseqdump --port=128:0 | \
while IFS=" ," read src ev1 ev2 ch label1 data1 label2 data2 rest; do
    case "$ev1 $ev2" in
        "Note on" ) echo -e "ON\r" > checkmidi.txt;;
        "Note off" ) echo -e "OFF\r" > checkmidi.txt;;
    esac
done
