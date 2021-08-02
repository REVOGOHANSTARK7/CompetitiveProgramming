# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).

def longestdigitrun(n):
  n=abs(n)
  s=str(n)
  max=0
  prev=0
  count=1
  for i in range(len(s)-1):
    if(s[i]==s[i+1]):
      count+=1
      if(count==prev  and  len(s)-2==i):
        if(max>int(s[i])):
          max=int(s[i])
    else:
      if(count==prev):
        if(max>int(s[i])):
          max=int(s[i])
          prev=count
          count=1
      if(max<int(s[i]) and count>prev):
        max=int(s[i])
        prev=count
      count=1
  return max
        
#   print(max)
# longestdigitrun(1177737888832)
      