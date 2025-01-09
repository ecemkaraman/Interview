# [20] https://leetcode.com/problems/valid-parentheses/
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""
DS: stack[] to keep track of pushed and popped char, 
dict ={closing para : opening para}
Loop through the string char by char. 
If opening bracket, push it onto the stack. 
Stack only contains opening brackets
If closing bracket, check if stack[-1] (top/last item) matches & pop stack[-1]. 
End: Return True if stack empty
Time Complexity: O(n)
Space Complexity: O(n) - worst case, store all the opening brackets in the stack
"""
def isValid(s):
    close_to_open = {')': '(', '}': '{', ']': '['}

    stack = [] #List implementation
    for c in s:
        if c in close_to_open: #loop through keys (closing brackets)
            # if stack not empty & last item in stack=corr. opening bracket
            if stack and stack[-1]==close_to_open[c]:
                stack.pop()
            else:
                return False
        else: #If we get an opening paranthese
            stack.append(c)
    return True if not stack else False #True if stack is empty at the end

print(isValid("[{()}]")) #True
print(isValid("[{(}]")) #False



# [856] https://leetcode.com/problems/score-of-parentheses/
# Given a balanced parentheses string S, compute the score of the string based on the following rule:
#
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

# Find a closed parantheses&check how many it's enclosed by
#Check Notion for explanation
#Time & Space complexity: O(n)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = [0]
        total = 0

        for ch in s:
            if ch == "(":
                stack.append(0)

            else:
                top = stack.pop()
                val = max(1,2*top)
                stack[-1] += val

        return stack.pop()

# [581] https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
# then the whole array will be sorted in ascending order, too.
from typing import List
def findUnsortedSubarray(nums: 'List[int]') -> int:
    stack, n = [], len(nums)
    l, r = n, 0
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            l = min(l, stack.pop())
        stack.append(i)

    stack.clear()

    for i in range(n)[::-1]:
        while stack and nums[stack[-1]] < nums[i]:
            r = max(r, stack.pop())
        stack.append(i)

    return r - l + 1 if r - l > 0 else 0


# [84] https://leetcode.com/problems/largest-rectangle-in-histogram/
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
def largestRectangleArea(heights: 'List[int]') -> 'int':
    s, res, heights = [], 0, [0] + heights + [0]
    for i, height in enumerate(heights):
        if len(s) > 0:
            while height < heights[s[-1]]:
                top = s.pop()
                res = max(res, heights[top] * (i - s[-1] - 1))
        s.append(i)
    return res


# [439] https://leetcode.com/problems/ternary-expression-parser/
# Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression.
# You can always assume that the given expression is valid and only consists of digits 0-9, ?, :, T and F
def parseTernary(expression):
    stack = []
    for c in reversed(expression):
        stack.append(c)
        if stack[-2:-1] == ['?']:
            stack[-5:] = stack[-3 if stack[-1] == 'T' else -5]
    return stack[0]


# [232] https://leetcode.com/problems/implement-queue-using-stacks/
# Implement the following operations of a queue using stacks.
class MyQueue:
    def __init__(self):
        self.push_stack, self.pop_stack = [], []

    def push(self, x: 'int') -> 'None':
        while self.pop_stack:
            self.push_stack.append(self.pop_stack.pop())
        self.push_stack.append(x)

    def pop(self) -> 'int':
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self) -> 'int':
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]

    def empty(self) -> 'bool':
        return len(self.push_stack) + len(self.pop_stack) == 0


# [155] https://leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# store gap between current and min
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = 0

    # store old minimum value when the current minimum value changes after pushing the new value x
    def push(self, x: 'int') -> 'None':
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self) -> 'None':
        if self.stack:
            pop = self.stack.pop()
            if pop < 0:
                self.min = self.min - pop

    def top(self) -> 'int':
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> 'int':
        return self.min


# [716] https://leetcode.com/problems/max-stack/
# Design a max stack that supports push, pop, top, peekMax and popMax.
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: 'int') -> 'None':
        self.stack.append(x)
        if len(self.max_stack) == 0 or x >= self.max_stack[-1][0]:
            self.max_stack.append((x, len(self.stack) - 1))

    def pop(self) -> 'int':
        if self.max_stack[-1][1] == len(self.stack) - 1:
            self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> 'int':
        return self.stack[-1]

    def peekMax(self) -> 'int':
        return self.max_stack[-1][0]

    def popMax(self) -> 'int':
        val, pos = self.max_stack.pop()
        del self.stack[pos]
        # traverse the number after maximum, find new max sequence and add to max_stack
        for i in range(pos, len(self.stack)):
            x = self.stack[i]
            if len(self.max_stack) == 0 or x >= self.max_stack[-1][0]:
                self.max_stack.append((x, i))
        return val