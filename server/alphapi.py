import serial
import time
import random

from sound import soundManager

from light import light

light = light()

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "/dev/ttyUSB0"
ser.open()

soundman = soundManager()

pir_spot = False
pir_room = False

pir_spot_time = 0
pir_room_time = 0
buy_time = 0
buy_light = False
while(42):
	
	line = ser.readline()
	print line,
	if(line.startswith("/o/b/")):
		slot = int(line[5])
		buy_time = time.time()
		buy_light = False
		soundman.playRandom("./sounds/buy/", False)	
	
	if(line.startswith("/o/d/1")): #door open
		soundman.playRandom("./sounds/door_open/", False)	
		
		
	if(line.startswith("/o/d/0")): #door closed
		soundman.playRandom("./sounds/door_closed/", False)	
		
	
	if(line.startswith("/o/p/0/")): #PIR spot
		motion = (line[7] == '1')
		delta = time.time() - pir_spot_time
		pir_spot_time = time.time()
		if(motion and delta > 10):
			soundman.playRandom("./sounds/welcome/", False)	
		
		if(motion):
			light.set(1,True)
			light.set(0,True)

		pir_spot = motion	

	if(line.startswith("/o/p/1/")): #PIR room
		motion = (line[7] == '1')
		delta = time.time() - pir_room_time
		pir_room_time = time.time()
		if(motion and delta > 20 and random.randint(0,4) == 0):
			soundman.playRandom("./sounds/random/", False)	
		
		if(motion):
			light.set(0,True)
		
		pir_room = motion

	if(time.time() - pir_room_time > 15 and time.time() - pir_spot_time > 5):
		light.set(0, False)	
	
	if(time.time() - pir_spot_time > 5):
		light.set(1, False)
	
	if(line.startswith("d") and time.time() - buy_time < 3):
		buy_light = ~buy_light
		light.set(2, buy_light)
	elif(time.time() - buy_time > 6):
		light.set(2, False)	
	elif(time.time() - buy_time > 3):
		light.set(2, True)	
