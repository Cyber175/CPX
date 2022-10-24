# Flash'em!
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.5, auto_write = True)

AQUA = (0, 255, 255)
BLACK = (0, 0, 0)
flash_time = 0.5

#Infinite loop
while True:
    pixels.fill(AQUA)
    time.sleep(flash_time)
    pixels.fill(BLACK)
    time.sleep(flash_time)