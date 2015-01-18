import serial
import time
import random

from sound import soundManager

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "/dev/ttyUSB0"
ser.open()

soundman = soundManager()

pir_spot = False
pir_room = False

pir_spot_time = 0
pir_room_time = 0

while(42):
	
	line = ser.readline()
	print line,
	if(line.startswith("/o/b/")):
		slot = int(line[5])

		soundman.playRandom("./sounds/buy/", False)	
	
	if(line.startswith("/o/d/1")): #door open
		soundman.playRandom("./sounds/door_open/", False)	
		
		
	if(line.startswith("/o/d/0")): #door closed
		soundman.playRandom("./sounds/door_closed/", False)	
		
	
	if(line.startswith("/o/p/0/")): #PIR spot
		motion = (line[7] == '1')
		if(motion):
			delta = time.time() - pir_spot_time
			pir_spot_time = time.time()
			if(delta > 10):
				soundman.playRandom("./sounds/welcome/", False)	

		pir_spot = motion	

	if(line.startswith("/o/p/1/")): #PIR room
		motion = (line[7] == '1')
		if(motion):
			delta = time.time() - pir_room_time
			pir_room_time = time.time()
			print delta
			if(delta > 20 and random.randint(0,4) == 0):
				soundman.playRandom("./sounds/random/", False)	
		pir_room = motion	
		
