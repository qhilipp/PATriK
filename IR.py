import math

def I(a, b):
    return -((a / (a+b) * math.log((a / (a+b)), 2)) + (b / (a+b) * math.log((b / (a+b)), 2)))