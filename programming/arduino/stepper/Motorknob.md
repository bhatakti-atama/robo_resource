
# MotorKnob
In this example, a potentiometer (or other sensor) on analog input 0 is used to control the movement of a stepper motor using the Arduino Stepper Library. The stepper is controlled by with digital pins 8, 9, 10, and 11 for either unipolar or bipolar motors.

 A stepper motor follows the turns of a potentiometer
 (or other sensor) on analog input 0.
 
    #include <Stepper.h>

change this to the number of steps on your motor

    #define STEPS 100

create an instance of the stepper class, specifying
the number of steps of the motor and the pins it's
attached to

    Stepper stepper(STEPS, 8, 9, 10, 11);

the previous reading from the analog input

    int previous = 0;

    void setup() {
set the speed of the motor to 30 RPMs

    stepper.setSpeed(30);
    }

    void loop() {

get the sensor value

    int val = analogRead(0);

move a number of steps equal to the change in the
sensor reading

    stepper.step(val - previous);

remember the previous value of the sensor

      previous = val;
    }
    
## For more info on Motor Knob, click [here](https://www.arduino.cc/en/Tutorial/LibraryExamples/MotorKnob)
