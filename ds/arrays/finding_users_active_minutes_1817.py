"""
Simple
basic usage of data structure of key --> set()
"""
from typing import List
from collections import defaultdict


def findingUsersActiveMinutes(logs: List[List[int]], k: int) -> List[int]:

    uam = defaultdict(set)
    answers = [0 for _ in range(k)]
    for user, minute in logs:
        uam[user].add(minute)

    for user, minutes in uam.items():
        current_uam = len(minutes) - 1
        answers[current_uam] +=1

    return answers


logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5

logs = [[1,1],[2,2],[2,3]]
k = 4

logs = [[0, 3], [0, 5], [0, 3]]
k = 3
print(findingUsersActiveMinutes(logs, k))


