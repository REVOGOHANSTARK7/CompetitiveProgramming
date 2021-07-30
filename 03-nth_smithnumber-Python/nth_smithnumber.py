# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

import math

# def dgtsm(k):
#     l=0
#     while(k>0):
#         l+=(k%10)
#         k//=10
#     return l

# def isprime(n):
#     if(n==2):
#         return True
#     elif(n%2==0 or n<2):
#         return False
#     for i in range(3,int(math.sqrt(n))+1,2):
#         if(n%i==0):
#             return False
#     return True
    

# def primefactors(n):
#     sum=0
#     a=n
#     while(n%2==0):
#         sum=sum+2
#         n/=2
#     for i in range(3,int(math.sqrt(n))+1,2):
#         while(n%i==0 and isprime(i)):
#             c=dgtsm(i)
#             sum=sum+c
#             n=n/i
#     if(n!=a and n!=1):
#         while(n>0):
#             sum=sum+(n%10)
#             n//=10
#     return sum

# def digitsum(y):
#     sum=0
#     while(y//10!=0):
#         t=y
#         while(t>0):
#             sum+=(t%10)
#             t//=10
#         y=sum
#         sum=0
#     return y
        
# def smithy(s):
#     sum1=dgtsm(s)
#     temp=primefactors(s)
#     sum2=dgtsm(temp)
#     if(sum2==sum1):
#         return True
#     else:
#         return False
                
# def fun_nth_smithnumber(n):
#     found=-1
#     got=0
#     while(found<=n):
#         got+=1
#         if(smithy(got)):
#             found+=1
#     return got

def SumOfDigits(n):
    return n if n<10 else n%10+SumOfDigits(n//10)

def isSmith(n):
    Digits=SumOfDigits(n)
    Factors,i=0,2
    while i*i<=n:
        if n%i:i+=1
        else:
            n//=i
            Factors+=SumOfDigits(i)
    return Digits==Factors+SumOfDigits(n)

def fun_nth_smithnumber(n):
    found=-1
    got=0
    while(found<=n):
        got+=1
        if(isSmith(got)):
            found+=1
    return got

print(fun_nth_smithnumber(0))
print(fun_nth_smithnumber(1))
print(fun_nth_smithnumber(2))
print(fun_nth_smithnumber(3))
print(fun_nth_smithnumber(4))
print(fun_nth_smithnumber(5))
print(fun_nth_smithnumber(6))
print(fun_nth_smithnumber(7))
print(fun_nth_smithnumber(8))
print(fun_nth_smithnumber(9))
print(fun_nth_smithnumber(10))
print(fun_nth_smithnumber(11))
print(fun_nth_smithnumber(12))