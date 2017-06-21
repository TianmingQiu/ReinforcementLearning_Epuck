# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 12:32:53 2017

@author: Lingfeng
"""

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



