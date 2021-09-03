from typing import List


def util(piles, i, j, turn, cache):

    if j - i + 1 == 1:
        if turn == 1: # if alice turn, alice wins
            cache[(turn, i, j)] = (piles[0], 0)
            return piles[i], 0
        # if bob's turn, bob wins
        cache[(turn, i, j)] = (0, piles[i])
        return 0, piles[i]

    if i > j:
        return 0, 0

    if (turn, i, j) in cache:
        # print('returning from cache')
        return cache[(turn, i, j)]

    if turn == 1: # alice turn
        alice_best_score_1, bob_best_score_1 = util(piles, i+1, j, 2, cache)
        alice_best_score_2, bob_best_score_2 = util(piles, i, j-1, 2, cache)
        if piles[i] + alice_best_score_1 > piles[j] + alice_best_score_2:
            cache[(1, i, j)] = (piles[i] + alice_best_score_1, bob_best_score_1)
            return piles[i] + alice_best_score_1, bob_best_score_1
        cache[(1, i, j)] = (piles[j] + alice_best_score_2, bob_best_score_2)
        return piles[j] + alice_best_score_2, bob_best_score_2

    if turn == 2:
        alice_best_score_1, bob_best_score_1 = util(piles, i+1, j, 1, cache)
        alice_best_score_2, bob_best_score_2 = util(piles, i, j-1, 1, cache)
        if piles[i] + bob_best_score_1 > piles[j] + bob_best_score_2:
            cache[(2, i, j)] = (alice_best_score_1,  piles[i] + bob_best_score_1)
            return alice_best_score_1,  piles[i] + bob_best_score_1
        cache[(2, i, j)] = (alice_best_score_2, piles[j] + bob_best_score_2)
        return alice_best_score_2, piles[j] + bob_best_score_2


def stoneGame(piles: List[int]) -> bool:

    n = len(piles)
    alice_best_score, bob_best_score = util(piles, 0, n-1, 1, {})
    print(alice_best_score, bob_best_score)
    return alice_best_score > bob_best_score

piles = [3, 4]
piles = [5, 3, 1]
piles = [5,3,4,5]
piles = [5, 6, 7, 8, 1, 2]
piles = [7,7,12,16,41,48,41,48,11,9,34,2,44,30,27,12,11,39,31,8,23,11,47,25,15,23,4,17,11,50,16,50,38,34,48,27,16,24,22,48,50,10,26,27,9,43,13,42,46,24]
print(stoneGame(piles))



