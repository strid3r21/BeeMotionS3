import time
import neopixel
import board, digitalio
import bms3

PIR = digitalio.DigitalInOut(board.PIR)
PIR.direction = digitalio.Direction.INPUT

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=True, pixel_order=neopixel.GRB)
bms3.set_ldo2_power(True)

while True:
   if PIR.value == True:
        pixel[0] = ( 0, 0, 255, 0.5)
        pixel.write()
        time.sleep(2)
   else:
          pixel[0] = ( 0, 0, 0, 0.5)
          pixel.write()
          time.sleep(2)