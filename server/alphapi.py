import serial

from sound import soundManager

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "/dev/ttyUSB0"
ser.open()

soundman = soundManager()


while(42):
	
	
	line = ser.readline()
	
	if(line.startswith("/o/b/")):
		slot = int(line[5])

		soundman.playRandom("./sounds/buy/", False)	
	
	if(line.startswith("/o/d/1")): #door open
		soundman.playRandom("./sounds/door_open/", False)	
		
		
	if(line.startswith("/o/d/0")): #door open
		soundman.playRandom("./sounds/door_closed/", False)	
		
		
		
