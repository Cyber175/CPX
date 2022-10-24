import time
from adafruit_circuitplayground.express import cpx
while True:
    print("Hello CPX CircuitPython World! with D13 Light, 2 Neopixels and 2 Tones")
    cpx.red_led = True
    time.sleep(3)
    cpx.red_led = False
    time.sleep(3)
    cpx.play_tone(262, 1)
    cpx.play_tone(294, 1)
    cpx.pixels.brightness = 0.3
    cpx.pixels[0] = (255, 0, 0)
    time.sleep(3)
    cpx.pixels[1] = (0, 0, 255)
    time.sleep(3)
    cpx.pixels[0] = (0, 0, 0)
    time.sleep(3)
    cpx.pixels[1] = (0, 0, 0)
    time.sleep(3)

