import time
from machine import Pin
import neopixel
import bms3

# Create a NeoPixel instance
# Brightness of 0.3 is ample for the 1515 sized LED
pixel = neopixel.NeoPixel(Pin(bms3.RGB_DATA), 1)
# Turn on the power to the NeoPixel
bms3.set_rgb_power(True)

# This code will monitor the battery voltage on a 1S lipo battery 
# plugged into the board. lipo max charge is around 4.2v and completely dead is 
# anything below 3.2v. 

while True:
        voltage =  bms3.get_battery_voltage()
        if voltage < 3.2:
                pixel[0] = ( 255, 0, 0, 0.5)
                pixel.write()
        if voltage >= 3.2 and voltage < 3.5 :
                pixel[0] = ( 252, 140, 3, 0.5)
                pixel.write()
        if voltage >= 3.5 and voltage < 4.0 :
                pixel[0] = ( 227, 252, 3, 0.5)
                pixel.write()
        if voltage >= 4.0:
                pixel[0] = (0, 255, 0, 0.5)   #set the RGB to green if the battery is above 4.0v
                pixel.write()
        print(voltage)
        time.sleep(.5) 
    