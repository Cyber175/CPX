import time
from adafruit_circuitplayground.express import cpx
while True:
    print("Hello World and Circuit Python!")
    cpx.red_led = True
    time.sleep(5)
    cpx.red_led = False
    time.sleep(5)