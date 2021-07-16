# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
  l=len(a)
  if(l>0):
    a.sort()
    d=max(a)
    for i in range(l-1):
      if(abs(a[i]-a[i+1])<d):
        d=abs(a[i]-a[i+1])
    return d
  else:
    return -1
    
  