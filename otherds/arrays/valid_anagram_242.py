from collections import Counter


def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    hash_s = Counter(s)
    for ch in t:
        if ch not in hash_s:
            return False
        else:
            hash_s[ch] -= 1
            if hash_s[ch] == 0:
                del hash_s[ch]
    return True

s = 'anagram'
t = 'nagaram'

# s = 'rat'
# t = 'car'

# s = ""
# t = ""

# s = 'ab'
# t = 'a'

# s = 'aacc'
# t = 'ccac'
print(isAnagram(s, t))