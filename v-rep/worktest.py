# -*- coding: utf-8 -*-

import vrep
import ePuckVRep
import time
import numpy as np
import random

def qlearning(reward,transition_matrix,start_state,goal_state):


    # Probability of random action
    epsilon = 0.90
    # Learning rate
    alpha = 0.1
    # Discount factor
    gamma = 0.99
    
    num_episodes = 1000
    pi = []
    valid_action = []
    Q = np.zeros((reward.shape[0],reward.shape[1]))
    
    for i in transition_matrix:
        Boolean = i >= 0 
        valid_action.append(np.array(list(range(reward.shape[1])))[Boolean == True])   
    
    for i in xrange(num_episodes):       
        current_state = start_state
    
        while current_state != goal_state:
            if np.random.rand() < epsilon:            
                action = valid_action[current_state][np.argmax(Q[current_state][valid_action[current_state]])]
            else: 
                action = random.sample(valid_action[current_state],1)
        
            next_state = int(transition_matrix[current_state][action])
            furture_reaward = []
    
            for action_nxt in valid_action[next_state]:
                furture_reaward.append(Q[next_state][action_nxt])
        
            Q[current_state][action] = Q[current_state][action] + alpha*(reward[current_state][action] + gamma * max(furture_reaward) - Q[current_state][action])           
            current_state = next_state

    for i in xrange(len(Q)):        
        pi.append(valid_action[i][np.argmax(Q[i][valid_action[i]])])

    return pi



def east(current_direction):
    speedl = 300
    speedr = 300    
    if current_direction == 0:
        turnspeed = 250
    elif current_direction == 1:
        turnspeed = -250
    elif current_direction == 3:
        turnspeed = 0
    else:
        turnspeed = 500
        
    epuck.set_motors_speed(speedl, speedr)
    epuck.step()
    time.sleep( 2 )
    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 2 )
    epuck.set_motors_speed(0, 0)
    epuck.step()
    print "Epuck is now going east"
    
def south(current_direction):
    speedl = 300
    speedr = 300    
    if current_direction == 2:
        turnspeed = -250
    elif current_direction == 3:
        turnspeed = 250
    elif current_direction == 1:
        turnspeed = 0        
    else:
        turnspeed = 500
        
    epuck.set_motors_speed(speedl, speedr)
    epuck.step()
    time.sleep( 2 )
    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 2 )
    epuck.set_motors_speed(0, 0)
    epuck.step()
    print "Epuck is now going south"

def west(current_direction):
    speedl = 300
    speedr = 300    
    if current_direction == 0:
        turnspeed = -250
    elif current_direction == 1:
        turnspeed = 250
    elif current_direction == 2:
        turnspeed = 0        
    else:
        turnspeed = 500
        
    epuck.set_motors_speed(speedl, speedr)
    epuck.step()
    time.sleep( 2 )
    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 2 )
    epuck.set_motors_speed(0, 0)
    epuck.step()  
    print "Epuck is now going west"

def north(current_direction):
    speedl = 300
    speedr = 300    
    if current_direction == 2:
        turnspeed = 250
    elif current_direction == 3:
        turnspeed = -250
    elif current_direction == 1:
        turnspeed = 0        
    else:
        turnspeed = 500
        
    epuck.set_motors_speed(speedl, speedr)
    epuck.step()
    time.sleep( 2 )
    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 2 )
    epuck.set_motors_speed(0, 0)
    epuck.step()  
    print "Epuck is now going north"

def Act(command, flag):
    speedl = 300
    speedr = 300
    if command == 0:
        north(flag)
    elif command == 1:
        south(flag)
    elif command == 2:
        west(flag)
    else:
        east(flag)
    epuck.set_motors_speed(200, 200)
    print "forward a step in oder to avoid detect same state 2 times"
    epuck.step()
    time.sleep(1)
    epuck.set_motors_speed(0, 0)
    epuck.step()
    while True :
        
        epuck._sensors_to_read = ['m']
        b = epuck.get_floor_sensors()

        

        #Stop
        if (b[0]>500 and b[0]<1000) or (b[1]>500 and b[1]<1000) or (b[2]>500 and b[2]<1000) :
            epuck.set_motors_speed(0, 0)
            epuck.step()
            time.sleep(3)
            print "arrive at a new state"
            break
            
		#Go straight
        if (b[0]>1000 and b[2]>1000) or (b[0]<500 and b[2]<500) :
            epuck.set_motors_speed(speedl, speedr)
            epuck.step()
            
		#Turn right
        elif ( b[0]>1000 and b[2]<500 ) :
			epuck.set_motors_speed(0.7*speedl, 0.1*speedr)
			epuck.step()
            
		#Turn left
        elif b[0]<500 and b[2]>1000 :
			epuck.set_motors_speed(0.1*speedl, 0.7*speedr)
			epuck.step()
		
        else :
            print "Here is an error!"
    
    
   




def run (transition_matrix,start_state,goal_state,start_orientation,pi):

    current_state = start_state
    current_orientation = start_orientation
    k = 1
    while current_state != goal_state:
        print "Epuck thinks it was at State%d" % current_state
        action = pi[current_state]
        time.sleep(1)
        Act(action, current_orientation)
        time.sleep(1)
        current_orientation = action        
        current_state = int(transition_matrix[current_state][action])
        k = k + 1







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
    reward = np.array([[ 0, 0, 0,-1],   #0
                       [ 0,-1,-1,-1],
                       [-1, 0, 0, 0],
                       [ 0,-1,-1,-1],
                       [ 0,-1,-1,-1],   
                       [-1,-1, 0,-1],   #5
                       [-1,-1,-1,-1],
                       [-1,-1,-1, 0],
                       [-1, 0,-1,-1],
                       [-1,10,-1, 0],
                       [-1, 0, 0, 0]])   #10
    
    
    # Transition Matrix in order(U D L R) 上下左右
    transition_matrix = np.array([[-1,-1,-1, 1],   #0
                          [-1, 2, 0, 3],
                          [ 1,-1,-1,-1],
                          [-1, 5, 1, 4],
                          [-1, 6, 3, 7],
                          [ 3, 8,-1, 6],    #5
                          [ 4, 8, 5, 7],
                          [ 4, 9, 6,-1],
                          [ 6,-1, 5, 9],
                          [ 7,10, 8,-1],
                          [ 9,-1,-1,-1]])   #10
    
    start_state = 0
    goal_state = 10
    start_orientation = 3    
################################################################################  
    pi = [3, 3, 0, 1, 3, 1, 1, 1, 3, 1, 0]
    run (transition_matrix,start_state,goal_state,start_orientation,pi)