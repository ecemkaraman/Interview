# [76] https://leetcode.com/problems/minimum-window-substring/
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T
#
# variation with finding minimum
from collections import Counter


def minWindow(s: str, t: str) -> str:
    counter = Counter(t)
    count, start, end, res = len(t), 0, 0, [float('inf'), 0]
    while end < len(s):
        counter[s[end]] -= 1
        # consider duplicate char in t
        if counter[s[end]] >= 0:
            count -= 1
        end += 1
        # valid in while
        while count == 0:
            # update minimum here, inner while loop
            if end - start < res[0]:
                res = (end - start, start)

            counter[s[start]] += 1
            if counter[s[start]] > 0:
                count += 1
            start += 1
    return s[res[1]:res[0] + res[1]] if res[0] != float('inf') else ''

