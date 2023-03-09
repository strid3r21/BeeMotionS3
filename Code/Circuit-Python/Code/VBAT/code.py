# please note that when the USB is plugged in it is actively charging the lipo battery which means the battery monitoring
# will report the battery as being fully charged. unplug the USB to see the true voltage of the battery by the RGB color or 
# or by sending the reading via MQTT.


import time, gc, os
import neopixel
import board, digitalio
import bms3

# Create a NeoPixel instance
# Brightness of 0.3 is ample for the 1515 sized LED
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=True, pixel_order=neopixel.GRB)
# Turn on the power to the NeoPixel
bms3.set_ldo2_power(True)

# This code will monitor the battery voltage on a 1S lipo battery 
# plugged into the board. lipo max charge is around 4.2v and completely dead is 
# anything below 3.2v.  it will turn the RGB LED Red for dead, Yellow for middle of the road and Green for charged
# or near full.

while True:
        vbat_voltage =  bms3.get_battery_voltage()
        if vbat_voltage < 3.2:
                pixel[0] = ( 255, 0, 0, 0.5)
                pixel.write()
        if vbat_voltage >= 3.2 and vbat_voltage < 3.5 :
                pixel[0] = ( 252, 140, 3, 0.5)
                pixel.write()
        if vbat_voltage >= 3.5 and vbat_voltage < 4.0 :
                pixel[0] = ( 227, 252, 3, 0.5)
                pixel.write()
        if vbat_voltage >= 3.8:
                pixel[0] = (0, 255, 0, 0.5)   #set the RGB to green if the battery is above 4.0v
                pixel.write()
        print(vbat_voltage)
        time.sleep(.5) 