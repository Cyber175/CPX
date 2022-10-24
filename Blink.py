import time
from adafruit_circuitplayground.express import cpx
while True:
    cpx.red_led = True
    time.sleep(2)
    cpx.red_led = False
    time.sleep(2)
