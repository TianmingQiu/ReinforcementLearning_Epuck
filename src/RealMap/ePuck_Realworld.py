#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#         ePuck_Realworld.py
#
#         Copyright 2017 Tianming Qiu   <tianming.qiu@tum.de>
#                        Lingfeng Zhang <lingfeng.zhang@gmx.de>
#                        Wenhan Hao     <ga94caf@mytum.de>
#
#         Applied Reinforcement Learning SoSe 2017
#         
#         This code is used for epuck training and final implementation on Vrep
#         



import time
import numpy as np
import random
from bluetooth import *
import ePuck



def qlearning_train(reward,start_state,goal_state):
    # Epsilon-greedy for Exploration-Exploitation problem
    # Probability of random action
    epsilon = 0.90
    # Learning rate
    alpha = 0.1
    # Discount factor
    gamma = 0.99
    
    # Set orientation to east initially
    start_orientation = 3
    current_orientation = start_orientation
    current_state = start_state
    valid_action = []

    # find the valid action for each state
    for i in reward:
        Boolean = i != 0 
        valid_action.append(np.array(list(range(reward.shape[1])))[Boolean == True]) 
    
      
    # Since we have to change the start state at each episode
    # so we save and load Q value table also at each episode
    Q = np.load("Q.npy")
    while current_state != goal_state:
        if np.random.rand() < epsilon:            
            action = valid_action[current_state][np.argmax(Q[current_state][valid_action[current_state]])]
        else: 
            action = int(random.sample(valid_action[current_state],1)[0])
        print "Current orientation：%d 0-North|1-South|2-West|3-East" %current_orientation
        print "Command：%d             0-North|1-South|2-West|3-East" %action
        
        # excute specific action on Vrep:
        Act(action, current_orientation)
        current_orientation = int(action)
        next_state = int(read_state())
        
        furture_reaward = []

        for action_nxt in valid_action[next_state]:
            furture_reaward.append(Q[next_state][action_nxt])
        
        # Update Q table
        Q[current_state][action] = Q[current_state][action] + alpha*(reward[current_state][action] + gamma * max(furture_reaward) - Q[current_state][action])           
        #print "Q value table at state%d" %current_state
        #print Q[current_state]
        current_state = next_state
        
        
    np.save("Q.npy",Q)
    np.set_printoptions(threshold='nan')
    print Q # after one time training, save Q table for this episode
            
    return



def east(current_direction):
 
    if current_direction == 0:
        turnspeed = 300
    elif current_direction == 1:
        turnspeed = -300
    elif current_direction == 3:
        turnspeed = 0
    else:
        turnspeed = 600
        

    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 0.72 )
    epuck.set_motors_speed(0, 0)
    epuck.step()
    print "Epuck is now going east"
    
def south(current_direction):
   
    if current_direction == 2:
        turnspeed = -300
    elif current_direction == 3:
        turnspeed = 300
    elif current_direction == 1:
        turnspeed = 0        
    else:
        turnspeed = 600
        

    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 0.72 )
    epuck.set_motors_speed(0, 0)
    epuck.step()
    print "Epuck is now going south"

def west(current_direction):
 
    if current_direction == 0:
        turnspeed = -300
    elif current_direction == 1:
        turnspeed = 300
    elif current_direction == 2:
        turnspeed = 0        
    else:
        turnspeed = 600
        

    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 0.72)
    epuck.set_motors_speed(0, 0)
    epuck.step()  
    print "Epuck is now going west"

def north(current_direction):
   
    if current_direction == 2:   # west
        turnspeed = 300
    elif current_direction == 3: # east
        turnspeed = -300
    elif current_direction == 1: # south
        turnspeed = 600        
    else:                        # nort
        turnspeed = 0
        

    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 0.72 )
    epuck.set_motors_speed(0, 0)
    epuck.step()  
    print "Epuck is now going north"

