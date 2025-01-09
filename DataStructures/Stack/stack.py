# stack common operation: push, pop, top
# stack is used in pairs, maintain extreme value
#
# FILO: First In, Last Out
# Time:  O(1)
# Space: O(n)

"""
4 implementations:
    -From scratch: Using List or LinkedList
    -Using libraries: collections.deque, queue.Queue
"""

"""---IMPLEMENTATIONS FROM SCRATCH---"""
#Implementation1: Using a list
#Insert&delete from end of list -> O(1)

def stack_operations():
    stack = []
    size = len(stack)
    stack.append(1) # enqueue to the end of list
    stack.pop() #dequeue from end of list - if len(stack) != 0
    stack.isEmpty()
    stack.top() #returns topmost, most recent element



# Implementation2: Using LL
# Enqueue & dequeue from the beginning of LL: both O(1)
# Head=top, Tail=bottom -> No need to keep track of bottom/tail

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackUsingLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp.value = temp.value.next
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height +=1

    def pop(self):
        if self.height==0:
            raise IndexError("Stack is empty")
        else:
            temp = self.top #temp enables us to return the popped node
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp
    
    def peek(self): #peek():return the head w/o popping
        if self.height == 0:
            raise IndexError("Stack is empty")
        else:
            return self.top.value
        

"""---IMPLEMENTATIONS USING LIBRARIES---"""
#Implementation3: Using collections.deque (double-ended queue)
#Mainly used for queue, but works for stack too 
#append() & pop(): both O(1)
from collections import deque

class StackUsingDeque:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)  # O(1) time complexity

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()  # O(1) time complexity

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage:
s = StackUsingDeque()
s.push(1)
s.push(2)
print(s.pop())  # Output: 2


#Implementation4: Using queue.LifoQueue
# UC: Multi-threaded environments 
# put() = enqueue, get() = dequeue 
from queue import LifoQueue

stack = LifoQueue()

# Push (enqueue) operation
stack.put(1)  # O(1) time complexity
stack.put(2)

# Pop (dequeue) operation
print(stack.get())  # Output: 2 (O(1) time complexity)