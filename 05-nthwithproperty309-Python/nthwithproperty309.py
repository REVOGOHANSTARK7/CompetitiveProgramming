# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def prop309(k):
  demo='0123456789'
  result=str(k**5)
  for i in demo:
    if i not in result:
      return False
  return True
  
def nthwithproperty309(n):
  found=0
  got=308
  while(found<=n):
    got+=1
    if(prop309(got)):
      found+=1
  return got

print(nthwithproperty309(1))