#!usr/bin/python
# -*- coding: utf-8 -*-

import vrep
import ePuckVRep
import time
import numpy as np
import random

# Read the current state
def read_current_state():
    
    # Statements for reading the current state
    
    return current_state
    
def get_command(current_state)
    
    # Statements
    
    return command
    
def Act(command, flag):
    #1 转弯
    #2 直走，follow the line
    
    # don't forget to modify the direction flag
    
    return 

    
def train():
    while True :
        #Initialize the initial state
        current_state = read_current_state()
        #Initialize the direction flag
        flag = 3
        while current_state != 2 #until current_state = terminal state
            # Get the command
            command = get_command(current_state)
            # Go to the next state
            Act(command, flag)
            # Read the new state
            new_state = read_current_state()
            # Update the Q-table
            update()
            # Update the current state
            current_state = new_state
    return
    
def pridict()
    current_state = read_current_state()
    while current_state != 2
        command = get_command(current_state)
        Act(command, flag)
        current_state = read_current_state()
    return
    
    
# def train()
    # # Initialize the direction flag
    # flag_dir = 3 
    # direction = 3
    # # Initialize the current state
    # current_state = read_current_state() 
    # while True :
        # Act(current_state, direction, flag_dir)
        # # Read the new state
        # new_state = read_current_state() 
        # # Give the reward according to the new state
        # reward()
        # # Update the current state
        # current_state = new_state 
    # return

time.sleep( 3 )
print " Program started "
vrep . simxFinish ( -1) # just in case , close all opened connection
clientID = vrep . simxStart ('127.0.0.1', 19999 , True , True , 5000 , 5)

if clientID != -1:
    print " Success !"
else :
    print " Connection fail ."
    
    
if __name__ == '__main__':
    epuck = ePuckVRep.ePuck( host ='127.0.0.1', port =19999 , debug = True )
       
    epuck.connect()
    epuck.set_debug(True)
    epuck.reset()
        
 #############################################################################
    train()
    save()
    Load()
    pridict()
    

    

################################################################################  
