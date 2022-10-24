# Light it up!
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.5, auto_write = True)
pixels.fill((255, 0, 0))

#Infinite loop
while True:
    pass