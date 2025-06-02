# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *
from time import time

# Begin project code

# DriveTrain Launch 

# Christina Cornejo 

# Last updated - 5/30/25

# This code tells the drivetrain to go back and forth while the motor spins ti lift the arm

start_time = time()
# this is to make sure the drivetrain only drives for 2 minutes on a constant loop 
while time() - start_time < 120:

    # this tells the train how far to go and how fast
    drivetrain.set_drive_velocity(70, PERCENT) 
    drivetrain.drive_for(FORWARD, 105, INCHES, wait=False)

    #this makes sure that the motor spins while the train is driving 
    while drivetrain.is_moving():
        motor_1.set_velocity(5, PERCENT)
        motor_1.spin_to_position(70, DEGREES, wait=False)
        
    #this makes sure the drivetrain goes backwards after 
    drivetrain.set_drive_velocity(70, PERCENT)
    drivetrain.drive_for(REVERSE, 115, INCHES)

    #this tells the motor to go back to 0 degrees 
    while drivetrain.is_moving():
        motor_1.set_velocity(4, PERCENT)
        motor_1.spin_to_position(0, DEGREES)
