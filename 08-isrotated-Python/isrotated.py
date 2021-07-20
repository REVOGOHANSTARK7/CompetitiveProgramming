# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
  for i in range(len(str1)):
    x=0
    m=str1[x+1:len(str1)]+str1[x]
    if(m==str2):
      return True
    else:
      str1=m
      x+=1
  return False
  