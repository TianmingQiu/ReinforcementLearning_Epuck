#!usr/bin/python
# -*- coding: utf-8 -*-

import vrep
import ePuckVRep

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
        
    speedl = 300.0
    speedr = 300.0
    epuck.set_motors_speed (speedl, speedr)
    epuck.step()
    k = 1
    while True :

        k = k +1
        epuck._sensors_to_read = ['n','m']
        #a=epuck.get_proximity()
        b = epuck.get_floor_sensors()

        #Stop
        if (b[0]>500 and b[0]<1000) or (b[1]>500 and b[1]<1000) or (b[2]>500 and b[2]<1000) :
            epuck.set_motors_speed(0, 0)
            epuck.step()
            
		#Go straight
        if (b[0]>1000 and b[2]>1000) or (b[0]<500 and b[2]<500) :
            epuck.set_motors_speed(speedl, speedr)
            epuck.step()
            
		#Turn right
        elif ( b[0]>1000 and b[2]<500 ) :
			epuck.set_motors_speed(0.5*speedl, 0.1*speedr)
			epuck.step()
            
		#Turn left
        elif b[0]<500 and b[2]>1000 :
			epuck.set_motors_speed(0.1*speedl, 0.5*speedr)
			epuck.step()
		
        else :
            print "Here is an error!"
		
        #Print the sensor value
        if k%2000 == 0:
			#print a
			x1 = int(b[0])
			x2 = int(b[1])
			x3 = int(b[2])
			print x1, x2, x3


        