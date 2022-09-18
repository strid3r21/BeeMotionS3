import time, gc, os
import neopixel
import board, digitalio
import bms3

# Create a NeoPixel instance
# Brightness of 0.3 is ample for the 1515 sized LED
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=True, pixel_order=neopixel.GRB)
# Turn on the power to the NeoPixel
bms3.set_ldo2_power(True)

# this code will detect if the USB is plugged in. this can be useful if you want your code to stop running when you've 
# plugged your board into your PC.
while True:
        vbus =  bms3.get_vbus_present()
        if vbus == False:
                pixel[0] = ( 255, 0, 0, 0.5)
                pixel.write()
        if vbus == True :
                pixel[0] = ( 0, 255, 0, 0.5)
                pixel.write()
        time.sleep(.5) 