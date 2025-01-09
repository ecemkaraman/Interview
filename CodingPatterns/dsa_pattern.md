##  14 Coding Patterns To Master

## Table of Contents
- <a href="#sliding-window">1. Sliding Window</a>
- <a href="#two-pointers">2. Two Pointers or Iterators</a>
- <a href="#fast-and-slow-pointers">3. Fast and Slow Pointers</a>
- <a href="#merge-intervals">4. Merge Intervals</a>
- <a href="#cyclic-sort">5. Cyclic Sort</a>
- <a href="#in-place-reversal-of-a-linked-list">6. In-place Reversal of a Linked List</a>
- <a href="#tree-bfs">7. Tree Breadth First Search</a>
- <a href="#tree-dfs">8. Tree Depth First Search</a>
- <a href="#two-heaps">9. Two Heaps</a>
- <a href="#subsets">10. Subsets</a>
- <a href="#modified-binary-search">11. Modified Binary Search</a>
- <a href="#top-k-elements">12. Top K Elements</a>
- <a href="#k-way-merge">13. K-way Merge</a>
- <a href="#topological-sort">14. Topological Sort</a>
- <a href="#conclusion">Conclusion</a>


<h1 id="sliding-window" style="color:#f85565;">1. Sliding Window</h1>

**Problem: Maximum Sum Subarray of Size K**

Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

**Example:**
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9 (The subarray [5, 1, 3] has the maximum sum of 9)

*#*Pseudocode:**
1. Initialize `maxSum` to a negative value to handle negative elements.
2. Initialize `windowSum` to 0 to keep track of the sum of the current sliding window.
3. Iterate through the array from index 0 to length - 1:
   - Add the current element to `windowSum`.
   - If the window size is equal to k, update `maxSum` to be the maximum of `maxSum` and `windowSum`.
   - If the window size is greater than k, subtract the element from the left of the window and update `windowSum`.
4. Return `maxSum`.

*#*Python Solution:**
```python
def max_sum_subarray(nums, k):
    max_sum = float('-inf')
    window_sum = 0

    for i in range(len(nums)):
        window_sum += nums[i]

        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[i - k + 1]

    return max_sum
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of elements in the `nums` array. We iterate through the </span>array only once.
**Space Complexity:** O(1), as we use a constant amount of extra space.</span>

## 2. Longest Substring Without Repeating Characters:

**Problem: Longest Substring Without Repeating Characters**

Given a string s, find the length of the longest substring without repeating characters.

**Example:**
Input: s = "abcabcbb"
Output: 3 (The longest substring without repeating characters is "abc")

*#*Pseudocode:**
1. Initialize `maxLength` to 0 to keep track of the maximum length of the substring.
2. Initialize `start` to 0 to mark the start index of the current substring.
3. Create an empty `seen` dictionary to store the most recent index of each character.
4. Iterate through the string using the variable `end`:
   - If the current character is in `seen` and its index is greater than or equal to `start`:
       - Update `start` to be the next index of the current character.
   - Update the `maxLength` to be the maximum of the current `maxLength` and `end - start + 1`.
   - Store the current index of the character in the `seen` dictionary.
5. Return `maxLength`.

*#*Python Solution:**
```python
def longest_substring(s):
    max_length = 0
    start = 0
    seen = {}

    for end in range(len(s)):
        if s[end] in seen and seen[s[end]] >= start:
            start = seen[s[end]] + 1

        max_length = max(max_length, end - start + 1)
        seen[s[end]] = end

    return max_length
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the length of the string `s`. We iterate through the string only once.</span>
**Space Complexity:** O(min(N, M)), where M is the size of the character set (e.g., ASCII or Unicode). In the worst case, the `seen` dictionary can st</span>ore all characters in the character set.

## 2. Two Pointers or Iterators:

## **Problem 1: Two Sum**
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Pseudocode:

1. Initialize a dictionary, **`numToIndex`**, to store the index of each number encountered in the array.
2. Iterate over the array elements, **`num`** and their indices, **`i`**:
    - Calculate the **`complement`** (target - num).
    - If the **`complement`** is already in **`numToIndex`**, return **`[numToIndex[complement], i]`**.
    - Otherwise, store the current **`num`**'s index in **`numToIndex`**.
