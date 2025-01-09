# Linked Lists

## Pros and Cons
### Pros
Insertion and deletion of a node in the list (given its location) is O(1) whereas in arrays the following elements will have to be shifted.

### Cons
Access time is linear because directly accessing elements by its position in the list is not possible (in arrays you can do arr[4] for example). You have to traverse from the start.

- Node= Value + Pointer → it is essentially a dictionary
- LL is essentially a set of nested dictionaries

## Time & Space Complexity 
- Remove the last item: O(n) →tail needs to point to the previous node, but it needs to move in the opposite direction to the LL →we don’t have a ref to the previous node
- End of LL- remove:O(n), add:O(1).  
- Beginning of LL - add&remove: O(1)
- Lookup an item: O(n) → you can’t access a node by index, you need to start from the beginning) 


## Use Cases
- Stack 
- Queue 
- Both stack&queue implementations of LL enqueue from end(tail), dequeue from start(head)


## Edge Cases
- Empty linked list (self.head=None or self.length=0)
- Single node
- Two nodes
- Linked list has cycles. **Tip:** Clarify beforehand with the interviewer whether there can be a cycle in the list. Usually the answer is no and you don't have to handle it in the code

## Common LL Operations to Master

- Counting the number of nodes in the linked list
- [Reversing a linked list in-place](https://github.com/ecemkaraman/leetcode-ek/blob/main/6_in-place-reversal-of-a-linked-list)
- Finding the middle node of the linked list using two pointers (fast/slow)
- Merging two linked lists together

- To delete a given node, set it equal to None: self.head=None & self.tail=None

## Types of linked lists

### **Singly linked list**

A linked list where each node points to the next node and the last node points to `null`.

### **Doubly linked list**

A linked list where each node has two pointers, `next` which points to the next node and `prev`which points to the previous node. The `prev` pointer of the first node and the `next` pointer of the last node point to `null`.

### **Circular linked list**

A singly linked list where the last node points back to the first node. There is a circular doubly linked list variant where the `prev` pointer of the first node points to the last node and the `next`pointer of the last node points to the first node.



## EXTRAS
- Generally 3 scenarios: LL is empty, LL=1 node, LL= multiple nodes
- Possible variables to create: temp, before, after
- When to return what: return T/F, return None/node
- Any method that involves an index (get, insert, remove) starts by excluding the index-out-of-range scenario: if index < 0 or index > self.length: return None
- Order of method declaration: Go from the simplest to most complex and reuse (e.g.append, prepend, get) in more complex methods
- Singly vs Doubly LL:
    - Which methods are very different: pop, get
- To remove a node even in a singly LL, the bond needs to be broken both ways → by setting the adjacent one to None
- Same node constructor for LL&S&Q

<img width="252" alt="image" src="https://github.com/user-attachments/assets/bca9ebfa-9d5f-4a96-965c-6a925227b3e1">







    ## Techniques

### **Sentinel/dummy nodes**

Adding a sentinel/dummy node at the head and/or tail might help to handle many edge cases where operations have to be performed at the head or the tail. The presence of dummy nodes essentially ensures that operations will never be done on the head or the tail, thereby removing a lot of headache in writing conditional checks to dealing with null pointers. Be sure to remember to remove them at the end of the operation.

### **Two pointers**

Two pointer approaches are also common for linked lists. This approach is used for many classic linked list problems.

- Getting the k^th from last node - Have two pointers, where one is k nodes ahead of the other. When the node ahead reaches the end, the other node is k nodes behind
- Detecting cycles - Have two pointers, where one pointer increments twice as much as the other, if the two pointers meet, means that there is a cycle
- Getting the middle node - Have two pointers, where one pointer increments twice as much as the other. When the faster node reaches the end of the list, the slower node will be at the middle

### **Using space**

Many linked list problems can be easily solved by creating a new linked list and adding nodes to the new linked list with the final result. However, this takes up extra space and makes the question much less challenging. The interviewer will usually request that you modify the linked list in-place and solve the problem without additional storage. You can borrow ideas from the [Reverse a Linked List](https://leetcode.com/problems/reverse-linked-list/) problem.

### **Elegant modification operations**

As mentioned earlier, a linked list's non-sequential nature of memory allows for efficient modification of its contents. Unlike arrays where you can only modify the value at a position, for linked lists you can also modify the `next` pointer in addition to the `value`.

Here are some common operations and how they can be achieved easily:

- Truncate a list - Set the `next` pointer to `null` at the last element
- Swapping values of nodes - Just like arrays, just swap the value of the two nodes, there's no need to swap the `next` pointer
- Combining two lists - attach the head of the second list to the tail of the first list

- Like arrays, linked lists are used to represent sequential data. The benefit of linked lists is that insertion and deletion of code from anywhere in the list is O(1), whereas in arrays, the elements have to be shifted. Linked lists problems share similarities with array problems. Think about how you would solve an array problem and apply it to a linked list.

- For deletion in linked lists, you can either modify the node values or change the node pointers. You might need to keep a reference to the previous element.
- For partitioning linked lists, create two separate linked lists and join them back together.


**General Tips:**

- Always draw out a LL diagram and determine different scenarios and edge cases. Then, decide which scenario to code first. Usually the out-of-range index or the condition that returns None/False is coded first.
- In the more complex methods, use the simpler methods instead of rewriting the code


Common Methods
