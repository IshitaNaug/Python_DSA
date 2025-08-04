# 1) Define a class Node to describe a node of Doubly Linked List.
class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next
        
# 2) Define a class DLL to implement Doubly Linked List with __init__() method to create and initialize start reference variable. 
       
class DLL:
    def __init__(self, head=None):
        self.head = head
        
# 3) Define a method is_empty() to check if the Linked List is empty in DLL class. 
       
    def is_empty(self):
        return self.head==None 
    
       
# 4) in a class DLL, define a method insert_at_start() to insert an element at the starting of list.
        
    def insert_at_start(self, data):
        n = Node(None, data, self.head)
        if not self.is_empty():
            self.head.prev = n
        self.head = n
        
# 5) in a class DLL, define a method insert_at_end() to insert an element at the end of list.
                     
    def insert_at_end(self, data):
        temp = self.head
        if self.head is not None:
            while temp.next is not None:
                temp = temp.next
        n= Node(temp, data, None)
        if temp == None:
            self.head = n
        else:
            temp.next = n
   
# 6) in a class DLL, define a method search() to find the node with specified item.
               
    def search(self, data):
        temp = self.head
        while temp != None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None 
       
# 7) in a class DLL, define a method insert_after() to insert a new node after a given node. 
              
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next != None:
                temp.next.prev = n
            temp.next = n            
                                  
            
   
        
 # 9) in a class DLL, define a method delete_first() to delete first element from the list.        
    def delete_first(self):
        if self.is_empty():
            pass  
        if self.head is not None:
            self.head = self.head.next
            self.head.prev = None
            
# 10) in a class DLL, define a method delete_last() to delete last element from the list. 
       
    def delete_last(self):
        if self.is_empty():
            pass
        elif self.head.next is None:
            self.head = None  
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None 
# 9) in a class SLL, define a method delete_item() to delete specific element from the list.  
    def delete_item(self, data):
        if self.is_empty():
            pass
        else:
            temp = self.head
            while temp.next is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else :
                        self.start = temp.next
                    break           
                temp = temp.next    
                
 # 8) in a class DLL, define a method to print all elements of the list.             
        
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.item, end=" ")
            temp=temp.next
        print("None")        
        
list = DLL()
list.insert_at_end(90)
list.insert_at_end(40)
list.insert_at_start(2)
list.insert_at_end(70)
list.display() 
list.delete_first()
list.delete_last()
list.display() 

           
                                    