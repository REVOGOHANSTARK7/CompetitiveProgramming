# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.
def isprime(n):
  if(n==2):
    return True
  elif(n%2==0 or n<2):
    return False
  else:
    for i in range(3,n//2,2):
      if(n%i==0):
        return False
  return True
      

def fun_hasnoprimes(l):
  for i in range(len(l)):
    for j in range(len(l[i])):
      if(isprime(l[i][j])==True):
        return False
  return True
  
        

