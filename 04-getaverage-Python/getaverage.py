# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.




def fun_getaverage(s):
  sum=0.0
  count=0
  counte=0
  p=s.split(",")
  for i in range(len(p)):
    if(p[i].isnumeric()):
      sum+=int(p[i])
      count+=1
    else:
      counte+=1
      if(counte==len(p)):
        return 0.0
  l=sum/count
  return l

print(fun_getaverage("13,excused,14,absent"))