3. If no pair is found, return **`None`**.

### Questions to Ask:

- Can the input array have duplicate elements?
- Are there guaranteed to be exactly one solution for each input?
- Can the input array be empty?


<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of elements in the **`nums`** array.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(N), where N is the number of elements in the **`nums`** array.</span>

### Python Solution:

```python
def two_sum(nums, target):
    numToIndex = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numToIndex:
            return [numToIndex[complement], i]
        numToIndex[num] = i
    return None
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of elements in the **`nums`** array.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(N), where N is the number of elements in the **`nums`** array.</span>

## **Problem 2: Container With Most Water**
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

### Pseudocode:

1. Initialize two pointers, **`left`** at the beginning and **`right`** at the end of the array.
2. Initialize **`maxArea`** to store the maximum area found so far.
3. Iterate until **`left`** is less than **`right`**:
    - Calculate the **`width`** as **`right - left`**.
    - Calculate the **`height`** as the minimum of the elements at indices **`left`** and **`right`**.
    - Calculate the **`area`** as **`width * height`**.
    - Update **`maxArea`** to the maximum of **`maxArea`** and **`area`**.
    - Move the pointer with the smaller element (the one that contributes less to the area) inward.
4. Return **`maxArea`**.

### Questions to Ask:

- Can the input array have negative integers?
- Can the input array have duplicate elements?
- Can the input array be empty?

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of elements in the **`height`** array.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(1).</span>

### Python Solution:

```python
def max_area(height):
    maxArea = 0
    left = 0
    right = len(height) - 1

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        maxArea = max(maxArea, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxArea
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of elements in the **`height`** array.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(1).</span>

## 3. Fast and Slow Pointers:

## **Problem 1: Linked List Cycle**
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

### Pseudocode:

1. Initialize **`slow`** and **`fast`** pointers, both starting at the head of the linked list.
2. Iterate the pointers as long as **`fast`** and **`fast.next`** are not **`null`**:
    - Move **`slow`** one step forward.
    - Move **`fast`** two steps forward.
    - If **`slow`** and **`fast`** meet at the same node, return **`true`** (cycle found).
3. If the loop exits, return **`false`** (no cycle).

### Questions to Ask:

- Can the linked list have duplicate elements?
- Can the linked list be empty?
- Will the linked list always be singly linked?

### Python Solution:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of nodes in the linked list.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(1).</span>

## **Problem 2: Middle of the Linked List**
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

### Pseudocode:

1. Initialize **`slow`** and **`fast`** pointers, both starting at the head of the linked list.
2. Iterate the pointers as long as **`fast`** and **`fast.next`** are not **`null`**:
    - Move **`slow`** one step forward.
    - Move **`fast`** two steps forward.
    - When **`fast`** reaches the end of the linked list, **`slow`** will be at the middle node.
3. Return the value of the middle node.

### Questions to Ask:

- Can the linked list have duplicate elements?
- Can the linked list be empty?
- Will the linked list always be singly linked?

### Python Solution:

```python
def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of nodes in the linked list.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(1).</span>

## 4. Merge Intervals:

## **Problem 1: Merge Intervals**

### Pseudocode:

1. Sort the intervals based on their start time.
2. Initialize an empty list, **`merged`**, to store the merged intervals.
3. Iterate through the sorted intervals:
    - If the current interval overlaps with the last interval in **`merged`**, merge them by updating the end time of the last interval.
    - Otherwise, add the current interval to **`merged`**.
4. Return the **`merged`** list.

### Questions to Ask:

- Can the intervals have negative start and end times?
- Can the intervals have overlapping ranges?

### Python Solution:

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals[1]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)

    return merged
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N log N), where N is the number of intervals in the array due to sorting.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(N) in the worst case when all intervals are non-overlapping and need to be merged.</span>

## *#f85565*Problem 2: Insert Interval**

### Pseudocode:

1. Initialize an empty list, **`merged`**, to store the merged intervals.
2. Iterate through the intervals:
    - If the current interval ends before the new interval starts, add it to **`merged`**.
    - If the current interval starts after the new interval ends, add the new interval to **`merged`** and update it to the current interval.
    - Otherwise, merge the intervals by updating the start and end times of the new interval to cover both.
3. Return the **`merged`** list.

### Questions to Ask:

- Can the intervals have negative start and end times?
- Can the intervals have overlapping ranges?


### Python Solution:

```python
def insert_interval(intervals, new_interval):
    merged = []
    i = 0

    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    merged.append(new_interval)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of intervals in the **`intervals`** array.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(N) in the worst case when all intervals need to be merged.</span>

## 5. Cyclic Sort:

## **Problem 1: Find the Missing Number**

### Pseudocode:

1. Use the cyclic sort algorithm to place each number in its correct position.
2. Iterate through the sorted array to find the first missing number (the index that does not have the correct number).
3. Return the missing number.

### Questions to Ask:

- Can the input array have negative integers?
- Can the input array have duplicate elements?
- Will there always be exactly one missing number?



### Python Solution:

```python
def find_missing_number(nums):
    n = len(nums)
    for i in range(n):
        while nums[i] < n and nums[i] != nums[nums[i]]:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

    for i in range(n):
        if nums[i] != i:
            return i

    return n
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of elements in the **`nums`** array.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(1).</span>

## **Problem 2: Find All Missing Numbers**

### Pseudocode:

1. Use the cyclic sort algorithm to place each number in its correct position.
2. Iterate through the sorted array to find all missing numbers (the indices that do not have the correct number).
3. Return the list of missing numbers.

### Questions to Ask:

- Can the input array have negative integers?
- Can the input array have duplicate elements?
- Will there be more than one missing number?

### Python Solution:

```python
def find_missing_numbers(nums):
    n = len(nums)
    for i in range(n):
        while nums[i] < n and nums[i] != nums[nums[i]]:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

    missing_numbers = []
    for i in range(n):
        if nums[i] != i:
            missing_numbers.append(i)

    return missing_numbers
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of elements in the **`nums`** array.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(1).</span>

<h1In-Place Reversal of Linked List:
<h1 id="in-place-reversal-of-a-linked-list" style="color:#f85565;">6. In-Place Reversal of Linked List</h1>

## **Problem 1: Reverse Linked List**

### Pseudocode:

1. Initialize **`prev`** as **`null`** to keep track of the previous node.
2. Iterate through the linked list:
    - Save the next node in **`temp`**.
    - Reverse the current node by updating its **`next`** to **`prev`**.
    - Move **`prev`** to the current node.
    - Move to the next node using **`temp`**.
3. Return **`prev`**, which will be the new head of the reversed linked list.

### Questions to Ask:

- Can the linked list be empty?
- Will the linked list always be singly linked?

### Python Solution:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of nodes in the linked list.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(1).</span>

## **Problem 2: Reverse Linked List II**

### Pseudocode:

1. Initialize **`dummy`** as a new node with value -1, pointing to the original head.
2. Initialize **`prev`** to **`dummy`**, **`current`** to **`head`**, and **`reverse_tail`** to **`current`**.
3. Iterate through the linked list until reaching position **`m`**:
    - Move **`prev`** to **`current`**.
    - Move **`current`** to the next node.
4. Continue iterating and reverse the nodes from position **`m`** to **`n`**:
    - Save the next node in **`temp`**.
    - Reverse the current node by updating its **`next`** to **`prev`**.
    - Move **`prev`** to the current node.
    - Move **`current`** to the next node using **`temp`**.
5. Update the pointers to link the reversed section back into the original list.
6. Return **`dummy.next`**, which will be the new head of the linked list.

### Questions to Ask:

- Can the linked list be empty?
- Will **`m`** and **`n`** always be valid indices within the linked list?

### Python Solution:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list_range(head, m, n):
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy

    for _ in range(m - 1):
        prev = prev.next

    current = prev.next
    reverse_tail = current
    prev_next = None

    for _ in range(n - m + 1):
        temp = current.next
        current.next = prev_next
        prev_next = current
        current = temp

    prev.next = prev_next
    reverse_tail.next = current

    return dummy.next
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of nodes in the linked list.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(1).</span>

<h1 id="tree-bfs" style="color:#f85565;">7. Tree BFS</h1>

## **Problem 1: Binary Tree Level Order Traversal**

### Pseudocode:

1. Initialize an empty list, **`result`**, to store the level order traversal.
2. Initialize a queue, **`queue`**, with the root node.
3. While the queue is not empty:
    - Initialize an empty list, **`currentLevel`**, to store the nodes at the current level.
    - Get the size of the queue (**`size`**), which represents the number of nodes at the current level.
    - Iterate **`size`** times to process all nodes at the current level:
        - Dequeue the front node from the queue.
        - Add the node's value to **`currentLevel`**.
        - Enqueue the left and right children of the node if they exist.
    - Add **`currentLevel`** to the **`result`**.
4. Return the **`result`**.

### Questions to Ask:

- Can the tree have duplicate values?
- Can the tree be empty?


### Python Solution:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current_level = []
        size = len(queue)

        for _ in range(size):
            node = queue.pop(0)
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of nodes in the binary tree.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(N) in the worst case when the tree is balanced and each level has N/2 nodes in the queue.</span>

## **Problem 2: Binary Tree Right Side View**

### Pseudocode:

1. Initialize an empty list, **`result`**, to store the right side view nodes.
2. Initialize a queue, **`queue`**, with the root node.
3. While the queue is not empty:
    - Initialize **`currentLevel`** to an empty list.
    - Get the size of the queue (**`size`**), which represents the number of nodes at the current level.
    - Iterate **`size`** times to process all nodes at the current level:
        - Dequeue the front node from the queue.
        - If it is the last node at the current level, add its value to **`currentLevel`**.
        - Enqueue the left and right children of the node if they exist.
    - Add the last node's value from **`currentLevel`** to the **`result`**.
4. Return the **`result`**.

### Questions to Ask:

- Can the tree have duplicate values?
- Can the tree be empty?

### Python Solution:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current_level = []
        size = len(queue)

        for i in range(size):
            node = queue.pop(0)
            if i == size - 1:
                current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level[-1])

    return result
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of nodes in the binary tree.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(N) in the worst case when the tree is a complete binary tree and the queue holds all nodes of the l</span>ast level.

