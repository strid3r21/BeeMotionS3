import time, gc, os
import neopixel
from machine import Pin
import bms3

# Create a NeoPixel instance
# Brightness of 0.3 is ample for the 1515 sized LED
pixel = neopixel.NeoPixel(Pin(bms3.RGB_DATA), 1)

# set the PIR
PIR = Pin(bms3.PIR,Pin.IN, Pin.PULL_UP)

# Turn on the power to the NeoPixel
bms3.set_rgb_power(True)

# When there is no motion, the RGB will be red
# when there is motion, the RGB will be green
while True:
    if not PIR.value():
        pixel[0] = (255,0,0, 0.5)
        pixel.write()
    else:
        pixel[0] = (0,255,0, 0.5)
        pixel.write()

    
