# Xmas-Wreath

### Based on LEGO set 40426 "Christmas Wreath 2-in-1"

A MINDSTORMS EV3 lights up each of the 4 Advent Candles according to current date.
Each candle is connected through a LEGO fiber optic element to a Power Function light, controlled by
the EV3 (an adapter cable is used).

EV3 also speaks a few orders ("Today is...") and plays a christmas music at the end.

Music is a [wav file](https://webzoom.freewebs.com/fmei75/M%20christmas/We%20Wish%20You%20A%20Merry%20Christmas.wav) I've found
and converted with ffmpeg to PCM mono and resampled to 22050 Hz so it can be used by ev3dev python
