import random
import globals

def read_blood_oxygen():
    # a triangular distribution was chosen to specify the maximum and minimum limits
    # while maintaining a distribution more realistic than a uniform distribution
    oxygen = random.triangular(0.90, 1.00, 0.99)

    # a blood oxygen value below 0.93 is considered unhealthy
    if oxygen < 0.93:
        globals.oxygen_flag = True
        globals.oxygen_value = oxygen
    else:
        globals.oxygen_flag = False

    return str(oxygen)
