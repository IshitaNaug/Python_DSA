# To create a SLL

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class SLL:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head == None
    
    def search(self, value):
        temp = self.head
        while temp != None:
            if temp.data == value:
                return temp
            else:
                temp = temp.next
        return None 
    
    #  To traverse a SLL
    
    def traverse(self):
        if self.is_empty():
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
# Insert a node at beginning

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            
 # Insert a node at end

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = new_node
            
# Insert a node at specified position            

    def insert_at_position(self, prev, data):
        if prev!=None:
            new_node = Node(data,prev.next)
            prev.next=new_node
            
# Delete the first node
            
    def delete_first(self):
        if self.is_empty():
            print("List is empty")
        else:
            self.head =self.head.next
            
# Delete the last node
                        
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
            
# Delete the node at specified position
                        
    def delete_at_position(self, data):
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
                
    
                       
#  Example usage
sll = SLL()

# Insertion
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_beginning(5)
sll.insert_at_position(sll.search(20),25)


print("Linked List after insertion:")
sll.traverse()

# Deletion
sll.delete_first()
sll.delete_last()
sll.delete_at_position(25)

print("Linked List after deletions:")
sll.traverse()