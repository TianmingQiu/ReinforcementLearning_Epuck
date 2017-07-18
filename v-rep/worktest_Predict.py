# -*- coding: utf-8 -*-

import vrep
import ePuckVRep
import time
import numpy as np
import random

def qlearning(reward,transition_matrix,start_state,goal_state):
    print "start training!"

    # Probability of random action
    epsilon = 0.90
    # Learning rate
    alpha = 0.1
    # Discount factor
    gamma = 0.99
    start_orientation = 3
    current_orientation = start_orientation
    num_episodes = 1000
    pi = []
    valid_action = []
    Q = np.zeros((reward.shape[0],reward.shape[1]))
    np.save("Q.npy",Q)
    
    for i in transition_matrix:
        Boolean = i >= 0 
        valid_action.append(np.array(list(range(reward.shape[1])))[Boolean == True])   
    
    for i in xrange(num_episodes):       
        current_state = start_state
        Q = np.load("Q.npy")
        while current_state != goal_state:
            if np.random.rand() < epsilon:            
                action = valid_action[current_state][np.argmax(Q[current_state][valid_action[current_state]])]
            else: 
                action = random.sample(valid_action[current_state],1)
            
            Act(action, current_orientation)
            current_orientation = action
            #next_state = int(transition_matrix[current_state][action])
            next_state = int(read_state())
            
            furture_reaward = []
    
            for action_nxt in valid_action[next_state]:
                furture_reaward.append(Q[next_state][action_nxt])
        
            Q[current_state][action] = Q[current_state][action] + alpha*(reward[current_state][action] + gamma * max(furture_reaward) - Q[current_state][action])           
            current_state = next_state
            np.save("Q.npy",Q)
            

    for i in xrange(len(Q)):        
        pi.append(valid_action[i][np.argmax(Q[i][valid_action[i]])])
    print "Finish training!"
    return pi



def east(current_direction):
 
    if current_direction == 0:
        turnspeed = 465
    elif current_direction == 1:
        turnspeed = -465
    elif current_direction == 3:
        turnspeed = 0
    else:
        turnspeed = 1000
        

    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 1.4 )
    epuck.set_motors_speed(0, 0)
    epuck.step()
    print "Epuck is now going east"
    
def south(current_direction):
   
    if current_direction == 2:
        turnspeed = -465
    elif current_direction == 3:
        turnspeed = 465
    elif current_direction == 1:
        turnspeed = 0        
    else:
        turnspeed = 1000
        

    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 1.4 )
    epuck.set_motors_speed(0, 0)
    epuck.step()
    print "Epuck is now going south"

def west(current_direction):
 
    if current_direction == 0:
        turnspeed = -465
    elif current_direction == 1:
        turnspeed = 465
    elif current_direction == 2:
        turnspeed = 0        
    else:
        turnspeed = 1000
        

    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 1.4 )
    epuck.set_motors_speed(0, 0)
    epuck.step()  
    print "Epuck is now going west"

def north(current_direction):
   
    if current_direction == 2:
        turnspeed = 465
    elif current_direction == 3:
        turnspeed = -465
    elif current_direction == 1:
        turnspeed = 0        
    else:
        turnspeed = 1000
        

    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 1.4 )
    epuck.set_motors_speed(0, 0)
    epuck.step()  
    print "Epuck is now going north"

def Act(command, flag):
    speedl = 700
    speedr = 700
    if command == 0:
        north(flag)
    elif command == 1:
        south(flag)
    elif command == 2:
        west(flag)
    else:
        east(flag)
        
    epuck.set_motors_speed(1000, 1000)
    #print "forward a step in oder to avoid detect same state 2 times"
    epuck.step()
    time.sleep(1.6)
    epuck.set_motors_speed(0, 0)
    #print "forward a step in oder to avoid detect same state 2 times"
    epuck.step()
    time.sleep(0.2)
    
    while True :
        
        epuck._sensors_to_read = ['m']
        b = epuck.get_floor_sensors()

        

        #Stop
        if (b[0]>500 and b[0]<1000) or (b[1]>500 and b[1]<1000) or (b[2]>500 and b[2]<1000) :
            epuck.set_motors_speed(0, 0)
            epuck.step()
            time.sleep(0.3)
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
    
    
   


