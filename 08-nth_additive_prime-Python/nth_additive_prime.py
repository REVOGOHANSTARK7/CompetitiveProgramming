# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

import math

def sums(n):
  n=abs(n)
  tot=0
  while(n>0):
    tot+=(n%10)
    n//=10
  return tot

def prime(n):
  if(n<2 or n%2==0):
    return False
  elif(n==2):
    return True
  fac=round(math.sqrt(n))
  for i in range(3,fac+1,2):
    if(n%i==0):
      return False
  return True

def additive(n):
  return (prime(n) and prime(sums(n)))

def fun_nth_additive_prime(n):
  found=0
  got=0
  while(found<=n):
    got+=1
    if(additive(got)):
      found+=1
  return got