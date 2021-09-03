import math


def winnerSquareGame(n: int) -> bool:

    winners = [False for _ in range(n+1)]
    winners[1] = True
    winners[0] = False
    for i in range(2, n+1):
        for k in range(1, math.floor(math.sqrt(i)) + 1):
            delta = i - k * k
            # print('i: {} delta: {}'.format(i, delta))
            if winners[delta] is False:
                winners[i] = True
                break
    # print(winners)
    return winners[n]

n = 144
print(winnerSquareGame(n))
