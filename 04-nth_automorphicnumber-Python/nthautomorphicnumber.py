# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def automorphic(n):
  y=n**2
  while(n>0):
    if(y%10!=n%10):
      return False
    n//=10
    y//=10
  return True
  
def nthautomorphicnumbers(n):
  found=0
  got=0
  while(True):
    if(automorphic(got)):
      found=found+1
    if(found==n):
      break
    got+=1
  return got