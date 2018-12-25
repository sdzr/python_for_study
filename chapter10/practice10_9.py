import math
import cmath

def safe_sqrt(x):
    try:
        re=math.sqrt(x)
    except ValueError:
        re=cmath.sqrt(x)
    return re

