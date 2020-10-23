# Stepper: step(steps)
## Description
Turns the motor a specific number of steps, at a speed determined by the most recent call to setSpeed(). This function is blocking; that is, it will wait until the motor has finished moving to pass control to the next line in your sketch. For example, if you set the speed to, say, 1 RPM and called step(100) on a 100-step motor, this function would take a full minute to run. For better control, keep the speed high and only go a few steps with each call to step().

## Parameters
steps: the number of steps to turn the motor - positive to turn one direction, negative to turn the other (int)

## Returns
None
