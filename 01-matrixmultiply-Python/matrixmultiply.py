# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    r1=len(m1)
    c1=len(m1[0])
    r2=len(m2)
    c2=len(m2[0])
    if(r2!=c1):
        return None
    n=[([0]*c2)for i in range(r1)]
    # for i in range(r1):
    #     n=[0]*c2
        
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                n[i][j]+=m1[i][k]*m2[k][j]
    return n
                
        




