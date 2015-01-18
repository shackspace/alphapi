import RPIO

class light:

	def __init__(self):
		RPIO.setup(27, RPIO.OUT)
		RPIO.setup(17, RPIO.OUT)
		RPIO.setup(22, RPIO.OUT)
		self.mapping = [17,27,22]
		
	def set(self, light, state):
		RPIO.output(self.mapping[light], state)
		#print "light ", light, state
