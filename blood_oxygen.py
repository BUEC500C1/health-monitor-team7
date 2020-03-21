import random

def read_blood_oxygen():
    # a triangular distribution was chosen to specify the maximum and minimum limits
    # while maintaining a distribution more realistic than a uniform distribution
    return random.triangular(0.90, 1.00, 0.99)