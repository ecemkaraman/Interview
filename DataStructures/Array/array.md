# Arrays

## Pros and Cons
### Pros
- Fast lookups (if you have the index, no need to traverse from head like LL)
- Fast append(push)/pop
- Ordered →Advantage over dict 

### Cons
- Addition and removal of elements into/from the middle an array is slow because they remaining elements need to be shifted to accommodate the new/missing element. An exception to this is if the position to be inserted/removed is at the end of the array.
- For certain languages where the array size is fixed, it cannot alter its size after initialization. if an insertion causes the total number of elements to exceed the size, a new array has to be allocated and the existing elements have to be copied over. The act of creating a new array and transferring elements over takes O(n) time.
- Slow inserts
- Slow deletes
- Fixed Size -> IF USING STATIC ARRAY

## Time & Space Complexity 
Add/remove element:
	-To the end: O(1)
	-Anywhere else: O(n) →the rest needs the be re-indexed

Search for an element:
	-by value: O(n) → you need to go through the whole list
	-by index: O(1) → you go directly to that index
Slicing/Joining lists: 
	-O(k), k=len(resulting/sliced_substring)

## Look Out For
- Clarify if there are duplicate values in the array. Would the presence of duplicate values affect the answer? Does it make the question simpler or harder?
- When using an index to iterate through array elements, be careful not to go out of bounds.
- Be mindful about slicing or concatenating arrays in your code. Typically, slicing and concatenating arrays would take O(n) time. Use start and end indices to demarcate a subarray/range where possible.
- Is the array sorted or partially sorted? If it is either, some form of binary search should be possible. This usually means that the interviewer is looking for a solution that is faster than O(n).
- Can you sort the array? Sometimes sorting the array first may significantly simplify the problem. Make sure that the order of array elements do not need to be preserved before attempting to sort it.
- For questions where summation or multiplication of a subarray is involved, pre-computation using hashing or a prefix, suffix sum, or product might be useful.
- If you are given a sequence and the interviewer asks for O(1) space, it might be possible to use the array itself as a hash table. For example, if the array has values only from 1 to N, where N is the length of the array, negate the value at that index (minus one) to indicate the presence of that number.


## Edge Cases
• Empty sequence
• Sequence with 1 or 2 elements
• Sequence with repeated elements
• Duplicated values in the sequence

<img width="635" alt="image" src="https://github.com/user-attachments/assets/20a91689-2556-4a98-b111-63e0f545b3e7">


## TACTICAL THINGS
### **Know how to:**

- Work with an array
- Get the length
- Get an element by a particular index

### **2D Arrays**

- Creation, indexing  →matrix or list of lists? → Know how your lang works w/ them
- Sorting, getting min/max →is it built-in?
- Partitioning, merging, slicing →Know the built-in functions, but also be able to write your own function
- List comprehensions, lambdas, reduce, map, filter etc


## COMMON ERRORS
- Off by 1 errors, boundary errors, indexing
- Test again 1 & 2 element arrays
- Time complexity of built-in array functions
- Matrix [y][x] ⇒ be careful with the order, use [row][column] instead


## **PATTERNS & CONCEPTS**
- We tend to insert elements at the end of an array
 - If you do it at the beginning, you need to scooch all other elements àthat’s linear time operation
- Index math
    - If you need to rotate an array regularly àlinear op every time
    - Instead, you can wrap it in another class & use index math. So, actually we’re just updating the indices
    - E.g. 2 pointers, swapping indices
- In-place modifications? Is it ok to modify the input or do I need to copy it?


## EXTRAS
    - Working with subarrays instead of the entire array (recursively or iteratively)
    - Working with matrices
    - Beware of whether your arrays are fixed length or not
        - E.g. it’s fixed length in Java, so how can I dynamically resize it?
    - Hash tables →when to use array vs hash table
