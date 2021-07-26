# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def wrapper(n,i=0,null=0):
  if(n==0):
    return null
  temp=n%10
  if(temp%2==0):
    null+=(10**i*temp)
    i+=1
  return wrapper(n//10,i,null)

def fun_recursion_onlyevendigits(l):
  empty=[]
  if(len(l)==0):
    return empty
  else:
    even=wrapper(l[0])
    empty.append(even)
    return empty+fun_recursion_onlyevendigits(l[1:])
  
  



  
  

