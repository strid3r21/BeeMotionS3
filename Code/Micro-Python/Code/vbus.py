import time
from machine import Pin
import neopixel
import bms3

# Create a NeoPixel instance
# Brightness of 0.3 is ample for the 1515 sized LED
pixel = neopixel.NeoPixel(Pin(bms3.RGB_DATA), 1)
# Turn on the power to the NeoPixel
bms3.set_rgb_power(True)

# this code will detect if the USB is plugged in. this can be useful if you want your code to stop running when you've 
# plugged your board in your
while True:
        vbus =  bms3.get_vbus_present()
        if vbus == False:
                pixel[0] = ( 255, 0, 0, 0.5)
                pixel.write()
        if vbus == True :
                pixel[0] = ( 0, 255, 0, 0.5)
                pixel.write()
        time.sleep(.5) 