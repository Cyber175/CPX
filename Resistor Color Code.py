import time
from adafruit_circuitplayground.express import cpx

while True:
    print("CPX Resistor Color Code")
    cpx.pixels.brightness = 0.5
    # 0-black
    cpx.pixels[0] = (4, 4, 4)
    time.sleep(3)
    # 1-brown
    cpx.pixels[1] = (8, 4, 0)
    time.sleep(3)
    # 2-red
    cpx.pixels[2] = (10, 0, 0)
    time.sleep(3)
    # 3-orange
    cpx.pixels[3] = (60, 20, 0)
    time.sleep(3)
    # 4-yellow
    cpx.pixels[4] = (50, 50, 0)
    time.sleep(3)
    # 5-green
    cpx.pixels[5] = (0, 10, 0)
    time.sleep(3)
    # 6-blue
    cpx.pixels[6] = (0, 0, 10)
    time.sleep(3)
    # 7-violet
    cpx.pixels[7] = (5, 0, 5)
    time.sleep(3)
    # 8-grey
    cpx.pixels[8] = (0, 4, 4)
    time.sleep(3)
    # 9-white
    cpx.pixels[9] = (20, 20, 20)
    time.sleep(3)
    cpx.pixels.fill((0, 0, 0))
    time.sleep(3)
