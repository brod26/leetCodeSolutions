import math
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

#! approach: recurisve depth first search

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# uses a recursive helper method
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def recursiveHelper(node,left,right):
            if not node: # if the recursion has hit an empty node, or the list is empty
                return True
            if not (node.val < right and node.val > left): # checks that the node value is less than the right child and greater than the left child
                return False
            return(recursiveHelper(node.left, left, node.val) # recurses down into the left most node, checks values on the way up in order
                and recursiveHelper(node.right, node.val, right))
        
        return recursiveHelper(root,float("-inf"), float("inf"))