# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.
import math

def fun_distance(x1, y1, x2, y2):
  s=(math.sqrt(((x1-x2)**2)+((y1-y2)**2)))
  return math.floor(s)