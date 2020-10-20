# What is Neopixel?

A NeoPixel is just a name that Adafruit uses to refer to a bunch of different RGB (and RGBW) individually addressable LEDs.Digital LEDs are the go-to solution for any project that uses RGB LEDs and you want to avoid the rat's nest that ensures when using multiple RGB LEDs, each colour requiring its own connection. Digitally addressable LEDs allow you to control large numbers of LEDs using digital communication to tiny onboard chips integrated into the LEDs which read these digital commands and do all the heavy lifting for you. The go to LED chip for these purposes has been the WS2812 which you might know most prominently as Adafruit’s NeoPixels. The WS2812B LEDs have been around for a few years now, and come in two different flavours, WS2812 and WS2812B. Both operate similarly, however, require slightly different timing according to the datasheet. There are also other chips which power NeoPixel branded LEDs that work in the exact same way, with the same code and are the drop-in replacement, however, the WS2812 line is the most common.

# Why Neopixel?

NeoPixel LEDs represent the first widely available DIY form of digital RGB LEDs with example code, libraries and supporting content to make them useable for makers everywhere. From just a single pin you can control a (theoretically) as many LEDs as you want(an Arduino Uno has 2kb of memory. One Neopixel led uses 3 bytes of memory. That means you can drive about 600 Neopixels, or a bit less, depending on the size of the rest of your program), however, there are a few limitations. Namely that each LED consumes a few bytes of RAM, and because of the relatively low speed of data, once you use more than a few hundred LEDs, you may start to notice slight buffering time across the pixels. Because of the slow (400Hz) refresh/PWM cycle, NeoPixels can't be used reliably for POV (Persistance of Vision) displays, or anything that requires high FPS.

NeoPixels, however, are incredibly cheap, especially compared to DotStar LEDs.

# Installing Neopixel library

It’s listed under the “Sketch>Library” dropdown menu. 

Then, we can search for and install the Adafruit NeoPixel Library. 

### Please read the [Adafruit NeoPixel Best Practices](https://learn.adafruit.com/adafruit-neopixel-uberguide/best-practices) guide before connecting your NeoPixels, it will save you a lot of time and effort.

# Following tutorials are aimed at giving you a basic understanding of niopixel library

#### [How to Control WS2812 RGB LED (NeoPixel) w/ Arduino](https://electropeak.com/learn/control-ws2812-rgb-led-neopixel-w-arduino-tutorial/)

#### [Adafruit’s NeoPixel Guide](https://learn.adafruit.com/adafruit-neopixel-uberguide/the-magic-of-neopixels) provides a great overview of what the WS2812 LEDs (aka NeoPixels) are and how to get started with them.

#### [Controlling and powering NeoPixels with Arduino](https://www.arduinoplatform.com/arduino-visual-output/controlling-and-powering-neopixels-with-arduino/)


