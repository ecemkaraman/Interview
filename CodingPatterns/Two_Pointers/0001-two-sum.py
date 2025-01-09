"""
Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.
You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice. We are guaranteed that an answer exists
You can assume that the given input array is not sorted. You can return the answer in any order.
"""
#https://www.notion.so/Two-Sum-c0505f2776bd413aab9aa29c48699550?pvs=4

from typing import List


#Approach 1: Two pass hash table
#Time:O(n), Space:O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index={} #value:index
        for i, num in enumerate(nums): #enumerate() returns (index, value)
            num_to_index[num] = i #swap the order to (value, index)
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index and num_to_index[complement] != i:
                return [i, num_to_index[complement]]
        return []

#Approach 2: One pass hash table
#Time:O(n), Space:O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index: #Valid Pair Check
                return [num_to_index[complement], i] #Pair Retrieval
            num_to_index[num] = i #Preparing for Future Lookups
        return [] #Handling No Solution -optional since we're guaranteed that answer exists