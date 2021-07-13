# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
  if(n>0):
    m=True
  else:
    m=False
  count=0
  n=abs(n)
  a=0
  b=0
  while(n>0):
    s=n%10
    if(count!=k):
      b=b+(10**a*s)
    else:
      b=b+(10**a*d)
    n//=10
    count+=1
    a+=1
  if(count==k):
    b=b+(10**a*d)
      
  if(m==True):
    return b
  else:
    return (-b)
      
      

