"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
"""

#Approach 1: Single Pass
# Time: O(n)
# Space: O(1)
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head
        
        # dummy node added before head
        dummy = ListNode(0, head)
        
        #Phase1: Reach node at position "left"
        leftPrev = dummy #leftPrev: the node right before left
        cur = head

        # iterate [left-1] times for cur to reach left
        for i in range(left-1):
            leftPrev, cur = cur, cur.next

        #Now cur="left", leftPrev="node before left"
        #Phase2: Reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tempNext = cur.next #use the temp var to record&re-assign cur.next
            cur.next = prev
            prev, cur = cur, tempNext
        
        #Phase3: Link the reversed sublist back into the LL
        leftPrev.next.next 


        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
    


#Approach 2: Stack
# Time: O(n)
# Space: O(n) ->bc of the stack