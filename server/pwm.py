from RPIO import PWM
import time


class pwm:

	def __init__(self):
		PWM.setup(3)
		PWM.init_channel(5, 3000)
		PWM.init_channel(6, 3000)
		PWM.init_channel(7, 3000)
		self.mapping = {17,27,22}
	
	def set(self, channel, value):
		if(channel < 0 or channel > 2):
			return

		if(value <= 0):
			PWM.clear_channel(channel)
		else:
			if(value > 1000):
				value = 1000
			PWM.add_channel_pulse(channel, self.mapping[channel], 0, value)
		
	

