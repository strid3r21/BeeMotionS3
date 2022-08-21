
from time import sleep
import esp32
import neopixel
from machine import Pin
from machine import deepsleep
from time import sleep
import bms3


# Create a NeoPixel instance
# Brightness of 0.3 is ample for the 1515 sized LED
pixel = neopixel.NeoPixel(Pin(bms3.RGB_DATA), 1)
# Turn on the power to the NeoPixel
bms3.set_rgb_power(True)

# set the wake up PIR Sensor to be pin in and name it wake1
wake1 = Pin(bms3.PIR, mode = Pin.IN)

# set GRB to red
pixel[0] = ( 255, 0, 0, 0.5)
pixel.write()

# set the wake up source to be the PIR motion sensor
esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ANY_HIGH)

print('Im awake, but Im going to sleep in 60 seconds')
# VERY IMPORTANT - set the sleep (ie, delay) to minimum 60 seconds.
# if this is set to a low number like 5, then if you need to change the code
# and re-upload it to the board, the board will go to sleep too quickly
# before you can get the new code uploaded. the only way to fix it in
# that scenario is to reflash the micropython firmware to the board.
sleep(60)

deepsleep()