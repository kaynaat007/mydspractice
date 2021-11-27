from typing import List


class Trie:
    def __init__(self):
        self.ds = {}

    def insert(self, ds, data, k):
        if not data:
            return
        if k >= len(data):
            return
        ch = data[k]
        if ch in ds:
            val = ds[ch]
            val['count'] += 1
        else:
            ds[ch] = {'count': 1}
        self.insert(ds[ch], data, k+1)

    def maximal_prefix(self, ds, strings):

        keys_len = len(ds.keys())
        if keys_len > 1:
            return ""

        for data in strings:
            if not data:
                return ""

        data = strings[0]

        ch = data[0]
        prefix = ch
        val = ds[ch]
        data = data[1:]
        count = val['count']
        ds = ds[ch]
        k = 0
        while k < len(data):
            ch = data[k]
            if count != ds[ch]['count']:
                break
            prefix += ch
            k += 1
            ds = ds[ch]
        return prefix


def longestCommonPrefix(strs: List[str]) -> str:

    t = Trie()
    if not strs:
        return ""
    for string in strs:
        if string:
            t.insert(t.ds, string, 0)
    return t.maximal_prefix(t.ds, strs)


strs = ['abcd', 'abcdef']
strs = ["flower","flow","flight"]

# strs = ["dog","racecar","car"]

strs = ['abc', "a"]

strs = []
print(longestCommonPrefix(strs))
