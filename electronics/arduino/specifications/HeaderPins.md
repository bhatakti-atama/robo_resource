# Digital Pins
<p> Two digital pin headers are along the top. These are the Digital Inputs or Outputs pins that are used to control a relay, 
    blink an LED, switches or connect to more complex components. They use 5V for HIGH signals, and 0V for LOW signals. The maximum current per pin is 40mA, 
    but the recommended is 20mA. </p>
<p> Starting from the right ... </p>

+  The two pins labelled 0 (RX) and 1 (TX) are the two Serial pins that are used to send data to and from the Arduino to the USB-Serial translator chip. 
   <b> Don't connect anything to Digital 0 or 1 unless you are super sure because it will affect Arduino's ability to communicate!</b>

+  Digital Pins 2 - 13 are normal digital pins. These pins can be used for both digital input (like telling if a button is pushed) and digital output (like                  powering an LED). Pin 13 is also connected to the L LED. When used the L LED will also blink at the same time.
   To use these pins, following functions are used:
  
   #### pinMode (pin_number, mode)
      This function is used to configure these pins as either INPUT or OUTPUT  
      pin_number is the pin which we want to use  
      mode is how you want to use it  
      pinMode (3, INPUT) sets the pin as an INPUT pin  
      pinMode (3, OUTPUT) sets the pin as an OUTPUT pin  
   #### digitalRead (pin_number)
      This function reads, or takes a digital value from the pin specified(pin_number) which can be assigned to a variable. The value is either HIGH (1) or LOW (0)  
      e.g. val = digitalRead (10)
   #### digitalWrite (pin_number, value)
      This function writes, meaning gives the digital value to the specified pin given by pin_number. value takes in two values HIGH(1) or LOW (0)
   
   The above functions can be easily understood with the Blink LED example.  
   Some of the pins (3,5,6,9,10,11) have ‘~’ in front of them. These are used for Pulse Width Modulation (PWM) and used with **analogWrite()** function.  
   To learn about PWM go this link, https://learn.sparkfun.com/tutorials/pulse-width-modulation  

# Analog Pins
<p>The Analog input pins are special pins that can read sensors. They can also be used as digital input/output pins. Each Analog pin can read a voltage between 0 and 5 V    (the same voltage used to power the Arduino). These pins can read the signal from an Analog sensor (like a temperature sensor) and convert it into a digital value 
   ( 0 - 1023, as we get 10-bit Analog-to-Digital Conversion in UNO) that we can read.</p>
   <b>Do not connect a voltage higher than 5V to the Analog input pins as they can be damaged!</b>
   These pins are used the same way digital pins are used i.e.
   
   #### pinMode (pin_number, mode)
   Specifies which pins will be used (pin_number) and in what mode (INPUT or OUTPUT) 
   #### analogRead (pin_number) 
   Function measure the voltage between 0-5V present at the specified pin and converts it into a digital value between 0 to 1023 which can be assigned to a variable.  
   e.g. val = analogRead (A0)
   #### analogWrite (pin_number, value)
   This function writes the value to the specified pin_number. Important thing to note is that the pins in this case are the PWM pins (3, 5, 6, 9, 10, 11) and value        ranges from 0 – 255.  
   
   These functions can be easily understood using the Fade LED example.  
   To know how Analog pins can also be used as Digital I/O (Input/Output) pins,see this link http://waihung.net/arduino-tip-turn-your-analog-pins-into-digital-io/

# Power Pins
   The power header is in the middle bottom. Used to borrow power from the USB or DC jack.  
   Starting from the *right* we have,  
   + **VIN PIN** - Connected to the power input from the DC Jack, so it is going to range from 7 V to 12 VDC, depending on what is plugged into the DC Jack. If the DC        Jack is not powered, it will provide the 5V from the USB connection.You can supply voltage through this pin, or, if supplying voltage via the power jack, access it through this pin but it should be in **7 - 12 V** range. 
   + **GND** - You get two of these here, they are the common GND connection for all power and data.
   + **5V PIN** - This is the clean regulated 5V power that the Arduino runs on, provided from the DC jack (if plugged in) or USB connection (if DC is not plugged in).        Provides up to about 500mA current draw.
   + **3.3V PIN** - This is a clean regulated 3.3V power, sometimes you'll need exactly this voltage for some sensors. Provides up to about 100mA current draw.
   

### Miscellaneous Pins
+  **AREF**(Digital) - Analog REFerence pin. Used for advanced Analog sensor reading. It is sometimes used to set an external reference voltage (between 0 and 5            Volts) as the upper limit for the Analog input pins. More about use of AREF can be seen in this link, https://tronixstuff.com/2013/12/12/arduino-tutorials-chapter-
+  Two unlabelled pins(Digital) (the labels are on the other side), the SDA and SCL pins, which are used for connecting I2C type (e.g. temperature sensors) sensors. They    are connected inside the PCB to A5 and A4 (Analog Pins). Do not use these unless you have an I2C sensor.
+ **RESET**(Power) - This is the same pin connected to the reset button.
+ **IOREF**(Power) - Used by shields (external pre-built Arduino compatible boards) to know what the IO voltage is. You can ignore this pin. 
+ **Unnamed pin**(Power) - Reserved for future use, don't connect to it!


Here's a link to know more in-depth about the Arduino's Pins,like ICSP, SPI, I2C, https://www.circuito.io/blog/arduino-uno-pinout/
