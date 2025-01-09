# [30] https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# variation with complex match policy

from typing import List
from collections import Counter

def findSubstring(s: str, words: 'List[str]') -> 'List[int]':
    if not words:
        return []

    word_len, res = len(words[0]), []

    # start offset from 0 to word_len, and step is word_len
    for i in range(word_len):
        # reset state every epoch
        counter = Counter(words)
        start, end, count = i, i, len(words)
        while end < len(s):
            cur_word = s[end:end + word_len]
            # check is not necessary here, just for performance
            if cur_word in counter:
                counter[cur_word] -= 1
                if counter[cur_word] >= 0:
                    count -= 1
            end += word_len

            if count == 0:
                res.append(start)

            # ensure consecutive words
            if end - start == word_len * len(words):
                cur_word = s[start:start + word_len]
                if cur_word in counter:
                    counter[cur_word] += 1
                    if counter[cur_word] > 0:
                        count += 1
                start += word_len

    # the order is not necessary here
    return res