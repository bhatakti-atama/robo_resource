# Stepper Library
This library allows you to control unipolar or bipolar stepper motors. To use it you will need a stepper motor, and the appropriate hardware to control it. For more on that, see [Tom Igoe's notes on steppers.](http://www.tigoe.com/pcomp/code/circuits/motors/stepper-motors/)

## To use this library
#include <Stepper.h>

## Circuits
Unipolar Steppers

[Bipolar Steppers](https://github.com/SamyakJain2002/robo_resource/blob/main/programming/arduino/stepper/docs/Bipolar.md)

## Functions
* Stepper(steps, pin1, pin2)
* Stepper(steps, pin1, pin2, pin3, pin4)
* setSpeed(rpm)
* step(steps)

## Examples
* [Motor Knob](https://github.com/SamyakJain2002/robo_resource/blob/main/programming/arduino/stepper/examples/Motorknob.md): Control a highly accurate stepper motor using a potentiometer.
* [Stepper One Revolution](https://github.com/SamyakJain2002/robo_resource/blob/main/programming/arduino/stepper/examples/stepperOneRevolution.md): Turn the shaft one revolution clockwise and one counterclockwise.
* [Stepper One Step At A Time](https://github.com/SamyakJain2002/robo_resource/blob/main/programming/arduino/stepper/examples/OneStepAt_aTime.md): Turn the shaft step by step to check the proper wiring of the motor.
* [Stepper Speed Control](https://github.com/SamyakJain2002/robo_resource/blob/main/programming/arduino/stepper/examples/SpeedControl.md): Control the stepping speed with a potentiometer.
