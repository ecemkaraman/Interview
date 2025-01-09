# Strings

## Time and Space Complexity
A strings is an array of characters, so the time complexities of basic string operations will closely resemble that of array operations.
- Access: O(1)
- Search: O(n)
- Insert: O(n)
- Remove: O(n)

<img width="635" alt="image" src="https://github.com/user-attachments/assets/4e12ac96-f736-42a7-a129-0bd7bdc56685">


## **Edge Cases in String Problems**

- Empty string
- String with 1 or 2 characters
- String with repeated characters
- Strings with only distinct characters
- Strings with special characters (spaces, punctuation, non-alpha)

## Interview Tips

- The tips for sequence apply to strings too.
- When you need to compare strings where the order isn’t important (like anagram), you may consider using a HashMap as a counter. If your language has a built-in `Counter` class like Python, ask to use that instead.
- If you need to keep a counter of characters, a common mistake is to say that the space complexity required for the counter is O(n). The space required for a counter is O(1) not O(n). This is because the upper bound is the range of characters, which is usually a fixed constant of 26. The input set is just lowercase Latin characters.
- Ask about input character set and case sensitivity (Usually lowercase Latin characters) 
    
## **STRING OPERATIONS**
    
    - Get the length or the $i^th$ character of a string
    - Concatenation, substrings (e.g. 3rd to the 7th char)
    - Contains, startswith, endswith type of functions
    - String comparison → compare by value vs reference
    - Convert string↔ int, get char code
    - Check uppercase, lowercase, punctuation, letter, number
    
## **PATTERNS & CONCEPTS**
    
    - Concatenation: runtime, how to concat many strings
    - Mutable? – If so, know how to swap characters etc
    - ASCII vs Unicode
    - Equality comparison – is it?:
    - Char by char comparison
    - Reference (aka memory location) comparison
    
## **POTENTIAL BUGS**
    
    - Null, empty strings, check how code runs on strings of length 1 or 2
    - ASCII vs Unicode
    - String comparison → ref vs char by char
    - Uppercase/lowercase, punctuation, letters vs numbers
    - Talk to the interviewer about assumptions you can make about those strings
    
## **EXTRAS**
    
    - StringBuilder → concat can get expensive with large input. How can you overcome that?

## Common Questions
Many string questions fall into one of these buckets.

### **Counting frequency of characters in a string**
*Most common method:* Use a hash table/map. If your language has a built-in Counter class like Python, ask if you can use that instead.
Common mistake: Space complexity of a counter of a string of lowercase Latin characters is O(1) not O(n). The upper bound is the range of characters → 26 for the latin alphabet. Drop the constant: O(26) = O(1)

### Anagrams
An anagram is word switch or word play. It is the result of re-arranging the letters of a word or phrase to produce a new word or phrase, while using all the original letters only once. In interviews, usually we are only bothered with words without spaces in them.
To determine if two strings are anagrams, there are a few approaches:
- Sorting both strings should produce the same resulting string. This takes O(n.log(n)) time and O(log(n)) space → n is the  length of the string
- If we map each character to a prime number and we multiply each mapped number together, anagrams should have the same multiple (prime factor decomposition). This takes O(n) time and O(1) space. Examples: [Group Anagram](https://leetcode.com/problems/group-anagrams/)
- Frequency counting of characters will help to determine if two strings are anagrams. This also takes O(n) time and O(1) space.

### Palindromes
A palindrome is a sequence that reads the same backward as forward, disregarding spaces, punctuation, and capitalization. such as `madam` or `racecar`.
Corner cases: Empty string, Single-character string, Strings with only one distinct character
2 ways to determine:
- Reverse the string and it should be equal to itself.  → `s == s[::-1]`
- Have two pointers at the start and end of the string. Move the pointers inward till they meet. At every point in time, the characters at both pointers should match.

The order of characters within the string matters, so hash tables are usually not helpful.

- **Odd-Length Palindromes**: These have a single center character. For example, in "racecar", "e" is the center. Start at left=right=center
- **Even-Length Palindromes**: These have two center characters. For example, in "abba", "bb" is the center. Start at left=center, right=center+1

- Valid Palindrome: 2 pointers moving inwards from opposite ends
- Counting the number of palindromes or Longest palindromic substring: 2 pointers start at middle and move outward

- When a question is about counting the number of palindromes, a common trick is to have two pointers that move outward, away from the middle. Note that palindromes can be even or odd length. For each middle pivot position, you need to check it twice: Once that includes the character and once without the character.
- For substrings, you can terminate early once there is no match.
- For subsequences, use dynamic programming as there are overlapping subproblems.

### **Non-repeating characters**

Use a 26-bit bitmask to indicate which lower case Latin characters are inside the string. To determine if two strings have common characters, perform & on the two bitmasks. If the result is non-zero, mask_a & mask_b > 0 , then the two strings have common characters.

Common data structures for looking up strings efficiently are
- Trie/Prefix Tree
- Suffix Tree

## Common String Operations
### How to Join Strings
TBD
