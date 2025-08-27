from Binary_Search_Tree import Binary_Search_Tree

#Challenge : Find min value in binary search tree------------------------
#Solution : 
#Time Complexity : O(h) where h is height of binary search tree. In a balanced BST, the height is log n so Time complexity become O(log n)
#Space Complexity : O(1) because constant extra memory is used.
def find_min(root): #Iterative
    if root is None:
        return None
    
    # Start from the root node.
    current = root
    
    while current.left_child:
        current = current.left_child
    
    return current.val

#Time Complexity : O(h) where h is height of binary search tree. In a balanced BST, the height is log n so Time complexity become O(log n)
#Space Complexity : O(h), In a balanced BST, the height is log n so Space complexity become O(log n) due to the recursive call stack.
def find_min_(root): #Recursive
    if root is None:
        return None
    
    if root.left_child is None:
        return root.val
    else:
        return find_min_(root.left_child)



#Challenge : Find kth Maximum Value in Binary Search Tree---------------------------
#Solution : Time Complexity : O(n), where n represents the number of nodes in binary search tree. or may be O(h + k)
#Space Complexity : O(n) because our algo uses space on call stack

def find_kth_max(root, k):
    return kth_largest_rec(root, [k]).val
    
def kth_largest_rec(node, k):
    if not node:
        return None
    
    # Start with the right subtree for kth largest
    right = kth_largest_rec(node.right_child, k)
    
    # If we've found our kth largest element in the right subtree, return it
    if right:
        return right
    
    k[0] -= 1
    
    if k[0] == 0:
        return node
    
    #Continue the left subtree
    return kth_largest_rec(node.left_child, k)    


#Challenge : Find Ancestors of a Given Node in a BST---------------------------
#Solution : 
#Time Complexity is O(n) is the tree is skewed and O(log n) if it is balanced binary search tree
#Space Complexity is O(h) in the worst case scenario with a leaf node targest as it needs to store ancestors up to root node.
def find_ancestors(root, k):
    result = []
    rec_find_ancestors(root, k, result)
    return result

def rec_find_ancestors(root, k, result):
    if root is None:
        return None
    
    elif root.val == k:
        return True
    
    recur_left = rec_find_ancestors(root.left_child, k, result)
    
    if recur_left:
        #If recursive find in either left or right subtree append root value and return true
        result.append(root.val)
        return True
    
    recur_right = rec_find_ancestors(root.right_child, k, result)
    
    if recur_right:
        result.append(root.val)
        return True
    
    return False

#Iteratice approach
#Time Complexity is O(n) is the tree is skewed and O(log n) if it is balanced binary search tree
#Space Complexity is O(h) in the worst case scenario with a leaf node target as it needs to store ancestors up to root node.
def find_ancestors_(root, k):
    if not root:
        return None
    
    ancestors = []
    current = root
    
    while current is not None:
        if k > current.val:
            ancestors.append(current.val)
            current = current.right_child
        
        elif k < current.val:
            ancestors.append(current.val)
            current = current.left_child
        
        else:
            return ancestors[::-1]
    
    return []
    


#Challenge : Find the height of the binary search tree----------------------------
#Solution : Time Complexity : O(n) where n is number of the node in bst
#Space Complexity : O(h) where h is the height of the give tree The space complexity of the solution above is determined by the recursion stack space used during the depth-first traversal of the tree. In the worst case, where we have a completely unbalanced binary search tree, the recursion stack can grow as large as the height of the tree. However, in the average-case and best-case scenarios where we have a balanced tree, the height of the tree is logarithmic in terms of the number of nodes, i.e., O(logn). Therefore, in such cases, the recursion stack would also be logarithmic, leading to a space complexity of O(logn).
def find_height(root):
    if root is None:
        return 0
    
    else:
        max_subtree_height = max(find_height(root.left_child), find_height(root.right_child))
        
        return 1 + max_subtree_height



#Challenge : Find Nodes at k Distance from the Root-----------------
#Solution : 

#Time Complexity : O(n) where n is the number of nodes in the binary tree. In the worst case, when k is the maximum depth of the tree, the solution explores all nodes of the binary tree, resulting in the time complexity of O(n)

#Space Complexity : O(h) where h is the height of the binary tree. At each level of recursion, there is a call stack maintained to keep track of the function calls. Because the depth of the recursion can reach up to the height of the tree in the worst case, the resulting space complexity is O(h)

def find_k_distance_nodes(root, k):
    result = []
    
    find_k(root, k, result) # Recurse the tree for node at k distance
    
    return result

# Helper recursive function to traverse tree and push all the nodes at k distance into result array
def find_k(root, k, result):
    if root is None:
        return None
    
    if k == 0:
        result.append(root.val) # Append the kth node tp
        return
    
    else:
        find_k(root.left_child, k - 1, result)
        find_k(root.right_child, k - 1, result)
        

bst = Binary_Search_Tree(15)

lst = [10,11,9,17,16,18]
for i in lst:
    bst.insert(i)


print(find_k_distance_nodes(bst.root, 2))