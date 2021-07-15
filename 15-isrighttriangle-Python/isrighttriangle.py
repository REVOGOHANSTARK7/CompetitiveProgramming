# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math

def distance(x1,y1,x2,y2):
  res=math.sqrt((x2-x1)**2+(y2-y1)**2)
  return res

def isrighttriangle(x1, y1, x2, y2, x3, y3):
  side1=distance(x1,y1,x2,y2)
  side2=distance(x2,y2,x3,y3)
  side3=distance(x3,y3,x1,y1)
  
  if(math.isclose(side1**2+side2**2,side3**2)):
    return True
  elif(math.isclose(side2**2+side3**2,side1**2)):
    return True
  elif(math.isclose(side3**2+side1**2,side2**2)):
    return True
  else:
    return False
  
  