<h1 id="tree-dfs" style="color:#f85565;">8. Tree DFS</h1>

## **Problem 1: Binary Tree Inorder Traversal**

### Pseudocode:

1. Initialize an empty list, **`result`**, to store the inorder traversal.
2. Define a recursive helper function, **`inorderTraversalRecursive`**, that takes the current node as an argument:
    - If the current node is not **`null`**, recursively call the function on the left child.
    - Add the current node's value to **`result`**.
    - If the current node is not **`null`**, recursively call the function on the right child.
3. Call the **`inorderTraversalRecursive`** function with the root node.
4. Return the **`result`**.

### Questions to Ask:

- Can the tree have duplicate values?
- Can the tree be empty?

### Python Solution:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []

    def inorder_traversal_recursive(node):
        if not node:
            return
        inorder_traversal_recursive(node.left)
        result.append(node.val)
        inorder_traversal_recursive(node.right)

    inorder_traversal_recursive(root)
    return result
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of nodes in the binary tree.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(N) for the recursion stack.</span>

## **Problem 2: Binary Tree Maximum Path Sum**

### Pseudocode:

1. Define a recursive helper function, **`maxPathSumRecursive`**, that takes the current node as an argument:
    - If the current node is **`null`**, return 0.
    - Recursively find the maximum path sum for the left and right subtrees using **`maxPathSumRecursive`**.
    - Calculate the local maximum path sum for the current node as the maximum value between:
        - The current node's value.
        - The sum of the current node's value and the maximum path sum from the left subtree (if positive).
        - The sum of the current node's value and the maximum path sum from the right subtree (if positive).
    - Update the **`maxSum`** as the maximum value between the current maximum path sum and the local maximum path sum.
    - Return the local maximum path sum.
