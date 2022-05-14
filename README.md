# Vehicle Trajectory Simulator

The goal of this project was to build a vehicle trajectory simulator that would calculate the state of a vehicle based on a series of inputs.

## The overall vehicle state is represented by the following variables:
- `x`: is the position on the x axis on an xy plane.
- `y`: is the position on the y axis on an xy plane.
- `v`: is the vehicle's speed (in the direction of travel of the vehicle).
- `theta`: is the angle with respect to the x-axis (0 rad means the vehicle is parallel to the x axis, in the positive direction; pi/2 rad means the vehicle is parallel to the y axis, in the positive direction).

## The 4 inputs are:
- `a`: value of vehicle acceleration.
- `wheel_angle`: steering angle, measured at the wheels; 0 rad means that the wheels are "straight" wrt the vehicle. A positive value means that the vehicle is turning counterclockwise.
- `dt`: duration of time after which we want to provide a state update (time step).

Following the calculation, a plot (on the xy plane) of the vehicle trajectory will be displayed.

## The math and trigonometry used to calculate the vehicles trajectory after a single step is shown below:
<p align="center">
  <img width="550" src="https://github.com/zachfrena/VehicleTrajectorySimulator/blob/main/vehicleTrajectoryMath.jpg">
</p>

