# -*- coding: utf-8 -*-

import vrep
import ePuckVRep
import time
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
        
    speedl = 100.0
    speedr = 100.0
    k = 1
    while True :
        epuck.set_motors_speed (500,500)
        epuck.step ()
        time.sleep( 1 )
        epuck.set_motors_speed (-500,-500)
        epuck.step ()
        time.sleep( 1 )
        epuck.set_motors_speed (500,0)
        epuck.step ()
        time.sleep( 2 )
        epuck.set_motors_speed (0,0)
        epuck.step ()
        time.sleep( 3 )

    #epuck._sensors_to_read = ['n','m']
    #a=epuck.get_proximity()
    #b = epuck.get_floor_sensors()
    
    
    
    
    #print a
    #print b
        
            
 
        