#!/ usr/bin/ python

import ePuckVRep

if __name__ == '__main__':
    epuck = ePuckVRep.ePuck( host ='127.0.0.1', port =19999 , debug = True )
    
    epuck.connect()
    epuck.set_debug(True)
    epuck.reset()
        
    speedl = 100.0
    speedr = 100.0
        
    while True :
        epuck.set_motors_speed(speedl, speedr)     
        epuck.step ()