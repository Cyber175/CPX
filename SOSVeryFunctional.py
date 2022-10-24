# Very Functional SOS!
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

def dit(dit_color, sleep_time):
    pixels.fill(dit_color)
    time.sleep(dit_pause)
    pixels.fill(BLACK)
    time.sleep(sleep_time)

def dah(dah_color, sleep_time):
    pixels.fill(dah_color)
    time.sleep(dah_pause)
    pixels.fill(BLACK)
    time.sleep(sleep_time)

while True:
    #S
    dit(light_color, between_dits_and_dahs)
    dit(light_color, between_dits_and_dahs)
    dit(light_color, between_letters_pause)

    #O
    dah(light_color, between_dits_and_dahs)
    dah(light_color, between_dits_and_dahs)
    dah(light_color, between_letters_pause)

    #S
    dit(light_color, between_dits_and_dahs)
    dit(light_color, between_dits_and_dahs)
    dit(light_color, between_letters_pause)

    time.sleep(between_words_pause)