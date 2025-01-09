#Easy
"""
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.
"""
"""
Explanation: https://www.notion.so/Linked-List-Cycle-I-7cc290e1539e44639ce2b6e1ee511f11?pvs=4
"""

#Fast and slow pointers
# Time: O(n)
# Space: O(1)
from typing import List, Optional
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None 
				
class Solution:
    def hasCycle(self, head:Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next: #= fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # check for cycle
                return True 

        return False

#Test case works in LC, but not in VSCode bc LC assumes the input is an LL
#but here, I am passing a list. So, I need a helper function to
#convert list->linkedlist
solution=Solution()
result = solution.hasCycle([3,2,0,-4])
print(result)



#Approach 2 (O(n) memory):Use a hashset to keep track of all the visited nodes 
# (as an object because values may be repeated) 
# check if the next node exists in the set