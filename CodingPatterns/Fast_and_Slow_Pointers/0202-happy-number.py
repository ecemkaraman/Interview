#Easy
"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process **ends in 1** are happy.

Return true if n is a happy number, and false if not.
"""
"""
In-depth explanation: https://www.notion.so/Happy-Number-8f7de1dc707040dba92bdb694d2043f8?pvs=4
"""

#Helper function - used in both approaches
def sumOfSquares(number): 
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

#Approach1: Fast and slow pointers (Floyd's Cycle Detection)
# Time: O(logn)
# Space: O(1)
def isHappy(self, n:int) -> bool:
    slow_runner = n
    fast_runner = sumOfSquares(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = sumOfSquares(slow_runner)
        fast_runner = sumOfSquares(sumOfSquares(fast_runner))
    return fast_runner == 1

#Approach2: Hashset
# Time: O(logn)
# Space: O(n)
def isHappy2(self, n:int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sumOfSquares(n)
 
    return n == 1


#Alternative implementation without built-in divmod()
def sumOfSquares2(self, n:int) -> int:
		output = 0
		while n: 
				digit = n%10
				digit = digit ** 2
				output += digit
				n = n//10
		return output 