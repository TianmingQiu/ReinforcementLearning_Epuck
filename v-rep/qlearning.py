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

    return pi,Q




