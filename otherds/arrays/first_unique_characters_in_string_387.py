from collections import Counter

def firstUniqChar(s: str) -> int:

    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1

s = 'leetcode'
print(firstUniqChar(s))

s = 'loveleetcode'
print(firstUniqChar(s))

