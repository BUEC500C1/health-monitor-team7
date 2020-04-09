from random import gauss
import globals

# Normal pulse rate of an average adult (non athlete): 60-100 beats per minute
def read_pulse():
	# Gives a value outside range [60,100] approx. 7% of the time
	pulse = round(gauss(80, 11))

	if pulse < 60 or pulse > 100:
		# Set flag to True when pulse is not normal
		globals.pulse_flag = True
		globals.pulse_value = pulse
	elif (globals.pulse_flag == True):
		# Set flag to False when pulse is back to normal
		globals.pulse_flag = False

	return str(pulse)
