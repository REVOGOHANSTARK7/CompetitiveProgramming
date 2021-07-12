# dicetoorderedhand(a, b, c) [5pts]
# Write the function dicetoorderedhand(a, b, c) that takes 3 dice and
# returns them in a hand, which is a 3-digit integer. However, even if the
# dice are unordered, the resulting hand must be ordered so that the largest
# die is on the left and smallest die is on the right. For example:
# assert(dicetoorderedhand(1,2,3) == 321)
# assert(dicetoorderedhand(6,5,4) == 654)
# assert(dicetoorderedhand(1,4,2) == 421)
# assert(dicetoorderedhand(6,5,6) == 665)
# assert(dicetoorderedhand(2,2,2) == 222)

def sample(n):
  c=(len(n)-1)
  numb=0
  for i in n:
    numb=numb+(i*(10**c))  # summing the number by multiplying in each iteration
    c=c-1                  # updating the exponential value for further iteration
  return numb

def dicetoorderedhand(a, b, c):
  temp=[a,b,c]
  temp.sort(reverse=True)
  return sample(temp)
  # s=str(temp)
  # print (s)
  

