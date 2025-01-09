# [904] https://leetcode.com/problems/fruit-into-baskets/
# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
# What is the total amount of fruit you can collect with this procedure?
#
# variation with list

from typing import List
from collections import defaultdict

def totalFruit(tree: 'List[int]') -> int:
    counter = defaultdict(int)
    count, start, end, res = 0, 0, 0, 0

    while end < len(tree):
        counter[tree[end]] += 1
        if counter[tree[end]] == 1:
            count += 1
        end += 1
        while count > 2:
            counter[tree[start]] -= 1
            if counter[tree[start]] == 0:
                count -= 1
            start += 1
        res = max(res, end - start)
    return res