def Act(command, flag):
    
    if command == 0:    
        north(flag)
    elif command == 1:
        south(flag)
    elif command == 2:
        west(flag)
    else:
        east(flag)
     
    # Leave the state unit after turning 
    
    epuck.set_motors_speed(200, 200)
    epuck.step()
    time.sleep(1.35)
    epuck.set_motors_speed(0, 0)
    epuck.step()
    time.sleep(0.2)
    
    speedl = 200
    speedr = 200
    while True :
        
        epuck.step()
        b = epuck.get_floor_sensors() 

        #Stop
        if (b[0]>500 and b[0]<800 and b[1]>500 and b[1]<800) or (b[1]>500 and b[1]<800 and b[2]>500 and b[2]<800) or (b[2]>500 and b[2]<800 and b[0]>500 and b[0]<800) :
            epuck.set_motors_speed(0, 0)
            epuck.step()
            time.sleep(1)
            print "arrive at a new state"
            break
            
        #Go straight
        if (b[0]>900 and b[2]>900) or (b[0]<450 and b[2]<450) :
            epuck.set_motors_speed(speedl, speedr)
            epuck.step()
            
      	#Turn right
        elif ( b[0]>900 and b[2]<450 ) :
    			epuck.set_motors_speed(0.5*speedl, 0.1*speedr)
    			epuck.step()
            
      	#Turn left
        elif b[0]<450 and b[2]>900 :
    			epuck.set_motors_speed(0.1*speedl, 0.5*speedr)
    			epuck.step()
    		
        else :
            print "Cannot recognize the color!"
    
    
    
   


def read_state():
    # From stop line to state encoder unit
    s = [3, 3, 3]
    time.sleep(1)
    speedl = 200
    speedr = 200 
    epuck.set_motors_speed(speedl, speedr)
    epuck.step()
    
    time.sleep(0.2)
    
    epuck.set_motors_speed(0,0)
    epuck.step()
    time.sleep(0.1)
    
    s[0] = read_state_step()
    s[1] = read_state_step()
    s[2] = read_state_step()
    state_number = 9 * s[0] + 3 * s[1] + s[2]
    print s
    print "State Reading: S_%d" % state_number
    return state_number
    
def read_state_step():

    epuck.step()
    sensor_value = epuck.get_floor_sensors()
    for i in [0,1,2]:
        if sensor_value[i] >= 900:
            b[i] = 2
        elif sensor_value[i] <= 450:
            b[i] = 0
        else:
            b[i] = 1
    print "sensor digital value"
    print b
    
    if ((b[0]==2 and b[1]==2) or (b[1]==2 and b[2]==2) or (b[0]==2 and b[2]==2)):
        digit = 2
    elif ((b[0]==0 and b[1]==0) or (b[1]==0 and b[2]==0) or (b[0]==0 and b[2]==0)):
        digit = 0
    elif ((b[0]==1 and b[1]==1) or (b[1]==1 and b[2]==1) or (b[0]==1 and b[2]==1)):
        digit = 1
    else:
        print "0 1 2 Error!"
        

    time.sleep(0.5)

    epuck.set_motors_speed(200, 200)
    epuck.step()
    time.sleep(0.4)
    epuck.set_motors_speed(0, 0)
    epuck.step()
    time.sleep(0.1)
    return digit
    

def run (start_state,goal_state,start_orientation):
    Q = np.load("Q_final.npy")
    
    current_state = start_state
    current_orientation = start_orientation

    while current_state != goal_state:
        
        action = int(np.argmax(Q[current_state]))
        time.sleep(0.2)
        Act(action, current_orientation)        
        time.sleep(1)
        current_orientation = action        
        current_state = read_state()
        print "State Reading: State%d" % current_state






# ---------------------------------------------
# Main body
print " Program started "
epuck = ePuck.ePuck("10:00:E8:D3:AA:03",False)

epuck.connect()
#robot.enable('floor', 'proximity')
epuck.enable('floor')
       

reward = np.array([[ 0, 0, -1,0],   #0
               [ 0,10,-1,-1],
               [-1, -1, 0, 0],
               [10,-1,0,-1],
               [-1,0,0,-1],
               [0,-1,-1,-1],   #5
               [-1,-1,10,0],
               [-1,0,-1,-1],
               [0,-1,-1,-1],
               [-1,-1,-1,0],
               [-1,-1,-1,0], #10
               [-1,0,0,-1],
               [0,-1,-1,-1],
               [-1,-1,-1,0],
               [-1,0,0,-1],
               [0,-1,-1,-1],  #15
               [-1,-1,-1,-1],
               [-1,0,0,-1],
               [0,0,0,-1],
               [0,0,0,-1],
               [0,0,-1,0],
               [0,0,-1,0]])   #21

start_state = 10
goal_state = 2
start_orientation = 3
#pi = [2, 1, 0, 0, 0, 2, 2, 2, 1, 2, 0, 3, 2, 2, 0, 2, 1, 2, 3, 3, 2, 2]
 

# -----------------------------------------------------
# Training:
qlearning_train(reward,start_state,goal_state)
# -----------------------------------------------------
# Final implementation run:
#run(start_state,goal_state,start_orientation)
