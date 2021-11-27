

import itertools
from typing import List


def letterCombinations(digits: str) -> List[str]:

    hash = {

        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']

    }

    if not digits:
        return []

    supply = []
    output = []
    for d in digits:
        supply.append(hash[int(d)])

    for element in itertools.product(*supply):
        output.append(''.join(element))

    return output


digits = "456"
digits = ""
print(letterCombinations(digits))

