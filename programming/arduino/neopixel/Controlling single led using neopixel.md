    #include <Adafruit_NeoPixel.h>
    #ifdef __AVR__
    #include <avr/power.h> // Required for 16 MHz Adafruit Trinket
    #endif

    #define PIN      6
    #define NUMPIXELS 7


    Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

    #define DELAYVAL 500 // Time (in milliseconds) to pause between pixels

    void setup() {
    pixels.begin();
    }

    void loop() {
    pixels.clear();
    pixels.setBrightness(10);
    pixels.setPixelColor(0, pixels.Color(255, 255, 255));
    pixels.setPixelColor(1, pixels.Color(255, 0, 0));
    pixels.setPixelColor(2, pixels.Color(0, 255, 0));
    pixels.setPixelColor(3, pixels.Color(0, 0, 255));
    pixels.setPixelColor(4, pixels.Color(255, 0, 255));
    pixels.setPixelColor(5, pixels.Color(255, 255, 0));
    pixels.setPixelColor(6, pixels.Color(0, 255, 255));
    pixels.show();
    }

## Code Explanation

    Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

The above function determine the number of LEDs and Arduino pins.

    pixels.begin();

This function does the initializations.

    pixel.setBrightness(b);

The above function set the light intensity. (The minimum number is 1 and maximum number is 255.)

    pixels.setPixelColor(Wich LED,Wich color(Red,Green,Blue));

Defines the LEDs color with the RGB system,  after specifying the LED number (from 0 to NUMPIXELS-1).

    pixels.show();

Displays the applied values.
