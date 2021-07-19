# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def fun_nth_happy_prime(n):
  found=0
  got=0
  while(found<=n):
    got+=1
    if(ishappy(got) and isaprime(got)):
      found+=1
  return got

def isaprime(x):
  if(x<2):
    return False
  if(x==2):
    return True
  if(x%2==0):
    return False
  maximfactor=round(x**0.5)
  for k in range(3,maximfactor+1,2):
    if(x%k==0):
      return False
  return True

def sumofsquares(n):
  sumofsquare=0
  while(n):
    sumofsquare=sumofsquare+((n%10)*(n%10))
    n=int(n/10)
  return sumofsquare

def ishappy(n):
  start=n
  stop=n
  while(True):
    start=sumofsquares(start)
    stop=sumofsquares(sumofsquares(stop))
    if(start!=stop):
      continue;
    else:
      break;
  return (start==1)


  