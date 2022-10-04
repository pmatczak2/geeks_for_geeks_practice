# Given the root of a binary tree. Check whether it is a BST or not.
# Note: We are considering that BSTs can not contain duplicate Nodes.
# A BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Example 1:
#
# Input:
#    2
#  /    \
# 1      3
# Output: 1
# Explanation:
# The left subtree of root node contains node
# with key lesser than the root nodes key and
# the right subtree of root node contains node
# with key greater than the root nodes key.
# Hence, the tree is a BST.
int_max = 123456789
int_min = -123456789

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst(node):
    return is_bst_unit(node, int_min, int_max)

def is_bst_unit(node, mini, maxi):
    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return is_bst_unit(node.left, mini, node.data - 1) and is_bst_unit(node.right, maxi, node.data + 1)

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(1)
    root.left.left = Node(2)

    if is_bst(root):
        print("Is BST")
    else:
        print("Is not BST")