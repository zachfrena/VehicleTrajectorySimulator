# The class CarSimulator is a simple 2D vehicle simulator.

# The vehicle states are:
# - x: is the position on the x axis on a xy plane
# - y: is the position on the y axis on a xy plane
# - v is the vehicle speed in the direction of travel of the vehicle
# - theta: is the angle wrt the x axis (0 rad means the vehicle
#   is parallel to the x axis, in the positive direction;
#   pi/2 rad means the vehicle is parallel
#   to the y axis, in the positive direction)

# simulatorStep() is a function that updates the vehicle states, given 3 inputs:
#  - a: commanded vehicle acceleration
#  - wheel_angle: steering angle, measured at the wheels;
#    0 rad means that the wheels are "straight" wrt the vehicle.
#    A positive value means that the vehicle is turning counterclockwise
#  - dt: duration of time after which we want to provide
#    a state update (time step)

# main() will run an arbitrary simulation for an arbitrary amount of time and 
# will generate a plot (on the xy plane) of the vehicle trajectory

import math
from matplotlib import pyplot as plt
import numpy as np


class CarSimulator():
    def __init__(self, wheelbase, v0, theta0):
        # the wheel base is the distance between the front and the rear wheels
        self.wheelbase = wheelbase
        self.x = 0
        self.y = 0
        self.v = v0
        self.theta = theta0

    def simulatorStep(self, a, wheel_angle, dt):
        arc_length = (self.v)*(dt)+0.5*a * math.pow(dt, 2)  # total distance traveled along curved path
        turning_radius = (self.wheelbase)/(math.tan(wheel_angle)) # assumes parallel steering and a constant wheel angle
        central_angle = (arc_length)/(turning_radius) # assumes a fixed point car turns about
        x_relative = (math.sin(central_angle))*turning_radius 
        y_relative = turning_radius-turning_radius*(math.cos(central_angle))
        self.x = self.x + (x_relative)*math.cos(self.theta) - y_relative*math.sin(self.theta) # accounting for the relative frame of reference
        self.y = self.y + (x_relative)*math.sin(self.theta) + y_relative*math.cos(self.theta) 
        self.v = self.v + a * (dt) # initial velocity plus acceleration component
        self.theta = self.theta + (arc_length/turning_radius) # accounting for relative frame of reference


def main():
    wheelbase = 4  # arbitrary 4m wheelbase
    v0 = 10
    theta0 = 0
    simulator = CarSimulator(wheelbase, v0, theta0)
    dt = 0.1  # arbitrarily set the time step to 0.1s
    x_coords = [simulator.x]  # populate with initial conditions
    y_coords = [simulator.y]
    theta = [simulator.theta]
   
#--- testing alternating left and right turns; should result in straight line---
    # steps = [[2, 0.374, dt],  # left turn
    #          [2, -0.374, dt],  # right turn
    #          [3, 0.374, dt],  # left turn
    #          [0, -0.374, dt],  # right turn
    #          [1, 0.374, dt],  # left turn
    #          [1, -0.374, dt],  # right turn
    #          [1, 0.374, dt]]  # left turn

#--- arbitrary input for acceleration and wheel_angle---
    steps = [[2, 0.474, dt],  # left turn
             [1.8, -0.633, dt],  # right turn
             [3.2, 0.524, dt],  # left turn
             [0, -0.634, dt],  # right turn
             [1, -0.334, dt],  # right turn
             [1.5, 0.606, dt],  # left turn
             [-1, 0.539, dt],  # left turn
             [2, -0.403, dt]]  # right turn


    for step in steps:
        simulator.simulatorStep(step[0], step[1], step[2]) # iterate through array of simulated steps  
        x_coords.append(simulator.x) # array used for plotting purposes
        y_coords.append(simulator.y)
        theta.append(simulator.theta)

#--- calculating the step lines (i.e. lines that represent the angle of car at each step)---
    step_lines=[]
    for i in range(0,len(steps)):
        intercept=y_coords[i]-math.tan(theta[i])*x_coords[i]
        step_lines.append([x_coords[i]-0.25, x_coords[i]+0.25])
        step_lines.append([math.tan(theta[i])*(x_coords[i]-0.25)+intercept, math.tan(theta[i])*(x_coords[i]+0.25)+intercept])

    # graphically plotting the vehicle trajectory on the xy plane
    plt.scatter(x_coords, y_coords, label="point that the car passes through")
    for i in range(0,len(step_lines),2): # plotting the short red car-angle lines
        plt.plot(step_lines[i], step_lines[i+1],'r-')
    plt.plot(step_lines[0], step_lines[1],"-r", label="angle of car (theta) at the beginning of each step")
    plt.title('Vehicle trajectory on the x-y plane')
    plt.xlabel('x_position')
    plt.ylabel('y_position')
    plt.legend()
    plt.ylim(-0.4,0.4) # good range for the selection of simulated steps. May require changing depending on steps 
    plt.show()


main()
