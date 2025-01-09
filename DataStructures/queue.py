# queue common operation: push, pop, top
# queue is widely used in BFS
# FIFO: First In, First Out
#
# Time:  O(1)
# Space: O(n)
"""
4 implementations:
    -From scratch: Using List or LinkedList
    -Using libraries: collections.deque, queue.Queue
"""

"""---IMPLEMENTATIONS FROM SCRATCH---"""
#Implementation1: Using a list, inefficient for large queues
#enqueue: O(1)->from end, dequeue: O(n)->from beginning 
class QueueUsingList:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)  # O(1) time complexity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.pop(0)  # O(n) time complexity due to shifting elements

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage:
q = QueueUsingList()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1

#Implementation 2: Using Linked Lists
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueUsingLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp=self.first
        while temp:
            print(temp.value)
            temp=temp.next
    
    #Optimal: Enqueue from tail, dequeue from head → O(1)
    def enqueue(self, value):
        new_node=Node(value)
        if self.first is None:
            self.first = self.last = new_node
        else:
            self.last.next=new_node
            self.last = new_node
        self.length +=1 #keeping track of length is optional

    def dequeue(self, value):
        if self.length == 0: #alternatively, if self.front is None:
            return None  #alternatively raise IndexError
        temp = self.first #temp:Element to drop 
        if self.length == 1:
            self.first = None
            self.last = None 
        else:
            self.first = self.first.next
            temp.next = None #Drop this element's link to the LL 
        self.length -=1
        return temp
    
q = QueueUsingLinkedList()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1


"""IMPLEMENTATIONS USING LIBRARIES"""
#Implementation3: Using collections.deque ->double-ended queue 
#efficient: enqueue&dequeue: O(1)
# Can be used for single/double-ended queues
from collections import deque

class QueueUsingDeque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)  # O(1) time complexity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.popleft()  # O(1) time complexity

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
# Example usage:
q = QueueUsingDeque()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1

#Implementation w/o class
def queue_operations():
    queue = deque()
    size = len(queue)
    queue.append(1) # Enqueue at the end
    queue.appendleft(1) # double-ended queue: Enqueue at the beginning
    head = queue[0]
    tail = queue[-1]
    queue.popleft() # Dequeue from the beginning
    queue.pop() # double-ended queue: Dequeue from back

    
    
#Implementation 4: Using queue.Queue ->for multi-threaded programming
#More complex than deque 
from queue import Queue

q = Queue(maxsize = 3)

q.qsize() #give the maxsize of the Queue

q.put('a') # Enqueue operation: O(1)
q.get() # Dequeue operation: O(1)

q.full() # Return Boolean for Full Queue
q.empty() # Return Boolean for Empty Queue

