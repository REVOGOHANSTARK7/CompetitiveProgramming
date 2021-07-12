# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
  emp=[]
  for i in range(3):
    emp.append(hand//10**(3-i-1))
    hand=hand%10**(3-i-1)
  return tuple(emp)
  # for i in range(len(str(hand))):
  #   emp.append(hand//10**(len(str(hand))-1))
  #   hand=hand%10**(len(str(hand))-1)
  # return tuple(emp)
    
    
    
    
