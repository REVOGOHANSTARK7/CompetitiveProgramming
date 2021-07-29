# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def tidyprop(x):
    x=abs(x)
    std=10
    while(x):
        y=x%10
        if(y>std):
            return False
        elif(std>=y):
            std=y
        x=x//10
    return True   

def fun_nth_tidynumber(n):
    found=0
    got=0
    while(found<=n):
        got+=1
        if(tidyprop(got)):
            found+=1
    return got
    