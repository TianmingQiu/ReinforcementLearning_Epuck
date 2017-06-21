def east(current_direction):
    if current_direction == 0:
        turnspeed = 250
    elif current_direction == 1:
        turnspeed = -250
    else:
        turnspeed = 500
        
    epuck.set_motors_speed(speedl, speedr)
    epuck.step()
    time.sleep( 2 )
    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 2 )
    epuck.set_motors_speed(0, 0)
    epuck.step()
    
def south(current_direction):
    if current_direction == 2:
        turnspeed = -250
    elif current_direction == 3:
        turnspeed = 250
    else:
        turnspeed = 500
        
    epuck.set_motors_speed(speedl, speedr)
    epuck.step()
    time.sleep( 2 )
    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 2 )
    epuck.set_motors_speed(0, 0)
    epuck.step()

def west(current_direction):
    if current_direction == 0:
        turnspeed = -250
    elif current_direction == 1:
        turnspeed = 250
    else:
        turnspeed = 500
        
    epuck.set_motors_speed(speedl, speedr)
    epuck.step()
    time.sleep( 2 )
    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 2 )
    epuck.set_motors_speed(0, 0)
    epuck.step()  

def north(current_direction):
    if current_direction == 2:
        turnspeed = 250
    elif current_direction == 3:
        turnspeed = -250
    else:
        turnspeed = 500
        
    epuck.set_motors_speed(speedl, speedr)
    epuck.step()
    time.sleep( 2 )
    epuck.set_motors_speed (turnspeed,-turnspeed)
    epuck.step ()
    time.sleep( 2 )
    epuck.set_motors_speed(0, 0)
    epuck.step()  

def Act(command, flag):
    if command == 0:
        north(flag)
    elif command == 1:
        south(flag)
    elif command == 2:
        west(flag)
    else:
        east(flag)
    while True :
        epuck._sensors_to_read = ['n','m']
        b = epuck.get_floor_sensors()

        #Stop
        if (b[0]>500 and b[0]<1000) or (b[1]>500 and b[1]<1000) or (b[2]>500 and b[2]<1000) :
            epuck.set_motors_speed(0, 0)
            epuck.step()
            time.sleep(3)
            break
            
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
    
    
   