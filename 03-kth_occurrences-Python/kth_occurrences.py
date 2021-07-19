# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
  temp={}
  for i in s:
    if i not in temp.keys():
      j=s.count(i)
      temp[i]=j
  k=list(temp.keys())
  v=list(temp.values())
  m=sorted(temp.values(),reverse=True)[n-1]
  l=v.index(m)
  return (k[l])
  
# fun_kth_occurrences("hello wooorld",1)

# def evaluate(k):
#   initial=1/2
#   sum=0
#   for i in range(k+1):
#     sum+=(initial**i)
#   print(sum)  # n^2
#   # using bitwise operators helper functions from powersum problem reduces complexity to 'nlogn'.
#   # to further reduce it to logn , the direct formula of GP can be printed so as to avoid redundancies.


# evaluate(3)

    
  
    
