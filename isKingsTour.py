# Background:  in Chess, a King can move from any square to
# any adjacent square.  A King’s Tour is a series of legal King
# moves so that every square is visited exactly once. 
# We can represent a Kings Tour in a 2d list where the 
# numbers represent the order the squares are visited, going 
# from 1 to N2.  For example, consider these 2d lists:

#    [ [  3, 2, 1 ],    	[ [  1, 2, 3 ],  	[ [ 3, 2, 1 ],
#  	[  6, 4, 9 ],      	[  7, 4, 8 ],    	[ 6, 4, 0 ],
#  	[  5, 7, 8 ] ]     	[  6, 5, 9 ] ]   	[ 5, 7, 8 ] ]

# The first is a legal Kings Tour but the second is not, 
# because there is no way to legally move from the 7 to the 8, 
# and the third is not, because it contains a 0 which is out
#  of range.  With this in mind, write the function 
# isKingsTour(board) that takes a 2d list of integers, 
# which you may assume is NxN for some N>0, and 
# returns True if it represents a legal Kings Tour 
# and False otherwise.

def pos(l,n):
    l0=[0,0]
    for i in range(len(l)):
        for j in range(len(l[0])):
            if(n==l[i][j]):
                l0[0]=i
                l0[1]=j
    return l0

def isKingsTour(board):
    row=len(board)
    col=len(board[0])
    s=row*col
    for i in range(1,s):
        p1=pos(board,i)
        p2=pos(board,i+1)
        x=abs(p1[0]-p2[0])
        y=abs(p1[1]-p2[1])
        if(x==1 and y==0):
            continue
        elif(x==0 and y==1):
            continue
        
        elif(x==1 and y==1):
            continue
        else:
            return False
    return True


print(isKingsTour([[3,2,1],[6,4,9],[5,7,8]]))

