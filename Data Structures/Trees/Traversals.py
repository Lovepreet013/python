from Binary_Search_Tree import Binary_Search_Tree

#Pre-Order Traversal : First print root value, then whole left subtree and whole right subtree.
def pre_order_traversal(node):
    if node is not None:
        print(node.val)
        pre_order_traversal(node.left_child)
        pre_order_traversal(node.right_child)


BST = Binary_Search_Tree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)

print("Pre Order Traversal : ")
pre_order_traversal(BST.root)


#Post-Order Traversal : the elements are traversed in “left-right-root” order. We first visit the left child, then the right child, and then finally the root/parent node
def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left_child)
        post_order_traversal(node.right_child)
        print(node.val)

print("Post Order Traversal : ")
post_order_traversal(BST.root)


#In-Order Traversal : In In-order traversal, the elements are traversed in “left-root-right” order so they are traversed in order. In other words, elements are printed in sorted ascending order with this traversal. We first visit the left child, then the root/parent node, and then the right child.
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left_child)
        print(node.val)
        in_order_traversal(node.right_child)

print("In Order Traversal : ")
in_order_traversal(BST.root)