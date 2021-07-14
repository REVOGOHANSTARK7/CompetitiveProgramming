# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def counting(a,b):
  count=0
  while(a):
    if(a%10==b):
      count+=1
    a=a//10
  return count

def mostfrequentdigit(n):
  n=abs(n)
  c=10
  occurrence=1
  if(n<10):
    return n
  for i in range(10,-1,-1):
    temp=counting(n,i)
    if(occurrence<=temp):
      occurrence=temp
      c=i
  return c


      
  