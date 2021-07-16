# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
  l=abs(digit)
  n=len(str(l))
  if(k>=n):
    return 0
  else:
    number=(l//(10**k))%10
    return number
  
