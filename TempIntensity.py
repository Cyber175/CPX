import time 
from adafruit_circuitplayground.express import cpx 
while True:
    print("Temperature:", cpx.temperature, ", Light Intensity:", cpx.light)
    time.sleep(1)
    