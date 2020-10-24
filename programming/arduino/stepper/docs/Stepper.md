# Stepper(steps, pin1, pin2)
# Stepper(steps, pin1, pin2, pin3, pin4)
## Description
This function creates a new instance of the Stepper class that represents a particular stepper motor attached to your Arduino board. Use it at the top of your sketch, above setup() and loop(). The number of parameters depends on how you've wired your motor - either using two or four pins of the Arduino board.

## Parameters
steps: the number of steps in one revolution of your motor. If your motor gives the number of degrees per step, divide that number into 360 to get the number of steps (e.g. 360 / 3.6 gives 100 steps). (int)

pin1, pin2: two pins that are attached to the motor (int)

pin3, pin4: optional the last two pins attached to the motor, if it's connected to four pins (int)

## Returns
A new instance of the Stepper motor class.

## Example
Stepper myStepper = Stepper(100, 5, 6);