2. Initialize **`maxSum`** to a minimum integer value.
3. Call the **`maxPathSumRecursive`** function with the root node.
4. Return **`maxSum`**.

### Questions to Ask:

- Can the tree have negative values?
- Can the tree have duplicate values?
- Can the tree be empty?

### Python Solution:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    max_sum = float("-inf")

    def max_path_sum_recursive(node):
        nonlocal max_sum
        if not node:
            return 0

        left_sum = max(0, max_path_sum_recursive(node.left))
        right_sum = max(0, max_path_sum_recursive(node.right))
        local_sum = node.val + left_sum + right_sum

        max_sum = max(max_sum, local_sum)

        return node.val + max(left_sum, right_sum)

    max_path_sum_recursive(root)
    return max_sum
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N), where N is the number of nodes in the binary tree.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(H), where H is the height of the binary tree for the recursion stack.</span>

<h1 id="two-heaps" style="color:#f85565;">9. Two Heaps</h1>

## **Problem: Find the Median of a Number Stream**

### Pseudocode:

1. Initialize a min heap, **`minHeap`**, to store the larger half of the numbers.



## 10. Subsets:

## **Problem 1: Subsets**

*#*Pseudocode:**

1. Initialize an empty list, **`result`**, to store the subsets.
2. Define a recursive helper function, **`backtrack`**, that takes the current index and the current subset as arguments.
3. Add the current subset to the **`result`**.
4. Iterate from the current index to the end of the **`nums`** array:
    - Include the current element in the subset.
    - Recursively call **`backtrack`** with the next index and the updated subset.
    - Exclude the current element from the subset.