def read_state():
    # 从停止线移动到状态区
    s = [2, 2, 2]
    time.sleep(1)
    speedl = 300
    speedr = 300 
    epuck.set_motors_speed(speedl, speedr)
    epuck.step()
    time.sleep(1.5)
    epuck.set_motors_speed(0,0)
    epuck.step()
    time.sleep(0.1)
    # 读第一个状态
    s[0] = read_state_step()
    s[1] = read_state_step()
    s[2] = read_state_step()
    state_number = 9 * s[0] + 3 * s[1] + s[2]
    print "State Reading: State%d" % state_number
    return state_number
    
    
def read_state_step():
    epuck._sensors_to_read = ['n','m']
    #a=epuck.get_proximity()
    sensor_value = epuck.get_floor_sensors()
    if ((sensor_value[0] + sensor_value[1] + sensor_value[2]) > 3500):
        digit = 2
    elif ((sensor_value[0] + sensor_value[1] + sensor_value[2])<1000):
        digit = 0
    else:
        digit = 1
        
    #print '读了一次'
    #print digit
    time.sleep(0.5)
    speedl = 600
    speedr = 600 
    epuck.set_motors_speed(speedl, speedr)
    epuck.step()
    time.sleep(0.75)
    epuck.set_motors_speed(0, 0)
    epuck.step()
    time.sleep(0.1)
    return digit
    

def run (start_state,goal_state,start_orientation,pi):
    print "start to predict"
    current_state = start_state
    current_orientation = start_orientation
    k = 1
    while current_state != goal_state:
        
        action = pi[current_state]
        time.sleep(0.2)
        Act(action, current_orientation)        
        time.sleep(1)
        current_orientation = action        
        current_state = read_state()
        print "State Reading: State%d" % current_state
        k = k + 1








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
    reward = np.array([[ 0, 0, -1,0],   #0
                       [ 0,10,-1,-1],
                       [-1, -1, 0, -1],
                       [10,-1,0,-1],
                       [-1,0,-1,-1],
                       [0,-1,-1,-1],   #5
                       [-1,-1,10,-1],
                       [-1,0,-1,-1],
                       [0,-1,-1,-1],
                       [-1,-1,-1,-1],
                       [-1,-1,-1,0], #10
                       [-1,0,-1,-1],
                       [0,-1,-1,-1],
                       [-1,-1,-1,-1],
                       [-1,0,-1,-1],
                       [0,-1,-1,-1],  #15
                       [-1,-1,-1,-1],
                       [-1,0,-1,-1],
                       [0,0,0,-1],
                       [0,0,0,-1],
                       [0,0,-1,0],
                       [0,0,-1,0]])   #21
    
    
    # Transition Matrix in order(U D L R) 上下左右
    transition_matrix = np.array([[ -1, -1, 17,-1],   #0
                       [ -1,2,18,5],
                       [1, 3, -1, 6],
                       [2,4,-1,7],
                       [3,-1,19,11],
                       [-1,6,1,8],   #5
                       [5,7,2,9],
                       [6,-1,3,10],
                       [-1,9,5,12],
                       [8,10,6,13],
                       [9,11,7,-1], #10
                       [10,-1,4,14],
                       [-1,13,9,16],
                       [12,14,9,16],
                       [13,-1,11,17],
                       [-1,16,13,21],  #15
                       [15,13,21,17],
                       [16,-1,14,0],
                       [-1,-1,-1,1],
                       [-1,-1,-1,4],
                       [-1,-1,15,-1],
                       [-1,-1,16,-1]])   #21
    
    start_state = 10
    goal_state = 2
    start_orientation = 3
    
    
   
################################################################################  
   # pi = [3, 3, 0, 1, 3, 1, 1, 1, 3, 1, 0]
    pi = [2, 1, 0, 0, 0, 2, 2, 2, 1, 2, 0, 3, 2, 2, 0, 2, 1, 2, 3, 3, 2, 2]
    #pi = qlearning(reward,transition_matrix,start_state,goal_state)
    print pi
    run (start_state,goal_state,start_orientation,pi)
    