# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k)  or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.

def power(x, y):
    res=1
    while(y>0):
        if((y & 1) == 1) :
            res=res*x
        y=y>>1
        x=x*x
    return res

def powerSum(n, k):
    sum=0
    if(n<0 or k<0):
        return 0
    else:
        for i in range(1,n+1):
            sum+=power(i,k)
        return sum
        
assert(powerSum(0,0) == 0)
assert(powerSum(2,10) == 1025)
assert(powerSum(10,2) == 385)
assert(powerSum(3,10) == 60074)
print ("All test cases passed...")
