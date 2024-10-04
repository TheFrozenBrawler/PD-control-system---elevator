# PD-control-system---elevator
Project for Microcomputer Systems course with code implementation for control a lift with motor, distance sensor and a platform.

# Details
Projec consist of tower, motor on top, plaftorm connected with motor by string and distance sensor at the bottom. Input signal was required distance set by user and output was position of the platform.

# Code
Code consist of four files:
- main.py - main program for control and startup
- motor_ctr.py - file with motor control function and treshhold created to prevent too low values of PWM
- PD_count.py - function to calculate output of PD regulator based on differential equation
- sensor.py - function to handle distance sensor
