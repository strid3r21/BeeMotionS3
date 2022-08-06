
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

print('Im awake, but Im going to sleep')
sleep(10)

deepsleep()