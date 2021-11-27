from collections import Counter


def numJewelsInStones(J: str, S: str) -> int:

    count = Counter(S)
    return sum(count[ch] for ch in J)


J = 'aA'
S = 'aAAbbbb'

# J = 'z'
# S = 'ZZ'
print(numJewelsInStones(J, S))