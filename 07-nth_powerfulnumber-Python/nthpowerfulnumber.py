# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math

def nthpowerfulnumber(n):   # n^2
  found=0
  got=0
  while(found<=n):
    got+=1
    if(powerfulprop(got)):
      found=found+1
  return got  

def powerfulprop(x):
  fac=round(math.sqrt(x))
  for squared in range(2,fac+1,1):
      k=0
      while(x%squared==0):
        x//=squared
        k+=1
      if(k==1):
        return False
  return(x==1) 





  