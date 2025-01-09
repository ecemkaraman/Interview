# [438] https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# variation with restrict between start and end
from typing import List
from collections import Counter

def findAnagrams(s: str, p: str) -> 'List[int]':
    len_p, len_s = len(p), len(s)
    if len_p > len_s:
        return []
    counter = Counter(p)
    count, start, end, res = len_p, 0, 0, []

    while end < len_s:
        # only update counter when match char in p
        counter[s[end]] -= 1
        if counter[s[end]] >= 0:
            count -= 1
        end += 1

        if count == 0:
            res.append(start)

        # not use a while, because restrict the length
        if end - start == len_p:
            counter[s[start]] += 1
            # exclude char not in p, because always negative
            if counter[s[start]] > 0:
                count += 1
            start += 1
    return res