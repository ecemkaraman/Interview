# [3] https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.
#
# variation with no pattern

from collections import defaultdict

def lengthOfLongestSubstring(s):
    # create a default dict to maintain state
    counter = defaultdict(int)
    count, start, end, res = 0, 0, 0, 0
    while end < len(s):
        counter[s[end]] += 1
        if counter[s[end]] > 1:
            count += 1
        end += 1
        while count > 0:
            counter[s[start]] -= 1
            if counter[s[start]] > 0:
                count -= 1
            start += 1
        res = max(res, end - start)
    return res