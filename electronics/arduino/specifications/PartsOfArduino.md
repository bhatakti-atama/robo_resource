![alt-text](https://cdn-learn.adafruit.com/assets/assets/000/033/494/small360/arduino_uno.jpg?1467213347 "Arduino UNO")

## Microcontroller
The 'brains' of the Arduino. The thing that you program when you program!. It's what runs the code, like a CPU (Central Processing Unit). 
The microcontroller has:  
•	28 Pins  
•	Powered by 3 or 5 Volts  
•	Requires about 0.1 Watts of power  
•	Runs at 16 MHz  
•	32 KB of flash storage  
•	2 KB of RAM  

## Powering the Board
There are two ways to power your Arduino: you can use the USB connector to connect to a computer or portable power pack or you can plug into a wall adapter, through the 
DC Power Jack. USB can be used to both power and program the board. DC can only be used for power.

The DC Power Jack can be used to provide any voltage from 7 Volts to 12 Volts. This voltage is then also available at **VIN Pin** on the Power Pins.
The onboard power supply allows you to use any wall adapter that gives you 7 Volts to 12 Volts and will regulate (adjust) that voltage down to a very clean 5 volts 
which is available through the **5V Pin** on the Power Headers.  
**NOTE**: The Board needs 2 Volts (may vary from Arduino to Arduino) above the desired level. In this case, 5 Volts + 2 Volts = 7 V. That's where the 7V minimum comes from.  
If you plug in 5V into the DC Power Jack the board will not work.The regulator will take 2 Volts off the input and leave you with just 3 Volts.  

Here's a link to know more about the Power Management System of an Arduino, https://technobyte.org/arduino-uno-power-supply-arduino-hardware-core/

## LEDs
Arduino has some LEDs that it can use to give you an idea of what it is up to. These are used to let you know if something is on and if there's an error.
The Arduino has four LEDs: L, RX, TX, and ON.  
•	**ON LED** - this LED shines green whenever the Arduino is powered. Always check this LED if your Arduino is not acting right, if its flickering or off then you should check your power supply.  
•	**RX and TX LEDs** - They blink whenever information is sent from or to the Arduino through the USB connection.  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The TX LED (transmitting) lights up yellow whenever data is sent from the Arduino to the computer USB port.  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The RX LED (receiving) lights up yellow whenever data is sent to the Arduino from the computer USB port.  
•	**L LED** - this is one LED that you can control. The ON, RX and TX LEDs all light up automatically. The L LED, however, is connected to the Arduino main chip 
    and you can turn it on or off when you start writing code.  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**L is connected to Digital Pin #13.**
    
## Reset Button
The Reset button is often right next to the USB jack but sometimes it’s on the right side of the board. This button is what you can use to restart the Arduino. 
It's handy if you want to re-run your program or if it gets stuck. It's just like restarting a phone if it hangs, but resetting an Arduino is instantaneous, 
it only takes about a second to restart.

## USB Fuse
The USB fuse is a part that is used to protect the Arduino and computer. Unlike a circuit breaker you do NOT have to switch or replace anything. Instead you just have to wait a few minutes and it will automatically heal itself. 

**NOTE: If you find your Arduino's ON LED is no longer on, or it is not connecting over USB. Try disconnecting it, shutting down your computer and waiting 5 minutes before restarting and trying again. This works 99% of the time!**

