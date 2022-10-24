# Functional SOS!
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.5, auto_write = True)

AQUA = (0, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

UNIT = 0.2
dit_pause = UNIT
dah_pause = UNIT * 3
between_dits_and_dahs = UNIT
between_letters_pause = UNIT * 3
between_words_pause = UNIT * 7

light_color = BLUE

def dit():
    pixels.fill(light_color)
    time.sleep(dit_pause)
    pixels.fill(BLACK)

def dah():
    pixels.fill(light_color)
    time.sleep(dah_pause)
    pixels.fill(BLACK)

while True:
    #S
    dit()
    time.sleep(between_dits_and_dahs)
    dit()
    time.sleep(between_dits_and_dahs)
    dit()
    time.sleep(between_letters_pause)

    #O
    dah()
    time.sleep(between_dits_and_dahs)
    dah()
    time.sleep(between_dits_and_dahs)
    dah()
    time.sleep(between_letters_pause)

    #S
    dit()
    time.sleep(between_dits_and_dahs)
    dit()
    time.sleep(between_dits_and_dahs)
    dit()
    time.sleep(between_letters_pause)

    time.sleep(between_words_pause)