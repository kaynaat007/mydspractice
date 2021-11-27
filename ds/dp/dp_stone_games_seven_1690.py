from typing import List


def util(stones, i, j, chance, alice, bob):

    print(' chance: {}, i: {}, j: {}, alice: {}, bob: {}'.format(chance, i, j, alice, bob))
    if i > j:
        return 0, 0

    if chance == 1:
        alice_score_max_1, bob_score_max_1 = util(stones, i+1, j, 2, alice, bob)
        alice_score_max_2, bob_score_max_2 = util(stones, i, j-1, 2, alice, bob)
        alice += max(sum(stones[i+1:j+1]) + alice_score_max_1, sum(stones[i:j]) + alice_score_max_2)
        if abs(bob_score_max_2 - alice) < abs(bob_score_max_1 - alice):
            return alice, bob_score_max_2
        return alice, bob_score_max_1
    else:
        alice_score_max_1, bob_score_max_1 = util(stones, i + 1, j, 1, alice, bob)
        alice_score_max_2, bob_score_max_2 = util(stones, i, j - 1, 1, alice, bob)
        alice = max(alice_score_max_1, alice_score_max_2)
        if abs(bob_score_max_2 - alice) < abs(bob_score_max_1 - alice):
            return alice, bob_score_max_2
        return alice, bob_score_max_1


def stoneGameVII(stones: List[int]) -> int:

    n = len(stones)
    alice, bob = util(stones, 0, n-1, 1, 0, 0)
    print(alice, bob)
    return alice - bob

stones = [1, 2, 3]
# stones = [5, 3, 1, 4, 2]
# stones = [5, 3, 1, 4, 2]
print(stoneGameVII(stones))

