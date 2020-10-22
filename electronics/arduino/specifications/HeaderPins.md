# Digital Pins

<p> Two digital pin headers are along the top. These are the Digital Inputs or Outputs pins that are used to control a relay, 
    blink an LED, switches or connect to more complex components. They use 5V for HIGH signals, and 0V for LOW signals. </p>
<p> Starting from the *right* ... </p>

+  The two pins labelled 0 (RX) and 1 (TX) are the two Serial pins that are used to send data to and from the Arduino to the USB-Serial translator chip. 
       <b> Don't connect anything to Digital 0 or 1 unless you are super sure because it will affect Arduino's ability to communicate!</b>

+  Digital Pins 2 - 13 are normal digital pins. These pins can be used for both digital input (like telling if a button is pushed) and digital output (like                    powering an LED). Pin 13 is also connected to the L LED. When used the L LED will also blink at the same time.
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
   Some of the pins (3,5,6,9,10,11) have ‘~’ in front of them. These are used for Pulse Width Modulation (PWM).  
   To learn about PWM go this link, https://learn.sparkfun.com/tutorials/pulse-width-modulation  
+  AREF - Analog REFerence pin. Used for advanced Analog sensor reading. It is sometimes used to set an external reference voltage (between 0 and 5 Volts) as the upper        limit for the Analog input pins. More about use of AREF can be seen in this link, https://tronixstuff.com/2013/12/12/arduino-tutorials-chapter-
