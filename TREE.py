class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

# Define BST class
class BST:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self._insert(root.left, data)
        elif data > root.item:
            root.right = self._insert(root.right, data)
        return root
    
    # Deletion
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        
        if key < root.item:
            root.left = self._delete(root.left, key)
        elif key > root.item:
            root.right = self._delete(root.right, key)
        else:
            #  1: No child
            if root.left is None and root.right is None:
                return None
            #  2: One child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            #  3: Two children
            temp = self._find_min(root.right)
            root.item = temp.item
            root.right = self._delete(root.right, temp.item)
        return root
    # Find size of tree
    def size(self,root):
        if root is None:
            return 0
        return 1 + self.size(root.left)+self.size(root.right)
    
    # #  Find minimum value node
    def find_min(self):
        current = self.root
        if current is None:
            return None
        while current.left:
            current = current.left
        return current


    # #  Find maximum value node
    def find_max(self):
        current = self.root
        if current is None:
            return None
        while current.right:
            current = current.right
        return current
   
    
    # Inorder traversal ( L → Root → R)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.item, end=' ')
            self.inorder(root.right)

    # Preorder traversal (Root → L → R)
    def preorder(self, root):
        if root:
            print(root.item, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder traversal (L → R → Root)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.item, end= ' ')
            
            
# Driver Code
bst = BST()

# Inserting nodes one by one
bst.insert(70)
bst.insert(10)
bst.insert(25)
bst.insert(90)
bst.insert(60)
bst.insert(40)
bst.insert(100)
bst.insert(45)

# Deleting a node
bst.delete(25)

# size
print("Size of BST:",bst.size(bst.root))

# Minimum and maximum
print("Min:", bst.find_min().item)
print("Max:", bst.find_max().item)

# Traversal
print("Inorder Traversal:")
bst.inorder(bst.root) 

print("\nPreorder Traversal:")
bst.preorder(bst.root)

print("\nPostorder Traversal:")
bst.postorder(bst.root)


