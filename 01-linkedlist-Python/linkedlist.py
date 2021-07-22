"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        c=self.head
        if(self.head):
            while(c.next):
                c=c.next
            c.next=new_element
        else:
            self.head=new_element
            
          
    def get_position(self, position):
        current=self.head
        count=1
        if(position<1):
            return None
        while(current and count<=position):
            if(count==position):
                return current
            current=current.next
            count+=1
        return current
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
       
    def insert(self, new_element, position):
        count=1
        current=self.head
        if(position<1):
            return None
        elif(position==1):
            new_element.next=self.head
            self.head=new_element
        else:
            while(current and count<position):
                if(count==position-1):
                    new_element.next=current.next
                    current.next=new_element
                current=current.next
                count+=1
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        current=self.head
        before=None
        while(current.value!=value and current.next):
            before=current
            current=current.next
        if(current.value==value):
            if(before):
                before.next=current.next
            else:
                self.head=current.next            
        
