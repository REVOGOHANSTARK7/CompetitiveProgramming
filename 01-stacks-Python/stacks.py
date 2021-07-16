"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        new_element.next=self.head
        self.head=new_element

    def delete_first(self):
        if(self.head):
            delt=self.head
            new=delt.next
            self.head=new
            return delt
        else:
            return None
        
    def search(self,element):
        # if(self.head==element):
        #     return True
        # elif(self.next==element):
        #     return True
        current=self.head
        while(current!=None):
            if(current==element):
                return True
            current=current.next
        return False
    
ll = LinkedList()  
ll.insert_first(3)
ll.insert_first(1)
ll.insert_first(5) 
assert(ll.search(3)==True)
        
        

class stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)
        

    def pop(self):
        return self.ll.delete_first()
    