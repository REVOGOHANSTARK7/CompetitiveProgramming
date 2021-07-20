# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
  final1=""
  k=len(s1)
  l=len(s2)
  if(k<l):
    for s in range(k):
      final1=final1+s1[s]+s2[s]
    final1=final1+s2[k:]
    return final1

  elif(k==l):
    for s in range(k):
      final1=final1+s1[s]+s2[s]
    return final1
  
  elif(k>l):
    for s in range(l):
      final1=final1+s1[s]+s2[s]
    final1=final1+s1[l:]
    return final1
  
      
	