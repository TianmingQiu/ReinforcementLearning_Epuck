# -*- coding: utf-8 -*-

import vrep
import ePuckVRep
import time
import numpy as np
import random
from PIL import Image
import pytesseract
import cv2

def east(current_direction):
    speedl = 300
    speedr = 300    
    if current_direction == 0:
        turnspeed = 250
    elif current_direction == 1:
        turnspeed = -250
    elif current_direction == 3:
        turnspeed = 0
    else:
        turnspeed = 500
        

    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 2 )
    epuck.set_motors_speed(0, 0)
    epuck.step()
    print "Epuck is now going east"
    
def south(current_direction):
    speedl = 300
    speedr = 300    
    if current_direction == 2:
        turnspeed = -250
    elif current_direction == 3:
        turnspeed = 250
    elif current_direction == 1:
        turnspeed = 0        
    else:
        turnspeed = 500
        

    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 2 )
    epuck.set_motors_speed(0, 0)
    epuck.step()
    print "Epuck is now going south"

def west(current_direction):
    speedl = 300
    speedr = 300    
    if current_direction == 0:
        turnspeed = -250
    elif current_direction == 1:
        turnspeed = 250
    elif current_direction == 2:
        turnspeed = 0        
    else:
        turnspeed = 500
        

    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 2 )
    epuck.set_motors_speed(0, 0)
    epuck.step()  
    print "Epuck is now going west"

def north(current_direction):
    speedl = 300
    speedr = 300    
    if current_direction == 2:
        turnspeed = 250
    elif current_direction == 3:
        turnspeed = -250
    elif current_direction == 1:
        turnspeed = 0        
    else:
        turnspeed = 500
        

    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 2 )
    epuck.set_motors_speed(0, 0)
    epuck.step()  
    print "Epuck is now going north"

def Act(command, flag):
    speedl = 300
    speedr = 300
    if command == 0:
        north(flag)
    elif command == 1:
        south(flag)
    elif command == 2:
        west(flag)
    else:
        east(flag)
    epuck.set_motors_speed(200, 200)
    print "forward a step in oder to avoid detect same state 2 times"
    epuck.step()
    time.sleep(1)
    epuck.set_motors_speed(0, 0)
    epuck.step()
    while True :
        
        epuck._sensors_to_read = ['m']
        b = epuck.get_floor_sensors()

        

        #Stop
        if (b[0]>500 and b[0]<1000) or (b[1]>500 and b[1]<1000) or (b[2]>500 and b[2]<1000) :
            epuck.set_motors_speed(0, 0)
            epuck.step()
            time.sleep(1)
            print "arrive at a new state"
            epuck.set_motors_speed(speedl, speedr)
            epuck.step()
            time.sleep( 2.2 )
            epuck.set_motors_speed(0,0)
            epuck.step()
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
    
def getImageAndSave():
    # getting the image data of the camera above the scene and saving it
    returnCode, resolution, image = vrep.simxGetVisionSensorImage(clientID, camera_handle, 0, vrep.simx_opmode_oneshot_wait)
    im = np.array(image, dtype=np.uint8)  # converting the image into a suitable format
    im.resize((resolution[0], resolution[1], 3))  # reshaping the array into an image
    mlp.imshow(im, origin='lower')  # showing the current image of the camera
    im = Image.fromarray(im)
    im.save("current_image.png")  # saving the current image

    

  
    
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
    
    #defining the object handle for the robot
    errorCode, ePuck_handle = vrep.simxGetObjectHandle(clientID, 'ePuck', vrep.simx_opmode_oneshot_wait)
    
    #defining the object handle for the camera above the scene
    res, camera_handle = vrep.simxGetObjectHandle(clientID, 'ePuck_camera', vrep.simx_opmode_oneshot_wait)
    returnCode, resolution, image = vrep.simxGetVisionSensorImage(clientID, camera_handle,0, vrep.simx_opmode_streaming)
    print returnCode, resolution, image
    #getImageAndSave()
    epuck.set_camera_parameters('RGB_365', 20, 20, 1)
    epuck._refresh_camera_parameters
    print epuck._cam_width


    