5. Call the **`backtrack`** function with index 0 and an empty subset.
6. Return the **`result`**.

*#*Questions to Ask:**

- Can the **`nums`** array have duplicate elements?
- Can the **`nums`** array be empty?


*#*Python Solution:**

```python
def subsets(nums):
    result = []

    def backtrack(index, current_subset):
        result.append(current_subset[])

        for i in range(index, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    backtrack(0, [])
    return result

```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(2^N), where N is the number of elements in the **`nums`** array, as each element can </span>either be included or excluded in the subsets.
<span/>**Space Complexity:** O(2^N) for the **`result`** list.

## **Problem 2: Subsets II**

*#*Pseudocode:**

1. Initialize an empty list, **`result`**, to store the subsets.
2. Define a recursive helper function, **`backtrack`**, that takes the current index and the current subset as arguments.
3. Add the current subset to the **`result`**.
4. Iterate from the current index to the end of the **`nums`** array:
    - If the current element is the same as the previous element and not the first element:
        - Skip to the next element to avoid duplicate subsets.
    - Include the current element in the subset.
    - Recursively call **`backtrack`** with the next index and the updated subset.
    - Exclude the current element from the subset.
5. Call the **`backtrack`** function with index 0 and an empty subset.
6. Return the **`result`**.

*#*Questions to Ask:**

- Can the **`nums`** array have duplicate elements?
- Can the **`nums`** array be empty?

*#*Python Solution:**

```python
def subsetsWithDup(nums):
    result = []

    def backtrack(index, current_subset):
        result.append(current_subset[])

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    nums.sort()
    backtrack(0, [])
    return result

```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(2^N), where N is the number of elements in the **`nums`** array, as each element can </span>either be included or excluded in the subsets.
<span/>**Space Complexity:** O(2^N) for the **`result`** list.

## 11. Modified Binary Search:

## **Problem 1: Find Minimum in Rotated Sorted Array**

*#*Pseudocode:**

1. Initialize **`left`** to 0 and **`right`** to the last index of the array.
2. While **`left`** is less than **`right`**:
    - Calculate the middle index as **`(left + right) / 2`**.
    - If the middle element is greater than the last element (rightmost element):
        - Update **`left`** to **`mid + 1`**.
    - Otherwise, update **`right`** to **`mid`**.
3. Return the element at index **`left`** as the minimum element.

*#*Python Solution:**

