# What is Neopixel?

A NeoPixel is just a name that Adafruit uses to refer to a bunch of different RGB (and RGBW) individually addressable LEDs.Digital LEDs are the go-to solution for any project that uses RGB LEDs and you want to avoid the rat's nest that ensures when using multiple RGB LEDs, each colour requiring its own connection. Digitally addressable LEDs allow you to control large numbers of LEDs using digital communication to tiny onboard chips integrated into the LEDs which read these digital commands and do all the heavy lifting for you. The go to LED chip for these purposes has been the WS2812 which you might know most prominently as Adafruit’s NeoPixels. The WS2812B LEDs have been around for a few years now, and come in two different flavours, WS2812 and WS2812B. Both operate similarly, however, require slightly different timing according to the datasheet. There are also other chips which power NeoPixel branded LEDs that work in the exact same way, with the same code and are the drop-in replacement, however, the WS2812 line is the most common.

# Why Neopixel?

There are multiple competing libraries, FastLED being the biggest and Adafruit NeoPixel being the most common for beginners.

On ESP8226, your primary choices are:

##### NeoPixelBus
* Smaller than FastLED, more features and pixel support than esp8266_ws2812_i2s
* On Esp8266 you can choose i2s DMA or UART, both avoiding interrupts (NMIs). FastLED uses interrupts which can be problematic if you use other code that relies on interrupts, or wifi (although FastLED allows other fast interrupts to fire in between pixel updates)
* Supports RGBW pixels (not supported by the other 2 libraries)
* Uses I2S interface to drive Neopixels via DMA providing an asynchronous update.
* Can use UART both in a synchronous and asynchronous model, but asynchronous limits the use of other UART libraries.
* Low level API with other features exposed by external classes.
* Pins available for use varies by platform due to hardware limitations.
* ESP32 support for using both RMT and i2s. RMT timing currently is sensitive to high interrupt frequency due to issues in the Core.

##### FastLED
* Very rich API, although at a cost of large code and memory size
* Interrupt driven on ESP8266, so it's sensitive to timing.
* ESP32 support uses RMT which currently is sensitive to timing.
##### Adafruit::NeoPixel
* Basic bit bang and interrupt driven library which does not support any other interrupt driven code to work. Not recommended.

On ESP32, both FastLED and NeoPixelBus can provide more than one channel/bus. FastLED primarily uses RMT to support 8 parallel channels. NeoPixelBus now supports the RMTs 8 channels and two more channels using i2s. Parallel channels provides for better refresh rate on longer strings (useful past 256 pixels). But do note that the latest cores have issues with high interrupt frequency causing timing issues.

# Installing Neopixel library

It’s listed under the “Sketch>Library” dropdown menu. 

Then, we can search for and install the Adafruit NeoPixel Library. 

### Please read the [Adafruit NeoPixel Best Practices](https://learn.adafruit.com/adafruit-neopixel-uberguide/best-practices) guide before connecting your NeoPixels, it will save you a lot of time and effort.

# Following tutorials are aimed at giving you a basic understanding of niopixel library

#### [How to Control WS2812 RGB LED (NeoPixel) w/ Arduino](https://electropeak.com/learn/control-ws2812-rgb-led-neopixel-w-arduino-tutorial/) Learn to interface neopixel with arduino

#### [Adafruit’s NeoPixel Guide](https://learn.adafruit.com/adafruit-neopixel-uberguide/the-magic-of-neopixels) provides a great overview of what the WS2812 LEDs (aka NeoPixels) are and how to get started with them.

#### [Controlling and powering NeoPixels with Arduino](https://www.arduinoplatform.com/arduino-visual-output/controlling-and-powering-neopixels-with-arduino/)


