# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

import math

def isprime(n):
  if(n<2):
    return False
  for i in range(2,n):
    if(n%i==0):
      return False
  return True

def circular(n):
  count=0
  temp=n
  while(temp>0):
    count+=1
    temp//=10
  temp2=n
  while(isprime(temp2)):
    rem=temp2%10
    quo=temp2//10
    temp2=int(((math.pow(10,(count-1)))*rem)+quo)
    if(temp2==n):
      return True
  return False
  
def nthcircularprime(n):
  found=0
  got=0
  while(found<=n):
    got+=1
    if(circular(got)):
      found+=1
  return got

print(nthcircularprime(0))
