from typing import List
from collections import defaultdict
'''
I was thinking may be O(n) sol could exists. 
Seems like it's Nklogk solution only 

'''

def groupAnagrams(strs: List[str]) -> List[List[str]]:

    output = defaultdict(list)
    for s in strs:
        output[''.join(sorted(s))].append(s)
    return list(output.values())

strs = ["eat","tea","tan","ate","nat","bat"]
strs = ['acc', 'cc', 'ccaaa']
print(groupAnagrams(strs))
