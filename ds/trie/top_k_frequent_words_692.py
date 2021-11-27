from collections import defaultdict
from functools import cmp_to_key
from collections import Counter
import heapq


class Node:

    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):

        if self.freq == other.freq:
            return self.word > other.word
        else:
            return self.freq < other.freq

def topKfrequentWords(words, k):
    """
    nlogn time
    n space
    """
    n = len(words)
    if n == 1:
        return []
    counts = Counter(words)
    l = sorted(counts, key=lambda word: (-counts[word], word))
    return l[:k]


def topKFrequentWordsNlogK(words, k):
    """
    nLogk time.

    """
    counts = Counter(words)
    r = []
    o = []
    for key, count in counts.items():
        heapq.heappush(r, Node(key, count))
        s = len(r)
        if s > k:
            heapq.heappop(r)

    while k:
        e = heapq.heappop(r)
        o.append(e.word)
        k = k - 1

    return o[::-1]

#
#
# words = ["i", "love", "leetcode", "i", "love", "coding"]
# k = 2

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4


print(topKfrequentWords(words, k))

print(topKFrequentWordsNlogK(words, k))