### Q) My Arduino Board is not listed?
Go to 'Tools' -> 'Board:' -> 'Boards Manager...'. Wait until the dialogue box has finished downloading some files. Now look for your board in the list. You can filter the list by typing keywords next to 'Type All' (leave it at 'All'). Once you have found your board, install it by clicking the 'Install' button. If you need a particular version, select it first. Installing a board can take a while, so be patient. Wait until the manager is ready, then close it. Go to 'Tools' -> 'Board:' and look for your board somewhere in the list. Select it if you need it now.

### Q) My Arduino Board is still not listed?
Go to the section **'How to install a Boards package?'** 

### Q) How to install a Boards package?
You need a link to a JSON file that describes the Boards package. The manufacturer of the board will have published this link somewhere. Copy it and paste the complete link into the 'Additional Boards Manager URLs:' field of the 'File' -> 'Preferences' dialogue. It is OK to have multiple URLs in this box as long as they are separated by commas.
Close the preferences by clicking 'OK' and then go to 'Tools' -> 'Board:' -> 'Boards Manager...'. Wait until the dialogue box has finished downloading some files. Now look for your new board in the list. You can filter the list by typing keywords next to 'Type All' (leave it at 'All'). Once you have found your board, install its Boards package by clicking the 'Install' button. If you need a particular version of the package, select it first.
Some Boards packages can be really big and downloading can take a while. Wait until the manager is ready, then close it. Go to 'Tools' -> 'Board:' and look for your new board somewhere in the list. Select it if you need it now.

### Q) Why won't the Arduino IDE upload my sketch?
Several causes are possible:
1. wrong or no port selected for the board. Make sure the board is recognized by the computer. You may need to restart the Arduino IDE to help it find the right port;
2. wrong board selected. Not all boards use the same upload speed. Choose the right board and try again;
3. the board is not responding for some reason (no power, automatic reset not working);
4. some boards have selectable upload speeds and you chose the wrong one. Go to the 'Tools' menu and look for a communication speed option. Set it right and try again;
5. bad connection. Use proper wires or a good cable and connect them (or it) properly, then try again;
6. too fast. Some boards allow for very high upload speeds that are too high for your cable/connection. Try a lower upload speed;
7. the program has errors and didn't compile completely. Fix the errors and try again;
8. the serial port of the board is connected to some peripheral like a GPS that may be interfering with the upload. Disconnect everything from the board's serial port except for the computer.

### Q) avrdude: ser_open(): can't open device?
You should do a checklist in order to jump to a conclusion:
1. Make sure that you connect Arduino to PC via USB cable
2. Check if selecting right COM port on Arduino IDE. On Arduino IDE, Go to **Tools >> Port**

a. **If the COM port is available on Arduino IDE:**
Check if any other software is using the same serial port. Two softwares cannot use the same serial port at the same time

b. **If the COM port is NOT available on Arduino IDE:**
* If you have one more USB cable, replace USB cable and then try again
* If you have one more PC, connect Arduino to another PC and then try again
* Reset your PC and then try again
* [Reinstall USB driver](https://www.arduino.cc/en/Guide/DriverInstallation)

### Q) The button doesn't work as expected. I used the digitalRead() function to read the state of the button, but the button state is not changed as expected when press and release button. I press the button once, but Arduino code detects several presses. Why?
Beginners usually get trouble when getting started with a button, pushbutton, switch using digitalRead() function.
To avoid this, beginners SHOULD pay attention to the following issues:

1. **Floating input problem:**

**Symptom:** the reading value from the input pin is not matched with the button's pressing state.

**Cause:** input pin is NOT used pull-up or pull-down resistor

**Solution:** Use pull-up or pull-down resistor. 

2. **Chattering phenomenon**
It should be considered in only some application that needs to detect exactly number of the pressing.

**Symptom:** Button is pressed once, but Arduino code detects several times.

**Cause:** Due to mechanical and physical issues, the state of the button (or switch) is quickly toggled between LOW and HIGH several times

**Solution:** Debounce. See [Arduino - Button Debounce](https://arduinogetstarted.com/tutorials/arduino-button-debounce)

### Q) LCD or LCD I2C LCD has no display. It does not display any characters when running "hello world" example from Arduino IDE. How can we solve it?
Do the following checklist:

1. Make sure that you wire LCD to Arduino correctly. See [Arduino - LCD](https://arduinogetstarted.com/tutorials/arduino-lcd)  or [Arduino - LCD I2C](https://arduinogetstarted.com/tutorials/arduino-lcd-i2c).
2. Make sure that you install the correct library.
3. Make sure that your code is correct.
4. Adjust the contrast of LCD by rotating potentiometer in the backside of LCD

In case of LCD I2C, you can check one more thing:

Depending on manufacturers, the I2C address of LCD may be different. Usually, the default I2C address of LCD is 0x27 or 0x3F. Try these values one by one. If you still failed, run this [I2C scanner code](https://arduinogetstarted.com/tutorials/arduino-lcd-i2c#content_troubleshooting_on_lcd_i2c) to find the correct I2C address.

### Q) Servo motor doesn't move, move slowly, or vibrate even when running the servo example code from Arduino IDE. How to fix it?
Do the following checklist:

1. If you power servo motor from Arduino board, because some kinds of servo motor require more power than Arduino board can provide, use the external power supply for servo motors. See [how to provide extra power for servo motor](https://arduinogetstarted.com/tutorials/arduino-servo-motor#content_additional_knowledge) 
2. If you already used a seperate power supply, make sure that the GND of the extra power supply is connected to GND of Arduino board.

