import math
import random
sdec = input ("Enter a small decimal: ")
ldec = input ("Enter a large decimal: ")
radius = (random.uniform(float(sdec), float(ldec)))
volume = (4/3*math.pi*(radius)**3)
print ("The volume of a sphere with a radius of " + (str(radius)) + " is " + (str(volume)))