# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

# https://github.com/vprusso/youtube_tutorials/blob/master/data_structures/trees/binary_trees/binary_tree.py

def median(a):
  low=0
  mid=len(a)//2
  if(len(a)==0):
    return None
  elif((len(a)%2)!=0):
    return a[(low+(len(a)-1))//2]
  else:
    return (a[mid]+a[~mid])/2
  