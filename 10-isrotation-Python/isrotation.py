# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

# def rotate(x):
#   leng=len(str(x))
#   r=x%10
#   q=x//10
#   x=10**(leng-1)*r+q
  
  
def isrotation(x, y):
  temp=x
  leng=len(str(x))
  if(x==y):
    return True
  s=list(str(x))
  l=list(str(y))
  # print(s[-1::-1])
  # print(l)
  if(s[-1::-1]==l):
    return True
  for i in range(leng+1):
    r=x%10
    q=x//10
    x=10**(leng-1)*r+q
    # x=rotate(x)
    if(x==y):
      return True
  return False

    
    
  