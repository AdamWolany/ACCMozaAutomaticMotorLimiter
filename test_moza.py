from moza import MozaController
import time

moza = MozaController()

print("Waiting for MOZA base...")
time.sleep(10)

print("Setting angle to 500 degrees")
moza.set_steering_angle(500)

time.sleep(5)

print("Setting angle to 360 degrees")
moza.set_steering_angle(360)

time.sleep(5)

moza.close()