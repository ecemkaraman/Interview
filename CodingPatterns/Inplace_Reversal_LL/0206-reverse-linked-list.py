# Easy
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
Notion: https://www.notion.so/Reverse-a-Linked-List-4799e8e5401440f3913095c9fe180abb?pvs=4
"""
# Time: O(n)
# Space: O(1)

from typing import Optional
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    def reverseLL(self, head:Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
    
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node 
        head = prev
        return prev
