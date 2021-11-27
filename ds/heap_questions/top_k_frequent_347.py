import heapq
from collections import Counter
from itertools import chain


class Node:

    def __init__(self, val, freq):
        self.val = val
        self.freq = freq

    def __lt__(self, other):
        return self.freq > other.freq

    def __str__(self):
        return 'val = {}, freq = {}'.format(self.val, self.freq)

def  topKFrequent(nums, k):

    """
    Klogn solution using Heap.
    """

    counts = Counter(nums)
    r = []
    o = []
    for key, count in counts.items():
        r.append(Node(key, count))

    heapq.heapify(r)
    while k:
        o.append(heapq.heappop(r).val)
        k = k - 1
    return o



def topKFrequentV2(nums, k):
    """
    O(n) solution using approach of Buckets
    """
    n = len(nums)
    bucket = [[] for _ in range(n)]
    for key, freq in Counter(nums).items():
        bucket[freq].append(key)
    return list(chain(*bucket))[-k:]


# nums = [3, 2, 1, 4]
# k = 2

nums = [1,1,1,2,2,3]
k = 3


#
# nums = [1]
# k = 1

print(topKFrequent(nums, k))
print(topKFrequentV2(nums, k))