```python
def find_min(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(log N), where N is the number of elements in the array.</span>
**Space Complexity:** O(1).</span>

## **Problem 2: Search in Rotated Sorted Array**

*#*Pseudocode:**

1. Initialize **`left`** to 0 and **`right`** to the last index of the array.
2. While **`left`** is less than or equal to **`right`**:
    - Calculate the middle index as **`(left + right) / 2`**.
    - If the middle element is equal to the target, return its index.
    - If the left half (from **`left`** to **`mid`**) is sorted:
        - If the target is within the left half, update **`right`** to **`mid - 1`**.
        - Otherwise, update **`left`** to **`mid + 1`**.
    - If the right half (from **`mid`** to **`right`**) is sorted:
        - If the target is within the right half, update **`left`** to **`mid + 1`**.
        - Otherwise, update **`right`** to **`mid - 1`**.
3. Return -1, indicating that the target element is not found.

*#*Python Solution:**

```python
def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(log N), where N is the number of elements in the array.</span>
**Space Complexity:** O(1).</span>

<h1 id="top-k-elements" style="color:#f85565;">12. Top K Elements</h1>

## **Problem 1: Kth Largest Element in an Array**

*#*Pseudocode:**

1. Sort the input array in descending order.
2. Return the element at the (k - 1) index, which represents the kth largest element.


*#*Python Solution:**

```python
def find_kth_largest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]

```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N log N), where N is the number of elements in the array due to the sorting step.</span>
**Space Complexity:** O(1) (in-place sorting).</span>

## **Problem 2: Top K Frequent Elements**

*#*Pseudocode:**

1. Create a frequency map to store the count of each element in the input array.
2. Create a list of tuples where each tuple contains the element and its corresponding frequency.
3. Sort the list of tuples based on the frequency in descending order.
4. Return the first k elements from the sorted list.

*#*Python Solution:**

```python
def top_k_frequent(nums, k):
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    sorted_entries = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
    return [entry[0] for entry in sorted_entries[:k]]

```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N log N) for sorting, where N is the number of elements in the array.</span>
**Space Complexity:** O(N) for the frequency map.</span>

<h1 id="k-way-merge" style="color:#f85565;">13. K-way Merge</h1>

## **Problem 1: Merge k Sorted Lists**

*#*Pseudocode:**

1. Create a min heap and insert the first node from each list into the heap.
2. Initialize a dummy head node and a current pointer.
3. While the heap is not empty:
    - Pop the smallest node from the heap.
    - Append the popped node to the current pointer.
    - Move the current pointer to the next node in the merged list.
    - If the popped node has a next node, insert the next node into the heap.
4. Return the next node of the dummy head, which represents the head of the merged list.

*#*Python Solution:**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    import heapq

    heap = []
    for list_node in lists:
        if list_node:
            heapq.heappush(heap, (list_node.val, list_node))

    dummy_head = ListNode()
    current = dummy_head

    while heap:
        val, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))

    return dummy_head.next

```

*#*Python Solution Explanation:**

- We import the **`heapq`** module to use a priority queue as a min heap.
- The **`merge_k_lists`** function takes a list of linked lists **`lists`** as input and returns the head of the merged sorted list.
- We create an empty **`heap`** to store tuples of **`(val, node)`** where **`val`** is the value of the node and **`node`** is the node itself.
- We push the first node from each linked list into the heap with their values as priorities.
- We create a dummy head node and a **`current`** pointer to keep track of the merged list.
- While the heap is not empty:
    - We extract the tuple with the smallest value (the root of the heap).
    - We assign the node from the tuple to the **`current.next`**.
    - If the extracted node has a next node, we push the next node into the heap with its value as priority.
    - We move the **`current`** pointer to the next node in the merged list.
- Finally, we return the head of the merged list (the next node of the dummy head).

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N log k), where N is the total number of nodes across all lists and k is the number of </span>lists. The heap operations (insertion and extraction) take O(log k) time, and we perform them N times.
<span/>**Space Complexity:** O(k), where k is the number of lists. The heap can contain at most k nodes at any time.

## **Problem 2: Merge Intervals**

Given a collection of intervals, merge overlapping intervals.

## Example:

Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]

*#*Pseudocode:**

1. Sort the intervals based on the start time in ascending order.
2. Initialize an empty list **`merged`** to store the merged intervals.
3. Iterate through the sorted intervals:
    - If **`merged`** is empty or the current interval's start is greater than the end of the last interval in **`merged`**, append the current interval to **`merged`**.
    - Otherwise, update the end time of the last interval in **`merged`** if the end time of the current interval is greater.
4. Return the **`merged`** list.

*#*Questions to Ask:**

- Can the input intervals be empty?
- Can the input intervals contain negative values?
- Can the input intervals have duplicate intervals?

*#*Python Solution:**

```python
def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals[1]:
        current_start, current_end = interval
        last_start, last_end = merged[-1]

        if current_start > last_end:
            merged.append(interval)
        else:
            merged[-1] = [last_start, max(current_end, last_end)]

    return merged

