# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
  n=abs(n)
  count=0
  if(n<=9):
    return False
  while(n>10):
    r1=n%10
    n//=10
    r2=n%10
    if(r1==r2):
      count+=1
  if(count>=1):
    return True
  else:
    return False
    
    