|Data Structure|Common Algorithms
| :---- | --- |
|Array|Search, Sort, Insert, Update, Delete|
|Stack|Push, Pop, Peek/Top|
|Queue|Enqueue, Dequeue, Front, Rear|
|Tree|Pre-order, In-order, Post-order Traversal|
|Graph|Breadth-First Search, Depth-First Search, Dijkstra|

<aside>
💡 General Approach:

Build the DS step by step. Start with the core constructors, then keep adding methods in order of complexity so that the simpler methods can be reused within more complex ones 

Determine which/how many temp variables to create

</aside>

When to use which DS:
The reason that you use one data structure over another is almost always about Big O.
- Array:
    - Good: Indexing
    - Bad: Searching, insertion, delete (except at the end)
- LL:
    - Good: Insertion, Deletion
    - Bad: Indexing, Searching
- Hashtable:
    - Good: Search, index, delete
    - Bad: 


Algorithm Patterns
Maximum Continuous Subarray

- Sliding Window: O(n)

Input Array is Sorted

- Binary Search: O(log n)
- Two Pointers: O(n)

Input is a Binary Tree

- DFS (Preorder, Inorder, Postorder): O(n)
- BFS (Level Order): O(n)

Input is a Binary Search Tree

- Left < Cur < Right: O(log n)
- Inorder Traversal visits the nodes in ascending (sorted) order: O(n)

Input is a Matrix/Graph

- DFS (Recursion, Stack): O(n)
- BFS (Queue): O(n)

Find the Shortest/Nearest Path/Distance in a Tree/Matrix/Graph

- BFS (non-weighted): O(n)
- Dijkstra (weighted): O(E log V)

String Concatenation

- StringBuilder: O(n) (Java, C#, etc.)
- String.join(): O(n) (Python)

Input is a Linked List

- `Dummy Node`
- Two Pointers: O(n)
- Fast & Slow Pointers: O(n)

Recomputing the Same Input

- Memoization

Recursion is Banned

- Stack

Permutations/Combinations/Subsets

- Backtracking

Find the Top/Least Kth element

- QuickSelect: O(n) average, O(n²) worst
- Heap: O(n log k)

Common Strings

- Map
- Trie

Sort

- Quick Sort: O(n log n) average, O(n²) worst
- Merge Sort: O(n log n)
- Built-in sorts: O(n log n)

Find the Smallest/Largest/Median in a Stream

- Two Heaps

Must Solve In-Place

- Swap corresponding values
- Store different values in the same pointer

**Maximum/Minimum Subarray/Subset/Options**

- `Dynamic Programming`

Map/Set

- Time: O(1)
- Space: O(n)

Deque

- Replaces Stack, Queue, and LinkedList