"""
repeat his question
Had to lookup the solution
it's a greedy approach problem and very good one with a good mathematical proof.
"""
from typing import List
import math


def util(a, b, n):

    store = [(a[i], b[i], a[i] + b[i]) for i in range(n)]
    store = sorted(store, key=lambda x: x[2], reverse=True)
    alex_score = 0
    bob_score = 0
    switch = True
    for i in range(n):
        current_alex_score, current_bob_score, total_sum = store[i]
        if switch:
            alex_score = alex_score + current_alex_score
        else:
            bob_score = bob_score + current_bob_score

        if switch:
            switch = False
        else:
            switch = True
    # print(alex_score, bob_score)

    if alex_score > bob_score:
        return  1
    elif alex_score == bob_score:
        return 0
    else:
        return -1


def stoneGameVI(aliceValues: List[int], bobValues: List[int]) -> int:

    n = len(aliceValues)
    return util(aliceValues, bobValues, n)

a = [1]
b = [2]

a = [1, 3]
b = [2, 1]

a = [1, 2]
b=  [3, 1]

a = [2,4,3]
b = [1, 6, 7]

print(stoneGameVI(a, b))
