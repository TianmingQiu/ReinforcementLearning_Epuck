# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 13:09:40 2017

@author: Ming
"""

#!usr/bin/python
# -*- coding: utf-8 -*-

import vrep
import ePuckVRep
import time

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
    print s
    epuck.set_motors_speed(-1000, 1000)
    epuck.step()
    time.sleep(1.3)
    
    epuck.set_motors_speed(1000, 1000)
    epuck.step()
    time.sleep(1.5)
    epuck.set_motors_speed(0,0)
    epuck.step()
    time.sleep(0.1)
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
    time.sleep(0.1)
    speedl = 600
    speedr = 600 
    epuck.set_motors_speed(speedl, speedr)
    epuck.step()
    time.sleep(0.75)
    epuck.set_motors_speed(0, 0)
    epuck.step()
    #time.sleep(0.1)
    return digit
    
    
     
    
   
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
        
    speedl = 1000.0
    speedr = 1000.0
    epuck.set_motors_speed (speedl, speedr)
    epuck.step()
    k = 1
    



        
    while True :

        k = k +1
        epuck._sensors_to_read = ['n','m']
        #a=epuck.get_proximity()
        b = epuck.get_floor_sensors()

       
            
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
            
         #Stop
        #if (b[0] > 1000 and b[1] > 1000 and b[2] > 1000):
        elif (b[0]>500 and b[0]<1000 ) or (b[1]>500 and b[1]<1000 ) or (b[2]>500 and b[2]<1000 ) :
            epuck.set_motors_speed(0, 0)
            epuck.step()
            #time.sleep(3)
            break
		
        else :
            print "Here is an error!"
		
        #Print the sensor value
        if k%2000 == 0:
			#print a
			x1 = int(b[0])
			x2 = int(b[1])
			x3 = int(b[2])
			print x1, x2, x3
            
s = read_state()
print s
            
        


        