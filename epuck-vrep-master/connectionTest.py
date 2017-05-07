#!/ usr/bin/ python

import vrep

print ("Program started")
vrep . simxFinish ( -1) # just in case , close all opened connection
clientID = vrep . simxStart ('127.0.0.1', 19999 , True , True , 5000 , 5)

if clientID != -1:
	print (" Success !")
else :
	print  ("Connection fail .")
