# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
  rsum=[]
  for i in a:
    rsum.append(sum(i))
  s=0
  for j in range(len(a)):
    for k in range(len(a)):
      s=s+a[j][k]
    rsum.append(s)
    s=0
  sum2=sum1=0
  for l in range(len(a)):
    sum2=sum2+a[l][l]
    sum1=sum1+a[l][len(a)-1-l]
  rsum.append(sum2)
    
  rsum.append(sum1)
  
#   print(rsum)
    
# ismostlymagicsquare([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12],[4, 15, 14, 1]])
  
  if(len(set(rsum))==1):
    return True
  else:
    return False
  
      
  
    
  
  