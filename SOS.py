# SOS!
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.5, auto_write = True)

AQUA = (0, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

UNIT = 0.2
dit_pause = UNIT
dah_pause = UNIT * 3
between_dits_and_dahs = UNIT
between_letters_pause = UNIT * 3
between_words_pause = UNIT * 7

while True:
    #S
    #.
    pixels.fill(RED)
    time.sleep(dit_pause)
    pixels.fill(BLACK)

    time.sleep(between_dits_and_dahs)
    #.
    pixels.fill(RED)
    time.sleep(dit_pause)
    pixels.fill(BLACK)

    time.sleep(between_dits_and_dahs)
    #.
    pixels.fill(RED)
    time.sleep(dit_pause)
    pixels.fill(BLACK)

    time.sleep(between_letters_pause)

    #O
    #-
    pixels.fill(RED)
    time.sleep(dah_pause)
    pixels.fill(BLACK)

    time.sleep(between_dits_and_dahs)
    #-
    pixels.fill(RED)
    time.sleep(dah_pause)
    pixels.fill(BLACK)

    time.sleep(between_dits_and_dahs)
    #-
    pixels.fill(RED)
    time.sleep(dah_pause)
    pixels.fill(BLACK)

    time.sleep(between_letters_pause)

    #S
    #.
    pixels.fill(RED)
    time.sleep(dit_pause)
    pixels.fill(BLACK)

    time.sleep(between_dits_and_dahs)
    #.
    pixels.fill(RED)
    time.sleep(dit_pause)
    pixels.fill(BLACK)

    time.sleep(between_dits_and_dahs)
    #.
    pixels.fill(RED)
    time.sleep(dit_pause)
    pixels.fill(BLACK)

    time.sleep(between_dits_and_dahs)

    time.sleep(between_words_pause)