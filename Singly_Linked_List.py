# 1) Define a class Node to describe a node of Singly Linked List.
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
# 2) Define a class SLL to implement Singly Linked List with __init__() method to create and initialize start reference variable.
class SLL:
    def __init__(self, head=None):
        self.head = head
        
# 3) Define a method is_empty() to check if the Linked List is empty in SLL class. 
    def is_empty(self):
        return self.head == None
    
 # 4) in a class SLL, define a method insert_at_front() to insert an element at the starting of list.

    def insert_at_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
# 5) in a class SLL, define a method insert_at_end() to insert an element at the end of list.            
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = new_node
            
# 4) in a class SLL, define a method search() to find the node with specified item.           
    def search(self, value):
        temp = self.head
        while temp != None:
            if temp.data == value:
                return temp
            else:
                temp = temp.next
        return None 
    
# 7) in a class SLL, define a method insert_after() to insert a new node after a given node.   
    def insert_after(self, prev, data):
        if prev!=None:
            new_node = Node(data,prev.next)
            prev.next=new_node
            
# 9) in a class SLL, define a method delete_first() to delete first element from the list.       
    def delete_first(self):
        if self.is_empty():
            print("List is empty")
        else:
            self.head =self.head.next
# 10) in a class SLL, define a method delete_last() to delete last element from the list.                 
    def delete_last(self):
        if self.is_empty():
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None  
# 9) in a class SLL, define a method delete_item() to delete specific element from the list.                 
    def delete_item(self, data):
        if self.is_empty():
            print("List is empty")
        elif self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next is not None and temp.next.data != data:
                temp = temp.next
            if temp.next is None:
                print("Item not found")
            else:
                temp.next = temp.next.next                

# 8) in a class SLL, define a method to print all elements of the list.             
        
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp=temp.next
        print("None") 
       
       
list = SLL()
list.insert_at_front(10)
list.insert_at_front(20)
list.insert_at_front(30)
list.insert_at_front(40)
list.insert_at_end(80)
list.insert_at_end(90)
list.insert_after(list.search(20),25)
list.display()
list.delete_first()
list.delete_last()
list.delete_item(10)
list.display()
       
        
                   