# What is Neopixel?

A NeoPixel is just a name that Adafruit uses to refer to a bunch of different RGB (and RGBW) individually addressable LEDs. We’re using a NeoPixel that is using a WS2812 RGB individually addressable LED. The LED itself has three inputs and three outputs. Power, ground, and data are the three inputs, and they are passed through to the next LED in the strip, allowing you to set the Red, Green, and Blue intensities for each LED in the strip individually. The data signal to control the LEDs brightness is timing dependent, and a little complex to generate. Luckily for us, the folks over at Adafruit wrote a nice library that takes care of all that complicated logic and makes it super simple for us to create cool light patterns.

# Installing Neopixel library

It’s listed under the “Sketch>Library” dropdown menu. 

Then, we can search for and install the Adafruit NeoPixel Library.