```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N log N) for sorting, where N is the number of intervals. The merging process takes O(N) time as we iterate through the sorted intervals only once.</span>
<span style="color:orange; font-weight=800;">Space Complexity -</span><span style="color:#e20421;">O(N) for the **`merged`** list.</span>

<h1 id="topological-sort" style="color:#f85565;">14. Topological Sort</h1>

## **Problem: Course Schedule**

### Pseudocode:

1. Initialize an empty list, **`result`**, to store the topological order of courses.
2. Initialize a dictionary, **`inDegrees`**, to keep track of the indegree (number of incoming edges) for each course.
3. Initialize a queue, **`queue`**, with courses that have an indegree of 0.
4. While the queue is not empty:
    - Dequeue a course from the queue and add it to the **`result`**.
    - Iterate through the prerequisites for the dequeued course:
        - Decrement the indegree of the prerequisite course.
        - If the indegree becomes 0, enqueue the prerequisite course to the queue.
5. Check if the number of courses in the **`result`** is equal to the total number of courses. If not, it means there is a cycle, and we cannot complete all courses.
6. Return the **`result`**.

### Questions to Ask:

- Can there be duplicate courses?
- Can the prerequisites list have duplicate entries?

### Python Solution:

```python
def can_finish(num_courses, prerequisites):
    result = []
    in_degrees = {}
    graph = {}

    for course, prereq in prerequisites:
        if prereq not in graph:
            graph[prereq] = []
        graph[prereq].append(course)

        in_degrees[course] = in_degrees.get(course, 0) + 1
        in_degrees[prereq] = in_degrees.get(prereq, 0)

    queue = []
    for course in in_degrees:
        if in_degrees[course] == 0:
            queue.append(course)

    while queue:
        curr_course = queue.pop(0)
        result.append(curr_course)

        if curr_course in graph:
            for next_course in graph[curr_course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    queue.append(next_course)

    return len(result) == num_courses
```

<span style="color:orange; font-weight=800;">Time Complexity - </span><span style="color:#e20421;">O(N + E), where N is the number of courses and E is the number of prerequisites.</span>
<span style="color:orange; font-weight=800;">Space Complexity - </span><span style="color:#e20421;"> O(N + E), for the **`in_degrees`** and **`graph`** dictionaries, and the **`queue`**.</span>

## Preparing for Problems:
1. Read and understand the problem statement carefully. Make sure to identify the input, output, and constraints.
2. Clarify any doubts by asking questions about the problem.
3. Identify the appropriate algorithm or data structure that can be used to solve the problem efficiently.
4. Break down the problem into smaller sub-problems and try to solve each sub-problem step by step.
5. Write the# pseudocode for the solution to the sub-problems and then combine them to form the final solution.
6. Test the# pseudocode with different test cases to verify its correctness.
7. Once the# pseudocode is correct, implement the solution in the desired programming language (JavaScript or Python).
8. Test the code thoroughly with various test cases to ensure it works as expected.
9. Analyze the time and space complexity of the solution to assess its efficiency.
10. Optimize the solution if possible by reducing the time or space complexity or improving the code readability.
11. Document the code properly with comments to explain the logic and any important steps.
12. Submit the solution and discuss the approach and code with others to gain insights and learn from different perspectives.
