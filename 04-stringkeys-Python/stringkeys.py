"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        temp=self.calculate_hash_value(string)
        # if(self.table[temp]!=None):
        #     while(self.table[temp]!=None):
        #         temp=temp+1
        #     self.table[temp]=string
        # else:
        self.table[temp]=string
                
        """Input a string that's stored in 
        the table."""
        
        # print (HashValue)
        # Your code goes here
        
        
    def lookup(self, string):
        if string in self.table:
            return self.table.index(string)
        else:
            return -1        
        """Return the hash value if the\
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        pass

    def calculate_hash_value(self, string):
        HashValue=ord(string[0])*100 + ord(string[1])
        return HashValue
        """Helper function to calulate a
        hash value from a string."""
        
        
# ht=HashTable()
# print(ht.store("he"))
        


