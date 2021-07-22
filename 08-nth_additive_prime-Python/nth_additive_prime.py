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

# import math

# def sums(n):
#   n=abs(n)
#   tot=0
#   while(n>0):
#     tot+=(n%10)
#     n//=10
#   return tot

# def prime(n):
#   if(n==2):
#     return True
#   elif(n<2 or n%2==0):
#     return False
  
#   fac=round(math.sqrt(n))
#   for i in range(3,fac+1,2):
#     if(n%i==0):
#       return False
#   return True

# def isAdditivePrime(n):
#   if(prime(n) and prime(sums(n))):
#     return True
#   else:
#     return False
  

# assert (isAdditivePrime(3) == True)
# assert (isAdditivePrime(5) == True)
# assert (isAdditivePrime(13) == False)
# assert (isAdditivePrime(23) == True)
# assert (isAdditivePrime(29) == True)
# assert (isAdditivePrime(41) == True)
# assert (isAdditivePrime(98) == False)
# assert (isAdditivePrime(198) == False)
# assert (isAdditivePrime(290) == False)
# assert (isAdditivePrime(67) == True)
# assert (isAdditivePrime(97) == False)
# print("All test cases passed... :-)")
