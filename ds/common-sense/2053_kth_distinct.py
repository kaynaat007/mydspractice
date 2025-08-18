from typing import List
from collections import Counter


def kthDistinctUtil(arr: List[str], k: int) -> str:
    store = Counter(arr)
    output = ""
    for s in arr:
        if store[s] == 1:
            k -= 1
            output = s
        if k == 0:
            break
    return output if k == 0 else ""


inp = ["a", "a", "b"]
k = 1

# inp = ["aaa", "aa", "a"]
# k = 1


# inp = ["a", "b", "a"]
# k = 3

#
# inp = ["d","b","c","b","c","a"]
# k = 2

print(kthDistinctUtil(inp, k))
