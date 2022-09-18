# Bee S3 Arduino Helper Library

Examples can be found in the [Bee Motion S3 Arduino Helper](https://github.com/strid3r21/BeeMotionS3-Arduino-Helper) repo OR these can also be loaded from the examples menu in the Arduino IDE.

## Installation

This library can be installed through the Arduino library manager or manually from github by following [the instructions here](https://docs.arduino.cc/software/ide-v1/tutorials/installing-libraries).

## List of functions

```c++

void begin();

// Set LDO2 on or off
void setLDO2Power(bool on);

// Set neopixel power on or off
void setPixelPower(bool on);

// Set neopixel color
void setPixelColor(uint8_t r, uint8_t g, uint8_t b);
void setPixelColor(uint32_t rgb);
void setPixelColor(green);  //green, red, blue, yellow, pink, purple, orange, white, aqua, off

// Set neopixel brightness
void setPixelBrightness(uint8_t brightness);

// Pack r,g,b (0-255) into a 32bit rgb color
static uint32_t color(uint8_t r, uint8_t g, uint8_t b);

// Convert a color wheel angle (0-255) to a 32bit rgb color
static uint32_t colorWheel(uint8_t pos);

// Get the battery voltage in volts
float getBatteryVoltage();

// Get the light sensor in volts (0-3.3)
float getLight();

// Detect if VBUS (USB power) is present
bool getVbusPresent();

```
