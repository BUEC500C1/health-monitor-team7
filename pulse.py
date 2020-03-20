from random import gauss
from globals import pulse_flag, pulse_value

# Normal pulse rate of an average adult (non athlete): 60-100 beats per minute
def read_pulse:
	# Gives a value outside range [60,100] approx. 7% of the time
	pulse = gauss(80, 11)
	
	if pulse < 60 or pulse > 100:
		# Set flag to True when pulse is not normal
		pulse_flag = True
		pulse_value = pulse
	elif (flag == True):
		# Set flag to False when pulse is back to normal
		pulse_flag = False

	return pulse