# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#! the approach here is to take both link list nodes, add them, and create a new linked list node in one pass

# example solution: Input: l1 = [2,4,3], l2 = [5,6,4]
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # create an empty LL pointer and assign a next variable that points to the start
        linkedListOut = ListNode()
        nextNode = linkedListOut
        numberToCarry = 0 # this is the number to carry during addition of the nodes    
        
        while any([l1,l2,numberToCarry]): # this any() is a boolean check for any of these variable being True
            # parse out the variables from the two given linked lists 
            l1Value = (l1.val if l1 else 0)
            l2Value = (l2.val if l2 else 0)
            numberToCarry, numberOut = divmod(l1Value + l2Value + numberToCarry,10) # this divmod() method will take two numbers and give you the floor division as the first return, and the modulo as another 
            
            nextNode.next = ListNode(numberOut) # sets the next chain in the nextNode as the number out
            nextNode = nextNode.next # moves one down the chain to conitue the operation
            
            # continue moving down both LLs or set them as None to stop the while lop
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return linkedListOut.next