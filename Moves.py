import time
from adafruit_circuitplayground.express import cpx
while True:
	print("X:", cpx.acceleration.x, ", Y:", cpx.acceleration.y, ", Z:", cpx.acceleration.z)
	time.sleep(1)
	
