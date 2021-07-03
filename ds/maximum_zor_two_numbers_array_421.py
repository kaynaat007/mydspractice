from typing import List


class Trie:

    def __init__(self):
        self.t = {}

    def insert(self, target):

        curr = self.t
        for i in range(32):
            bit = target[i]
            while True:
                if bit in curr:
                    curr = curr[bit]
                else:
                    curr[bit] = {}
                    break
            curr['#'] = {}






def findMaximumXOR(nums: List[int]) -> int:


