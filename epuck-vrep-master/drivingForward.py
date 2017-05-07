#!/usr/bin/python

import ePuckVRep

if __name__ == '__main__ ':
    epuck = ePuckVRep.ePuck(host ='localhost', port =19999 , debug = True)
    epuck.connect ()
    
    
    epuck.reset ()
    
    speedl = 100.0
    speedr = 100.0

    while True:
        epuck.set_motors_speed(speedl,speedr)
        epuck.step()
