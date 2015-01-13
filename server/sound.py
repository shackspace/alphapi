
import os
import subprocess
import random


class soundManager:

	def __init__(self):
		
		self.process = None

	
	def isplaying(self):
		if(self.process == None):
			return False	
		if(self.process.poll() == None):
			return True
		else:
			return False
	
	def stop(self):
		
		if(self.isplaying()):
			self.process.kill()
			self.process.wait()
	

	def play(self, sound, override):
		if(~override and self.isplaying()):
			return
		
		if(override and self.isplaying()):
			self.stop()	
		
		print "playing sound " + sound
		self.process = subprocess.Popen(["mplayer", sound])
		

	def playRandom(self, dir, override):

 
		soundfiles = os.listdir(dir)
		id = random.randint(0,len(soundfiles)-1)
		sound = dir + soundfiles[id]
		self.play(sound, override)	
