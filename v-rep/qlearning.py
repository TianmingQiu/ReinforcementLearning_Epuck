# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:51:26 2017

@author: Lingfeng
"""
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
    #np.save("Q.npy",Q)
    
    for i in reward:
        Boolean = i != 0 
        valid_action.append(np.array(list(range(reward.shape[1])))[Boolean == True])   
    
    for i in xrange(num_episodes):       
        current_state = start_state
        #Q = np.load("Q.npy")
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
            
            #np.save("Q.npy",Q)
            
    #Q = np.load("Q.npy")
    
    for i in xrange(len(Q)):        
        pi.append(valid_action[i][np.argmax(Q[i][valid_action[i]])])

    return pi,Q

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
                [-1,2,18,5],
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

start_state = 17
goal_state = 2
start_orientation = 3


[pi,Q] = qlearning(reward,transition_matrix,start_state,goal_state)
sss=[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,]
print sss
print pi
np.set_printoptions(threshold='nan')
print Q
np.save("Q1.npy",Q)