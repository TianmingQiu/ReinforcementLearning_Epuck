# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 12:32:53 2017

@author: Lingfeng
"""

import numpy as np


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
pi = [3, 3, 0, 1, 3, 1, 1, 1, 3, 1, 0]


######################################################################################################


def run (transition_matrix,start_state,goal_state,start_orientation):

    current_state = start_state
    current_orientation = start_orientation
    
    while current_state != goal_state:
        action = pi[current_state]
        Done = False
    
        while not Done:
            print("老子是坑") ### 此处应有执行函数
            Done = True
        
        current_state = int(transition_matrix[current_state][action])



run (transition_matrix,start_state,goal_state,start_orientation)