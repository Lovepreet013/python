class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        self.parent = None
    
    #Iterative methods:
    
    def insert2(self, val):
        current = self
        print(self)
        
        parent = None
        
        while current:
            parent = current
            if val < current.val:
                current = current.left_child
            else:
                current = current.right_child
        
        if val < parent.val:
            parent.left_child = Node(val)
        else:
            parent.right_child = Node(val)
        
        return print(f'{val} added')
    
    def search2(self, val):
        current = self
        
        while current is not None:
            if val < current.val:
                current = current.left_child
            elif val > current.val: 
                current = current.right_child
            else:
                return True
        
        return False
            
    #Recursive methods:
    
    def insert(self, val):
        # print(f' self value : {self.val}')
        if val < self.val:
            if self.left_child:
                self.left_child.insert(val)
            else:
                self.left_child = Node(val)
                # return print("left child added", val)
        else:
            if self.right_child:
                self.right_child.insert(val)
            else:
                self.right_child = Node(val)
                # return print("right child added", val)
    
    def search(self, val):
        if val < self.val:
            if self.left_child:
                return self.left_child.search(val)
            else : 
                return False
            
        elif val > self.val:
            if self.right_child:
                return self.right_child.search(val)
            else:
                return False
            
        else:
            return True
        
        return False
    
    
    def delete(self, val):
        # if current node's val is less than that of root node,
        # then only search in left subtree otherwise right subtree
        if val < self.val:
            if self.left_child:
                self.left_child = self.left_child.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return self
        
        elif val > self.val:
            if self.right_child:
                self.right_child = self.right_child.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return self
        
        else:
            # deleting node with no children
            if self.left_child is None and self.right_child is None:
                self = None
                return None
            
            # deleting node with right child
            elif self.left_child is None:
                temp = self.right_child
                self = None
                return temp
            
            #deleting node with left child
            elif self.right_child is None:
                temp = self.right_child
                self = None
                return temp
            
            # deleting node with two children
            current = self.right_child
            
            # loop down to find the leftmost leaf
            while current.left_child is not None:
                current = current.left_child
                
            self.val = current.val
            self.right_child = self.right_child.delete(current.val)
        
        return self
    
    def print(self):
        current = self
        while current is not None:
            print(current.val)
            current = current.right_child

class Binary_Search_Tree:
    def __init__(self, val):
        self.root = Node(val)
    
    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)
            return True

    def search(self, value):
        if self.root:
            return self.root.search(value)
        else:
            return False
    
    def delete(self, val):
        if self.root is not None:
            self.root = self.root.delete(val)

    def print(self):
        if self.root:
            self.root.print()
        

# BST = Binary_Search_Tree(1)
# BST.insert(4)
# BST.insert(3)
# BST.insert(2)

# BST.print()